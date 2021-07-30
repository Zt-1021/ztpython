import unittest
import HTMLTestRunner
import time
from unit_test.test_message_02 import MessageTest

suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(MessageTest))

now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
with open('../report/'+now+' message_test.html', 'wb') as file:
    runner = HTMLTestRunner.HTMLTestRunner(stream=file,
                                           verbosity=2,
                                           title='测试vucauk的系统消息接口')
    runner.run(suite)
