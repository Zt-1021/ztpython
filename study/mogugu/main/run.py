import unittest
import HTMLTestRunner
from study.mogugu.unit_test.home_page_test import homepage


loader = unittest.TestLoader()
suite = loader.loadTestsFromModule(homepage)

with open('../report/test.html', 'wb') as file:
    runner = HTMLTestRunner.HTMLTestRunner(stream=file,
                                           verbosity=2,
                                           title='测试mogugu首页')
    runner.run(suite)
