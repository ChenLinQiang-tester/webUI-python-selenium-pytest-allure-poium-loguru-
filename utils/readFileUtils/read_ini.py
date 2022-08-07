import configparser
import os

from common.config import RunConfig

base_path = RunConfig.base_path
ini_path_ = os.path.join(base_path, "common", "pytest.ini")


class ReadIni(object):
    def __init__(self, ini_path):
        self.ini_path = ini_path
        self.ini = configparser.ConfigParser()
        self.ini.read(self.ini_path)

    def get_ini_object(self):
        return self.ini

    def get_ini(self, section, k):
        value = self.ini[section][k]
        return value

    def set_ini(self, section, k, v):
        self.ini.set(section, k, v)
        with open(self.ini_path, "w") as f:
            self.ini.write(f)

    def add_ini(self, section, k, v):
        self.ini.add_section(section)
        self.set_ini(section, k, v)


if __name__ == '__main__':
    ReadIni(ini_path_).add_ini("root2", "username", "aaaa")
