import os
import unittest

from PIL import Image as PImage

from utils_base import Image

DIR_TEST = os.path.join('tests', 'image')
DIR_TEST_OUTPUT = os.path.join(DIR_TEST, '_output')


class TestImage(unittest.TestCase):
    def setUp(self):
        self.pimage = PImage.open(os.path.join(DIR_TEST, "_test_image.png"))
        self.image = Image(self.pimage)

    def test_load(self):
        file_path = os.path.join(DIR_TEST, "_test_image.png")
        self.pimage.save(file_path)
        loaded_image = Image.load(file_path)
        self.assertEqual(loaded_image.size, self.pimage.size)

    def test_write(self):
        file_path = os.path.join(DIR_TEST_OUTPUT, "__test_write.png")
        path = self.image.write(file_path)
        self.assertEqual(path, file_path)

    def test_write_temp(self):
        path = self.image.write_temp()
        self.assertTrue(os.path.exists(path))
        print(path)

    def test_crop(self):
        width_height = (200, 200)
        cropped_image = self.image.crop((10, 10), width_height=width_height)
        self.assertEqual(cropped_image.size, width_height)
        cropped_image.write(os.path.join(DIR_TEST_OUTPUT, "__test_crop.png"))

    def test_resize(self):
        expected_width, expected_height = 1024, 1024
        self.assertEqual(self.image.size, (expected_width, expected_height))
        factor = 1 / 10
        resized_image = self.image.resize(factor)
        resized_width, resized_height = [
            int(x * factor) for x in self.image.size
        ]
        self.assertEqual(resized_image.size, (resized_width, resized_height))
        resized_image.write(
            os.path.join(DIR_TEST_OUTPUT, "__test_resize.png")
        )

    def test_draw_text(self):
        text_image = self.image.draw_text(
            (312, 300), "Beautiful Image of Sri Lanka"
        )
        self.assertIsInstance(text_image, Image)
        text_image.write(
            os.path.join(DIR_TEST_OUTPUT, "__test_draw_text.png")
        )

    def test_equalize_map(self):
        equalized_map = Image.equalize_map([1, 2, 3, 4, 5])
        self.assertEqual(
            equalized_map, {1: 0.0, 2: 0.2, 3: 0.4, 4: 0.6, 5: 0.8}
        )

    def test_equalize(self):
        equalized_image = Image.equalize(self.image.im.convert('L'), 0, 360)
        self.assertIsInstance(equalized_image, PImage.Image)

    def test_equalize_hue(self):
        equalized_value_image = self.image.equalize_hue()
        self.assertIsInstance(equalized_value_image, Image)
        equalized_value_image.write(
            os.path.join(DIR_TEST_OUTPUT, "__test_equalize_hue.png")
        )

    def test_enhance(self):
        enhanced_image = self.image.enhance(2)
        self.assertIsInstance(enhanced_image, Image)
        enhanced_image.write(
            os.path.join(DIR_TEST_OUTPUT, "__test_enhance.png")
        )


if __name__ == '__main__':
    unittest.main()
