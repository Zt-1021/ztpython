import unittest
import json
import requests
import common.constant
from common.login_all import loginaccount
from configer.conf_class import Conf
from unit.order import Order
from ddt import ddt, data
from common.excel_class import DoExcel


cases01 = DoExcel(common.constant.case_dir_admin, "getorderinfo").read_test_data()
cases02 = DoExcel(common.constant.case_dir_admin, "getpaymentinfo").read_test_data()
cases03 = DoExcel(common.constant.case_dir_admin, "getuserorderinfo").read_test_data()
cases04 = DoExcel(common.constant.case_dir_admin, "updateuserorderstate").read_test_data()
cases05 = DoExcel(common.constant.case_dir_admin, "getaccountbalanceinfo").read_test_data()
cases06 = DoExcel(common.constant.case_dir_admin, "updateAccountBanlanceState").read_test_data()
cases07 = DoExcel(common.constant.case_dir_admin, "addTransactionInfo").read_test_data()


@ddt
class TestOrder(unittest.TestCase):
    def setUp(self):
        self.baseurl = Conf("../configer/test.conf").get("Api", "url")
        self.session = requests.session()
        self.loginAccount = loginaccount(self.baseurl, self.session)
        self.loginAccount.login_user("admin@163.com", "000000")
        self.order = Order(self.baseurl, self.session)

    def tearDown(self):
        pass

    @data(*cases01)
    def test_case01_getorderinfo(self, case):
        response = self.order.get_orderinfo(json.loads(case[4])["pageNum"])
        self.assertIn(json.loads(case[5]), response.text)

    @data(*cases02)
    def test_case02_getpaymentinfo(self, case):
        response = self.order.get_paymentinfo(json.loads(case[4])["transactionId"],
                                              json.loads(case[4])["orderId"],
                                              json.loads(case[4])["orderStatus"])
        self.assertIn(json.loads(case[5]), response.text)

    @data(*cases03)
    def test_case03_getuserorderinfo(self, case):
        response = self.order.get_userorderinfo(json.loads(case[4])["matchOrderId"],
                                                json.loads(case[4])["orderIdentity"],
                                                json.loads(case[4])["pageNum"])
        self.assertIn(json.loads(case[5]), response.text)

    @data(*cases04)
    def test_case04_updateuserorderstate(self, case):
        response = self.order.put_updateuserorderstate(json.loads(case[4])["state"],
                                                       json.loads(case[4])["userOrderId"])
        self.assertIn(json.loads(case[5]), response.text)

    @data(*cases05)
    def test_case05_getaccountbalanceinfo(self, case):
        response = self.order.get_accountbalanceinfolist(json.loads(case[4])["pageSize"],
                                                         json.loads(case[4])["pageNum"])
        self.assertIn(json.loads(case[5]), response.text)

    @data(*cases06)
    def test_case06_updateAccountBanlanceState(self, case):
        response = self.order.put_updateAccountBanlanceState(json.loads(case[4])["accountBalanceId"],
                                                             json.loads(case[4])["balanceType"])
        self.assertIn(json.loads(case[5]), response.text)

    @data(*cases07)
    def test_case07_addTransactionInfo(self, case):
        response = self.order.post_addTransactionInfo(json.loads(case[4])["orderBuyerId"],
                                                      json.loads(case[4])["orderTransferId"],
                                                      json.loads(case[4])["orderSharesNumber"],
                                                      json.loads(case[4])["orderSharesPaid"],
                                                      json.loads(case[4])["enterpriseId"],
                                                      json.loads(case[4])["transactionElectronicReceipt"],
                                                      json.loads(case[4])["transactionVoucher"],
                                                      json.loads(case[4])["stampDuty"],
                                                      json.loads(case[4])["vat"],
                                                      json.loads(case[4])["vucaPoundage"],
                                                      json.loads(case[4])["mangoPayPoundage"],
                                                      json.loads(case[4])["amount"])
        self.assertIn(json.loads(case[5]), response.text)
