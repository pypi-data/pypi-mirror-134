"""
This module testing client.py module.

Classes
-------
TestClient(unittest.TestCase)
    Testing the correct formation of messages in the JIM format.
"""

import unittest

from client import *


class TestClient(unittest.TestCase):
    """
    This class extend parent and testing the correct formation of messages in the JIM format client.py module.

    Methods
    -------
    test_presence_default
        Test of compliance with the sample of the presence message JIM formats with default login.
    test_presence_name
        Test of compliance with the sample of the presence message JIM formats with passed login.
    test_presence_default_isinstance
        Test of compliance with the sample of the presence message JIM formats to the ``dict`` type with default login.
    test_presence_name_isinstance
        Test of compliance with the sample of the presence message JIM formats to the ``dict`` type with passed login.
    """

    def test_presence_default(self):
        """
        This method testing compliance with the sample of the presence message JIM formats with default login.

        Parameters
        ----------
        client_test
            Instance class ``Client`` with arguments needs for runs test.
        presence
            Message JIM format created via call method ``create_presence()`` ``client_test`` object.
        assertEqual
            Check the equivalence of the ``presence`` message for compliance with the requirements for it.
        """
        client_test = Client(True, 'Tim', 'Tim')
        presence = client_test.obj.create_presence()
        self.assertEqual({ACT: PRESENCE, TIME: presence['time'], USER: {AC_NAME: 'Guest'}, MODE: DEFAULT_MODE},
                         presence)

    def test_presence_name(self):
        """
        This method testing compliance with the sample of the presence message JIM formats with passed login.

        Parameters
        ----------
        client_test
            Instance class ``Client`` with arguments needs for runs test.
        presence
            Message JIM format created via call method ``create_presence('new_user')`` ``client_test`` object.
        assertEqual
            Check the equivalence of the ``presence`` message for compliance with the requirements for it.
        """
        client_test = Client(True, 'Tim', 'Tim')
        presence = client_test.obj.create_presence('new_user')
        self.assertEqual({ACT: PRESENCE, TIME: presence['time'], USER: {AC_NAME: 'new_user'}, MODE: DEFAULT_MODE},
                         presence)

    def test_presence_default_isinstance(self):
        """
        This method testing compliance with the sample of the presence message to the ``dict`` type with default login.

        Parameters
        ----------
        client_test
            Instance class ``Client`` with arguments needs for runs test.
        presence
            Message JIM format created via call method ``create_presence()`` ``client_test`` object.
        assertIsInstance
            Check the ``presence`` message for compliance on ``dict`` data type.
        """
        client_test = Client(True, 'Tim', 'Tim')
        presence = client_test.obj.create_presence()
        self.assertIsInstance(presence, dict)

    def test_presence_name_isinstance(self):
        """
        This method testing compliance with the sample of the presence message to the ``dict`` type with default login.

        Parameters
        ----------
        client_test
            Instance class ``Client`` with arguments needs for runs test.
        presence
            Message JIM format created via call method ``create_presence('new_user')`` ``client_test`` object.
        assertIsInstance
            Check the ``presence`` message for compliance on ``dict`` data type.
        """
        client_test = Client(True, 'Tim', 'Tim')
        presence = client_test.obj.create_presence('new_user')
        self.assertIsInstance(presence, dict)


if __name__ == '__main__':
    unittest.main()
