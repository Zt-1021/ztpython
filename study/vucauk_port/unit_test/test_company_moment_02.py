import unittest
import json
from common import constant, request
from configer import conf_class
from common.new_ddt import ddt, data
from common.excel_class_02 import DoExcel


cases01 = DoExcel(constant.case_dir_admin, "addcompanymoment").read_test_data()
cases02 = DoExcel(constant.case_dir_admin, "updatecompanymoment").read_test_data()
cases03 = DoExcel(constant.case_dir_admin, "getEMomentInfoAll").read_test_data()
cases04 = DoExcel(constant.case_dir_admin, "getCompanyMomentInfo").read_test_data()
datas = []


@ddt
class Testcompanymoment(unittest.TestCase):

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
    def test_case01_addcompanymoment(self, case):  # 添加公司动态
        response = self.request.request(case['method'], case['url'], json.loads(case['data']))
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_admin, "addcompanymoment").write_test_data(case["id"], response.text, "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_admin, "addcompanymoment").write_test_data(case["id"], response.text, "Pass")

        if "Save success" in response.text:
            datas.append(response.json())

    @data(*cases02)
    def test_case02_updatecompanymomentinfo(self, case):  # 更新公司动态
        response = self.request.request(case['method'], case['url'], json.loads(case['data']))
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_admin, "updatecompanymoment").write_test_data(case["id"], response.text, "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_admin, "updatecompanymoment").write_test_data(case["id"], response.text, "Pass")

    @data(*cases03)
    def test_case03_getemomentinfoall(self, case):  # 获取公司动态全部
        response = self.request.request(case['method'], case['url'], json.loads(case['data']))
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_admin, "getEMomentInfoAll").write_test_data(case["id"], response.text, "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_admin, "getEMomentInfoAll").write_test_data(case["id"], response.text, "Pass")

    @data(*cases04)
    def test_case04_getCompanyMomentInfo(self, case):  # 获取公司单条动态详细信息
        response = self.request.request(case['method'], case['url'], json.loads(case['data']))
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_admin, "getCompanyMomentInfo").write_test_data(case["id"], response.text, "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_admin, "getCompanyMomentInfo").write_test_data(case["id"], response.text, "Pass")

    def test_case05_deleteCompanyMomentInfo(self):  # 删除公司动态
        cmids = []
        for i in range(0, len(datas)):
            cmresult = datas[i]["results"]
            cmids.append(cmresult["companyMomentInfoId"])
        data = {"companyMomentInfoIds": cmids}
        response = self.request.request("delete", "/rdt/deleteCompanyMomentInfo", data)
        self.assertIn("Delete successfully！", response.json()['message'])

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.request.session.close()
