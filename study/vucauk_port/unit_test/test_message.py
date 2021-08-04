import unittest
import json
import requests
import time
import common.constant
from common.login_all import loginaccount
from configer.conf_class import Conf
from unit.message import Message
from ddt import ddt, data
from common.excel_class import DoExcel


cases01 = DoExcel(common.constant.case_dir_admin, "getnotice").read_test_data()
cases02 = DoExcel(common.constant.case_dir_admin, "changemessagestate").read_test_data()
data01 = []

@ddt
class MessageTest(unittest.TestCase):
    def setUp(self):
        self.baseurl = Conf("../configer/test.conf").get("Api", "url")
        self.session = requests.session()
        self.loginAccount = loginaccount(self.baseurl, self.session)
        self.loginAccount.login_user("vuca@vucacapital.com", "000000")
        self.Message = Message(self.baseurl, self.session)

    def tearDown(self):
        pass

    @data(*cases01)
    def test_case01_getnotice(self, case):
        response = self.Message.get_getNotice(json.loads(case[4])["flag"])
        self.assertIn(json.loads(case[5]), response.text)
        data01.append(response.json())

    @data(*cases02)
    def test_case02_changemessagestate(self, case):
        # now = time.localtime()
        # 转换为时间数组
        # timeArray = time.strptime(now, "%Y-%m-%d %H:%M:%S")
        # 转换为时间戳
        # timestamp = int(time.mktime(now))
        timestamp = data01[0][0][0]["publishmentDate"]
        response = self.Message.put_changeMessageState(json.loads(case[4])["sid"], timestamp)
        self.assertIn(json.loads(case[5]), response.text)
