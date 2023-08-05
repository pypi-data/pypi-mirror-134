"""
This module testing func.py module.

Classes
-------
Sock
    Imitation of a socket class.
SockString
    Imitation of a socket class for return string.
SockBytes
    Imitation of a socket class for return bytes.
TestFunc(unittest.TestCase)
    Testing the correct works functions ``send_msg`` and ``get_msg``.
"""

import unittest

from common.func import *


class Sock:
    """
    This class imitation socket class.

    Methods
    -------
    send(msg_bytes)
        Adds the received data ``msg_bytes`` to list ``b``.
    recv(max_len)
        Imitation receive socket data by meaningless calculations with ``max_len`` and return first value of ``b`` list.
    b
        Return list ``b``.
    """

    def __init__(self):
        """
        This class constructor create empty list ``b``.

        Parameters
        ----------
        b
            Empty list.
        """
        self.b = []

    def send(self, msg_bytes):
        """
        This method add ``msg_bytes`` in ``b`` list.

        Parameters
        ----------
        b.append(msg_bytes)
            Add ``msg_bytes`` in ``b`` list.
        """
        self.b.append(msg_bytes)

    def recv(self, max_len):
        """
        This method imitates receiving socket data and return value first element ``b`` list.

        Parameters
        ----------
        max_len
            Meaningless calculations.

        Returns
        -------
        socket data
            Value first element list ``b``.
        """
        max_len += max_len
        return self.b[0]

    def b(self):
        """
        This method return list ``b``.

        Returns
        -------
        list data
            List ``b``.
        """
        return self.b


class SockString:
    """
    This class imitation received value ``str`` data type.

    Methods
    ----------
    recv(max_len)
        Imitation receive socket data by meaningless calculations with ``max_len`` and return 'not valid'.
    """

    def __init__(self):
        """
        This class constructor does nothing.
        """
        pass

    @staticmethod
    def recv(max_len):
        """
        This method imitates receiving socket data and return 'not valid'.

        Parameters
        ----------
        max_len
            Meaningless calculations.

        Returns
        -------
        str
            String 'not valid'
        """
        max_len += max_len
        return 'not valid'


class SockBytes:
    """
    This class imitation received value ``bytes`` data type.

    Methods
    -------
    recv(max_len)
        Imitation receive socket data by meaningless calculations with ``max_len`` and return byte data type.
    """

    def __init__(self):
        """
        This class constructor does nothing.
        """
        pass

    @staticmethod
    def recv(max_len):
        """
        This method imitates receiving socket data and return byte data type.

        Parameters
        ----------
        max_len
            Meaningless calculations.

        Returns
        -------
        bytes
            Byte string 'not valid'.
        """
        max_len += max_len
        return b'not valid'


class TestFunc(unittest.TestCase):
    """
    This class extend parent and testing function ``send_msg`` and ``get_msg`` from func.py module.

    Methods
    -------
    test_send_msg_valid
        Comparison of two identical data of the ``dict`` type conversion to bytes.
    test_send_msg_isinstance
        Checking the conversion of the ``send_msg`` function of data of the ``dict`` type to data of the ``bytes`` type.
    test_get_msg_valid
        Comparison of the received data of the ``get_msg`` function with data of the ``dict`` type.
    test_get_msg_isinstance
        Comparison of the received data of the ``get_msg`` function with ``dict`` type.
    test_get_msg_not_bytes
        Calling the ``ValueError`` exception when calling the ``get_msg`` function with received data of type ``str``.
    test_get_msg_not_json_bytes
        Calling the ``ValueError`` exception when calling the ``get_msg`` function with received data of type ``bytes``.
    """

    sock = Sock()
    send_msg(sock, {'cat': 'murk'})
    sock_string = SockString()
    sock_bytes = SockBytes()

    def test_send_msg_valid(self):
        """
        This method comparison of two identical data of the ``dict`` type conversion to bytes via function ``send_msg``.

        Parameters
        ----------
        assertEqual
            Check for equivalence of data received via the ``send_msg`` and ``json.dumps`` functions.
        """
        self.assertEqual(self.sock.b[0], json.dumps({'cat': 'murk'}).encode(ENC))

    def test_send_msg_isinstance(self):
        """
        This method check the data received using the ``send_msg`` function with the ``bytes`` data type.

        Parameters
        ----------
        assertIsInstance
            Check the data received using the ``send_msg`` function with the ``bytes`` data type.
        """
        self.assertIsInstance(self.sock.b[0], bytes)

    def test_get_msg_valid(self):
        """
        This method check the data received using the ``get_msg`` function with the ``dict`` data type.

        Parameters
        ----------
        assertEqual
            Check the data received using the ``get_msg`` function with the ``dict`` data type.
        """
        self.assertEqual(get_msg(self.sock), {'cat': 'murk'})

    def test_get_msg_isinstance(self):
        """
        This method compliance check  the data received using the ``get_msg`` function with the ``dict`` data type.

        Parameters
        ----------
        assertEqual
            Compliance check the data received using the ``get_msg`` function with the ``dict`` data type.
        """
        self.assertIsInstance(get_msg(self.sock), dict)

    def test_get_msg_not_bytes(self):
        """
        This method check for the ``ValueError`` exception when passing data of the ``str`` type ``get_msg`` function.

        Parameters
        ----------
        assertRaises
            Check for the ``ValueError`` exception when passing data of the ``str`` type ``get_msg`` function.
        """
        self.assertRaises(ValueError, get_msg, self.sock_string)

    def test_get_msg_not_json_bytes(self):
        """
        This method check for the ``ValueError`` exception when passing data of the ``bytes`` type ``get_msg`` function.

        Parameters
        ----------
        assertRaises
            Check for the ``ValueError`` exception when passing data of the ``bytes`` type ``get_msg`` function.
        """
        self.assertRaises(ValueError, get_msg, self.sock_bytes)


if __name__ == '__main__':
    unittest.main()
