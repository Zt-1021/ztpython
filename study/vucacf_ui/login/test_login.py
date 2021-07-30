import unittest
import time
from selenium import webdriver
# from ddt import ddt,data


# @ddt(DoExcel.read_data())
class TestLogin(unittest.TestCase):

    def __init__(self, username, password, vercode, expected, methodName):
        super(TestLogin, self).__init__(methodName)
        self.username = username
        self.password = password
        self.vercode = vercode
        self.expected = expected

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://rdt.vucacf.com/#/login")
        # self.driver.implicitly_wait(25)
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()

    # @data(*data)
    def test_login(self, username, password, vercode, expected):
        self.driver.find_element_by_name("username").send_keys(username)
        self.driver.find_element_by_name("password").send_keys(password)
        self.driver.find_element_by_name("vercode").send_keys(vercode)
        self.driver.find_element_by_class_name("btn").click()
        divcontent01 = self.driver.find_element_by_class_name("btn_pic2").text
        print("已进入该执行")

        try:
            self.assertEqual(divcontent01, expected)
            print("1")
        except AssertionError as e:
            print("2")
            raise e




