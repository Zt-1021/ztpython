"""初学测试集"""
import unittest
# from study.testMathMethod import TestMathMethodAdd
from study.test import testMathMethod
import HTMLTestRunner



# 加载用例
# suite = unittest.TestSuite()
# 通过对象加载用例
# suite.addTest(testMathMethod.TestMathMethodAdd('test_two_zero'))   # TestMathMethodAdd('test_two_zero')

loader = unittest.TestLoader()
# 通过类加载用例
# suite = loader.loadTestsFromTestCase(testMathMethod.TestMathMethodAdd)   # TestMathMethodAdd

# 通过模块加载
suite = loader.loadTestsFromModule(testMathMethod)

# 执行报告
# with open('math.txt', 'w', encoding='utf-8') as file:
with open('math.html', 'wb') as file:
    # 执行用例
    # runner = unittest.TextTestRunner(stream=file, descriptions=True, verbosity=2)
    runner = HTMLTestRunner.HTMLTestRunner(stream=file,
                                           verbosity=2,
                                           title='测试数学方法的测试用例',
                                           description="第一份测试报告")
    runner.run(suite)


