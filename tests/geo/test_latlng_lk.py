import unittest

from utils_base import LatLngLK


class TestLatLngLK(unittest.TestCase):
    def setUp(self):
        self.width = 120.0
        self.height = 120.0
        self.padding = 10.0

    def test_get_t(self):
        t = LatLngLK.get_func_t_lk(self.width, self.height, self.padding)
        self.assertEqual(t(LatLngLK.NORTH)[1], 10)
        self.assertEqual(t(LatLngLK.SOUTH)[1], 110)
        self.assertEqual(t(LatLngLK.EAST)[0], 110)
        self.assertEqual(t(LatLngLK.WEST)[0], 10)

    def test_cities(self):
        for city1, city2, expected_distance in [
            (LatLngLK.COLOMBO, LatLngLK.KANDY, 95),
            (LatLngLK.COLOMBO, LatLngLK.GALLE, 105),
            (LatLngLK.COLOMBO, LatLngLK.JAFFNA, 304),
            (LatLngLK.KANDY, LatLngLK.JAFFNA, 271),
            (LatLngLK.GALLE, LatLngLK.JAFFNA, 402),
        ]:
            self.assertEqual(
                int(city1.distance(city2)),
                expected_distance,
            )

    def test_bbox(self):
        bbox = LatLngLK.BBOX
        self.assertEqual(int(bbox[0].distance(bbox[1])), 505)


if __name__ == '__main__':
    unittest.main()
