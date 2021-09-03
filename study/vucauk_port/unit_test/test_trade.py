import unittest
import ast
from common import constant, request, mysql
from configer import conf_class
from common.new_ddt import ddt, data
from common.excel_class_02 import DoExcel


cases01 = DoExcel(constant.case_dir_user, "saveUserTransactionOrder").read_test_data()
cases02 = DoExcel(constant.case_dir_admin, "addTransactionInfo").read_test_data()
cases03 = DoExcel(constant.case_dir_user, "saveAccountBalanceInfo").read_test_data()
cases04 = DoExcel(constant.case_dir_admin, "updateAccountBanlanceState").read_test_data()
cases05 = DoExcel(constant.case_dir_admin, "updateTransactionStatus").read_test_data()
datas = {}
datas02 = {}


@ddt
class TestTrade(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.request = request.Request()
        cls.host = conf_class.Conf(constant.testconf_dir).get("MysqlDatabase", "host")
        cls.username = conf_class.Conf(constant.testconf_dir).get("MysqlDatabase", "username")
        cls.password = conf_class.Conf(constant.testconf_dir).get("MysqlDatabase", "password")
        cls.database = conf_class.Conf(constant.testconf_dir).get("MysqlDatabase", "database")
        cls.port = conf_class.Conf(constant.testconf_dir).get("MysqlDatabase", "port")
        cls.mysql = mysql.Mysql(cls.host, cls.username, cls.password, cls.database, int(cls.port))

    def setUp(self):
        pass

# 1.卖方发出订单
    @data(*cases01)
    def test_case01_saveUserTransactionOrder(self, case):

        self.request.request("get", "/code/image")
        username = conf_class.Conf(constant.testconf_dir).get("User", "shareholder_user_name")
        password = conf_class.Conf(constant.testconf_dir).get("User", "shareholder_user_password")
        self.request.request("post", "/authentication/form",
                            {"username": username, "password": password, "imageCode": "0"})
        self.request.request("get", "/code/judgingIdentity", {"email": username})

        data = ast.literal_eval(case['data'])
        if data['certificateId'] == "{$certificateId}":
            certificateId = self.mysql.fetchone(
                'select id from t_share_certificate_info where user_id = 125 and tran_id=58 ORDER BY id desc limit 1')
            data['certificateId'] = certificateId

        response = self.request.request(case['method'], case['url'], data)
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_user, "saveUserTransactionOrder").write_test_data(case["id"], response.text, "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_user, "saveUserTransactionOrder").write_test_data(case["id"], response.text, "Pass")

        self.request.session.close()

# 2.买方选择订单购买
    def test_case02_saveUserTransactionOrder(self):
        self.request.request("get", "/code/image")
        username = conf_class.Conf(constant.testconf_dir).get("User", "investor_user_name")
        password = conf_class.Conf(constant.testconf_dir).get("User", "investor_user_password")
        self.request.request("post", "/authentication/form",
                             {"username": username, "password": password, "imageCode": "0"})
        self.request.request("get", "/code/judgingIdentity", {"email": username})

        response = self.request.request('post', '/rdt/saveUserTransactionOrder',
                                        {"enterpriseId": "18",
                                         "userorderIdentity": "0",
                                         "userorderSharesNumber": "10.00",
                                         "intuserorderSharesPaid": "1.21",
                                         "userId": "122",
                                         "certificateId": "0"})

        self.assertIn('Submitted successfully, your order has been accepted!', response.json()['message'])
        self.request.session.close()

# 3.管理员进行匹配订单
    @data(*cases02)
    def test_case03_addTransactionInfo(self, case):

        self.request.request("get", "/code/image")
        username = conf_class.Conf(constant.testconf_dir).get("User", "admin_user_name")
        password = conf_class.Conf(constant.testconf_dir).get("User", "admin_user_password")
        self.request.request("post", "/authentication/form",
                             {"username": username, "password": password, "imageCode": "0"})
        self.request.request("get", "/code/judgingIdentity", {"email": username})

        data = ast.literal_eval(case['data'])
        if data['orderBuyerId'] == "{$orderBuyerId}":
            buyerid = self.mysql.fetchone('select id from t_user_order_info where enterprise_id=18 and user_id=122 ORDER BY id desc limit 1')
            data['orderBuyerId'] = buyerid[0]
        if data['orderTransferId'] == "{$orderTransferId}":
            sellerid = self.mysql.fetchone('select id from t_user_order_info where enterprise_id=18 and user_id=125 ORDER BY id desc limit 1')
            data['orderTransferId'] = sellerid[0]
        response = self.request.request(case['method'], case['url'], data)
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_admin, "addTransactionInfo").write_test_data(case["id"], response.text, "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_admin, "addTransactionInfo").write_test_data(case["id"], response.text, "Pass")

        if 'Information Acquisition Success.' in response.text:
            datas['result'] = response.json()["results"]

        self.request.session.close()
# 4.买方打款

    @data(*cases03)
    def test_case04_saveaccountbalanceinfo(self, case):

        self.request.request("get", "/code/image")
        username = conf_class.Conf(constant.testconf_dir).get("User", "investor_user_name")
        password = conf_class.Conf(constant.testconf_dir).get("User", "investor_user_password")
        self.request.request("post", "/authentication/form",
                             {"username": username, "password": password, "imageCode": "0"})
        self.request.request("get", "/code/judgingIdentity", {"email": username})

        data = ast.literal_eval(case['data'])
        if data['transactionNumber'] == "{$transactionNumber}":
            transactionid = datas['result']
            sql = 'select transaction_number from t_transaction_info where id = '+ str(transactionid)
            transactionNumber = self.mysql.fetchone(sql)
            data['transactionNumber'] = transactionNumber[0]

        response = self.request.request(case['method'], case['url'], data)
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_user, "saveAccountBalanceInfo").write_test_data(case["id"], response.text, "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_user, "saveAccountBalanceInfo").write_test_data(case["id"], response.text, "Pass")

        if 'Play with success.' in response.text:
            datas02['result'] = response.json()["results"]

        self.request.session.close()

# 5.管理员确认

    @data(*cases04)
    def test_case05_updateAccountBalanceState(self, case):

        self.request.request("get", "/code/image")
        username = conf_class.Conf(constant.testconf_dir).get("User", "admin_user_name")
        password = conf_class.Conf(constant.testconf_dir).get("User", "admin_user_password")
        self.request.request("post", "/authentication/form",
                             {"username": username, "password": password, "imageCode": "0"})
        self.request.request("get", "/code/judgingIdentity", {"email": username})

        data = ast.literal_eval(case['data'])
        if data['accountBalanceId'] == "{$accountBalanceId}":
            data['accountBalanceId'] = datas02['result']

        response = self.request.request(case['method'], case['url'], data)
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_admin, "updateAccountBanlanceState").write_test_data(case["id"], response.text, "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_admin, "updateAccountBanlanceState").write_test_data(case["id"], response.text, "Pass")

        self.request.session.close()

# 6.管理员修改订单状态--先修改成3，然后再修改成4，为了省步骤，直接更改为4了，即交易完成

    @data(*cases05)
    def test_case06_updateUserOrderState(self, case):

        self.request.request("get", "/code/image")
        username = conf_class.Conf(constant.testconf_dir).get("User", "admin_user_name")
        password = conf_class.Conf(constant.testconf_dir).get("User", "admin_user_password")
        self.request.request("post", "/authentication/form",
                             {"username": username, "password": password, "imageCode": "0"})
        self.request.request("get", "/code/judgingIdentity", {"email": username})

        data = ast.literal_eval(case['data'])
        if data['tranId'] == "{$tranId}":
            data['tranId'] = datas['result']

        response = self.request.request(case['method'], case['url'], data)
        try:
            self.assertIn(case['excepted'], response.json()['message'])
        except AssertionError as e:
            DoExcel(constant.case_dir_admin, "updateTransactionStatus").write_test_data(case["id"], response.text, "Failed")
            print(e)
        else:
            DoExcel(constant.case_dir_admin, "updateTransactionStatus").write_test_data(case["id"], response.text, "Pass")

        self.request.session.close()

# 7.卖方提取钱款 ---先获取余额，再提取：逻辑时一次性取清
    def test_case07_payout(self):

        self.request.request("get", "/code/image")
        username = conf_class.Conf(constant.testconf_dir).get("User", "shareholder_user_name")
        password = conf_class.Conf(constant.testconf_dir).get("User", "shareholder_user_password")
        self.request.request("post", "/authentication/form",
                             {"username": username, "password": password, "imageCode": "0"})
        self.request.request("get", "/code/judgingIdentity", {"email": username})

        response01 = self.request.request('get', '/rdt/getAccountBalance')
        sumAccountBalance = response01.json()['results']
        response02 = self.request.request('post', '/rdt/payOut', {'sumAccountBalance': sumAccountBalance})
        self.assertIn("The withdrawal request has been submitted, pending the administrator's confirmation.", response02.json()['message'])

        self.request.session.close()

# 8.管理员同意--

    def test_case06_updateAccountBanlanceState(self):
        accountBalanceId = self.mysql.fetchone('select id from t_account_balance_info where user_id = 125 and balance_type=3 ORDER BY id desc limit 1')
        response = self.request.request('put', '/rdt/updateAccountBalanceState', {"accountBalanceId":accountBalanceId[0],"balanceType":"3"})
        self.assertIn('confirmation successful.', response.json()['message'])

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.mysql.close()
        cls.request.session.close()
