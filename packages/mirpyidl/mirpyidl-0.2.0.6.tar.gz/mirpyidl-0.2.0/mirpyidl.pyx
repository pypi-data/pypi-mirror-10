# -*- coding: utf-8 -*-
"""
********
mirpyidl
********

author
======
  Novimir Antoniuk Pablant
  - npablant@pppl.gov
  - novimir.pablant@amicitas.com

purpose
=======
  Allows for integration of IDL routines into Python.

warning
=======
  I have not been careful with generalizing the data types.
  At this point this will only work on 64 bit systems.

descripton
==========
  A library to call IDL (Interactive Data Language) from python.  
  Allows trasparent wrapping of IDL routines and objects as well 
  as arbitrary execution of IDL code.  

  *mirpyidl* is hosted at: 
    https://bitbucket.org/amicitas/mirpyidl

  Documentation can be found at:
    http://amicitas.bitbucket.org/mirpyidl
  
  To build use the command:
    python setup.py build_ext


  Known Issues:
    As written, this will only work if the idlrpc server is using the
    default ServerId.

    This module includes routines to start an idlrpc server if one
    is not already running. This currently has some problems:
     
    - I don't know a good way to check wheather the server is ready
      for connections.  Currently I wait for the licence server to
      start, then wait an addition 0.5 seconds.
       
    - The idlrpc server is left running regardless of whether it was
      an existing process or started by this module.  This is not
      really the best way to handle things.

IDL side variables
==================
  mirpyidl creates a number of variables within the IDL session to track pyidl 
  instances and objects.  These variables are then used to provide unique name 
  spaces for different pyidl objects.

  Here is a list of the persistent IDL side variables:
    - _mirpyidl_instance_counter
    - _mirpyidl_object_counter
  
"""

# For python 2.7/3.0 compatability.
from __future__ import print_function
from __future__ import unicode_literals
str_builtin = str
str = ''.__class__


import logging

# Import the Python-level symbols of numpy
import numpy as np

# Import the C-level symbols of numpy
cimport numpy as np

# Numpy must be initialized. When using numpy from C or Cython you must
# _always_ do that, or you will have segfaults
np.import_array()


# ==============================================================================
# ==============================================================================
cdef extern from "idl_export.h":

    # Define IDL_VARIABLE flags.
    DEF IDL_V_ARR = 4
    DEF IDL_V_FILE = 8
    DEF IDL_V_STRUCT = 32
    DEF IDL_V_NOT_SCALAR = (IDL_V_ARR | IDL_V_FILE | IDL_V_STRUCT)
    
    # Define IDL data types.
    ctypedef int IDL_INT
    ctypedef int IDL_UINT
    ctypedef int IDL_LONG
    ctypedef int IDL_ULONG
    ctypedef int IDL_LONG64
    ctypedef int IDL_ULONG

    ctypedef unsigned char UCHAR

    # Define IDL_VARIABLE type values.
    DEF IDL_TYP_UNDEF = 0
    DEF IDL_TYP_BYTE = 1
    DEF IDL_TYP_INT = 2
    DEF IDL_TYP_LONG = 3
    DEF IDL_TYP_FLOAT = 4
    DEF IDL_TYP_DOUBLE = 5
    DEF IDL_TYP_COMPLEX = 6
    DEF IDL_TYP_STRING = 7
    DEF IDL_TYP_STRUCT = 8
    DEF IDL_TYP_DCOMPLEX = 9
    DEF IDL_TYP_PTR = 10
    DEF IDL_TYP_OBJREF = 11
    DEF IDL_TYP_UINT = 12
    DEF IDL_TYP_ULONG = 13
    DEF IDL_TYP_LONG64 = 14
    DEF IDL_TYP_ULONG64 = 15

    # Define the memory types.
    DEF IDL_TYP_MEMINT = IDL_TYP_LONG
    ctypedef int IDL_MEMINT

    # --------------------------------------------------------------------------
    # String definitions
    ctypedef struct IDL_STRING:
        int slen
        char *s
        
    # --------------------------------------------------------------------------
    # Array definitions
    
    # Maximum # of array dimensions
    DEF IDL_MAX_ARRAY_DIM = 8
    
    ctypedef void (* IDL_ARRAY_FREE_CB)(UCHAR *data)
    
    ctypedef int IDL_ARRAY_DIM[IDL_MAX_ARRAY_DIM]
    ctypedef struct IDL_ARRAY:
        int elt_len              # Length of element in char units */
        int arr_len		# Length of entire array (char) */
        int n_elts		# total # of elements */
        char *data			# ^ to beginning of array data */
        char n_dim			# # of dimensions used by array */
        char flags			# Array block flags */
        short file_unit		        # # of assoc file if file var */
        IDL_ARRAY_DIM dim		# dimensions */
        #IDL_ARRAY_FREE_CB free_cb	# Free callback */
        #IDL_FILEINT offset		# Offset to base of data for file var */
        #IDL_MEMINT data_guard	        # Guard longword */


    # --------------------------------------------------------------------------
    # Structure definitions

    ctypedef struct _idl_structure:
        int ntags
    
    ctypedef _idl_structure *IDL_StructDefPtr

    ctypedef struct IDL_SREF:
        IDL_ARRAY *arr
        _idl_structure *sdef
        
    int IDL_StructNumTags(IDL_StructDefPtr sdef)


    ctypedef union IDL_ALLTYPES:    
        char sc
        UCHAR c
        IDL_INT i
        IDL_UINT ui
        IDL_LONG l
        IDL_ULONG ul
        IDL_LONG64 l64
        #IDL_ULONG64 ul64
        float f
        double d
        #IDL_COMPLEX cmp
        #IDL_DCOMPLEX dcmp
        IDL_STRING str
        IDL_ARRAY *arr
        IDL_SREF s
        #IDL_HVID hvid

        #IDL_MEMINT memint
        #IDL_FILEINT fileint
        #IDL_PTRINT ptrint   

        
    ctypedef struct IDL_VARIABLE:
        char type
        char flags
        IDL_ALLTYPES value
    
    ctypedef IDL_VARIABLE *IDL_VPTR

    ctypedef int IDL_INIT_DATA_OPTIONS_T
    ctypedef struct IDL_INIT_DATA:
        IDL_INIT_DATA_OPTIONS_T options
    
    # Copied from idl_export.h
    int IDL_Initialize(IDL_INIT_DATA *init_data)
    int IDL_Cleanup(int just_cleanup)
    int IDL_ExecuteStr(char *cmd)

    
    IDL_VPTR IDL_Gettmp()
    IDL_VPTR IDL_GetVarAddr(char *name)
    IDL_VPTR IDL_GetVarAddr1(char *name, int ienter)
    IDL_VPTR IDL_FindNamedVariable(char *name, int ienter)
    
    void IDL_StoreScalar(IDL_VPTR dest, int type, IDL_ALLTYPES *value)
    IDL_VPTR IDL_ImportNamedArray(char *name, int n_dim,
        IDL_MEMINT dim[],  int type, UCHAR *data,  IDL_ARRAY_FREE_CB free_cb, 
        IDL_StructDefPtr s);
    
    void IDL_StrStore(IDL_STRING *s, const char *fs)

    
