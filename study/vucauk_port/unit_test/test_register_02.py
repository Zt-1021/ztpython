import unittest
import json
import ast
from common import constant, request, mysql
from configer import conf_class
from common.new_ddt import ddt, data
from common.excel_class_02 import DoExcel


cases01 = DoExcel(constant.case_dir_admin, "saveuserapplicationinfo").read_test_data()
cases02 = DoExcel(constant.case_dir_admin, "sendRegisterMail").read_test_data()
cases03 = DoExcel(constant.case_dir_admin, "saveInvestorTypeInfo").read_test_data()
cases04 = DoExcel(constant.case_dir_admin, "saveCustomerDueDiligenceInfo").read_test_data()
cases05 = DoExcel(constant.case_dir_admin, "saveInvestmentTestInfo").read_test_data()
cases06 = DoExcel(constant.case_dir_admin, "saveQuantitativeTestInfo").read_test_data()
cases07 = DoExcel(constant.case_dir_admin, "saveSignatureTemplate").read_test_data()
cases08 = DoExcel(constant.case_dir_admin, "getUserApplicationInfos").read_test_data()
cases09 = DoExcel(constant.case_dir_admin, "getUserApplicationInfo").read_test_data()
cases10 = DoExcel(constant.case_dir_admin, "saveUserAccountInfo").read_test_data()
cases11 = DoExcel(constant.case_dir_admin, "updateAccountStatus").read_test_data()
data01 = {}


