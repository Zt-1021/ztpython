import configparser
import os
# cf = configparser.ConfigParser()
# cf.read("test_conf.conf", encoding="utf-8")
# value = cf.get("StudentInfo", "s1")
# print(value)

# proDir = os.path.split(os.path.realpath(__file__))[0]
# configPath = os.path.join(proDir, "test.conf")
# import common.constant


class Conf:
    def __init__(self, filename):
        self.cf = configparser.ConfigParser()
        self.cf.read(filename, encoding="utf-8")

    def get(self, section, option):
        return self.cf.get(section, option)

    def getboolean(self, section, option):
        return self.cf.getboolean(section, option)


if __name__ == '__main__':
    print(Conf("test.conf").get("Api", "url"))
    # print(Conf(common.constant.conffile_dir).getvalue("User", "admin_user_name"))
