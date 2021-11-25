import logging
from unittest import TestCase

from ini import load


class Test(TestCase):
    def test_load(self):
        cfg = load('config.ini')
        logging.info(cfg)
