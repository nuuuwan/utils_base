import unittest

from utils_base import Parse


class TestParses(unittest.TestCase):
    def test_parse_int(self):
        self.assertEqual(Parse.int(' 10 '), 10)
        self.assertEqual(Parse.int(' 10,000 '), 10000)
        self.assertEqual(Parse.int('abc'), None)

    def test_parse_float(self):
        self.assertEqual(Parse.float(' 10.5 '), 10.5)
        self.assertEqual(Parse.float(' 10,000.5 '), 10000.5)
        self.assertEqual(Parse.float('abc'), None)


if __name__ == '__main__':
    unittest.main()
