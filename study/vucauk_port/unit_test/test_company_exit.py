import unittest
import json
import requests
import common.constant
from common.login_all import loginaccount
from configer.conf_class import Conf
from unit.company_exit import CompanyExit
from ddt import ddt, data
from common.excel_class import DoExcel


cases01 = DoExcel(common.constant.case_dir_admin, "companybasicinfo").read_test_data()
cases02 = DoExcel(common.constant.case_dir_admin, "addcompanydetailinfo").read_test_data()
cases03 = DoExcel(common.constant.case_dir_admin, "searchenterprise").read_test_data()
cases04 = DoExcel(common.constant.case_dir_admin, "getEdetailinfo").read_test_data()
cases05 = DoExcel(common.constant.case_dir_admin, "savevaluerecord").read_test_data()
cases06 = DoExcel(common.constant.case_dir_admin, "getvaluerecord").read_test_data()
cases07 = DoExcel(common.constant.case_dir_admin, "saveintellectualproper").read_test_data()
cases08 = DoExcel(common.constant.case_dir_admin, "getinteiiproperinfos").read_test_data()
cases09 = DoExcel(common.constant.case_dir_admin, "getinteiipropereach").read_test_data()
cases10 = DoExcel(common.constant.case_dir_admin, "getvaluecordeach").read_test_data()
cases11 = DoExcel(common.constant.case_dir_admin, "EnterpriseAllotmentShares").read_test_data()
cases12 = DoExcel(common.constant.case_dir_admin, "DistributingUserInfo").read_test_data()
cases13 = DoExcel(common.constant.case_dir_admin, "saveTargetedCapitalIncrease").read_test_data()
cases14 = DoExcel(common.constant.case_dir_admin, "saveAdminRigthsRecord").read_test_data()
datas05 = []
datas07 = []
datas11 = []


