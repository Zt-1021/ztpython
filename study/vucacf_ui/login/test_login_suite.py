import unittest
import HTMLTestRunner
from study.vucacf.login import test_data_login
from study.vucacf.login.test_login import TestLogin

test_data = test_data_login.DoExcel().read_data()

suite = unittest.TestSuite()
for item in test_data:
    suite.addTest(TestLogin(item[2], item[3], item[4], item[5], "test_login"))

with open('login.html', 'wb') as file:
    # 执行用例
    # runner = unittest.TextTestRunner(stream=file, descriptions=True, verbosity=2)
    runner = HTMLTestRunner.HTMLTestRunner(stream=file,
                                           verbosity=2,
                                           title='测试vucacf的登录',
                                           description="测试vucacf的登录")
    runner.run(suite)

