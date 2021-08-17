import unittest
import json
import ast
from common import mysql
from common import constant, request
from configer import conf_class
from ddt import ddt, data
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
datas = {}


@ddt
class Testcompanyexit(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.request = request.Request()

        cls.host = conf_class.Conf(constant.testconf_dir).get("MysqlDatabase", "host")
        cls.username = conf_class.Conf(constant.testconf_dir).get("MysqlDatabase", "username")
        cls.password = conf_class.Conf(constant.testconf_dir).get("MysqlDatabase", "password")
        cls.database = conf_class.Conf(constant.testconf_dir).get("MysqlDatabase", "database")
        cls.port = conf_class.Conf(constant.testconf_dir).get("MysqlDatabase", "port")
        cls.mysql = mysql.Mysql(cls.host, cls.username, cls.password, cls.database, int(cls.port))

        cls.request.request("get", "/code/image")
        username = conf_class.Conf(constant.testconf_dir).get("User", "admin_user_name")
        password = conf_class.Conf(constant.testconf_dir).get("User", "admin_user_password")
        cls.request.request("post", "/authentication/form",
                             {"username": username, "password": password, "imageCode": "0"})
        cls.request.request("get", "/code/judgingIdentity", {"email": username})

    def setUp(self):
        pass

    @data(*cases01)     # 接口返回结果{"code":"S01","message":"Operation is successful!","results":8}，，有公司id
    def test_case01_savecompanybasicinfo(self, case):  # 添加公司---保存公司基本信息basicinfo---添加和修改共用一个

        data = ast.literal_eval(case['data'])
        if data['enterpriseName'] == "{$enterpriseName}":
            enterpriseName = self.mysql.fetchone("select enterprise_name from t_enterprise_info ORDER BY id desc limit 1")
            newenterpriseName = enterpriseName[0] + "1"
            data['enterpriseName'] = newenterpriseName

        response = self.request.request(case['method'], case['url'], data)
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_admin, "companybasicinfo").write_test_data(case["id"], response.text, "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_admin, "companybasicinfo").write_test_data(case["id"], response.text, "Pass")

        if "Operation is successful!" in response.text:
            datas['result'] = response.json()["results"]

    @data(*cases02)
    def test_case02_savecompanydetailinfo(self, case):  # 添加公司---保存公司详细信息

        data = ast.literal_eval(case['data'])
        if data['enterpriseId'] == "{$enterpriseId}":
            data['enterpriseId'] = datas["result"]

        response = self.request.request(case['method'], case['url'], data)

        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_admin, "addcompanydetailinfo").write_test_data(case["id"], response.text, "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_admin, "addcompanydetailinfo").write_test_data(case["id"], response.text, "Pass")

    @data(*cases03)
    def test_case03_updatecompanydetailinfo(self, case):  # 修改公司详细信息

        data = ast.literal_eval(case['data'])
        if data['enterpriseId'] == "{$enterpriseId}":
            data['enterpriseId'] = datas["result"]

        response = self.request.request(case['method'], case['url'], data)
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_admin, "updatecompanydetailinfo").write_test_data(case["id"], response.text, "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_admin, "updatecompanydetailinfo").write_test_data(case["id"], response.text, "Pass")

    @data(*cases04)
    def test_case04_searchEnterprise(self, case):  # 管理员根据条件筛选公司信息
        response = self.request.request(case['method'], case['url'], json.loads(case['data']))  # 页码， 条件（公司名字/公司报价名字）
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_admin, "searchenterprise").write_test_data(case["id"], response.text, "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_admin, "searchenterprise").write_test_data(case["id"], response.text, "Pass")

    @data(*cases05)
    def test_case05_getEdetailinfo(self, case):  # 获取公司基本信息
        response = self.request.request(case['method'], case['url'], json.loads(case['data']))
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_admin, "getEdetailinfo").write_test_data(case["id"], response.text, "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_admin, "getEdetailinfo").write_test_data(case["id"], response.text, "Pass")

    @data(*cases06)
    def test_case06_savevaluationrecordinfo(self, case):  # 保存估值记录信息

        data = ast.literal_eval(case['data'])
        if data['enterpriseId'] == "{$enterpriseId}":
            data['enterpriseId'] = datas["result"]

        response = self.request.request(case['method'], case['url'], data)
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_admin, "savevaluerecord").write_test_data(case["id"], response.text, "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_admin, "savevaluerecord").write_test_data(case["id"], response.text, "Pass")

        if "Save success" in response.text:
            datas06.append(response.json())

    @data(*cases07)
    def test_case07_getValuationRecordInfoList(self, case):

        data = ast.literal_eval(case['data'])
        if data['enterpriseId'] == "{$enterpriseId}":
            data['enterpriseId'] = datas["result"]

        response = self.request.request(case['method'], case['url'], data)
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_admin, "getvaluerecord").write_test_data(case["id"], response.text, "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_admin, "getvaluerecord").write_test_data(case["id"], response.text, "Pass")

    @data(*cases08)
    def test_case08_getValuationRecordInfo(self, case):
        response = self.request.request(case['method'], case['url'], json.loads(case['data']))
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_admin, "getvaluecordeach").write_test_data(case["id"], response.text, "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_admin, "getvaluecordeach").write_test_data(case["id"], response.text, "Pass")

    def test_case09_deletevaluationrecordinfo(self):  # 删除估值记录信息
        for i in range(0, len(datas06)):
            cmresult = datas06[i]["results"]
            data = {"valuationRecordId": cmresult["valuationRecordId"]}
            response = self.request.request("put", "/rdt/deleteValuationRecordInfo", data)
            self.assertIn("Delete the success！", response.json()['message'])

    @data(*cases09)
    def test_case10_saveIntellectualPropertyRightsInfo(self, case):

        data = ast.literal_eval(case['data'])
        if data['enterpriseId'] == "{$enterpriseId}":
            data['enterpriseId'] = datas["result"]

        response = self.request.request(case['method'], case['url'], data)
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_admin, "saveintellectualproper").write_test_data(case["id"], response.text, "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_admin, "saveintellectualproper").write_test_data(case["id"], response.text, "Pass")

        if "Save success" in response.text:
            datas09.append(response.json())

    @data(*cases10)
    def test_case11_getIntellectualPropertyRightsInfos(self, case):

        data = ast.literal_eval(case['data'])
        if data['enterpriseId'] == "{$enterpriseId}":
            data['enterpriseId'] = datas["result"]

        response = self.request.request(case['method'], case['url'], data)
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_admin, "getinteiiproperinfos").write_test_data(case["id"], response.text, "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_admin, "getinteiiproperinfos").write_test_data(case["id"], response.text, "Pass")

    @data(*cases11)
    def test_case12_getIntellectualPropertyRightsInfo(self, case):
        response = self.request.request(case['method'], case['url'], json.loads(case['data']))
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_admin, "getinteiipropereach").write_test_data(case["id"], response.text, "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_admin, "getinteiipropereach").write_test_data(case["id"], response.text, "Pass")

    def test_case13_deleteIntellectualPropertyRightsInfo(self):
        for i in range(0, len(datas09)):
            cmresult = datas09[i]["results"]
            data = {"intellectualPropertyId": cmresult["intellectualPropertyId"]}
            response = self.request.request("put", "/rdt/deleteIntellectualPropertyRightsInfo", data)
            self.assertIn("Delete the success！", response.json()['message'])

    @data(*cases12)
    def test_case14_getEnterpriseAllotmentShares(self, case):

        data = ast.literal_eval(case['data'])
        if data['enterpriseId'] == "{$enterpriseId}":
            data['enterpriseId'] = datas["result"]

        response = self.request.request(case['method'], case['url'], data)
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_admin, "EnterpriseAllotmentShares").write_test_data(case["id"], response.text, "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_admin, "EnterpriseAllotmentShares").write_test_data(case["id"], response.text, "Pass")

        if "Information Acquisition Success." in response.text:
            datas14.append(response.json())

    @data(*cases13)
    def test_case15_getDistributingUserInfo(self, case):
        cmresult = datas14[0]["results"]
        data = json.loads(case['data'])
        if data['enterpriseId'] == "{$enterpriseId}":
            data['enterpriseId'] = datas["result"]
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
        cmresult = datas14[0]["results"]
        data = ast.literal_eval(case['data'])
        if data['enterpriseId'] == "{$enterpriseId}":
            data['enterpriseId'] = datas["result"]
        if data['tciUserStockList'] == "{$tciUserStockList}":
            data['tciUserStockList'] = cmresult["enterpriseTotalShares"]

        response = self.request.request(case['method'], case['url'], data)
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_admin, "saveTargetedCapitalIncrease").write_test_data(case["id"], response.text, "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_admin, "saveTargetedCapitalIncrease").write_test_data(case["id"], response.text, "Pass")

    @data(*cases15)
    def test_case17_postsaveAdminRigthsRecord(self, case):

        data = ast.literal_eval(case['data'])
        if data['enterpriseId'] == "{$enterpriseId}":
            data['enterpriseId'] = datas["result"]

        response = self.request.request(case['method'], case['url'], data)
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
        enterpriseId = datas["result"]
        cls.mysql.modifydata("delete from t_enterprise_info where id = " + str(enterpriseId))
        cls.mysql.modifydata("delete from t_enterprise_detail_info where enterprise_id = " + str(enterpriseId))

        cls.mysql.close()
        cls.request.session.close()

