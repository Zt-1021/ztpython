import unittest
import json
import ast
from common import constant, request, mysql
from configer import conf_class
from ddt import ddt, data
from common.excel_class_02 import DoExcel


cases01 = DoExcel(constant.case_dir_admin, "saveuserapplicationinfo").read_test_data()
cases02 = DoExcel(constant.case_dir_admin, "sendRegisterMail").read_test_data()
cases03 = DoExcel(constant.case_dir_admin, "saveInvestorTypeInfo").read_test_data()
data01 = []


@ddt
class TestRegister(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.request = request.Request("test")
        cls.host = conf_class.Conf(constant.conffile_dir).getvalue("MysqlDatabase", "test_database_host")
        cls.username = conf_class.Conf(constant.conffile_dir).getvalue("MysqlDatabase", "test_database_username")
        cls.password = conf_class.Conf(constant.conffile_dir).getvalue("MysqlDatabase", "test_database_password")
        cls.database = conf_class.Conf(constant.conffile_dir).getvalue("MysqlDatabase", "test_database")
        cls.port = conf_class.Conf(constant.conffile_dir).getvalue("MysqlDatabase", "test_database_port")
        cls.mysql = mysql.Mysql(cls.host, cls.username, cls.password, cls.database, int(cls.port))

    def setUp(self):
        pass

    @data(*cases01)
    def test_case01_saveUserApplicationInfo(self, case):

        data = ast.literal_eval(case['data'])
        if data['userapplyEmail'] == "${email}":
            useremail = self.mysql.fetchone("select user163email FROM t_user_info ORDER BY id DESC LIMIT 1")
            data['userapplyEmail'] = useremail[0]+"1"

        response = self.request.request(case['method'], case['url'], data)
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_admin, "saveuserapplicationinfo").write_test_data(case["id"], response.text, "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_admin, "saveuserapplicationinfo").write_test_data(case["id"], response.text, "Pass")

    @data(*cases02)
    def test_case02_sendRegisterMail(self, case):
        # uid = data01[0]["results"]["uid"]
        response = self.request.request(case['method'], case['url'], json.loads(case['data']))
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_admin, "sendRegisterMail").write_test_data(case["id"], response.text, "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_admin, "sendRegisterMail").write_test_data(case["id"], response.text, "Pass")

    # @data(*cases03)
    # def test_case03_saveInvestorTypeInfo(self, case):
    #     response = self.request.request(case['method'], case['url'], json.loads(case['data']))
    #     try:
    #         self.assertIn(case['excepted'], response.json()['message'])
    #     except AssertionError as e:
    #         DoExcel(constant.case_dir_admin, "saveInvestorTypeInfo").write_test_data(case["id"], response.text, "Failed")
    #         print(e)
    #     else:
    #         DoExcel(constant.case_dir_admin, "saveInvestorTypeInfo").write_test_data(case["id"], response.text, "Pass")

    def tearDown(self):
        pass
