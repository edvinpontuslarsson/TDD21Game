import os
import sys
import unittest

currentWorkingDirectory = os.getcwd()
sys.path.append(currentWorkingDirectory + '/card_game/')

import app

class TestApp(unittest.TestCase):

    def test_ping_should_pong(self):
        self.assertNotEqual(app.ping(), 'ping')
        self.assertEqual(app.ping(), 'pong')


if __name__ == '__main__':
    unittest.main()

