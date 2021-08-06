import unittest
import HTMLTestRunner
import time
from unit_test.test_company_exit_02 import Testcompanyexit
from unit_test.test_company_moment_02 import Testcompanymoment
from unit_test.test_login_02 import Testlogin
from unit_test.test_message_02 import MessageTest
from unit_test.test_order_02 import TestOrder
from unit_test.test_system_workinfo_02 import Testsystemworkinfo
from unit_test.test_user_02 import TestUser
from unit_test.test_userport_02 import Testuserport


suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(Testlogin))
suite.addTest(loader.loadTestsFromTestCase(Testcompanyexit))
suite.addTest(loader.loadTestsFromTestCase(Testcompanymoment))
suite.addTest(loader.loadTestsFromTestCase(TestOrder))
suite.addTest(loader.loadTestsFromTestCase(TestUser))
suite.addTest(loader.loadTestsFromTestCase(Testuserport))
suite.addTest(loader.loadTestsFromTestCase(MessageTest))
suite.addTest(loader.loadTestsFromTestCase(Testsystemworkinfo))

now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
with open('../report/'+now+' systemworkorder_test.html', 'wb') as file:
    runner = HTMLTestRunner.HTMLTestRunner(stream=file,
                                           verbosity=2,
                                           title='测试vucauk接口')
    runner.run(suite)
