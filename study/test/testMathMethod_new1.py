"""改版后的测试用例"""
import unittest
from study.test.MathMethod import MathMethod
from study.test.testDataExcel import DoExcel

# test_data = DoExcel("test_data.xlsx", "Add")


class TestMathMethod(unittest.TestCase):

    def __init__(self, case_id, case_name, a, b, expected, methodName):
        super(TestMathMethod, self).__init__(methodName)
        self.case_id = case_id
        self.case_name = case_name
        self.a = a
        self.b = b
        self.expected = expected

    def setUp(self):
        print("-----开始执行测试用例-----")
        print("正在执行第{}条用例{}".format(self.case_id, self.case_name))

    def tearDown(self):
        print("-----结束测试-----")

    def test_add(self):
        result = MathMethod(self.a, self.b).add()
        try:
            self.assertEqual(self.expected, result)
            print("两数相加，结果为{},与期望值一致，测试通过".format(result))
            test_result = "pass"
        except AssertionError as e:
            print("断言失败，期望结果{}，实际结果是{}".format(self.expected, result))
            test_result = "not pass"
            raise e
        # return test_result
        finally:
            DoExcel("test_data.xlsx", "Add").write_test_data(self.case_id, result, test_result)

    # def test_sub(self):
    #     result = MathMethod(self.a, self.b).sub()
    #     try:
    #         self.assertEqual(self.expected, result)
    #         print("两数相减，结果为{}，与期望值一致，测试通过".format(result))
    #     except AssertionError as e:
    #         print("断言失败，期望结果是{}，实际结果是{}".format(self.expected,result))
    #         raise e
