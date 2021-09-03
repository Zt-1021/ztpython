import unittest
import json
from common import constant, request,mysql
from configer import conf_class
from common.new_ddt import ddt, data
from common.excel_class_02 import DoExcel


cases01 = DoExcel(constant.case_dir_admin, "addworkorder").read_test_data()
cases02 = DoExcel(constant.case_dir_admin, "getworkorders").read_test_data()
cases03 = DoExcel(constant.case_dir_admin, "getworkorder").read_test_data()
datas01 = {}

@ddt
class Testsystemworkinfo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.request = request.Request()

        cls.host = conf_class.Conf(constant.testconf_dir).get("MysqlDatabase", "host")
        cls.username = conf_class.Conf(constant.testconf_dir).get("MysqlDatabase", "username")
        cls.password = conf_class.Conf(constant.testconf_dir).get("MysqlDatabase", "password")
        cls.database = conf_class.Conf(constant.testconf_dir).get("MysqlDatabase", "database")
        cls.port = conf_class.Conf(constant.testconf_dir).get("MysqlDatabase", "port")
        cls.mysql = mysql.Mysql(cls.host, cls.username, cls.password, cls.database, int(cls.port))

        cls.request.request("get", "/code/image")
        username = conf_class.Conf(constant.testconf_dir).get("User", "admin_user_name")
        password = conf_class.Conf(constant.testconf_dir).get("User", "admin_user_password")
        cls.request.request("post", "/authentication/form",
                             {"username": username, "password": password, "imageCode": "0"})
        cls.request.request("get", "/code/judgingIdentity", {"email": username})

    def setUp(self):
        pass

    @data(*cases01)
    def test_case01_addwoinfo(self, case):
        response = self.request.request(case['method'], case['url'], json.loads(case['data']))
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_admin, "addworkorder").write_test_data(case["id"], response.text, "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_admin, "addworkorder").write_test_data(case["id"], response.text, "Pass")

        if "Add successful！" in response.text:
            datas01['result'] = response.json()["results"]

    @data(*cases02)
    def test_case02_getuserworkorders(self, case):
        response = self.request.request(case['method'], case['url'], json.loads(case['data']))
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_admin, "getworkorders").write_test_data(case["id"], response.text, "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_admin, "getworkorders").write_test_data(case["id"], response.text, "Pass")

    @data(*cases03)
    def test_case03_getuserworkorder(self, case):
        response = self.request.request(case['method'], case['url'], json.loads(case['data']))
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_admin, "getworkorder").write_test_data(case["id"], response.text, "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_admin, "getworkorder").write_test_data(case["id"], response.text, "Pass")

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        userWorkOrderId = datas01["result"]["userWorkOrderId"]
        cls.mysql.modifydata("delete from t_enterprise_info where id = " + str(userWorkOrderId))
        cls.mysql.close()
        cls.request.session.close()

