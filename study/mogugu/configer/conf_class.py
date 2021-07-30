import configparser

# cf = configparser.ConfigParser()
# cf.read("test_conf.conf", encoding="utf-8")
# value = cf.get("StudentInfo", "s1")
# print(value)


class Conf:
    def __init__(self, filename):
        self.cf = configparser.ConfigParser()
        self.cf.read(filename, encoding="utf-8")

    def getvalue(self, section, option):
        return self.cf.get(section, option)


if __name__ == '__main__':
    print(Conf("conf.conf").getvalue("DomainName", "test"))
