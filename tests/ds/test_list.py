import unittest

from utils_base import List


class TestList(unittest.TestCase):
    def setUp(self):
        self.list_class = List([1, 2, 3, 4, 5])

    def test_tolist(self):
        self.assertEqual(self.list_class.raw, [1, 2, 3, 4, 5])

    def test_iter(self):
        self.assertEqual(list(iter(self.list_class)), [1, 2, 3, 4, 5])

    def test_len(self):
        self.assertEqual(len(self.list_class), 5)

    def test_getitem(self):
        self.assertEqual(self.list_class[1], 2)

    def test_setitem(self):
        self.list_class[1] = 10
        self.assertEqual(self.list_class[1], 10)

    def test_eq(self):
        self.assertFalse(self.list_class == List([1, 10, 3, 4, 5]))
        self.assertTrue(self.list_class == List([1, 2, 3, 4, 5]))

    def test_add(self):
        added_list = self.list_class + List([6, 7, 8])
        self.assertEqual(added_list.raw, [1, 2, 3, 4, 5, 6, 7, 8])

    def test_flatten(self):
        self.list_class = List([[1, 2], [3, 4]])
        self.assertEqual(self.list_class.flatten().raw, [1, 2, 3, 4])

    def test_unique(self):
        self.list_class = List([1, 2, 2, 3, 3, 3])
        self.assertEqual(self.list_class.unique().raw, [1, 2, 3])

    def test_map(self):
        mapped_list = self.list_class.map(lambda x: x**2)
        self.assertEqual(mapped_list.raw, [1, 4, 9, 16, 25])

    def test_filter(self):
        filtered_list = self.list_class.filter(lambda x: x > 2)
        self.assertEqual(filtered_list.raw, [3, 4, 5])


if __name__ == '__main__':
    unittest.main()
