import access_project_directory
import app
from test_view import test_UserInterface
import unittest


class TestApp(unittest.TestCase):

    def test_ping_should_pong(self):
        self.assertNotEqual(app.ping(), 'ping')
        self.assertEqual(app.ping(), 'pong')

