"""
This module use for storing constants.

Constants
---------
MAX_LEN: int
    Maximum length received socket data.
ENC: str
    Encoding for coding data.
DEFAULT_PORT: int
    Default port for making a socket connection.
DEFAULT_IP_ADDRESS: str
    Default ip-address for socket connection.
MAX_CONNECT: int
    Maximum connections per socket in queue connections.
ACT: str
    JSON format field 'action'.
TIME: str
    JSON format field 'time'.
USER: str
    JSON format field 'user'.
TO: str
    JSON format field 'to'.
FROM: str
    JSON format field 'from'.
AC_NAME: str
    JSON format field 'account_name'.
PRESENCE: str
    JSON format field 'presence'.
MESSAGE: str
    JSON format field 'message'.
RESPONSE: str
    JSON format field 'response'.
ERROR: str
    JSON format field 'error'.
ALERT: str
    JSON format field 'alert'.
GET_CONTACTS: str
    JSON format field 'get_contacts'.
ADD_CONTACT: str
    JSON format field 'add_contact'.
DEL_CONTACT: str
    JSON format field 'del_contact'.
USER_ID: str
    JSON format field 'user_id'.
DEFAULT_PATH_SERVER: str
    Default path to server database.
DEFAULT_PATH_CLIENT: str
    Default path to client database.
DEFAULT_MODE: str
    Default mode of the module client.py.
MODE: str
    JSON format field 'mode'.
CHECK_CLIENT: str
    JSON format field 'check_client'.
PASSWORD: str
    JSON format field 'password'.
SALT: str
    JSON format field 'salt'.
LOG_LVL: int
    Logging level of the logging module.
"""

import logging

MAX_LEN = 1024
ENC = 'utf-8'
DEFAULT_PORT = 7777
DEFAULT_IP_ADDRESS = '127.0.0.1'
MAX_CONNECT = 5
ACT = 'action'
TIME = 'time'
USER = 'user'
TO = 'to'
FROM = 'from'
AC_NAME = 'account_name'
PRESENCE = 'presence'
MESSAGE = 'message'
RESPONSE = 'response'
ERROR = 'error'
ALERT = 'alert'
GET_CONTACTS = 'get_contacts'
ADD_CONTACT = 'add_contact'
DEL_CONTACT = 'del_contact'
USER_ID = 'user_id'
DEFAULT_PATH_SERVER = 'storage_server.db'
DEFAULT_PATH_CLIENT = 'storage_client.db'
DEFAULT_MODE = 'console'
MODE = 'mode'
CHECK_CLIENT = 'check_client'
PASSWORD = 'password'
SALT = 'salt'
LOG_LVL = logging.DEBUG