# ==============================================================================
# ==============================================================================
cdef extern from "idl_rpc.h":

    # Define the CLIENT structure for connection to the RPC server.
    struct CLIENT:
        pass
    
    CLIENT *IDL_RPCInit( long lServerId, char* pszHostname)
    int IDL_RPCExecuteStr( CLIENT *pClient, char * pszCommand)

    IDL_VPTR IDL_RPCGettmp()
    IDL_VPTR IDL_RPCGetVariable(CLIENT *pClient, char *Name)
    
    void IDL_RPCStrStore( IDL_STRING *s, char *fs)
    int IDL_RPCSetVariable(CLIENT *pClient, char *Name, IDL_VPTR pVar)
    IDL_VPTR IDL_RPCImportArray(int n_dim, int dim[], int type, 
                                UCHAR *data, void* free_cb)




    
# ==============================================================================
# ==============================================================================
# Define module level variables.

m_log = logging.getLogger('mirpyidl')

# This is our module level flag for wether CallableIDL has been initialized.
m_initialized = False

# This is our module level idlrpc connection.
m_connection = None


# ==============================================================================
# ==============================================================================
# Define module level functions.

def setLoggingLevel(level=logging.INFO):
    m_log.setLevel(level)

        
def InitializeIdl():
    """
    Initialize the IDL interpreter.

    This only needs to be done once.  
    I don't think there is a problem calling this multiple times, but just to be
    save the initialization state internally.
    """
    
    global m_initialized
    cdef IDL_INIT_DATA init_data
        
    if not m_initialized:
        init_data.options = 0
    
        IDL_Initialize(&init_data)

        m_initialized = True

        
def _IDLCleanup():

    cdef int just_cleanup
    just_cleanup = 0
    IDL_Cleanup(just_cleanup)

    
    
# ==============================================================================
# ==============================================================================
# Define module level functions.

def setLoggingLevel(level=logging.INFO):
    m_log.setLevel(level)
    

cdef _getIDLRPCClient():
    """
    Get reference to the current client object if available.  
    If it is not available, then create a new object.
    """
    
    global m_connection
        
    if m_connection is None:
        m_connection = _IDLRPCClient()

    return m_connection

    
cdef CLIENT *_connectToIDLRPC():
    """
    Connect to the IDLRPC server.

    Note: The C routine IDL_RPCInit fails with a segmenation fault if the
          RPC server is not available (Arrrrggg, another reason to get away
          from IDL).
    """

    cdef CLIENT *pClient
        
    pClient = IDL_RPCInit(0, b'')

    if pClient:
        m_log.info('Connected to the IDLRPC server.')
    else:
        raise Exception('Could not connect to an IDLRPC server.')

    return pClient


def _checkForIDLRPCProcess():

    # psutil is only needed for starting the IDLRPC server.
    import psutil
    
    found_idlrpc = False
    for process in psutil.process_iter():
        if process.name() == 'idlrpc':
            found_idlrpc = True
            break

    if not found_idlrpc:
        raise IdlConnectionError('Could not find a running idlrpc process to connect to.')


cdef CLIENT *_checkAndConnectToIDLRPC():
    """
    Attempt to connect to the IDLRPC server.
    If this fails, then start a new server.

    Note: The C routine IDL_RPCInit fails with a segmenation fault if the
          RPC server is not available.  For this reason, I manually
          check if an RPC process is available before trying to connect.

          This will only work if the default ServerId is being used.
    """
    global m_connected
    
    cdef CLIENT *pClient

    # psutil is only needed for starting the IDLRPC server.
    import psutil

    
    _checkForIDLRPCProcess()
    
    pClient = _connectToIDLRPC()
    m_connected = True

    return pClient



