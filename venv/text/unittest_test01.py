from selenium import webdriver
import unittest,time


class TestBaidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://baidu.com")

    def tearDown(self):
        self.driver.quit()

    def TestCase_map(self):
        self.driver.find_element_by_css_selector("#u1 > a:nth-child(3)").click()

    def TestCase_find(self):
        self.driver.find_element_by_css_selector("#kw").send_keys("selenium2")
        time.sleep(3)

if __name__ == "__main__":
    unittest.main(verbosity=2)

