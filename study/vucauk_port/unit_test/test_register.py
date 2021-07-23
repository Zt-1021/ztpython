import unittest
import json
import requests
import common.constant
from common.login_all import loginaccount
from configer.conf_class import Conf
from unit.register import Register
from ddt import ddt, data
from common.excel_class import DoExcel


cases01 = DoExcel(common.constant.case_dir_admin, "saveuserapplicationinfo").read_test_data()
cases02 = DoExcel(common.constant.case_dir_admin, "sendRegisterMail").read_test_data()
cases03 = DoExcel(common.constant.case_dir_admin, "getworkorder").read_test_data()
data01 = []


@ddt
class Testsystemworkinfo(unittest.TestCase):
    def setUp(self):
        self.baseurl = Conf("../configer/conf.conf").getvalue("Http", "testurl")
        self.session = requests.session()
        # self.loginAccount = loginaccount(self.baseurl, self.session)
        # self.loginAccount.login_user("admin@163.com", "000000")
        self.systemwork = Register(self.baseurl, self.session)

    def tearDown(self):
        pass

    @data(*cases01)
    def test_case01_saveUserApplicationInfo(self, case):
        response = self.systemwork.post_saveUserApplicationInfo(json.loads(case[4])["userapplyName"],
                                                                json.loads(case[4])["userapplyEmail"],
                                                                json.loads(case[4])["password"],
                                                                json.loads(case[4])["userapplyCellphone"],
                                                                json.loads(case[4])["userGender"])
        self.assertIn(json.loads(case[5]), response.text)
        # if response.test["message"] == "Application is successful!":
        #     data01.append(response.json())

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
