import unittest
import json
from common import constant, request, mysql
from configer import conf_class
from ddt import ddt, data
from common.excel_class_02 import DoExcel


cases01 = DoExcel(constant.case_dir_admin, "saveuserapplicationinfo").read_test_data()
cases02 = DoExcel(constant.case_dir_admin, "sendRegisterMail").read_test_data()
cases03 = DoExcel(constant.case_dir_admin, "getworkorder").read_test_data()
data01 = []


@ddt
class TestRegister(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # cls.host = conf_class.Conf(constant.conffile_dir).getvalue("MysqlDatabase", "test_database_host")
        # cls.username = conf_class.Conf(constant.conffile_dir).getvalue("MysqlDatabase", "test_database_username")
        # cls.password = conf_class.Conf(constant.conffile_dir).getvalue("MysqlDatabase", "test_database_password")
        # cls.database = conf_class.Conf(constant.conffile_dir).getvalue("MysqlDatabase", "test_database")
        # cls.port = conf_class.Conf(constant.conffile_dir).getvalue("MysqlDatabase", "test_database_port")
        # cls.mysql = mysql.Mysql(cls.host, cls.username, cls.password, cls.database, cls.port)
        # cls.cursor = cls.mysql.cursor()
        # useremail = cls.cursor.execute("select max(user163email) from t_user_info")
        pass

    def setUp(self):
        pass

    @data(*cases01)
    def test_case01_saveUserApplicationInfo(self, case):

        # data = json.loads(case['data']
        # if data['userapplyEmail'] == "${email}":
        #     data['userapplyEmail'] =
        response = self.request.request(case['method'], case['url'], json.loads(case['data']))
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_admin, "getnotice").write_test_data(case["id"], response.text, "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_admin, "getnotice").write_test_data(case["id"], response.text, "Pass")

    @data(*cases02)
    def test_case02_sendRegisterMail(self, case):
        # uid = data01[0]["results"]["uid"]
        response = self.systemwork.post_sendRegisterMail(json.loads(case[4])["userId"],
                                                         json.loads(case[4])["url"])
        self.assertIn(json.loads(case[5]), response.text)

    @data(*cases03)
    def test_case03_saveInvestorTypeInfo(self, case):
        response = self.systemwork.post_saveInvestorTypeInfo(json.loads(case[4])["userId"],
                                                             json.loads(case[4])["investorType"])
        self.assertIn(json.loads(case[5]), response.text)

    def tearDown(self):
        pass
