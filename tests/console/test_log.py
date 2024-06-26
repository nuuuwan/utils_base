import unittest

from utils_base import Log


class TestCase(unittest.TestCase):
    def test_log(self):
        for log in [Log('custom'), Log.main, Log.default, Log.pipeline]:
            self.assertIsNotNone(log)
            for label, func in [
                ('debug', log.debug),
                ('info', log.info),
                (dict(info='info'), log.info),
                ('warning', log.warning),
                ('error', log.error),
                ('critical', log.critical),
            ]:
                func(label)


if __name__ == '__main__':
    unittest.main()
