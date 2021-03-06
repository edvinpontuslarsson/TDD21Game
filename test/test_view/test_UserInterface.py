import os
import sys

currentWorkingDirectory = os.getcwd()
sys.path.append(currentWorkingDirectory + '/card_game/')

from view import UserInterface
import unittest


class TestUI(unittest.TestCase):

    def setUp(self):
        self.sut = UserInterface.UserInterface()

    def test_user_wanna_play(self):
        self.assertFalse(self.sut.user_wanna_play('x'))
        self.assertTrue(self.sut.user_wanna_play('p'))

