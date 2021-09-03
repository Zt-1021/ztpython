import unittest
import json
import requests
import common.constant
from common.login_all import loginaccount
from configer.conf_class import Conf
from unit.company_moment import CompanyMoment
from common.new_ddt import ddt, data
from common.excel_class import DoExcel


cases01 = DoExcel(common.constant.case_dir_admin, "addcompanymoment").read_test_data()
cases02 = DoExcel(common.constant.case_dir_admin, "updatecompanymoment").read_test_data()
datas = []


@ddt
class Testcompanymoment(unittest.TestCase):
    def setUp(self):
        self.baseurl = Conf("../configer/test.conf").get("Api", "url")
        self.session = requests.session()
        self.loginAccount = loginaccount(self.baseurl, self.session)
        self.loginAccount.login_user("admin@163.com", "000000")
        self.companymoment = CompanyMoment(self.baseurl, self.session)

    def tearDown(self):
        pass

    @data(*cases01)
    def test_case01_addcompanymoment(self, case):
        response = self.companymoment.post_addcompanymoment(json.loads(case[4])["enterpriseId"],
                                                            json.loads(case[4])["eventsContent"],
                                                            json.loads(case[4])["eventsTitle"])
        self.assertIn(json.loads(case[5]), response.text)

        if "Save success" in response.text:
            datas.append(response.json())

    @data(*cases02)
    def test_case02_updatecompanymomentinfo(self, case):
        response = self.companymoment.post_updatecompanymomentinfo(json.loads(case[4])["companyMomentInfoId"],
                                                                   json.loads(case[4])["eventsContent"],
                                                                   json.loads(case[4])["eventsTitle"])
        self.assertIn(json.loads(case[5]), response.text)

    def test_case03_getCompanyMomentInfo(self):
        pass

    def test_case04_deleteCompanyMomentInfo(self):
        cmids = []
        for i in range(0, len(datas)):
            cmresult = datas[i]["results"]
            cmids.append(cmresult["companyMomentInfoId"])
        response = self.companymoment.delete(cmids)
        for j in range(0, len(cmids)):
            self.assertIn(cmids[j], json.loads(response.text)["results"])


