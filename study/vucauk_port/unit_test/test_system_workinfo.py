import unittest
import json
import requests
import common.constant
from common.login_all import loginaccount
from configer.conf_class import Conf
from unit.system_workinfo import SystemWork
from ddt import ddt, data
from common.excel_class import DoExcel


cases01 = DoExcel(common.constant.case_dir_admin, "addworkorder").read_test_data()
cases02 = DoExcel(common.constant.case_dir_admin, "getworkorders").read_test_data()
cases03 = DoExcel(common.constant.case_dir_admin, "getworkorder").read_test_data()


@ddt
class Testsystemworkinfo(unittest.TestCase):
    def setUp(self):
        self.baseurl = Conf("../configer/conf.conf").getvalue("Http", "testurl")
        self.session = requests.session()
        self.loginAccount = loginaccount(self.baseurl, self.session)
        self.loginAccount.login_user("admin@163.com", "000000")
        self.systemwork = SystemWork(self.baseurl, self.session)

    def tearDown(self):
        pass

    @data(*cases01)
    def test_case01_addwoinfo(self, case):
        response = self.systemwork.post_addwoinfo(json.loads(case[4])["workContactTheme"],
                                                  json.loads(case[4])["workContactName"],
                                                  json.loads(case[4])["workContactEmail"],
                                                  json.loads(case[4])["workContactPhone"],
                                                  json.loads(case[4])["workContent"])
        self.assertIn(json.loads(case[5]), response.text)

    @data(*cases02)
    def test_case02_getuserworkorders(self, case):
        response = self.systemwork.get_userworkorders(json.loads(case[4])["pageNum"])
        self.assertIn(json.loads(case[5]), response.text)

    @data(*cases03)
    def test_case03_getuserworkorder(self, case):
        response = self.systemwork.get_userworkorder(json.loads(case[4])["userWorkOrderId"])
        self.assertIn(json.loads(case[5]), response.text)




