"""
This module testing server.py module.

Classes
-------
TestServer(unittest.TestCase)
    Extend parent and testing forming message JIM format.
"""

import unittest

from server import *


class TestServer(unittest.TestCase):
    """
    This class extend parent and testing forming message JIM format.

    Methods
    -------
    test_process_client_msg_200_valid
        Checking the messages using the ``process_client_msg`` function with the standard.
    test_process_client_msg_200_in
        Checking the messages using the ``process_client_msg`` function for the occurrence of the key ``RESPONSE``.
    test_process_client_msg_200_isinstance
        Check the data received using the ``process_client_msg`` function with the ``dict`` data type.
    test_process_client_msg_400_isinstance
        Check the incorrect data received using the ``process_client_msg`` function with the ``dict`` data type.
    test_process_client_msg_400_valid
        Check the incorrect data using the ``process_client_msg`` function the occurrence keys ``RESPONSE``, ``ERROR``.
    test_process_client_msg_without_keys_1
        Check the incorrect data using the ``process_client_msg`` for the correct messenger server answer.
    test_process_client_msg_without_keys_2
        Check the incorrect data using the ``process_client_msg`` for the correct messenger server answer.
    test_process_client_msg_act_not_presence
        Check the incorrect data using the ``process_client_msg`` for the correct messenger server answer.
    """

    answer_not_valid = {RESPONSE: 400, ERROR: 'Bad request'}

    def test_process_client_msg_200_valid(self):
        """
        This method checking the messages using the ``process_client_msg`` function with the standard.

        Parameters
        ----------
        server_test
            Start the messenger server in testing mode.
        msg
            Correct message JIM format.
        answer
            Call the ``process_client_msg`` function and passing the ``msg`` message to it.
        assertEqual
            Check for equivalence of data received via the ``process_client_msg`` and correct message JIM format.
        """
        server_test = Server(True, f'../{DEFAULT_PATH_SERVER}')
        msg = {ACT: PRESENCE, TIME: time.time(), USER: {AC_NAME: 'Tim'}}
        answer = server_test.obj.process_client_msg(msg)
        self.assertEqual(answer, {RESPONSE: 200, SALT: '53b7f5ee3119f1e28f7d359c92c288c5'})

    def test_process_client_msg_200_in(self):
        """
        This method checking using the ``process_client_msg`` function for the occurrence of the key ``RESPONSE``.

        Parameters
        ----------
        server_test
            Start the messenger server in testing mode.
        msg
            Correct message JIM format.
        answer
            Call the ``process_client_msg`` function and passing the ``msg`` message to it.
        assertIn
            Check for occurrence of data received via the ``process_client_msg`` key ``RESPONSE``.
        """
        server_test = Server(True, f'../{DEFAULT_PATH_SERVER}')
        msg = {ACT: PRESENCE, TIME: time.time(), USER: {AC_NAME: 'Tim'}}
        answer = server_test.obj.process_client_msg(msg)
        self.assertIn(RESPONSE, answer)

    def test_process_client_msg_200_isinstance(self):
        """
        This method checking using the ``process_client_msg`` function for compliance with the ``dict`` data type.

        Parameters
        ----------
        server_test
            Start the messenger server in testing mode.
        msg
            Correct message JIM format.
        answer
            Call the ``process_client_msg`` function and passing the ``msg`` message to it.
        assertIsInstance
            Check for compliance with the ``dict`` data type of data received via the ``process_client_msg`` function.
        """
        server_test = Server(True, f'../{DEFAULT_PATH_SERVER}')
        msg = {ACT: PRESENCE, TIME: time.time(), USER: {AC_NAME: 'Tim'}}
        answer = server_test.obj.process_client_msg(msg)
        self.assertIsInstance(answer, dict)

    def test_process_client_msg_400_isinstance(self):
        """
        This method checking using the ``process_client_msg`` function for compliance with the ``dict`` data type.

        Parameters
        ----------
        server_test
            Start the messenger server in testing mode.
        msg
            Incorrect message JIM format.
        answer
            Call the ``process_client_msg`` function and passing the ``msg`` message to it.
        assertIsInstance
            Check for compliance with the ``dict`` data type of data received via the ``process_client_msg`` function.
        """
        server_test = Server(True, f'../{DEFAULT_PATH_SERVER}')
        msg = {ACT: PRESENCE}
        answer = server_test.obj.process_client_msg(msg)
        self.assertIsInstance(answer, dict)

    def test_process_client_msg_400_valid(self):
        """
        This method checking using the ``process_client_msg`` function  for occurrence keys ``ERROR`` and ``RESPONSE``.

        Parameters
        ----------
        server_test
            Start the messenger server in testing mode.
        msg
            Incorrect message JIM format.
        answer
            Call the ``process_client_msg`` function and passing the ``msg`` message to it.
        assertIn
            Check using the ``process_client_msg`` function  for occurrence keys ``ERROR`` and ``RESPONSE``.
        """
        server_test = Server(True, f'../{DEFAULT_PATH_SERVER}')
        msg = {ACT: PRESENCE}
        answer = server_test.obj.process_client_msg(msg)
        self.assertIn(ERROR and RESPONSE, answer)

    def test_process_client_msg_without_keys_1(self):
        """
        This method checking the messages using the ``process_client_msg`` function with the standard.

        Parameters
        ----------
        server_test
            Start the messenger server in testing mode.
        msg
            Incorrect message JIM format.
        answer
            Call the ``process_client_msg`` function and passing the ``msg`` message to it.
        assertEqual
            Check using the ``process_client_msg`` function  for compliance standard answer.
        """
        server_test = Server(True, f'../{DEFAULT_PATH_SERVER}')
        msg = {ACT: PRESENCE}
        answer = server_test.obj.process_client_msg(msg)
        self.assertEqual(answer, self.answer_not_valid)

    def test_process_client_msg_without_keys_2(self):
        """
        This method checking the messages using the ``process_client_msg`` function with the standard.

        Parameters
        ----------
        server_test
            Start the messenger server in testing mode.
        msg
            Incorrect message JIM format.
        answer
            Call the ``process_client_msg`` function and passing the ``msg`` message to it.
        assertEqual
            Check using the ``process_client_msg`` function  for compliance standard answer.
        """
        server_test = Server(True, f'../{DEFAULT_PATH_SERVER}')
        msg = {ACT: PRESENCE, TIME: time.time()}
        answer = server_test.obj.process_client_msg(msg)
        self.assertEqual(answer, self.answer_not_valid)

    def test_process_client_msg_act_not_presence(self):
        """
        This method checking the messages using the ``process_client_msg`` function with the standard.

        Parameters
        ----------
        server_test
            Start the messenger server in testing mode.
        msg
            Incorrect message JIM format.
        answer
            Call the ``process_client_msg`` function and passing the ``msg`` message to it.
        assertEqual
            Check using the ``process_client_msg`` function  for compliance standard answer.
        """
        server_test = Server(True, f'../{DEFAULT_PATH_SERVER}')
        msg = {ACT: 'dog', TIME: time.time(), USER: {AC_NAME: 'Guest'}}
        answer = server_test.obj.process_client_msg(msg)
        self.assertEqual(answer, self.answer_not_valid)


if __name__ == '__main__':
    unittest.main()
