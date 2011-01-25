
"""
Utilities for the OpenFlow test framework
"""

import random
import oftest.message as message

def gen_xid():
    return random.randrange(1,0xffffffff)

def of_error_msg_make(type, code, data):
    """ Construct a new ofp_error message
    
    @param type one of ofp.OFPET_*
    @param code an error code, corresponding to the type
    @param data either a string or an ofp_message
    
    #@todo should probably move into oftest.messages, BUT that's autogenerated code!
    """
    err = message.error()
    err.type = type
    err.code = code
    if isinstance(data,str):
        err.data = data
    else:
        err.data= data.pack()
    return err