# ==============================================================================
# ==============================================================================
# Define module level convenience functions.
def callFunction(*args, **kwargs):
    idl = PyIDL()
    return idl.callFunction(*args, **kwargs)

def callPro(*args, **kwargs):
    idl = PyIDL()
    return idl.callPro(*args, **kwargs)

def execute(*args):
    idl = PyIDL()
    idl.execute(*args)

def setVariable(*args):
    idl = PyIDL()
    idl.setVariable(*args)

def getVariable(*args):
    idl = PyIDL()
    return idl.getVariable(*args)

def ex(*args):
    idl = PyIDL()
    idl.execute(*args)

def set(*args):
    idl = PyIDL()
    idl.setVariable(*args)

def get(*args):
    idl = PyIDL()
    return idl.getVariable(*args)


# ==============================================================================
# ==============================================================================
# Define the connection class
cdef class _IDLRPCClient:
    """
    This is a python class just to hold the IDL_RPC client structure. 
    Using this class provides more control of creation and destruction of
    connections, rather than just handling the client at the module level. 
    """

    cdef CLIENT *client
    cdef bint connected
    cdef long _id
    
    def __init__(self):
        """
        Get a new client object, and initialize the IDL_RPC client. 
        As part of this process we will get a new connection id and
        increment the connection counter.
        """

        # Setup default values
        self._id = 0
        self.connected = 0
        
        # Initiaize a new conneciton.
        self.client = _checkAndConnectToIDLRPC()
        self.connected = 1

        # Initialize the connection id and connection count.
        self._id = self.requestNewConnectionId()
        self.incrementConnectionCount()
        
        
    def __dealloc__(self):
        self.decrementConnectionCount()
        count = self.getConnectionCount()
        
        print('DEBUG: Destroying PyIDLClient with id: {}'.format(self._id))
        print('DEBUG: Number of active pyidlrpc connections remaining: {}'.format(count))
        print('DEBUG: PyIDLClient DELORTED!!!!')

        
    def requestNewConnectionId(self):
        """
        Get a new unique identifier for this idlrpc connection.

        It is possible for multiple python processes to connect to the same
        idlrpc server.  This method allows the idlrpc server to keep track of
        a unique idl connection identifier number for each of these connections.
        """
        cdef IDL_VPTR vptr

        if not self.connected:
            raise Exception('No connection to idlrpc server.')
            
        IDL_RPCExecuteStr(self.client
                          ,b'IF ~ ISA(_pyidlrpc_connection_counter) THEN _pyidlrpc_connection_counter=0L')
        IDL_RPCExecuteStr(self.client
                          ,b'_pyidlrpc_connection_counter += 1')
        vptr = IDL_RPCGetVariable(self.client, b'_pyidlrpc_connection_counter')
        new_id = vptr.value.l

        m_log.debug('New PyIDL connection id: {}'.format(new_id))

        return new_id

        
    def incrementConnectionCount(self):
        """
        Increase the connection count on the idlrpc server by one.
        """

        if not self.connected:
            raise Exception('No connection to idlrpc server.')
            
        IDL_RPCExecuteStr(self.client
                          ,b'IF ~ ISA(_pyidlrpc_connection_count) THEN _pyidlrpc_connection_count=0L')
        IDL_RPCExecuteStr(self.client
                          ,b'_pyidlrpc_connection_count += 1')

        
    def decrementConnectionCount(self):
        """
        Decrese the connection count on the idlrpc server by one.
        """

        if not self.connected:
            raise Exception('No connection to idlrpc server.')
            
        IDL_RPCExecuteStr(self.client
                          ,b'IF ~ ISA(_pyidlrpc_connection_count) THEN _pyidlrpc_connection_count=0L')
        IDL_RPCExecuteStr(self.client
                          ,b'_pyidlrpc_connection_count -= 1')

        
    def getConnectionCount(self):
        """
        Return the number of active pyidlrpc connections on the idlrpc server
        """
        cdef IDL_VPTR vptr

        if not self.connected:
            raise Exception('No connection to idlrpc server.')
            
        IDL_RPCExecuteStr(self.client
                          ,b'IF ~ ISA(_pyidlrpc_connection_counter) THEN _pyidlrpc_connection_counter=0')
        vptr = IDL_RPCGetVariable(self.client, b'_pyidlrpc_connection_count')
        count = vptr.value.l

        return count

    
# ==============================================================================
# ==============================================================================
# Define the core pyidlrpc class
def _IDL_ExecuteStr(command_bytes):
    m_log.debug('Calling IDL_ExecuteStr')
    return IDL_ExecuteStr(command_bytes)


cdef IDL_VPTR _IDL_GetVariablePointer(varname_bytes):
    return IDL_FindNamedVariable(varname_bytes, False)


