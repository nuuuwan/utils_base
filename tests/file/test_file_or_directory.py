import os
import unittest

from utils_base import File, FileOrDirectory


class TestCase(unittest.TestCase):

    def test_general(self):
        os.makedirs(os.path.join("tests", "_output"), exist_ok=True)
        file_path = os.path.join("tests", "_output", "test.txt")
        f = File(file_path)
        content = "12345678" * 1_000
        f.write(content)
        self.assertTrue(f.exists)
        self.assertEqual(hash(f), hash(file_path))
        self.assertEqual(f.size, len(content))
        self.assertEqual(f.size_humanized, "8.0 kB")
        self.assertEqual(str(f), f"{file_path} (8.0 kB)")

    def test_small_file(self):
        os.makedirs(os.path.join("tests", "_output"), exist_ok=True)
        file_path = os.path.join("tests", "_output", "test_small.txt")
        f = File(file_path)
        content = "12345678"
        f.write(content)
        self.assertEqual(str(f), f"{file_path} (8 B)")

    def test_dir(self):
        dir_path = os.path.join("tests", "file", "_input")
        d = FileOrDirectory(dir_path)
        self.assertTrue(d.exists)
        self.assertEqual(d.size, 2_169_623)
        self.assertEqual(d.size_humanized, "2.2 MB")
