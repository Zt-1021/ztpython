import unittest
import HTMLTestRunner
import time
from unit_test.test_system_workinfo_02 import Testsystemworkinfo

suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(Testsystemworkinfo))

now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
with open('../report/'+now+' systemworkorder_test.html', 'wb') as file:
    runner = HTMLTestRunner.HTMLTestRunner(stream=file,
                                           verbosity=2,
                                           title='测试vucauk的提交工作表单接口')
    runner.run(suite)
