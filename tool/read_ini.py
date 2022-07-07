import configparser
import os

from config import RunConfig

base_path = RunConfig.base_path
ini_path = os.path.join(base_path, "data", "pytest.ini")


class ReadIni:
    def __init__(self):
        self.ini = configparser.ConfigParser()
        self.ini.read(ini_path)

    def get_user(self, name):
        value = self.ini["user"][name]
        return value

    def set_user(self, name, newname):
        self.ini.set("user", name, newname)
        with open(ini_path, "w") as f:
            self.ini.write(f)


if __name__ == '__main__':
    print(ini_path)
    a = ReadIni()
    print(a.get_user("password"))
