import unittest

from utils_base import parse_float, parse_int


class TestParses(unittest.TestCase):
    def test_parse_int(self):
        self.assertEqual(parse_int(' 10 '), 10)
        self.assertEqual(parse_int(' 10,000 '), 10000)
        self.assertEqual(parse_int('abc'), None)

    def test_parse_float(self):
        self.assertEqual(parse_float(' 10.5 '), 10.5)
        self.assertEqual(parse_float(' 10,000.5 '), 10000.5)
        self.assertEqual(parse_float('abc'), None)


if __name__ == '__main__':
    unittest.main()
