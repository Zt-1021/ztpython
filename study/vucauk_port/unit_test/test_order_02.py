import unittest
import json
from common import constant, request
from configer import conf_class
from common.new_ddt import ddt, data
from common.excel_class_02 import DoExcel


cases01 = DoExcel(constant.case_dir_admin, "getorderinfo").read_test_data()
cases02 = DoExcel(constant.case_dir_admin, "getpaymentinfo").read_test_data()
cases03 = DoExcel(constant.case_dir_admin, "getuserorderinfo").read_test_data()
cases04 = DoExcel(constant.case_dir_admin, "updateuserorderstate").read_test_data()
cases05 = DoExcel(constant.case_dir_admin, "getaccountbalanceinfo").read_test_data()
cases06 = DoExcel(constant.case_dir_admin, "updateAccountBanlanceState").read_test_data()
cases07 = DoExcel(constant.case_dir_admin, "addTransactionInfo").read_test_data()


@ddt
class TestOrder(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.request = request.Request()
        cls.request.request("get", "/code/image")
        username = conf_class.Conf(constant.testconf_dir).get("User", "admin_user_name")
        password = conf_class.Conf(constant.testconf_dir).get("User", "admin_user_password")
        cls.request.request("post", "/authentication/form",
                             {"username": username, "password": password, "imageCode": "0"})
        cls.request.request("get", "/code/judgingIdentity", {"email": username})

    def setUp(self):
        pass

    @data(*cases01)
    def test_case01_getorderinfo(self, case):
        response = self.request.request(case['method'], case['url'], json.loads(case['data']))
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_admin, "getorderinfo").write_test_data(case["id"], response.text, "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_admin, "getorderinfo").write_test_data(case["id"], response.text, "Pass")

    @data(*cases02)
    def test_case02_getpaymentinfo(self, case):
        response = self.request.request(case['method'], case['url'], json.loads(case['data']))
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_admin, "getpaymentinfo").write_test_data(case["id"], response.text, "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_admin, "getpaymentinfo").write_test_data(case["id"], response.text, "Pass")

    @data(*cases03)
    def test_case03_getuserorderinfo(self, case):
        response = self.request.request(case['method'], case['url'], json.loads(case['data']))
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_admin, "getuserorderinfo").write_test_data(case["id"], response.text, "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_admin, "getuserorderinfo").write_test_data(case["id"], response.text, "Pass")

    @data(*cases04)
    def test_case04_updateuserorderstate(self, case):
        response = self.request.request(case['method'], case['url'], json.loads(case['data']))
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_admin, "updateuserorderstate").write_test_data(case["id"], response.text, "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_admin, "updateuserorderstate").write_test_data(case["id"], response.text, "Pass")

    @data(*cases05)
    def test_case05_getaccountbalanceinfo(self, case):
        response = self.request.request(case['method'], case['url'], json.loads(case['data']))
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_admin, "getaccountbalanceinfo").write_test_data(case["id"], response.text,
                                                                                     "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_admin, "getaccountbalanceinfo").write_test_data(case["id"], response.text, "Pass")

    @data(*cases06)
    def test_case06_updateAccountBanlanceState(self, case):
        response = self.request.request(case['method'], case['url'], json.loads(case['data']))
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_admin, "updateAccountBanlanceState").write_test_data(case["id"], response.text,
                                                                                      "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_admin, "updateAccountBanlanceState").write_test_data(case["id"], response.text, "Pass")

    @data(*cases07)
    def test_case07_addTransactionInfo(self, case):
        response = self.request.request(case['method'], case['url'], json.loads(case['data']))
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_admin, "addTransactionInfo").write_test_data(case["id"], response.text,
                                                                                           "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_admin, "addTransactionInfo").write_test_data(case["id"], response.text,
                                                                                           "Pass")

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.request.session.close()
