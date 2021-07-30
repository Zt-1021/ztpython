import unittest
import HTMLTestRunner
import time
from unit_test.test_company_moment_02 import Testcompanymoment

suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(Testcompanymoment))

now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
with open('../report/'+now+'companymoment_test.html', 'wb') as file:
    runner = HTMLTestRunner.HTMLTestRunner(stream=file,
                                           verbosity=2,
                                           title='测试vucauk的添加公司动态接口')
    runner.run(suite)
