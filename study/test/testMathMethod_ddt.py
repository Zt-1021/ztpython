import unittest
from ddt import ddt, data
from study.test.MathMethod import MathMethod
from study.test.testDataExcel import DoExcel
from study.test.conf import Conf
from study.test.test_logging import Log


cases = DoExcel("test_data.xlsx", "Add").read_test_data()
# datas = eval(Conf("test_conf.conf").getvalue("data", "data"))
my_logger = Log()

@ddt
class TestMathMethod(unittest.TestCase):

    # def __init__(self, a, b, expected, methodName):
    #     super(TestMathMethod, self).__init__(methodName)
    #     self.a = a
    #     self.b = b
    #     self.expected = expected

    def setUp(self):
        print("-----开始执行测试用例-----")    # my_logger.getinfo

    def tearDown(self):
        print("-----结束测试-----")   # my_logger.getinfo

    @data(*cases)
    def test_add(self, case):
        # if case[0] in datas:
            result = MathMethod(case[2], case[3]).add()
            try:
                self.assertEqual(case[4], result)
                my_logger.getinfo("两数相加，结果为{},与期望值一致，测试通过".format(result))   # my_logger.getinfo
                test_result = "pass"
            except AssertionError as e:
                print("断言失败，期望结果{}，实际结果是{}".format(case[4], result))    # my_logger.geterror
                test_result = "not pass"
                raise e
            # return test_result
            finally:
                DoExcel("test_data.xlsx", "Add").write_test_data(case[0], result, test_result)

    # def test_sub(self):
    #     result = MathMethod(self.a, self.b).sub()
    #     try:
    #         self.assertEqual(self.expected, result)
    #         print("两数相减，结果为{}，与期望值一致，测试通过".format(result))
    #     except AssertionError as e:
    #         print("断言失败，期望结果是{}，实际结果是{}".format(self.expected,result))
    #         raise e
