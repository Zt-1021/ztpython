import unittest
import json
from common import constant, request
from configer import conf_class
from ddt import ddt, data
from common.excel_class_02 import DoExcel


cases01 = DoExcel(constant.case_dir_admin, "getnotice").read_test_data()
cases02 = DoExcel(constant.case_dir_admin, "changemessagestate").read_test_data()
data01 = []


@ddt
class MessageTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.request = request.Request("test")
        cls.request.request("get", "/code/image")
        username = conf_class.Conf(constant.conffile_dir).getvalue("User", "admin_user_name")
        password = conf_class.Conf(constant.conffile_dir).getvalue("User", "admin_user_password")
        cls.request.request("post", "/authentication/form",
                             {"username": username, "password": password, "imageCode": "0"})
        cls.request.request("get", "/code/judgingIdentity", {"email": username})

    def setUp(self):
        pass

    @data(*cases01)
    def test_case01_getnotice(self, case):
        response = self.request.request(case['method'], case['url'], json.loads(case['data']))
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_admin, "getnotice").write_test_data(case["id"], response.text, "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_admin, "getnotice").write_test_data(case["id"], response.text, "Pass")
        data01.append(response.json())

    @data(*cases02)
    def test_case02_changemessagestate(self, case):
        # now = time.localtime()
        # 转换为时间数组
        # timeArray = time.strptime(now, "%Y-%m-%d %H:%M:%S")
        # 转换为时间戳
        # timestamp = int(time.mktime(now))
        # timestamp = data01[0][0][0]["publishmentDate"]
        response = self.request.request(case['method'], case['url'], json.loads(case['data']))
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_admin, "changemessagestate").write_test_data(case["id"], response.text, "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_admin, "changemessagestate").write_test_data(case["id"], response.text, "Pass")

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.request.session.close()