def _IDL_SetVariableScalar(varname_bytes, vartype, vardata):
    cdef IDL_VPTR vptr
    cdef IDL_STRING s
    cdef IDL_ALLTYPES varvalue

    vptr = IDL_FindNamedVariable(varname_bytes, 1)

    if vartype == IDL_TYP_BYTE:
        varvalue.c = vardata
    elif vartype == IDL_TYP_LONG:
        varvalue.l = vardata
    elif vartype == IDL_TYP_LONG64:
        varvalue.l = vardata
    elif vartype == IDL_TYP_FLOAT:
        varvalue.f = vardata
    elif vartype == IDL_TYP_DOUBLE:
        varvalue.d = vardata
    elif vartype == IDL_TYP_STRING:
        if isinstance(vardata, str):
            vardata_bytes = vardata.encode()
        else:
            vardata_bytes = vardata
        IDL_StrStore(&s, <char *> vardata_bytes)
        varvalue.str = s
    else:
        raise Exception('Unknown IDL data type: {}'.format(vartype))

    IDL_StoreScalar(vptr, vartype, &varvalue)


def _IDL_SetVariableArray(varname_bytes, vartype, ndarray):
    cdef IDL_VPTR vptr

    vptr = IDL_ImportNamedArray(
        varname_bytes
        ,np.PyArray_NDIM(ndarray)
        ,<IDL_LONG64 *> np.PyArray_DIMS(ndarray)
        ,vartype
        ,<UCHAR *> np.PyArray_DATA(ndarray)
        ,NULL
        ,NULL)

        
# ==============================================================================
# ============================================================================== 
cdef IDL_VPTR _IDLRPC_GetVariablePointer(varname_bytes):
    cdef _IDLRPCClient idlrpc
    idlrpc = _getIDLRPCClient()
    return IDL_RPCGetVariable(idlrpc.client, varname_bytes)


cdef _IDLRPC_ExecuteStr(command_bytes):
    cdef _IDLRPCClient idlrpc
    idlrpc = _getIDLRPCClient()
    m_log.debug('Calling IDL_RPCExecuteStr')
    status = IDL_RPCExecuteStr(idlrpc.client, command_bytes)

    # Make the returned status mean the same as IDL_ExecuteStr.
    if status == 0:
        raise Exception('Invalid command string.')
    elif status == 1:
        return 0
    else:
        return status
    

cdef _IDLRPC_SetVariableScalar(varname_bytes, vartype, vardata):    
    cdef IDL_VPTR vptr
    cdef IDL_STRING s
    
    cdef _IDLRPCClient idlrpc
    idlrpc = _getIDLRPCClient()

    vptr = IDL_RPCGettmp()

    vptr.type = vartype

    if vptr.type == IDL_TYP_BYTE:
        vptr.value.c = vardata
    elif vptr.type == IDL_TYP_LONG:
        vptr.value.l = vardata
    elif vptr.type == IDL_TYP_LONG64:
        vptr.value.l = vardata
    elif vptr.type == IDL_TYP_FLOAT:
        vptr.value.f = vardata
    elif vptr.type == IDL_TYP_DOUBLE:
        vptr.value.d = vardata
    elif vptr.type == IDL_TYP_STRING:
        if isinstance(vardata, str):
            vardata_bytes = vardata.encode()
        else:
            vardata_bytes = vardata
        IDL_RPCStrStore(&s, <char *> vardata_bytes)
        vptr.value.str = s
    else:
        raise Exception('Unknown IDL data type: {}'.format(vptr.type))

    status = IDL_RPCSetVariable(idlrpc.client, varname_bytes, vptr)

    return status


cdef _IDLRPC_SetVariableArray(varname_bytes, vartype, ndarray):
    cdef IDL_VPTR vptr

    cdef _IDLRPCClient idlrpc
    idlrpc = _getIDLRPCClient()

    vptr = IDL_RPCImportArray(np.PyArray_NDIM(ndarray)
                              ,<IDL_LONG64 *> np.PyArray_DIMS(ndarray)
                              ,vartype
                              ,<UCHAR *> np.PyArray_DATA(ndarray)
                              ,NULL)

    status = IDL_RPCSetVariable(idlrpc.client, varname_bytes, vptr)

    return status


