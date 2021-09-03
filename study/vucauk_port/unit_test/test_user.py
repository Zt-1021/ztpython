import unittest
import json
import requests
import common.constant
from common.login_all import loginaccount
from configer.conf_class import Conf
from unit.user_exit import UserExit
from common.new_ddt import ddt, data
from common.excel_class import DoExcel


cases01 = DoExcel(common.constant.case_dir_admin, "saveuserinfo").read_test_data()
cases02 = DoExcel(common.constant.case_dir_admin, "updateuserinfo").read_test_data()
cases03 = DoExcel(common.constant.case_dir_admin, "getuserinfolist").read_test_data()
cases04 = DoExcel(common.constant.case_dir_admin, "getUserInfo").read_test_data()
cases05 = DoExcel(common.constant.case_dir_admin, "getUserTransactionInfo").read_test_data()
cases06 = DoExcel(common.constant.case_dir_admin, "getUserNameInfoList").read_test_data()
cases07 = DoExcel(common.constant.case_dir_admin, "updateuserstatus").read_test_data()


@ddt
class TestUser(unittest.TestCase):
    def setUp(self):
        self.baseurl = Conf("../configer/test.conf").get("Api", "url")
        self.session = requests.session()
        self.loginAccount = loginaccount(self.baseurl, self.session)
        self.loginAccount.login_user("admin@163.com", "000000")
        self.userexit = UserExit(self.baseurl, self.session)

    def tearDown(self):
        pass

    @data(*cases01)
    def test_case01_saveuser(self, case):
        response = self.userexit.post_saveUserInfo(json.loads(case[4])["uid"],
                                                   json.loads(case[4])["userName"],
                                                   json.loads(case[4])["userGender"],
                                                   json.loads(case[4])["userCellphone"],
                                                   json.loads(case[4])["user163Email"],
                                                   json.loads(case[4])["userBirthday"],
                                                   json.loads(case[4])["userType"],
                                                   json.loads(case[4])["userNationality"],
                                                   json.loads(case[4])["userBankAccount"],
                                                   json.loads(case[4])["userDomicile"],
                                                   json.loads(case[4])["userPassport"],
                                                   json.loads(case[4])["countryOfResidence"],
                                                   json.loads(case[4])["city"],
                                                   json.loads(case[4])["area"],
                                                   json.loads(case[4])["userAccountNumber"],
                                                   json.loads(case[4])["userPostalcode"],
                                                   json.loads(case[4])["password"],
                                                   json.loads(case[4])["userTaxResidency"],
                                                   json.loads(case[4])["swiftCode"],
                                                   json.loads(case[4])["userResidenceProof"])
        self.assertIn(json.loads(case[5]), response.text)

    @data(*cases02)
    def test_case02_updateuser(self, case):
        response = self.userexit.post_updateUserInfo(json.loads(case[4])["uid"],
                                                     json.loads(case[4])["userName"],
                                                     json.loads(case[4])["userGender"],
                                                     json.loads(case[4])["userCellphone"],
                                                     json.loads(case[4])["user163Email"],
                                                     json.loads(case[4])["userBirthday"],
                                                     json.loads(case[4])["userType"],
                                                     json.loads(case[4])["userNationality"],
                                                     json.loads(case[4])["userBankAccount"],
                                                     json.loads(case[4])["userDomicile"],
                                                     json.loads(case[4])["userPassport"],
                                                     json.loads(case[4])["countryOfResidence"],
                                                     json.loads(case[4])["city"],
                                                     json.loads(case[4])["area"],
                                                     json.loads(case[4])["userAccountNumber"],
                                                     json.loads(case[4])["userPostalcode"],
                                                     json.loads(case[4])["userTaxResidency"],
                                                     json.loads(case[4])["swiftCode"],
                                                     json.loads(case[4])["userResidenceProof"])
        self.assertIn(json.loads(case[5]), response.text)

    @data(*cases03)
    def test_case03_userinfolist(self, case):
        response = self.userexit.get_userinfolist(json.loads(case[4])["pageNum"])
        self.assertIn(json.loads(case[5]), response.text)

    @data(*cases04)
    def test_case04_userinfo(self, case):
        response = self.userexit.get_userinfo(json.loads(case[4])["userId"])
        self.assertIn(json.loads(case[5]), response.text)

    @data(*cases05)
    def test_case05_usertransationinfo(self, case):
        response = self.userexit.get_usertransationinfo(json.loads(case[4])["userId"])
        self.assertIn(json.loads(case[5]), response.text)

    @data(*cases06)
    def test_case06_usernameinfolist(self, case):
        response = self.userexit.get_usernameinfolist(json.loads(case[4])["userName"],
                                                      json.loads(case[4])["pageNum"])
        self.assertIn(json.loads(case[5]), response.text)

    @data(*cases07)
    def test_case07_updateuserstatus(self, case):
        response = self.userexit.put_updateuserstatus(json.loads(case[4])["username"],
                                                      json.loads(case[4])["status"])
        self.assertIn(json.loads(case[5]), response.text)
