from .function import function
import unittest

class TestFunction(unittest.TestCase):

    def test_make_basic_function(self):
        function("x", compile("pass"))


if __name__ == "__main__":
    unittest.main()
