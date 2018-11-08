import access_project_directory
import app
from test_view import test_UserInterface
import unittest


class TestApp(unittest.TestCase):

    def __init__(self):
        self.ui_test = test_UserInterface.TestUI()

    def test_ping_should_pong(self):
        self.assertNotEqual(app.ping(), 'ping')
        self.assertEqual(app.ping(), 'pong')

    def test_all_other_tests(self):
        self.ui_test.test_user_wanna_play()


if __name__ == '__main__':
    unittest.main()

