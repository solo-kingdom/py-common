from unittest import TestCase

from common.common.file import ensure_path


class Test(TestCase):
    def test_ensure_path(self):
        ensure_path('log/logs')