# ==============================================================================
# ==============================================================================
# Define the core mirpyidl class    
cdef class PyIDLCore(object):
    """
    This is the core mirpyidl class that handles all of the  calls to the 
    idlrpc client C API that are needed for IDL execution and variable
    transfers.

    In general, this class should not be used directly; instead one should
    use the PyIDL class which contains advanced functionality written in
    python/IDL.

    This class does not handle creating and destroying idlrpc connections.
    Instead it simply grabs a client object.
    """

    cdef public long _id
    cdef public int idlrpc
    
    def __init__(self, use_idlrpc=False):
        """
        Get a reference to the module level idlrpc connection.
        """
        self._id = 0
        self.use_idlrpc = use_idlrpc
        
        if not self.use_idlrpc:
            # Initialize Callable IDL.
            InitializeIdl()
            

        self._id = self._requestNewInstanceId()

        
    def _requestNewInstanceId(self):
        """
        Get a new unique identifier for this mirpyidl instance.

        I need a way to identify which PyIDL object instance is interacting
        with the idlrpc server.

        This method allows the idlrpc server to keep track of a unique identifier
        for each PyIDL instance.
        """
        self.execute('IF ~ ISA(_mirpyidl_instance_counter) THEN _mirpyidl_instance_counter=0L')
        self.execute('_mirpyidl_instance_counter += 1')
        new_id = self.getVariable('_mirpyidl_instance_counter')

        m_log.debug('New PyIDL instance id: {}'.format(new_id))
        return new_id
    

    cdef IDL_VPTR _getVariablePointer(self, varname):
        varname_bytes = varname.encode()
        if self.use_idlrpc:
            return _IDLRPC_GetVariablePointer(varname_bytes)
        else:
            return _IDL_GetVariablePointer(varname_bytes)


    def _executeStr(self, command):
        command_bytes = command.encode()
        if self.use_idlrpc:
            return _IDLRPC_ExecuteStr(command_bytes)
        else:
            return _IDL_ExecuteStr(command_bytes)

        
    def _setVariableScalar(self, varname, vardata):
        vartype = self.getIDLType(vardata)   
        varname_bytes = varname.encode()
        
        if self.use_idlrpc:
            return _IDLRPC_SetVariableScalar(varname_bytes, vartype, vardata)
        else:
            return _IDL_SetVariableScalar(varname_bytes, vartype, vardata)


    def _setVariableArray(self, varname, ndarray):
        vartype = self.getTypeIDLFromNumpy(np.PyArray_TYPE(ndarray))        
        varname_bytes = varname.encode()
        
        if self.use_idlrpc:
            return _IDLRPC_SetVariableArray(varname_bytes, vartype, ndarray)
        else:
            return _IDL_SetVariableArray(varname_bytes, vartype, ndarray)
        

    def execute(self, command):
        """
        Execute a command in the IDLRPC session.

        The call to IDL_ExecuteStr does not give me the status code that I
        want, which is if there was an unrecovered error in the sent command.
        Instead the status code is whatever is in !ERROR_STATE.CODE.  That code
        however will tell me what the last error was, even if an error handler
        successfuly dealt with the error.

        To get around this I add on a MEASSAGE, /RESET to the end of every
        call. If there is an unrecoverd error, this will not get called and the
        status code will be returned correctly.  If the command completes, even
        with recoverd errors, then the status will be success.
        
        """
        m_log.debug('Sending command: {}'.format(command))

        command += " & MESSAGE, /RESET"
        status = self._executeStr(command)

        if status != 0:
            IDL_ExecuteStr(b"HELP, /TRACEBACK")
            IDL_ExecuteStr(b"RETALL")
            IDL_ExecuteStr(b"MESSAGE, /RESET")

            # Get a string for the returned IDL error code.
            temp_name = "_mirpyidl_id{}_message".format(self._id)
            message_command = '{} = STRMESSAGE({})'.format(temp_name, status)
            self._executeStr(message_command)
            message = self.getVariable(temp_name)
            m_log.error(message)
            
            raise IdlExecutionError('Error ({}) in executing command: {}'.format(status, command))


    def getVariable(self, varname):
        """
        Retrive a variable from the IDL session.

        Note: Certain types of structures apparently cannot be retrieved
              using IDL_RPCGetVariable. For now I need to catch all exceptions
              when trying to get structures, not only IdlTypeError.
        """
        cdef IDL_VPTR vptr
        vptr = self._getVariablePointer(varname)
        if vptr == NULL:
            raise IdlNameError("Varible does not exist in the IDL main scope: {}".format(varname))

        if vptr.flags & IDL_V_STRUCT:
            raise IdlTypeError("Structure variables are not currently supported.")
        elif vptr.flags & IDL_V_ARR:
            return self._getVariableArray(vptr)
        elif not (vptr.flags & IDL_V_NOT_SCALAR):
            return self._getVariableScalar(vptr)
        else:
            raise IdlTypeError("Only Scalar and Array variable currently supported.")


        
    cdef _getVariableScalar(self, IDL_VPTR vptr):
        
        if vptr.type == IDL_TYP_BYTE:
            return vptr.value.c
        elif vptr.type == IDL_TYP_INT:
            return vptr.value.i
        elif vptr.type == IDL_TYP_LONG:
            return vptr.value.l
        elif vptr.type == IDL_TYP_LONG64:
            return vptr.value.l
        elif vptr.type == IDL_TYP_FLOAT:
            return vptr.value.f
        elif vptr.type == IDL_TYP_DOUBLE:
            return vptr.value.d
        elif vptr.type == IDL_TYP_STRING:
            if vptr.value.str.slen > 0:
                return str(vptr.value.str.s)
            else:
                return ''
        else:
            raise IdlTypeError("IDL data type {} not yet supported.".format(vptr.type))


        
    cdef _getVariableArray(self, IDL_VPTR vptr):

        cdef IDL_STRING *s
            
        # Choose the correct numpy type that matches the IDL type.
        numpy_type = self.getTypeNumpyFromIDL(vptr.type)


        # I need to treat numerical arrays and strings differently.
        #
        # For strings the IDL variable only contains the memory addresses,
        # not the actual data.
        if numpy_type == np.NPY_STRING:
            
            string_list = []
            for ii in range(vptr.value.arr.n_elts):
                s = <IDL_STRING *> (vptr.value.arr.data + <int> ii*vptr.value.arr.elt_len)
                if s.slen > 0:
                    string_list.append(<char *>s.s)
                else:
                    string_list.append('')
                
            ndarray = np.array(string_list)


            shape = [vptr.value.arr.dim[ii] for ii in range(vptr.value.arr.n_dim)]
            ndarray = ndarray.reshape(shape)

        else:
            # Use the PyArray_SimpleNewFromData function from numpy to create a
            # new Python object pointing to the existing data
            ndarray = np.PyArray_SimpleNewFromData(vptr.value.arr.n_dim
                                                   ,<np.npy_intp *> vptr.value.arr.dim
                                                   ,numpy_type
                                                   ,<void *> vptr.value.arr.data)

        # Tell Python that it can deallocate the memory when the ndarray
        # object gets garbage collected
        # As the OWNDATA flag of an array is read-only in Python, we need to
        # call the C function PyArray_UpdateFlags
        #np.PyArray_UpdateFlags(ndarray, ndarray.flags.num | np.NPY_OWNDATA)
        
        return ndarray


    def setVariable(self, varname, vardata):
        
        if isinstance(vardata, np.ndarray):
            self._setVariableArray(varname, vardata)
        elif np.isscalar(vardata):
            self._setVariableScalar(varname, vardata)
        else:
            raise Exception, "Only scalar and array types can be assigned to IDL variables."


    def getTypeNumpyFromIDL(self, idl_type):

        if idl_type == IDL_TYP_BYTE:
            numpy_type = np.NPY_BYTE
        elif idl_type == IDL_TYP_INT:
            numpy_type = np.NPY_SHORT
        elif idl_type == IDL_TYP_LONG:
            numpy_type = np.NPY_INT
        elif idl_type == IDL_TYP_LONG64:
            numpy_type = np.NPY_LONG
        elif idl_type == IDL_TYP_FLOAT:
            numpy_type = np.NPY_FLOAT
        elif idl_type == IDL_TYP_DOUBLE:
            numpy_type = np.NPY_DOUBLE
        elif idl_type == IDL_TYP_STRING:
            numpy_type = np.NPY_STRING
        else:
            raise Exception, "No matching Numpy data type defined for given IDL type."

        return numpy_type
    

    def getIDLType(self, data):

        if isinstance(data, np.number):
            dtype = np.PyArray_DescrFromScalar(data)
            idl_type = self.getTypeIDLFromNumpy(dtype.type_num)
            
        elif isinstance(data, bool):
            idl_type = IDL_TYP_BYTE
        elif isinstance(data, int):
            idl_type = IDL_TYP_LONG
        elif isinstance(data, long):
            idl_type = IDL_TYP_LONG64
        elif isinstance(data, float):
            idl_type = IDL_TYP_DOUBLE
        elif isinstance(data, str):
            idl_type = IDL_TYP_STRING
        elif isinstance(data, str_builtin):
            idl_type = IDL_TYP_STRING
        else:
            raise Exception, "No matching IDL data type defined for given DATA type: {}".format(type(data))

        return idl_type

  
    def getTypeIDLFromNumpy(self, numpy_type):

        if numpy_type == np.NPY_BYTE:
            idl_type = IDL_TYP_BYTE
        elif numpy_type == np.NPY_SHORT:
            idl_type = IDL_TYP_INT
        elif numpy_type == np.NPY_INT:
            idl_type = IDL_TYP_LONG
        elif numpy_type == np.NPY_LONG:
            idl_type = IDL_TYP_LONG64
        elif numpy_type == np.NPY_FLOAT:
            idl_type = IDL_TYP_FLOAT
        elif numpy_type == np.NPY_DOUBLE:
            idl_type = IDL_TYP_DOUBLE
        elif numpy_type == np.NPY_STRING:
            idl_type = IDL_TYP_STRING
        else:
            raise Exception, "No matching IDL data type defined for given Numpy type: {}".format(numpy_type)

        return idl_type