@ddt
class TestRegister(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.request = request.Request()
        cls.host = conf_class.Conf(constant.testconf_dir).get("MysqlDatabase", "host")
        cls.username = conf_class.Conf(constant.testconf_dir).get("MysqlDatabase", "username")
        cls.password = conf_class.Conf(constant.testconf_dir).get("MysqlDatabase", "password")
        cls.database = conf_class.Conf(constant.testconf_dir).get("MysqlDatabase", "database")
        cls.port = conf_class.Conf(constant.testconf_dir).get("MysqlDatabase", "port")
        cls.mysql = mysql.Mysql(cls.host, cls.username, cls.password, cls.database, int(cls.port))

    def setUp(self):
        pass

    @data(*cases01)
    def test_case01_saveUserApplicationInfo(self, case):

        data = ast.literal_eval(case['data'])
        if data['userapplyEmail'] == "${email}":
            useremail = self.mysql.fetchone("select user163email FROM t_user_info ORDER BY id DESC LIMIT 1")
            registeremail = useremail[0]+"1"
            data['userapplyEmail'] = registeremail
            data01['userapplyEmail'] = registeremail
            data01['password'] = data['password']

        response = self.request.request(case['method'], case['url'], data)
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_admin, "saveuserapplicationinfo").write_test_data(case["id"], response.text, "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_admin, "saveuserapplicationinfo").write_test_data(case["id"], response.text, "Pass")
        if "Application is successful!" in response.text:
            data01['result'] = response.json()["results"]

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

    @data(*cases03)
    def test_case03_saveInvestorTypeInfo(self, case):

        userid = data01["result"]["uid"]
        self.mysql.modifydata("update t_user_info set validation_email = 1 where id = " + str(userid))

        self.request.request("get", "/code/image")
        self.request.request("post", "/authentication/form",
                            {"username": data01["userapplyEmail"], "password": data01['password'], "imageCode": "0"})
        self.request.request("get", "/code/judgingIdentity", {"email": data01["userapplyEmail"]})

        response = self.request.request(case['method'], case['url'], json.loads(case['data']))
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_admin, "saveInvestorTypeInfo").write_test_data(case["id"], response.text, "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_admin, "saveInvestorTypeInfo").write_test_data(case["id"], response.text, "Pass")
        self.request.session.close()

    @data(*cases04)
    def test_case04_saveCustomerDueDiligenceInfo(self, case):

        self.request.request("get", "/code/image")
        self.request.request("post", "/authentication/form",
                             {"username": data01["userapplyEmail"], "password": data01['password'], "imageCode": "0"})
        self.request.request("get", "/code/judgingIdentity", {"email": data01["userapplyEmail"]})

        response = self.request.request(case['method'], case['url'], json.loads(case['data']))
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_admin, "saveCustomerDueDiligenceInfo").write_test_data(case["id"], response.text,
                                                                                     "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_admin, "saveCustomerDueDiligenceInfo").write_test_data(case["id"], response.text, "Pass")
        self.request.session.close()

    def test_case05_saveRiskWarningInfo(self):
        self.request.request("get", "/code/image")
        self.request.request("post", "/authentication/form",
                             {"username": data01["userapplyEmail"], "password": data01['password'], "imageCode": "0"})
        self.request.request("get", "/code/judgingIdentity", {"email": data01["userapplyEmail"]})

        response = self.request.request("post", "/rdt/saveRiskWarningInfo")
        self.assertIn("Save success!", response.json()['message'])

        self.request.session.close()

    @data(*cases05)
    def test_case06_saveInvestmentTestInfo(self, case):
        self.request.request("get", "/code/image")
        self.request.request("post", "/authentication/form",
                             {"username": data01["userapplyEmail"], "password": data01['password'], "imageCode": "0"})
        self.request.request("get", "/code/judgingIdentity", {"email": data01["userapplyEmail"]})

        response = self.request.request(case['method'], case['url'], json.loads(case['data']))
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_admin, "saveInvestmentTestInfo").write_test_data(case["id"], response.text, "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_admin, "saveInvestmentTestInfo").write_test_data(case["id"], response.text, "Pass")
        self.request.session.close()

    @data(*cases06)
    def test_case07_saveQuantitativeTestInfo(self, case):
        self.request.request("get", "/code/image")
        self.request.request("post", "/authentication/form",
                             {"username": data01["userapplyEmail"], "password": data01['password'], "imageCode": "0"})
        self.request.request("get", "/code/judgingIdentity", {"email": data01["userapplyEmail"]})

        response = self.request.request(case['method'], case['url'], json.loads(case['data']))
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_admin, "saveQuantitativeTestInfo").write_test_data(case["id"], response.text,
                                                                                       "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_admin, "saveQuantitativeTestInfo").write_test_data(case["id"], response.text,
                                                                                       "Pass")
        self.request.session.close()

    def test_case08_saveInvestorNotification(self):
        self.request.request("get", "/code/image")
        self.request.request("post", "/authentication/form",
                             {"username": data01["userapplyEmail"], "password": data01['password'], "imageCode": "0"})
        self.request.request("get", "/code/judgingIdentity", {"email": data01["userapplyEmail"]})

        response = self.request.request("post", "/rdt/saveInvestorNotification")
        self.assertIn("Save success!", response.json()['message'])

        self.request.session.close()

    @data(*cases07)
    def test_case09_saveSignatureTemplate(self, case):
        self.request.request("get", "/code/image")
        self.request.request("post", "/authentication/form",
                             {"username": data01["userapplyEmail"], "password": data01['password'], "imageCode": "0"})
        self.request.request("get", "/code/judgingIdentity", {"email": data01["userapplyEmail"]})

        response = self.request.request(case['method'], case['url'], json.loads(case['data']))
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_admin, "saveSignatureTemplate").write_test_data(case["id"], response.text, "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_admin, "saveSignatureTemplate").write_test_data(case["id"], response.text, "Pass")
        self.request.session.close()

    @data(*cases08)
    def test_case10_getUserApplicationInfos(self, case):
        self.request.request("get", "/code/image")
        username = conf_class.Conf(constant.testconf_dir).get("User", "admin_user_name")
        password = conf_class.Conf(constant.testconf_dir).get("User", "admin_user_password")
        self.request.request("post", "/authentication/form",
                            {"username": username, "password": password, "imageCode": "0"})
        self.request.request("get", "/code/judgingIdentity", {"email": username})

        response = self.request.request(case['method'], case['url'], json.loads(case['data']))
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_admin, "getUserApplicationInfos").write_test_data(case["id"], response.text, "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_admin, "getUserApplicationInfos").write_test_data(case["id"], response.text, "Pass")
        self.request.session.close()

    @data(*cases09)
    def test_case11_getUserApplicationInfo(self, case):
        self.request.request("get", "/code/image")
        username = conf_class.Conf(constant.testconf_dir).get("User", "admin_user_name")
        password = conf_class.Conf(constant.testconf_dir).get("User", "admin_user_password")
        self.request.request("post", "/authentication/form",
                             {"username": username, "password": password, "imageCode": "0"})
        self.request.request("get", "/code/judgingIdentity", {"email": username})

        data = ast.literal_eval(case['data'])
        if data['userId'] == "{$userid}":
            data['userId'] = data01["result"]["uaid"]

        response = self.request.request(case['method'], case['url'], data)
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_admin, "getUserApplicationInfo").write_test_data(case["id"], response.text, "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_admin, "getUserApplicationInfo").write_test_data(case["id"], response.text, "Pass")
        self.request.session.close()

    @data(*cases10)
    def test_case12_saveUserAccountInfo(self, case):
        self.request.request("get", "/code/image")
        username = conf_class.Conf(constant.testconf_dir).get("User", "admin_user_name")
        password = conf_class.Conf(constant.testconf_dir).get("User", "admin_user_password")
        self.request.request("post", "/authentication/form",
                             {"username": username, "password": password, "imageCode": "0"})
        self.request.request("get", "/code/judgingIdentity", {"email": username})

        data = ast.literal_eval(case['data'])
        if data['userId'] == "{$userid}":
            data['userId'] = data01["result"]["uaid"]

        response = self.request.request(case['method'], case['url'], data)
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_admin, "saveUserAccountInfo").write_test_data(case["id"], response.text, "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_admin, "saveUserAccountInfo").write_test_data(case["id"], response.text, "Pass")
        self.request.session.close()

    @data(*cases11)
    def test_case13_updateAccountStatus(self, case):
        self.request.request("get", "/code/image")
        username = conf_class.Conf(constant.testconf_dir).get("User", "admin_user_name")
        password = conf_class.Conf(constant.testconf_dir).get("User", "admin_user_password")
        self.request.request("post", "/authentication/form",
                             {"username": username, "password": password, "imageCode": "0"})
        self.request.request("get", "/code/judgingIdentity", {"email": username})

        data = ast.literal_eval(case['data'])
        if data['userEmail'] == "{$userEmail}":
            data['userEmail'] = data01["userapplyEmail"]

        response = self.request.request(case['method'], case['url'], data)
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_admin, "updateAccountStatus").write_test_data(case["id"], response.text, "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_admin, "updateAccountStatus").write_test_data(case["id"], response.text, "Pass")
        self.request.session.close()

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        userid = data01["result"]["uid"]
        cls.mysql.modifydata("update t_user_info set whether_del = 1 where id = " + str(userid))
        cls.mysql.close()
        cls.request.session.close()
