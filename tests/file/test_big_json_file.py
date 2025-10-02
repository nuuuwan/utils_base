import os
import shutil
import unittest

from utils_base import BigJSONFile


class TestCase(unittest.TestCase):

    def test_empty(self):
        dir_path = os.path.join("tests", "output", "test_big_json_file_empty")
        shutil.rmtree(dir_path, ignore_errors=True)
        big_json_file = BigJSONFile(dir_path)
        data_list = big_json_file.read()
        self.assertEqual(data_list, [])
        big_json_file.write([])
        data_list2 = big_json_file.read()
        self.assertEqual(data_list2, [])
        shutil.rmtree(dir_path, ignore_errors=True)
