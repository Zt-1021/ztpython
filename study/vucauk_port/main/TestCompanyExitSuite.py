import unittest
import HTMLTestRunner
import time
from unit_test.test_company_exit_02 import Testcompanyexit

suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(Testcompanyexit))

now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
with open('../report/'+now+'companyexit_test.html', 'wb') as file:
    runner = HTMLTestRunner.HTMLTestRunner(stream=file,
                                           verbosity=2,
                                           title='测试vucauk的编辑公司信息接口')
    runner.run(suite)
