import unittest
import json
from common import constant, request
from ddt import ddt, data
from common.excel_class_02 import DoExcel

cases = DoExcel(constant.case_dir_admin, "login").read_test_data()


@ddt
class Testlogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.request = request.Request("test")

    def setUp(self):
        pass

    @data(*cases)
    def test_case01_login(self, case):  # 登录接口
        # print("正在执行第{0}条用例:{1}".format(case['id'], case['casename']))
        # print(case)
        self.request.request('get', '/code/image')
        response = self.request.request(case['method'], case['url'], json.loads(case['data']))
        try:
            self.assertEqual(json.loads(case['excepted']), response.json())
        except AssertionError as e:
            DoExcel(constant.case_dir_admin, "login").write_test_data(case['id'], response.text, "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_admin, "login").write_test_data(case['id'], response.text, "Pass")
        # print("第{0}条用例执行结束,status_code为{1},实际结果为{2}".format(case['id'], response.status_code, response.json()))

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.request.session.close()
