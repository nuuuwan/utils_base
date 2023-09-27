import os
from unittest import TestCase

from utils import Directory


class TestDirectory(TestCase):
    def test_init(self):
        dir_tests = Directory(os.path.join('src', 'utils'))
        self.assertEqual(dir_tests.path, os.path.join('src', 'utils'))
        self.assertEqual(dir_tests.name, 'utils')
