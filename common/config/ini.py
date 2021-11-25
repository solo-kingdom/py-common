# coding: utf-8

from configparser import ConfigParser


class InitConfig:
    def __init__(self, pt: str):
        self.pt = pt
        self.cp = ConfigParser()
        self.cp.read(pt)
