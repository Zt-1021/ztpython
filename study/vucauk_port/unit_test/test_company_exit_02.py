import unittest
import json
from common import constant, request
from configer import conf_class
from common.new_ddt import ddt, data
from common.excel_class_02 import DoExcel


cases01 = DoExcel(constant.case_dir_admin, "companybasicinfo").read_test_data()
cases02 = DoExcel(constant.case_dir_admin, "addcompanydetailinfo").read_test_data()
cases03 = DoExcel(constant.case_dir_admin, "updatecompanydetailinfo").read_test_data()
cases04 = DoExcel(constant.case_dir_admin, "searchenterprise").read_test_data()
cases05 = DoExcel(constant.case_dir_admin, "getEdetailinfo").read_test_data()
cases06 = DoExcel(constant.case_dir_admin, "savevaluerecord").read_test_data()
cases07 = DoExcel(constant.case_dir_admin, "getvaluerecord").read_test_data()
cases08 = DoExcel(constant.case_dir_admin, "getvaluecordeach").read_test_data()
cases09 = DoExcel(constant.case_dir_admin, "saveintellectualproper").read_test_data()
cases10 = DoExcel(constant.case_dir_admin, "getinteiiproperinfos").read_test_data()
cases11 = DoExcel(constant.case_dir_admin, "getinteiipropereach").read_test_data()
cases12 = DoExcel(constant.case_dir_admin, "EnterpriseAllotmentShares").read_test_data()
cases13 = DoExcel(constant.case_dir_admin, "DistributingUserInfo").read_test_data()
cases14 = DoExcel(constant.case_dir_admin, "saveTargetedCapitalIncrease").read_test_data()
cases15 = DoExcel(constant.case_dir_admin, "saveAdminRigthsRecord").read_test_data()
datas06 = []
datas09 = []
datas14 = []

