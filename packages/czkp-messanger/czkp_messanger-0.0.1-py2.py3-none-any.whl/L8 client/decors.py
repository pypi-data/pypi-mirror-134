"""
This module use for decorators.

Functions
---------
log
    Decorator defines which module is used and records logs.
login_required
    Decorator defines whether the user authorized.

Classes
-------
Log
    Decorator defines which module is used and records logs.
"""

import traceback
import inspect
import re
from functools import wraps

from log.conf.client_log_config import *
from log.conf.server_log_config import *


def log(func):
    """This function return ``wrapper`` wrapper function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        This function defines which module is used and records logs.

        Parameters
        ----------
        filename
            Info about the module being launched.
        logger
            Logging object.
        ret_func
            Decorator wrapped function.
        logger.debug
            Record a message 'called function name: {func.__name__}, ...' through a logger object at debug level.

        Returns
        -------
        Function object
            Decorator wrapped function.
        """
        global logger
        filename = inspect.getfile(func)
        if re.findall('server.py', filename):
            logger = logging.getLogger('chat.server')
        elif re.findall('client.py', filename):
            logger = logging.getLogger('chat.client')
        ret_func = func(*args, **kwargs)
        logger.debug(f'called function name: {func.__name__}, args: {args}, kwargs: {kwargs}, return: {ret_func} '
                     f'from (inspect): {inspect.stack()[1][3]}() and '
                     f'equal from (traceback): {traceback.format_stack()[0].split()[-1]} and '
                     f'equal from (sys): {sys._getframe(1).f_code.co_name}()', stacklevel=2)
        return ret_func
    return wrapper


class Log:
    """
    This class defines which module is used and records logs.
    """

    def __call__(self, func):
        """This method return ``c_wrapper`` wrapper function."""

        @wraps(func)
        def c_wrapper(*args, **kwargs):
            """
            This function defines which module is used and records logs.

            Parameters
            ----------
            filename
                Info about the module being launched.
            logger
                Logging object.
            ret_func
                Decorator wrapped function.
            logger.debug
                Record a message 'called function name: {func.__name__}, ...' through a logger object at debug level.

            Returns
            -------
            Function object
                Decorator wrapped function.
            """
            global logger
            filename = inspect.getfile(func)
            if re.findall('server.py', filename):
                logger = logging.getLogger('chat.server')
            elif re.findall('client.py', filename):
                logger = logging.getLogger('chat.client')
            ret_func = func(*args, **kwargs)
            logger.debug(f'called function name: {func.__name__}, args: {args}, kwargs: {kwargs}, return: {ret_func} '
                         f'from (inspect): {inspect.stack()[1][3]}() and '
                         f'equal from (traceback): {traceback.format_stack()[0].split()[-1]} and '
                         f'equal from (sys): {sys._getframe(1).f_code.co_name}()', stacklevel=2)
            return ret_func
        return c_wrapper


def login_required(func):
    """This function return ``wrapper`` wrapper function."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        This function determines whether the user is authorized.

        Parameters
        ----------
        login_required_func
            Decorator wrapped function.

        Returns
        -------
        Function object
            Decorator wrapped function.
        """
        if args[0].authorized is True:
            login_required_func = func(*args, **kwargs)
        else:
            return print('User do not authorized')
        return login_required_func
    return wrapper
