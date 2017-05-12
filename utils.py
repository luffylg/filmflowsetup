import os
from configparser import ConfigParser


def getconfig(section, key):
    config = ConfigParser()
    path = os.path.split(os.path.realpath(__file__))[0] + '\\pros.conf'
    config.read(path)
    return config.get(section, key)