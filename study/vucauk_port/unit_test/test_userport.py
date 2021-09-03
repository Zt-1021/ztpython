import unittest
import json
import requests
import common.constant
from common.login_all import loginaccount
from configer.conf_class import Conf
from unit.user_port import UserPort
from common.new_ddt import ddt, data
from common.excel_class import DoExcel


cases01 = DoExcel(common.constant.case_dir_user, "getOrderDetailsDto").read_test_data()
cases02 = DoExcel(common.constant.case_dir_user, "saveAccountBalanceInfo").read_test_data()
cases03 = DoExcel(common.constant.case_dir_user, "getEnterpriseData").read_test_data()
cases04 = DoExcel(common.constant.case_dir_user, "saveUserEnterpriseReleation").read_test_data()
cases05 = DoExcel(common.constant.case_dir_user, "getShareCertificateInfos").read_test_data()
cases06 = DoExcel(common.constant.case_dir_user, "downloadShareCertificate").read_test_data()
cases07 = DoExcel(common.constant.case_dir_user, "saveUserTransactionOrder").read_test_data()
cases08 = DoExcel(common.constant.case_dir_user, "getUserOrderInfoDTO").read_test_data()
cases09 = DoExcel(common.constant.case_dir_user, "updateUserOrderState").read_test_data()
cases10 = DoExcel(common.constant.case_dir_user, "getuserinfo").read_test_data()


@ddt
class Testuserport(unittest.TestCase):
    def setUp(self):
        self.baseurl = Conf("../configer/test.conf").get("Api", "url")
        self.session = requests.session()
        self.loginAccount = loginaccount(self.baseurl, self.session)
        self.loginAccount.login_user("zt_1021@163.com", "zt123456")
        self.userport = UserPort(self.baseurl, self.session)

    def tearDown(self):
        pass

    def test_case01_getuserunpaidorder(self):
        response = self.userport.get_UserUnpaidOrder()
        self.assertIn("Get information successfully.", response.text)

    def test_case02_getaccountbalance(self):
        response = self.userport.get_accountbalance()
        self.assertIn("Get success.", response.text)

    @data(cases01)
    def test_case03_getorderdetail(self, case):
        response = self.userport.get_orderdetail(json.loads(case[4])["transactionNumber"])
        self.assertIn(json.loads(case[5]), response.text)

    @data(cases02)
    def test_case04_saveaccountbalanceinfo(self, case):
        response = self.userport.post_saveacconuntbalabceinfo(json.loads(case[4])["transactionNumber"],
                                                              json.loads(case[4])["decimal"])
        self.assertIn(json.loads(case[5]), response.text)

    @data(cases03)
    def test_case05_getEnterpriseData(self, case):
        response = self.userport.get_getEnterpriseData(json.loads(case[4])["pageNum"])
        self.assertIn(json.loads(case[5]), response.text)

    @data(cases04)
    def test_case06_saveUserEnterpriseReleation(self, case):
        response = self.userport.post_saveUserEnterpriseReleation(json.loads(case[4])["enterpriseId"])
        self.assertIn(json.loads(case[5]), response.text)

    @data(cases05)
    def test_case07_getShareCertificateInfos(self, case):
        response = self.userport.get_sharecertificateinfo(json.loads(case[4])["enterpriseId"])
        self.assertIn(json.loads(case[5]), response.text)

    @data(cases06)
    def test_case08_downloadShareCertificate(self, case):
        response = self.userport.get_downloadShareCertificate(json.loads(case[4])["shareId"])
        self.assertIn(json.loads(case[5]), response.text)

    @data(cases07)
    def test_case09_saveUserTransactionOrder(self, case):
        response = self.userport.post_saveUserTransactionOrder(json.loads(case[4])["enterpriseId"],
                                                               json.loads(case[4])["userorderIdentity"],
                                                               json.loads(case[4])["userorderSharesNumber"],
                                                               json.loads(case[4])["intuserorderSharesPaid"],
                                                               json.loads(case[4])["userId"],
                                                               json.loads(case[4])["certificateId"])
        self.assertIn(json.loads(case[5]), response.text)

    @data(cases08)
    def test_case10_getUserOrderInfoDTO(self, case):
        response = self.userport.get_getUserOrderInfoDTO(json.loads(case[4])["userOrderId"])
        self.assertIn(json.loads(case[5]), response.text)

    @data(cases09)
    def test_case11_updateUserOrderState(self, case):
        response = self.userport.put_updateUserOrderState(json.loads(case[4])["state"],
                                                          json.loads(case[4])["userOrderId"])
        self.assertIn(json.loads(case[5]), response.text)

    @data(cases10)
    def test_case12_getUserInfo(self, case):
        response = self.userport.get_UserInfo(json.loads(case[4])["userId"])
        self.assertIn(json.loads(case[5]), response.text)




