import unittest

from utils_base import LatLngLK


class TestLatLngLK(unittest.TestCase):
    def setUp(self):
        self.width = 120.0
        self.height = 120.0
        self.padding = 10.0

    def test_get_t(self):
        t_func = LatLngLK.get_t(self.width, self.height, self.padding)
        self.assertEqual(t_func(LatLngLK.NORTH)[1], 10)
        self.assertEqual(t_func(LatLngLK.SOUTH)[1], 110)
        self.assertEqual(t_func(LatLngLK.EAST)[0], 110)
        self.assertEqual(t_func(LatLngLK.WEST)[0], 10)


if __name__ == '__main__':
    unittest.main()
