import requests
import unittest
from study.mogugu.configer.conf_class import Conf


class TestHomePage(unittest.TestCase):
    def setUp(self):
        # print("-----start-----")
        self.domain_name = Conf("D:\ztpython\study\mogugu\configer\conf.conf").getvalue("DomainName", "test")
        # self.host = Conf("D:\ztpython\study\mogugu\configer\conf.conf").getvalue(
        #                                                                         "MysqlDatabase", "test_database_host")
        # self.port = Conf("D:\ztpython\study\mogugu\configer\conf.conf").getvalue(
        #                                                                         "MysqlDatabase", "test_database_port")
        # self.username = Conf("D:\ztpython\study\mogugu\configer\conf.conf").getvalue(
        #                                                                     "MysqlDatabase", "test_database_username")
        # self.password = Conf("D:\ztpython\study\mogugu\configer\conf.conf").getvalue(
        #                                                                     "MysqlDatabase", "test_database_password")

    def tearDown(self):
        pass

    def test_case01_getLoginInfo(self):
        response = requests.get(url=self.domain_name + "/user/code/getLoginInfo")
        self.assertEqual(response.status_code, 200)

    def test_case02_popularCompanies(self):
        response = requests.get(url=self.domain_name + "/enterprise/code/popularCompanies")
        self.assertEqual(response.status_code, 200)
        result = response.json()
        # print(result)
        self.assertEqual(result["code"], "S01")
        self.assertEqual(len(result["results"]), 10)

    def test_case03_parentProducts(self):
        response = requests.get(url=self.domain_name + "/enterprise/code/parentProducts")
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertEqual(result["code"], "S01")

    def test_case04_getOpenId(self):
        response = requests.get(url=self.domain_name + "/wxservice/getOpenId", params={
                                                                            "code": "051v0hGa1rmKdA0OAvIa1xBA1p0v0hGL"})
        self.assertEqual(response.status_code, 200)

    def test_case05_getEnterpriseCount(self):
        response = requests.get(url=self.domain_name + "/enterprise/code/getEnterpriseCount")
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertEqual(result["code"], "S01")


if __name__ == '__main__':
    TestHomePage()
