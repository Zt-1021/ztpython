"""初学编写测试用例，每条用例都是定死的数据"""
import unittest
from study.test.MathMethod import MathMethod


class TestMathMethodAdd(unittest.TestCase):

    def setUp(self):
        print("-----开始执行测试用例-----")

    def tearDown(self):
        print("-----结束测试-----")

    def test_two_zero(self):
        result = MathMethod(0, 0).add()
        try:
            self.assertEqual(0, result)
            print("两个0相加，结果为{},与期望值一致，测试通过".format(result))
        except AssertionError as e:
            print("断言失败，期望结果0，实际结果是{}".format(result))
            raise e

    def test_two_negative(self):
        result = MathMethod(-1, -3).add()
        try:
            self.assertEqual(0, result)
            print("两个负数相加，结果为{},与期望值一致，测试通过".format(result))
        except AssertionError as e:
            print("断言失败，期望结果-4，实际结果是{}".format(result))
            raise e

    def test_positive_negative(self):
        result = MathMethod(1, -3).add()
        try:
            self.assertEqual(-2, result)
            print("一正一负相加，结果为{},与期望值一致，测试通过".format(result))
        except AssertionError as e:
            print("断言失败，期望结果-2，实际结果是{}".format(result))
            raise e


class TestMathMethodSub(unittest.TestCase):
    def test_two_zero_sub(self):
        result = MathMethod(0, 0).sub()
        try:
            self.assertEqual(0, result)
            print("两0相减，结果为0，与期望值一致，测试通过")
        except AssertionError as e:
            print("断言失败，期望结果是0，实际结果是{}".format(result))
            raise e

    def test_two_negative_sub(self):
        result = MathMethod(-1, -3).sub()
        try:
            self.assertEqual(2, result)
            print("两个负数相减，结果为2，与期望值一致，测试通过")
        except AssertionError as e:
            print("断言失败，期望结果是2，实际结果是{}".format(result))
            raise e

    def test_positive_negative_sub(self):
        result = MathMethod(1, -3).sub()
        try:
            self.assertEqual(4, result)
            print("一正一负相减，结果为4，与期望值一致，测试通过")
        except AssertionError as e:
            print("断言失败，期望结果是4，实际结果是{}".format(result))
            raise e
