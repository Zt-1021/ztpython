import unittest
import json
from common import constant, request
from configer import conf_class
from ddt import ddt, data
from common.excel_class_02 import DoExcel


cases01 = DoExcel(constant.case_dir_user, "getOrderDetailsDto").read_test_data()
# cases02 = DoExcel(constant.case_dir_user, "saveAccountBalanceInfo").read_test_data()
cases03 = DoExcel(constant.case_dir_user, "getEnterpriseData").read_test_data()
cases04 = DoExcel(constant.case_dir_user, "saveUserEnterpriseReleation").read_test_data()
cases05 = DoExcel(constant.case_dir_user, "getShareCertificateInfos").read_test_data()
cases06 = DoExcel(constant.case_dir_user, "downloadShareCertificate").read_test_data()
# cases07 = DoExcel(constant.case_dir_user, "saveUserTransactionOrder").read_test_data()
cases08 = DoExcel(constant.case_dir_user, "getUserOrderInfoDTO").read_test_data()
# cases09 = DoExcel(constant.case_dir_user, "updateUserOrderState").read_test_data()
cases10 = DoExcel(constant.case_dir_user, "getuserinfo").read_test_data()


@ddt
class Testuserport(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.request = request.Request()
        cls.request.request("get", "/code/image")
        username = conf_class.Conf(constant.testconf_dir).get("User", "investor_user_name")
        password = conf_class.Conf(constant.testconf_dir).get("User", "investor_user_password")
        cls.request.request("post", "/authentication/form",
                             {"username": username, "password": password, "imageCode": "0"})
        cls.request.request("get", "/code/judgingIdentity", {"email": username})

    def setUp(self):
        pass

    def test_case01_getuserunpaidorder(self):
        response = self.request.request("get", "/rdt/getUserUnpaidOrder")
        self.assertIn("Get information successfully.", response.text)

    def test_case02_getaccountbalance(self):
        response = self.request.request("get", "/rdt/getAccountBalance")
        self.assertIn("Get success.", response.text)

    @data(*cases01)
    def test_case03_getorderdetail(self, case):
        response = self.request.request(case['method'], case['url'], json.loads(case['data']))
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_user, "getOrderDetailsDto").write_test_data(case["id"], response.text,
                                                                                        "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_user, "getOrderDetailsDto").write_test_data(case["id"], response.text,
                                                                                        "Pass")

    # @data(*cases02)
    # def test_case04_saveaccountbalanceinfo(self, case):
    #     response = self.request.request(case['method'], case['url'], json.loads(case['data']))
    #     try:
    #         self.assertIn(case['excepted'], response.json()['message'])
    #     except AssertionError as e:
    #         DoExcel(constant.case_dir_user, "saveAccountBalanceInfo").write_test_data(case["id"], response.text, "Failed")
    #         print(e)
    #     else:
    #         DoExcel(constant.case_dir_user, "saveAccountBalanceInfo").write_test_data(case["id"], response.text, "Pass")

    @data(*cases03)
    def test_case05_getEnterpriseData(self, case):
        response = self.request.request(case['method'], case['url'], json.loads(case['data']))
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_user, "getEnterpriseData").write_test_data(case["id"], response.text, "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_user, "getEnterpriseData").write_test_data(case["id"], response.text, "Pass")

    @data(*cases04)
    def test_case06_saveUserEnterpriseReleation(self, case):
        response = self.request.request(case['method'], case['url'], json.loads(case['data']))
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_user, "saveUserEnterpriseReleation").write_test_data(case["id"], response.text, "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_user, "saveUserEnterpriseReleation").write_test_data(case["id"], response.text, "Pass")

    @data(*cases05)
    def test_case07_getShareCertificateInfos(self, case):
        response = self.request.request(case['method'], case['url'], json.loads(case['data']))
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_user, "getShareCertificateInfos").write_test_data(case["id"], response.text, "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_user, "getShareCertificateInfos").write_test_data(case["id"], response.text, "Pass")

    @data(*cases06)
    def test_case08_downloadShareCertificate(self, case):
        response = self.request.request(case['method'], case['url'], json.loads(case['data']))
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_user, "downloadShareCertificate").write_test_data(case["id"], response.text, "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_user, "downloadShareCertificate").write_test_data(case["id"], response.text, "Pass")

    # @data(*cases07)
    # def test_case09_saveUserTransactionOrder(self, case):
    #     response = self.request.request(case['method'], case['url'], json.loads(case['data']))
    #     try:
    #         self.assertIn(case['excepted'], response.json()['message'])
    #     except AssertionError as e:
    #         DoExcel(constant.case_dir_user, "saveUserTransactionOrder").write_test_data(case["id"], response.text, "Failed")
    #         print(e)
    #     else:
    #         DoExcel(constant.case_dir_user, "saveUserTransactionOrder").write_test_data(case["id"], response.text, "Pass")

    @data(*cases08)
    def test_case10_getUserOrderInfoDTO(self, case):
        response = self.request.request(case['method'], case['url'], json.loads(case['data']))
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_user, "getUserOrderInfoDTO").write_test_data(case["id"], response.text, "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_user, "getUserOrderInfoDTO").write_test_data(case["id"], response.text, "Pass")

    # @data(*cases09)
    # def test_case11_updateUserOrderState(self, case):
    #     response = self.request.request(case['method'], case['url'], json.loads(case['data']))
    #     try:
    #         self.assertIn(case['excepted'], response.json()['message'])
    #     except AssertionError as e:
    #         DoExcel(constant.case_dir_user, "updateUserOrderState").write_test_data(case["id"], response.text, "Failed")
    #         print(e)
    #     else:
    #         DoExcel(constant.case_dir_user, "updateUserOrderState").write_test_data(case["id"], response.text, "Pass")

    @data(*cases10)
    def test_case12_getUserInfo(self, case):
        response = self.request.request(case['method'], case['url'], json.loads(case['data']))
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_user, "getuserinfo").write_test_data(case["id"], response.text, "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_user, "getuserinfo").write_test_data(case["id"], response.text, "Pass")

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.request.session.close()


