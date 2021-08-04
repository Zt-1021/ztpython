import pymysql


class Mysql:
    def __init__(self, host, username, password, database, port):
        self.mysql = pymysql.connect(host=host, user=username, password=password, database=database, port=port)
        self.cursor = self.mysql.cursor()

    # 获取单条数据
    def fetchone(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    # 获取多条数据
    def fetmany(self, sql, size):
        self.cursor.execute(sql)
        return self.cursor.fetchmany(size)

    # 获取所有数据
    def fetall(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    # 添加,更新，删除
    def modifydata(self, sql):   # 功能根据sql语句来决定是添加还是更新，删除
        try:
            self.cursor.execute(sql)
            self.mysql.commit()
        except:
            self.mysql.rollback()  # 如果发生错误，则回滚

    # 添加多条数据
    def insertmany(self, sql, data):
        self.cursor.executemany(sql, data)
        self.mysql.commit()
        return result

    def close(self):
        self.cursor.close()
        self.mysql.close()


if __name__ == "__main__":

    mysql = Mysql("192.168.2.105", "select", "select", "vuca_uk", 3306)
    sql = 'select * from t_user_info where user_name = "zt"'
    # result = mysql.fetchone(sql)

    # result = mysql.fetmany(sql, 4)
    # for i in range(0, len(result)):
    #     print(result[i])

    result = mysql.fetall(sql)
    print(result)
    mysql.close()