@ddt
class Testcompanyexit(unittest.TestCase):
    def setUp(self):
        self.baseurl = Conf("../configer/test.conf").get("Api", "url")
        self.session = requests.session()
        self.loginAccount = loginaccount(self.baseurl, self.session)
        self.loginAccount.login_user("admin@163.com", "000000")
        self.companyexit = CompanyExit(self.baseurl, self.session)

    def tearDown(self):
        pass

    # @data(*cases01)
    # def test_case01_savecompanybasicinfo(self, case):
    #     response = self.companyexit.post_saveenterpriseinfo(json.loads(case[4])["enterpriseName"],
    #                                                         json.loads(case[4])["enterpriseCapitalType"],
    #                                                         json.loads(case[4])["enterpriseType"],
    #                                                         json.loads(case[4])["detailBusinessCertificateNumber"],
    #                                                         json.loads(case[4])["detailCommercialEnterprise"],
    #                                                         json.loads(case[4])["enterpriseGicscode"],
    #                                                         json.loads(case[4])["detailCorporateRepresentative"],
    #                                                         json.loads(case[4])["enterpriseEstablishdate"],
    #                                                         json.loads(case[4])["detailOfficeaddress"],
    #                                                         json.loads(case[4])["enterpriseRegisteredcapital"],
    #                                                         json.loads(case[4])["detailStuffamount"],
    #                                                         json.loads(case[4])["enterpriseTotalShares"],
    #                                                         json.loads(case[4])["detailFinancingRound"],
    #                                                         json.loads(case[4])["enterpriseParValue"],
    #                                                         json.loads(case[4])["systemType"],
    #                                                         json.loads(case[4])["enterpriseId"],
    #                                                         json.loads(case[4])["enterpriseRegisteredaddress"])
    #     self.assertIn(json.loads(case[5]), response.text)
    #
    # @data(*cases02)
    # def test_case02_savecompanydetailinfo(self, case):
    #     response = self.companyexit.post_addEnterpriseDetailInfo(json.loads(case[4])["enterpriseQuotename"],
    #                                                              json.loads(case[4])["enterpriseIntroduce"],
    #                                                              json.loads(case[4])["detailPhonenumber"],
    #                                                              json.loads(case[4])["detailEmail"],
    #                                                              # json.loads(case[4])["detailOfficialwebsite"],
    #                                                              json.loads(case[4])["enterpriseId"],
    #                                                              json.loads(case[4])["detailTrademark"])
    #     self.assertIn(json.loads(case[5]), response.text)
    #
    # @data(*cases03)
    # def test_case03_searchEnterprise(self, case):
    #     response = self.companyexit.get_searchEnterprise(json.loads(case[4])["pageNum"],
    #                                                      json.loads(case[4])["conditions"])
    #     self.assertIn(json.loads(case[5]), response.text)
    #
    # @data(*cases04)
    # def test_case04_getEdetailinfo(self, case):
    #     response = self.companyexit.get_edetailinfo(json.loads(case[4])["enterpriseId"])
    #     self.assertIn(json.loads(case[5]), response.text)
    #
    # @data(*cases05)
    # def test_case05_savevaluationrecordinfo(self, case):
    #     response = self.companyexit.post_savevaluationrecordinfo(json.loads(case[4])["enterpriseId"],
    #                                                              json.loads(case[4])["valuationTime"],
    #                                                              json.loads(case[4])["valuationResult"],
    #                                                              json.loads(case[4])["valuationResultsDate"],
    #                                                              json.loads(case[4])["valuationRecordId"],
    #                                                              json.loads(case[4])["valuationEvaluator"])
    #     self.assertIn(json.loads(case[5]), response.text)
    #     if "Save success" in response.text:
    #         datas05.append(response.json())
    #
    # def test_case06_deletevaluationrecordinfo(self):
    #     cmids = []
    #     for i in range(0, len(datas05)):
    #         cmresult = datas05[i]["results"]
    #         cmids.append(cmresult["valuationRecordId"])
    #     response = self.companyexit.put_deletevaluationrecordinfo(cmids)
    #     print(response.text)
    #     for j in range(0, len(cmids)):
    #         self.assertEqual(cmids[j], json.loads(response.text)["results"])
    #
    # @data(*cases06)
    # def test_case07_getValuationRecordInfoList(self, case):
    #     response = self.companyexit.get_ValuationRecordInfoList(json.loads(case[4])["pageNum"],
    #                                                             json.loads(case[4])["pageSize"],
    #                                                             json.loads(case[4])["enterpriseId"])
    #     self.assertIn(json.loads(case[5]), response.text)
    #
    # @data(*cases10)
    # def test_case08_getValuationRecordInfo(self, case):
    #     response = self.companyexit.get_getValuationRecordInfo(json.loads(case[4])["valuationRecordId"])
    #     self.assertIn(json.loads(case[5]), response.text)
    #
    # @data(*cases07)
    # def test_case09_saveIntellectualPropertyRightsInfo(self, case):
    #     response = self.companyexit.post_saveIntellectualPropertyRightsInfo(json.loads(case[4])["intellectualPropertyName"],  #  255
    #                                                                         json.loads(case[4])["intellectualPropertyType"],
    #                                                                         json.loads(case[4])["intellectualPropertyStartTime"],
    #                                                                         json.loads(case[4])["intellectualPropertyEndTime"],
    #                                                                         json.loads(case[4])["enterpriseId"],
    #                                                                         json.loads(case[4])["intellectualPropertyId"])
    #     self.assertIn(json.loads(case[5]), response.text)
    #     if "Save success" in response.text:
    #         datas07.append(response.json())
    #
    # def test_case10_deleteIntellectualPropertyRightsInfo(self):
    #     cmids = []
    #     for i in range(0, len(datas07)):
    #         cmresult = datas07[i]["results"]
    #         cmids.append(cmresult["intellectualPropertyId"])
    #     response = self.companyexit.put_deleteIntellectualPropertyRightsInfo(cmids)
    #     print(response.text)
    #     for j in range(0, len(cmids)):
    #         self.assertEqual(cmids[j], json.loads(response.text)["results"]["id"])
    #
    # @data(*cases08)
    # def test_case11_getIntellectualPropertyRightsInfos(self, case):
    #     response = self.companyexit.get_IntellectualPropertyRightsInfos(json.loads(case[4])["pageNum"],
    #                                                                     json.loads(case[4])["pageSize"],
    #                                                                     json.loads(case[4])["enterpriseId"])
    #     self.assertIn(json.loads(case[5]), response.text)
    #
    # @data(*cases09)
    # def test_case12_getIntellectualPropertyRightsInfo(self, case):
    #     response = self.companyexit.get_IntellectualPropertyRightsInfo(json.loads(case[4])["intellectualPropertyId"])
    #     self.assertIn(json.loads(case[5]), response.text)

    @data(*cases11)
    def test_case13_getEnterpriseAllotmentShares(self, case):
        response = self.companyexit.get_EnterpriseAllotmentShares(json.loads(case[4])["enterpriseId"])
        self.assertIn(json.loads(case[5]), response.text)
        if "Information Acquisition Success." in response.text:
            datas11.append(response.json())

    @data(*cases12)
    def test_case14_getDistributingUserInfo(self, case):
        cmresult = datas11[0]["results"]
        sharesnumber = cmresult["undistributedShares"]
        response = self.companyexit.get_DistributingUserInfo(json.loads(case[4])["pageNum"],
                                                             json.loads(case[4])["enterpriseId"],
                                                             sharesnumber)
        self.assertIn(json.loads(case[5]), response.text)

    @data(*cases13)
    def test_case15_postsaveTargetedCapitalIncrease(self, case):
        response = self.companyexit.post_saveTargetedCapitalIncrease(json.loads(case[4])["enterpriseId"],
                                                                     json.loads(case[4])["tciUserIdList"],
                                                                     json.loads(case[4])["tciUserStockList"])
        self.assertIn(json.loads(case[5]), response.text)

    @data(*cases14)
    def test_case16_postsaveAdminRigthsRecord(self, case):
        response = self.companyexit.post_saveAdminRigthsRecord(json.loads(case[4])["enterpriseId"],
                                                               json.loads(case[4])["tciPrice"],
                                                               json.loads(case[4])["tciShares"])
        self.assertIn(json.loads(case[5]), response.text)
