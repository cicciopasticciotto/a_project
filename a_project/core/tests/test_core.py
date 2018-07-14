import unittest
from a_project.core.core import a_sleep_function


class TestSleep(unittest.TestCase):
    def test_sleep(self):
        a_sleep_function()
