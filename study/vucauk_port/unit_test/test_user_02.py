import unittest
import json
from common import constant, request
from configer import conf_class
from common.new_ddt import ddt, data
from common.excel_class_02 import DoExcel


cases01 = DoExcel(constant.case_dir_admin, "saveuserinfo").read_test_data()
cases02 = DoExcel(constant.case_dir_admin, "updateuserinfo").read_test_data()
cases03 = DoExcel(constant.case_dir_admin, "getuserinfolist").read_test_data()
cases04 = DoExcel(constant.case_dir_admin, "getUserInfo").read_test_data()
cases05 = DoExcel(constant.case_dir_admin, "getUserTransactionInfo").read_test_data()
cases06 = DoExcel(constant.case_dir_admin, "getUserNameInfoList").read_test_data()
cases07 = DoExcel(constant.case_dir_admin, "updateuserstatus").read_test_data()


@ddt
class TestUser(unittest.TestCase):

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
    def test_case01_saveuser(self, case):
        response = self.request.request(case['method'], case['url'], json.loads(case['data']))
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_admin, "saveuserinfo").write_test_data(case["id"], response.text, "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_admin, "saveuserinfo").write_test_data(case["id"], response.text, "Pass")

    @data(*cases02)
    def test_case02_updateuser(self, case):
        response = self.request.request(case['method'], case['url'], json.loads(case['data']))
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_admin, "updateuserinfo").write_test_data(case["id"], response.text, "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_admin, "updateuserinfo").write_test_data(case["id"], response.text, "Pass")

    @data(*cases03)
    def test_case03_userinfolist(self, case):
        response = self.request.request(case['method'], case['url'], json.loads(case['data']))
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_admin, "getuserinfolist").write_test_data(case["id"], response.text, "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_admin, "getuserinfolist").write_test_data(case["id"], response.text, "Pass")

    @data(*cases04)
    def test_case04_userinfo(self, case):
        response = self.request.request(case['method'], case['url'], json.loads(case['data']))
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_admin, "getUserInfo").write_test_data(case["id"], response.text, "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_admin, "getUserInfo").write_test_data(case["id"], response.text, "Pass")

    @data(*cases05)
    def test_case05_usertransationinfo(self, case):
        response = self.request.request(case['method'], case['url'], json.loads(case['data']))
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_admin, "getUserTransactionInfo").write_test_data(case["id"], response.text, "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_admin, "getUserTransactionInfo").write_test_data(case["id"], response.text, "Pass")

    @data(*cases06)
    def test_case06_usernameinfolist(self, case):
        response = self.request.request(case['method'], case['url'], json.loads(case['data']))
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_admin, "getUserNameInfoList").write_test_data(case["id"], response.text, "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_admin, "getUserNameInfoList").write_test_data(case["id"], response.text, "Pass")

    @data(*cases07)
    def test_case07_updateuserstatus(self, case):
        response = self.request.request(case['method'], case['url'], json.loads(case['data']))
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_admin, "updateuserstatus").write_test_data(case["id"], response.text, "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_admin, "updateuserstatus").write_test_data(case["id"], response.text, "Pass")

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.request.session.close()
