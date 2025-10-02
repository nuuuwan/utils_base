import unittest

from utils_base import Parse


class TestParses(unittest.TestCase):
    def test_parse_int(self):
        self.assertEqual(Parse.int(" 10 "), 10)
        self.assertEqual(Parse.int(" 10,000 "), 10000)
        self.assertEqual(Parse.int("abc"), None)

    def test_parse_float(self):
        self.assertEqual(Parse.float(" 10.5 "), 10.5)
        self.assertEqual(Parse.float(" 10,000.5 "), 10000.5)
        self.assertEqual(Parse.float("abc"), None)

    def test_time_str(self):
        for x, expected_result in [
            ("2023-10-01 12:30", "2023-10-01 12:30"),
            ("2023-10-01T12:30:00Z", "2023-10-01 12:30"),
            ("October 1, 2023, 12:30 PM", "2023-10-01 12:30"),
            ("2023/10/01 12:30:00", "2023-10-01 12:30"),
            ("01 Oct 2023 12:30", "2023-10-01 12:30"),
        ]:

            self.assertEqual(Parse.time_str(x), expected_result)


if __name__ == "__main__":
    unittest.main()
