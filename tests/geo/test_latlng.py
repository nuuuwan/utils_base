import unittest

from utils_base import LatLng


class TestLatLng(unittest.TestCase):
    def setUp(self):
        self.latlng1 = LatLng(10.0, 20.0)
        self.latlng2 = LatLng(10.0, 20.0)
        self.latlng3 = LatLng(30.0, 40.0)

    def test_eq(self):
        self.assertTrue(self.latlng1 == self.latlng2)
        self.assertFalse(self.latlng1 == self.latlng3)

    def test_str(self):
        self.assertEqual(str(self.latlng1), '10.000000°N, 20.000000°E')

    def test_parse(self):
        self.assertEqual(LatLng.parse('10.0°N,20.0°E'), self.latlng1)

    def test_distance(self):
        self.assertAlmostEqual(
            self.latlng1.distance(self.latlng3), 3035.7289569056334, places=2
        )

    def test_angle(self):
        self.assertAlmostEqual(
            self.latlng1.angle(self.latlng3), 45.0, places=2
        )

    def test_bbox(self):
        self.assertEqual(
            LatLng.bbox([self.latlng1, self.latlng3]),
            (self.latlng1, self.latlng3),
        )


if __name__ == '__main__':
    unittest.main()
