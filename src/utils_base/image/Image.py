import tempfile

from PIL import Image as PImage
from PIL import ImageDraw, ImageEnhance, ImageFont

from utils_base.Log import Log

log = Log(__name__)


class Image:
    def __init__(self, im: PImage):
        self.im = im

    @staticmethod
    def load(image_path: str):  # -> Image
        return Image(PImage.open(image_path))

    def write(self, image_path: str) -> str:
        self.im.save(image_path)
        log.debug(f'Saved {image_path}')
        return image_path

    def write_temp(self) -> str:
        return self.write(tempfile.NamedTemporaryFile(suffix='.png').name)

    @property
    def size(self):
        return self.im.size

    def crop(
        self, left_top: tuple[float], width_height: tuple[float]
    ):  # -> Image
        width, height = width_height
        im_width, im_height = self.im.size

        if height > im_height or width > im_width:
            return self

        left, top = left_top
        bbox = (left, top, left + width, top + height)
        im = self.im.crop(bbox)
        log.debug(f'crop: {left},{top} & {width}x{height}')
        return Image(im)

    def resize(self, ratio: float):  # -> Image
        im = self.im
        width, height = im.size
        new_width, new_height = (int(width * ratio), int(height * ratio))
        im = im.resize((new_width, new_height))
        log.debug(f'resize({ratio}) -> {new_width}x{new_height}')
        return Image(im)

    def draw_text(
        self,
        left_top: tuple[float],
        text: str,
        fill: tuple = None,
        font_family: str = None,
        font_size: int = None,
    ):  # -> Image
        draw = ImageDraw.Draw(self.im)
        font = ImageFont.truetype(font_family or 'arial.ttf', font_size or 40)
        draw.text(left_top, text, fill=fill or (0, 0, 0), font=font)
        left, top = left_top
        log.debug(f'draw_text(({left},{top}), "{text}")')
        return Image(self.im)

    @staticmethod
    def equalize_map(x_list: list[float]) -> list[float]:
        x_list_sorted = sorted(x_list)
        n = len(x_list_sorted)
        idx = {}
        for i, x in enumerate(x_list_sorted):
            p = i / n
            if x not in idx:
                idx[x] = p
        return idx

    @staticmethod
    def equalize(c):
        idx = Image.equalize_map(list(c.getdata()))
        return c.point(lambda x: int(idx.get(x, 0) * 255))

    def equalize_value(self) -> 'Image':
        im = self.im.convert('HSV')
        h, s, v = im.split()
        v = Image.equalize(v)

        im = PImage.merge('HSV', (h, s, v))
        im = im.convert('RGB')
        log.debug('Equalized hue')
        return Image(im)

    def enhance(self, factor: float) -> 'Image':
        enhancer = ImageEnhance.Contrast(self.im)
        im2 = enhancer.enhance(factor)
        return Image(im2)
