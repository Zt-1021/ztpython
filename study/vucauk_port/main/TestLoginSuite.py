import unittest
import HTMLTestRunner
from unit_test.test_login_02 import Testlogin

suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(Testlogin))

with open('../report/test.html', 'wb') as file:
    runner = HTMLTestRunner.HTMLTestRunner(stream=file,
                                           verbosity=2,
                                           title='测试vucauk的登录接口')
    runner.run(suite)