# ==============================================================================
# ==============================================================================
# Define the user mirpyidl class.
    
class PyIDL(PyIDLCore):
    """
    Contains additional shortcut methods based on Python code.

    In particular this attempts to simplify wapping of IDL routines.
    It also provides a workaround for structure, list and hash passing.
    """

    def __init__(self, *args, **kwargs):
        PyIDLCore.__init__(self, *args, **kwargs)

        # Setup a pref
        self._id_prefix = '_mirpyidl_id{}'.format(self._id)

    
    def _getNewObjectId(self):
        """
        Get a new unique object identifier for this idlrpc session.

        \description
           I need a way to be able to create multiple objects in the idlrpc
           session.  It is also possible that multiple python processes could
           connect to the same idlrpc server.

           This method allows the idlrpc server to keep track of a unique idl
           object identifier number and retrieves that number.
        """
        self.execute('IF ~ ISA(_mirpyidl_object_counter) THEN _mirpyidl_object_counter=0L')
        self.execute('_mirpyidl_object_counter += 1')
        new_id = self.getVariable('_mirpyidl_object_counter')

        m_log.debug('New PyIDL object id: {}'.format(new_id))
        return new_id

    
    def newObject(self, name, params=None, keywords=None):
        """
        Create a new object and return a string identifier.

        parameters
        ----------
        
        function
          A string containing the object creation function.
          For example:  "OBJ_NEW"
        """
        
        obj_id = self._getNewObjectId()
        obj_name = '_mirpyidl_id{id}_obj{obj_id}'.format(id=self._id, obj_id=obj_id)

        self.callMethod(name
                        ,params=params
                        ,keywords=keywords
                        ,function=True

                        ,result_name=obj_name
                        ,return_result=False
                        ,cleanup=False)

        return obj_name

    
    def destroyObject(self, object_name):
        """
        Destroy the given IDL object.
        """
        if not object_name is None:
            command = 'IF OBJ_VALID({name}) THEN OBJ_DESTROY, {name}'.format(name=object_name)
            self.execute(command)

        
    def callMethod(self
                   ,name
                   ,params=None
                   ,keywords=None
                   ,function=False
                   ,object_name=None

                   ,result_name=None
                   ,return_result=True
                   ,cleanup=True):
        """
        Call an idl subroutine or method.


        result_name (string)
            default = None
            
            The name of the temporary result variable to use in the IDL function call.
            If None, a temporary name will be automatically generated.

        return_result (bool)
            default = True

            If true, and function=True, then retrieve and return the result from IDL. 
            If false, then do not return the result. 

            This option is used internally for object creation.
             
        cleanup (bool)
            default = True

            If true the result from a function call will be deleted in the IDL session.
            
            This object is used internally for object creation
        """
                
        
        # Set the params variables:
        if params:
            param_names = ['_mirpyidl_id{}_param_{}'.format(self._id, str(x)) for x in range(len(params))]
            params_string = ', '.join(param_names)
            for ii, value in enumerate(params):
                if value is not None:
                    if isinstance(value, dict):
                        self.setStructure(param_names[ii], value)
                    else:
                        self.setVariable(param_names[ii], value)
        else:
            params_string = ''

        # Set the keywords variables:
        if keywords:
            key_names = ['_mirpyidl_id{}_key_'.format(self._id)+key for key in keywords.keys()]
            keywords_string = ', '.join([key+"="+key_names[ii] for ii, key in enumerate(keywords.keys())])
            for ii, value in enumerate(keywords.values()):
                if isinstance(value, dict):
                    self.setStructure(key_names[ii], value)
                else:
                    self.setVariable(key_names[ii], value)
        else:
            keywords_string = ''


        # ----------------------------------------------------------------------
        # Create the command string.
        command = ''

        if function:
            # Generate a temporary name for the result if needed.
            if result_name is None:
                result_name = '_mirpyidl_id{id}_fresult'.format(id=self._id)
            command += result_name+' = '

        if object_name is not None:
            command += object_name+'.'

        command += name
        if function:
            command += '('
        else:
            command += ', '

        # Join the param and keywords strings, filter out empty strings.
        command += ', '.join(filter(None, [params_string, keywords_string]))

        if function:
            command += ')'

        # ----------------------------------------------------------------------
        # Send the command.
        self.execute(command)


        # ----------------------------------------------------------------------
        # Retrive the results.
        if function and return_result:
            # Get the result variable if this   was a fuction.
            ret_value = self.getVariable(result_name)

            if cleanup:
                # Cleanup by deleting the temporary result variable.
                self.deleteVariable(result_name)


        # ----------------------------------------------------------------------
        # Clean up the params and keyword temporary variables from IDL.
        if params:
            for ii, value in enumerate(params):
                if value is not None:
                    self.deleteVariable(param_names[ii])

        if keywords:
            for key in key_names:
                self.deleteVariable(key)


        # ----------------------------------------------------------------------
        # finally return the function value.
        if function and return_result:
            return ret_value

        
    def callFunction(self, name, params=None, keywords=None):
        """
        A shortcut routine to call IDL functions.

        This just calls :py:meth:`callMethod` with the options appropriate for
        an IDL function.
        """
        return self.callMethod(name
                                ,params=params
                                ,keywords=keywords
                                ,function=True)
        
    def callPro(self, name, params=None, keywords=None):
        """
        A shortcut routine to call IDL procedure.

        This just calls :py:meth:`callMethod` with the options appropriate for
        an IDL procedure.
        """
        self.callMethod(name
                        ,params=params
                        ,keywords=keywords
                        ,function=False)
        
    def isStructure(self, name):
        temp = '_mirpyidl_id{id}_tmp_'.format(id=self._id)
        self.execute('{} = ISA({}, "struct")'.format(temp, name))
        return self.getVariable(temp)


    def isHash(self, name):
        temp = '_mirpyidl_id{id}_tmp_'.format(id=self._id)
        self.execute('{tmp} = (OBJ_VALID({name}) ? OBJ_ISA({name}, "HASH") : 0)'.format(tmp=temp, name=name))
        return self.getVariable(temp)


    def getVariable(self, name, **kwargs):
        """
        Get a varible from the idlrpc server.  Check for complex types. 
        """

        # I want this to be as efficent as possible when retriving
        # arrays and scalars.  My methods for retriveing structures and
        # hash objects uses alot of string manipulation and are probably
        # a bit slow.
        try:
            output = super(PyIDL, self).getVariable(name)
        except IdlTypeError:      
            if self.isStructure(name):
                output = self.getStructure(name, **kwargs)
            elif self.isHash(name):
                output = self.getHash(name, **kwargs)
            else:
                raise IdlTypeError('Variable {} has an unknown IDL data type.'.format(name))
        except:
            raise

        return output


    def deleteVariable(self, name, **kwargs):
        """
        Delete a variable from the idlrpc server.
        """

        self.execute("DELVAR, {name}".format(name=name))

                
    def getStructure(self, name, recursive=False):
        """
        I do not have a way to actually pass structures from IDL to python.
        In fact, without rebuilding the idl_rpc client/server I can't even
        see that I am requesting a structure.
        
        This is a work around.  Not particularly efficent.
        """

        tempname = '_mirpyidl_id{id}_tmp_'.format(id=self._id)
        self.execute("{tmp} = TAG_NAMES({name})".format(tmp=tempname, name=name))
        tag_names = self.getVariable(tempname)

        output = {}
        for tag in tag_names:
            varname = "_mirpyidl_id{id}_{st}_{tag}".format(id=self._id, st=name, tag=tag)
            self.execute("{var} = {st}.{tag}".format(var=varname, st=name, tag=tag))
            output[tag] = self.getVariable(varname, recursive=recursive)
            self.deleteVariable(varname)

        return output


    def setStructure(self, name, input_dict):
        """
        Create a structure in IDL from  dictionary in Python.
        
        I cannot directly pass structures to IDL at this point since the
        structure definition is proprietary.  The tools that IDL provides
        requireds that the IDL interpreter is running, which is not an option.   
        """
        for key, value in input_dict.iteritems():
            self.setVariable('_mirpyidl_id{}_{}'.format(self._id, key), value)
            
        command = ', '.join([key+":"+'TEMPORARY(_mirpyidl_id{}_{})'.format(self._id, key) for key in input_dict.keys()])
        command = name+" = {"+command+"}"
        self.execute(command)

        
    def getHash(self, name, recursive=False):
        """
        I do not have a way to actually pass hash objects from IDL to python.
        In fact, without rebuilding the idl_rpc client/server I can't even
        see that I am requesting an object.
        
        This is a work around.  Not particularly efficent.

        \warning
          This will only work if all of the hash tags are strings.
          
        \warning
          This will probably fail if the hash that is being retrieved is empty.
        """

        tempname = '_mirpyidl_id{id}_tmp_'.format(id=self._id)
        self.execute("{tmp} = ({name}.keys()).toArray()".format(tmp=tempname, name=name))
        tag_names = self.getVariable(tempname)

        output = {}
        for tag in tag_names:
            varname = "_mirpyidl_id{id}_{name}_{tag}".format(id=self._id, name=name, tag=tag)
            self.execute("{var} = {name}['{tag}']".format(var=varname, name=name, tag=tag))
            output[tag] = self.getVariable(varname, recursive=recursive)
            self.deleteVariable(varname)

        return output

                                 

    # ==========================================================================
    # ==========================================================================
    # Method shortcuts.
    # ==========================================================================
    # ==========================================================================

    
    def ex(self, command):
        """A shortcut to the execute method."""
        self.execute(command)

    def get(self, varname):
        """A shortcut to the getVariable method."""
        return self.getVariable(varname)

    def set(self, varname, vardata):
        """A shortcut to the setVariable method."""
        self.setVariable(varname, vardata)


        
