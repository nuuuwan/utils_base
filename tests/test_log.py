import unittest

from utils_base import Log, _log


class TestCase(unittest.TestCase):
    def test_log(self):
        for __log in [_log, Log('custom')]:
            self.assertIsNotNone(__log)
            __log.debug('test debug')
            __log.info('test info')
            __log.warning('test warning')
            __log.error('test error')
            __log.critical('test critical')


if __name__ == '__main__':
    unittest.main()
