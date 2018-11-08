# Module inspired by: https://www.internalpointers.com/post/run-painless-test-suites-python-unittest

import unittest

import test_app
import test_view

# initializes test suite
loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(test_view))
suite.addTests(loader.loadTestsFromModule(test_app))

# initializes & runs runner
runner = unittest.TextTestRunner(verbosity=3)
runner.run(suite)