@ddt
class Testcompanyexit(unittest.TestCase):

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
    def test_case01_savecompanybasicinfo(self, case):  # ????????????---????????????????????????basicinfo---???????????????????????????
        response = self.request.request(case['method'], case['url'], json.loads(case['data']))
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_admin, "companybasicinfo").write_test_data(case["id"], response.text, "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_admin, "companybasicinfo").write_test_data(case["id"], response.text, "Pass")

    @data(*cases02)
    def test_case02_savecompanydetailinfo(self, case):  # ????????????---????????????????????????
        response = self.request.request(case['method'], case['url'], json.loads(case['data']))
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_admin, "addcompanydetailinfo").write_test_data(case["id"], response.text, "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_admin, "addcompanydetailinfo").write_test_data(case["id"], response.text, "Pass")

    @data(*cases03)
    def test_case03_updatecompanydetailinfo(self, case):  # ????????????????????????
        response = self.request.request(case['method'], case['url'], json.loads(case['data']))
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_admin, "updatecompanydetailinfo").write_test_data(case["id"], response.text, "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_admin, "updatecompanydetailinfo").write_test_data(case["id"], response.text, "Pass")

    @data(*cases04)
    def test_case04_searchEnterprise(self, case):  # ???????????????????????????????????????
        response = self.request.request(case['method'], case['url'], json.loads(case['data']))  # ????????? ?????????????????????/?????????????????????
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_admin, "searchenterprise").write_test_data(case["id"], response.text, "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_admin, "searchenterprise").write_test_data(case["id"], response.text, "Pass")

    @data(*cases05)
    def test_case05_getEdetailinfo(self, case):  # ????????????????????????
        response = self.request.request(case['method'], case['url'], json.loads(case['data']))
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_admin, "getEdetailinfo").write_test_data(case["id"], response.text, "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_admin, "getEdetailinfo").write_test_data(case["id"], response.text, "Pass")

    @data(*cases06)
    def test_case06_savevaluationrecordinfo(self, case):  # ????????????????????????
        response = self.request.request(case['method'], case['url'], json.loads(case['data']))
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_admin, "savevaluerecord").write_test_data(case["id"], response.text, "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_admin, "savevaluerecord").write_test_data(case["id"], response.text, "Pass")

        if "Save success" in response.text:
            datas06.append(response.json())

    def test_case07_deletevaluationrecordinfo(self):  # ????????????????????????
        for i in range(0, len(datas06)):
            cmresult = datas06[i]["results"]
            data = {"valuationRecordId": cmresult["valuationRecordId"]}
            response = self.request.request("put", "/rdt/deleteValuationRecordInfo", data)
            self.assertIn("Delete the success???", response.json()['message'])

    @data(*cases07)
    def test_case08_getValuationRecordInfoList(self, case):
        response = self.request.request(case['method'], case['url'], json.loads(case['data']))
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_admin, "getvaluerecord").write_test_data(case["id"], response.text, "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_admin, "getvaluerecord").write_test_data(case["id"], response.text, "Pass")

    @data(*cases08)
    def test_case09_getValuationRecordInfo(self, case):
        response = self.request.request(case['method'], case['url'], json.loads(case['data']))
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_admin, "getvaluecordeach").write_test_data(case["id"], response.text, "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_admin, "getvaluecordeach").write_test_data(case["id"], response.text, "Pass")

    @data(*cases09)
    def test_case10_saveIntellectualPropertyRightsInfo(self, case):
        response = self.request.request(case['method'], case['url'], json.loads(case['data']))
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_admin, "saveintellectualproper").write_test_data(case["id"], response.text, "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_admin, "saveintellectualproper").write_test_data(case["id"], response.text, "Pass")

        if "Save success" in response.text:
            datas09.append(response.json())

    def test_case11_deleteIntellectualPropertyRightsInfo(self):
        for i in range(0, len(datas09)):
            cmresult = datas09[i]["results"]
            data = {"intellectualPropertyId": cmresult["intellectualPropertyId"]}
            response = self.request.request("put", "/rdt/deleteIntellectualPropertyRightsInfo", data)
            self.assertIn("Delete the success???", response.json()['message'])

    @data(*cases10)
    def test_case12_getIntellectualPropertyRightsInfos(self, case):
        response = self.request.request(case['method'], case['url'], json.loads(case['data']))
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_admin, "getinteiiproperinfos").write_test_data(case["id"], response.text, "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_admin, "getinteiiproperinfos").write_test_data(case["id"], response.text, "Pass")

    @data(*cases11)
    def test_case13_getIntellectualPropertyRightsInfo(self, case):
        response = self.request.request(case['method'], case['url'], json.loads(case['data']))
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_admin, "getinteiipropereach").write_test_data(case["id"], response.text, "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_admin, "getinteiipropereach").write_test_data(case["id"], response.text, "Pass")

    @data(*cases12)
    def test_case14_getEnterpriseAllotmentShares(self, case):
        response = self.request.request(case['method'], case['url'], json.loads(case['data']))
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_admin, "EnterpriseAllotmentShares").write_test_data(case["id"], response.text, "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_admin, "EnterpriseAllotmentShares").write_test_data(case["id"], response.text, "Pass")

        if "Information Acquisition Success." in response.text:
            datas14.append(response.json())
    #
    @data(*cases13)
    def test_case15_getDistributingUserInfo(self, case):
        cmresult = datas14[0]["results"]
        data = json.loads(case['data'])
        if data['sharesNumber'] == "{$shareNumber}":
            data['sharesNumber'] = cmresult["undistributedShares"]
        response = self.request.request(case['method'], case['url'], data)
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_admin, "DistributingUserInfo").write_test_data(case["id"], response.text, "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_admin, "DistributingUserInfo").write_test_data(case["id"], response.text, "Pass")

    @data(*cases14)
    def test_case16_postsaveTargetedCapitalIncrease(self, case):
        response = self.request.request(case['method'], case['url'], json.loads(case['data']))
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_admin, "saveTargetedCapitalIncrease").write_test_data(case["id"], response.text, "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_admin, "saveTargetedCapitalIncrease").write_test_data(case["id"], response.text, "Pass")

    @data(*cases15)
    def test_case17_postsaveAdminRigthsRecord(self, case):
        response = self.request.request(case['method'], case['url'], json.loads(case['data']))
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_admin, "saveAdminRigthsRecord").write_test_data(case["id"], response.text, "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_admin, "saveAdminRigthsRecord").write_test_data(case["id"], response.text, "Pass")

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.request.session.close()