# ==============================================================================
# ==============================================================================
# Create a IDL object wrapper class

class PyIDLObject(object):
    """
    This is base class to use when wrapping IDL object. All python wrapper
    object should inherit from this class.

    This class mostly just takes care of handling the mirpyidl object id
    so that it does not need to be delt with explicitly when wrapping.
    """

    _creation_command = None
    _creation_params = None
    _creation_kewords = None
    
    def __init__(self):
        """
        The constructor for the PyIDLObject.  If a creation command has been
        set, then this will also create the IDL object.
        """

        # Create a PyIDL connection object.
        self._idl = self._getPyIDL()
        self._object_name = None

        # Initialize the IDL object.
        if self._creation_command is not None:
            self._initObject(self._creation_command
                             ,self._creation_params
                             ,self._creation_keywords)

    
    def __del__(self):
        """
        The destructor for this object. This also destroys the IDL object.
        """
        self._idl.destroyObject(self._object_name)

        
    def _getPyIDL(self):
        """Return the PyIDL object. This is separated to simplify sublcassing."""
        return PyIDL()

    
    def _initObject(self, command, params, keywords):
        """
        Initialize the IDL object using the given command.

        
        programming notes
        -----------------
        
        I've kept this separate from the __init__ method just incase any
        subclasses need to do something fancy for object initialization.
        """
        self._object_name = self._idl.newObject(command, params, keywords)

        
    def callMethod(self 
                   ,name
                   ,params=None
                   ,keywords=None
                   ,function=False):
        """
        Call a method of this object.

        This is simply a wrapper of :py:class:`PyIDL`, except that the object
        name is automaically provided. 
        """
        return self._idl.callMethod(name
                                     ,object_name=self._object_name
                                     ,params=params
                                     ,keywords=keywords
                                     ,function=function)

        
    def callMethodFunction(self, name, params=None, keywords=None):
        """
        Call a function method of the object.
         
        This is simply a wrapper of :py:meth:`callMethod` but with the 
        appropriate options for a function.
        """

        return self.callMethod(name
                               ,params=params
                               ,keywords=keywords
                               ,function=True)

        
    def callMethodPro(self, name, params=None, keywords=None):
        """
        Call a procedure method of the object.
         
        This is simply a wrapper of :py:meth:`callMethod` but with the 
        appropriate options for a procedure.
        """

        return self.callMethod(name
                               ,params=params
                               ,keywords=keywords
                               ,function=False)


# ==============================================================================
# ==============================================================================
# Define exception classes
class IdlTypeError(TypeError):
    pass

class IdlNameError(NameError):
    pass

class IdlExecutionError(RuntimeError):
    pass

class IdlConnectionError(RuntimeError):
    pass
    
# ==============================================================================
# ==============================================================================
# Setup conifiguration for module level logging.
logging.basicConfig()
setLoggingLevel(logging.INFO)
