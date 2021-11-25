# coding: utf-8
import logging
import logging.handlers
import sys

LOG_K_PATH = 'path'
LOG_K_NAME = 'name'
LOG_K_SIZE = 'file_size_mb'
LOG_K_FILE_NUMBER = 'log_file_number'


class ILogger:
    def __init__(self, cfg=None):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        fmt = logging.Formatter('[%(asctime)s] %(levelname)s %(message)s',
                                '%Y-%m-%d %H:%M:%S')
        console_handler = logging.StreamHandler(stream=sys.stdout)
        console_handler.setFormatter(fmt)
        console_handler.setLevel(logging.INFO)
        self.logger.addHandler(console_handler)

        if cfg:
            file_handler = logging.handlers.RotatingFileHandler(cfg[LOG_K_PATH],
                                                                maxBytes=cfg[LOG_K_SIZE],
                                                                backupCount=cfg[LOG_K_FILE_NUMBER])
            file_handler.setFormatter(fmt)
            file_handler.setLevel(logging.INFO)
            self.logger.addHandler(file_handler)

    def debug(self, msg, *args, **kwargs):
        self.logger.debug(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        self.logger.info(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        self.logger.warning(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        self.logger.error(msg, *args, **kwargs)
