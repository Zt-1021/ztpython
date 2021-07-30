"""加载多个数据的测试集---最初"""
import unittest
from study.test.testMathMethod_new1 import TestMathMethod
import HTMLTestRunner


# 测试数据
test_data = [[0, 0, 0], [-1, -3, -4], [-1, 3, 2]]
# 加载用例
suite = unittest.TestSuite()
# 通过模块加载
for item in test_data:
    suite.addTest(TestMathMethod(item[0], item[1], item[2], 'test_add'))

# 执行报告
# with open('math.txt', 'w', encoding='utf-8') as file:
with open('math_new1.html', 'wb') as file:
    # 执行用例
    # runner = unittest.TextTestRunner(stream=file, descriptions=True, verbosity=2)
    runner = HTMLTestRunner.HTMLTestRunner(stream=file,
                                           verbosity=2,
                                           title='测试数学方法的测试用例',
                                           description="第一份测试报告")
    runner.run(suite)


