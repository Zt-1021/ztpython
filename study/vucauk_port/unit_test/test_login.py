import unittest
import json
import requests
import common.constant
from unit.login import Login
from configer.conf_class import Conf
from ddt import ddt, data
from common.excel_class import DoExcel

cases = DoExcel(common.constant.case_dir_admin, "login").read_test_data()


@ddt
class Testlogin(unittest.TestCase):
    def setUp(self):
        self.baseurl = Conf("../configer/test.conf").get("Api", "url")
        self.session = requests.session()

    def tearDown(self):
        pass

    @data(*cases)
    def test_case01_login(self, case):
        login = Login(self.baseurl, self.session)  # 创建一个Login对象
        login.get_image()
        response = login.post_form(json.loads(case[4])["username"],
                                   json.loads(case[4])["password"],
                                   json.loads(case[4])["imagecode"])
        # 该接口除正常登录是200，其他都是401
        # response.raise_for_status()  # 状态码不是200时抛出异常
        # self.assertEqual(200, response.status_code)  # 判断状态码是否是200
        self.assertEqual(json.loads(case[5]), response.json())
        print(response.json())
