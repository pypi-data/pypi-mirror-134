"""
This module use for send and get data via socket.

Functions
---------
get_msg (socket object)
    Gets data from a socket.
send_msg (socket object, dict)
    Sends data via socket.
"""

import json

from common.settings import MAX_LEN, ENC


def get_msg(sock):
    """
    Function gets data from a socket.

    She gets socket data with length constant MAX_LEN. Checked received data on matching per bytes. If passed
    verification - doing decode data with encoding constant ENC and converted to json format, otherwise - raise
    exception ValueError. Then it is checked json data for compliance with the data type - dict. If successful - return
    this data, otherwise - exception ValueError.

    Parameters
    ----------
    sock
        Socket object.

    Returns
    -------
    dict
        Json data.

    Raises
    ------
    ValueError
        If the socket data has not passed the byte data type check and the JSON data has not passed the dictionary data
        type check.
    """
    enc_response = sock.recv(MAX_LEN)
    if isinstance(enc_response, bytes):
        response = json.loads(enc_response.decode(ENC))
        if isinstance(response, dict):
            return response
        raise ValueError
    raise ValueError


def send_msg(sock, msg):
    """
    Function sends data via socket.

    Message converting to json data, encode in encoding constant ENC and sent via socket.

    Parameters
    ----------
    sock
        Socket object.
    msg: dict
        Message created on JIM protocol.
    """
    j_msg = json.dumps(msg)
    enc_msg = j_msg.encode(ENC)
    sock.send(enc_msg)
