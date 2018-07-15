import unittest
from a_project.core.core import a_sleep_function, plot_something


class TestSleep(unittest.TestCase):
    def test_sleep(self):
        a_sleep_function()

    def test_plot(self):
        plot_something()
        
