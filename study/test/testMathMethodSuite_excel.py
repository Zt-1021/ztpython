"""excel读写测试数据的测试集"""

import unittest
import HTMLTestRunner
from study.test.testMathMethod_new1 import TestMathMethod
# from study.test.testMathMethod_ddt import TestMathMethod
from study.test.testDataExcel import DoExcel


# 测试数据
test_data = DoExcel("test_data.xlsx", "Add").read_test_data()
# 加载用例
suite = unittest.TestSuite()
for item in test_data:
    suite.addTest(TestMathMethod(item[0], item[1], item[2], item[3], item[4], 'test_add'))
#     # DoExcel.write_test_data(item[0], item[2], item[3])
#     print("这是第{}条用例，用例名为{},a为{},b为{},期望值为{}".format(item[0], item[1], item[2], item[3], item[4]))

# suite.addTest(TestMathMethod('test_add'))

# 执行报告
# with open('math.txt', 'w', encoding='utf-8') as file:
with open('math.html', 'wb') as file:
    # 执行用例
    # runner = unittest.TextTestRunner(stream=file, descriptions=True, verbosity=2)
    runner = HTMLTestRunner.HTMLTestRunner(stream=file,
                                           verbosity=0,
                                           title='测试数学方法的测试用例',
                                           description="第一份测试报告")
    runner.run(suite)


