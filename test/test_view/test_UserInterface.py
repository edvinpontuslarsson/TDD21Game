# TODO: read about how to do multiple tests

import sys
sys.path.append('..')
from view import UserInterface
import unittest

class TestUI(unittest.TestCase):

    def __init__(self):
        self.sut = UserInterface.UserInterface()

    def test_user_wanna_play(self):
        self.assertFalse(self.sut.user_wanna_play('x'))
        self.assertTrue(self.sut.user_wanna_play('p'))


if __name__ == '__main__':
    unittest.main()
