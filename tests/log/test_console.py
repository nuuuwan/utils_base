import unittest

from utils_base import (COLOR_BACKGROUND, COLOR_FOREGROUND, COLOR_FORMAT,
                        Console)


class TestConsole(unittest.TestCase):
    def test_format(self):
        self.assertEqual(
            Console.format(
                'Hello', foreground='red', background='blue', format='bold'
            ),
            'redblueboldHello' + COLOR_FORMAT.RESET,
        )

    def test_visual_self(self):
        print('')
        for text, foreground, background, format in [
            (
                'Red foreground, yellow background, normal',
                COLOR_FOREGROUND.RED,
                COLOR_BACKGROUND.YELLOW,
                COLOR_FORMAT.NORMAL,
            ),
            (
                'Red foreground, white background, bold',
                COLOR_FOREGROUND.RED,
                COLOR_BACKGROUND.WHITE,
                COLOR_FORMAT.BOLD,
            ),
            (
                'Blue foreground, green background, faint',
                COLOR_FOREGROUND.BLUE,
                COLOR_BACKGROUND.GREEN,
                COLOR_FORMAT.FAINT,
            ),
            (
                'Green foreground, blue background, italic',
                COLOR_FOREGROUND.GREEN,
                COLOR_BACKGROUND.BLUE,
                COLOR_FORMAT.ITALIC,
            ),
            (
                'Yellow foreground, red background, underline',
                COLOR_FOREGROUND.YELLOW,
                COLOR_BACKGROUND.RED,
                COLOR_FORMAT.UNDERLINE,
            ),
            (
                'White foreground, black background, bold',
                COLOR_FOREGROUND.WHITE,
                COLOR_BACKGROUND.BLACK,
                COLOR_FORMAT.BOLD,
            ),
            (
                'Black foreground, white background, reverse',
                COLOR_FOREGROUND.BLACK,
                COLOR_BACKGROUND.WHITE,
                COLOR_FORMAT.REVERSE,
            ),
            (
                'Magenta foreground, cyan background, invisible',
                COLOR_FOREGROUND.MAGENTA,
                COLOR_BACKGROUND.CYAN,
                COLOR_FORMAT.INVISIBLE,
            ),
            (
                'Cyan foreground, magenta background, striketrough',
                COLOR_FOREGROUND.CYAN,
                COLOR_BACKGROUND.MAGENTA,
                COLOR_FORMAT.STRIKETHROUGH,
            ),
            (
                'Black foreground, yellow background, bold',
                COLOR_FOREGROUND.BLACK,
                COLOR_BACKGROUND.YELLOW,
                COLOR_FORMAT.BOLD,
            ),
        ]:
            Console.print(
                text,
                foreground=foreground,
                background=background,
                format=format,
            )

    def test_visual_styles(self):
        Console.print_lines(
            '',
            Console.h1('# Sri Lanka'),
            Console.h2('## Economy'),
            Console.normal(
                "According to the International Monetary Fund,"
                + " Sri Lanka's GDP in terms of purchasing power parity"
                + " is the second highest in the South Asian"
                + " region in terms of per capita income. In the 19th"
                + " and 20th centuries, Sri Lanka became a plantation"
                + " economy famous for its production and export of"
                + " cinnamon, rubber, and Ceylon tea,"
                + " which remains a trademark national export."
            ),
            Console.note("This is from Wikipedia."),
            '',
        )

    def test_visual_md5(self):
        print(
            Console.md5(
                '',
                '# Sri Lanka',
                '## Economy',
                "According to the International Monetary Fund,"
                + " Sri Lanka's GDP in terms of purchasing power parity"
                + " is the second highest in the South Asian"
                + " region in terms of per capita income.",
                "*This is from Wikipedia.*",
                '',
            )
        )
