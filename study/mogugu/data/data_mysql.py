import pymysql
# from study.mogugu.configer.conf_class import Conf


# # 获取配置文件中数据库的相关信息
# host = Conf("D:\ztpython\study\mogugu\configer\test.conf").getvalue("MysqlDatabase", "host")
# port = Conf("D:\ztpython\study\mogugu\configer\test.conf").getvalue("MysqlDatabase", "port")
# username = Conf("D:\ztpython\study\mogugu\configer\test.conf").getvalue("MysqlDatabase", "username")
# password = Conf("D:\ztpython\study\mogugu\configer\test.conf").getvalue("MysqlDatabase", "password")
#
# #连接数据库
# db = pymysql.connect(host, port, username, password,)


class Database:
    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password

    def connect_database(self, db):
        return pymysql.connect(self.host, self.port, self.username, self.password, db)

    def read_data(self):
        pass
