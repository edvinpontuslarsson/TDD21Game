import os
import sys
import unittest

currentWorkingDirectory = os.getcwd()
sys.path.append(currentWorkingDirectory + '/card_game/')

import app


# TODO: use unittest instead
# def test_ping_should_pong():
#     assert app.ping() == 'pong'

class TestApp(unittest.TestCase):

    def test_ping_should_pong(self):
        response = app.ping()
        self.assertEqual(response, 'pong')


if __name__ == '__main__':
    unittest.main()

