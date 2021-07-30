# coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


driver = webdriver.chorm()
driver.get("http://www.modgo.pro")

"""
显性等待
so = WebDriverWait(driver,10).until(expected_conditions.element_to_be_clickable((By.ID,"kw")))
so.send_keys("selenium2")
driver.find_element_by_id("su").click()
time.sleep(10)
"""
"""
鼠标悬浮：move_to_element
ac = ActionChains(driver)
location = driver.find_element_by_xpath('//*[@id="u1"]/a[8]')
ac.move_to_element(location).perform()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="wrapper"]/div[6]/a[1]').click()
time.sleep(3)
"""

time.sleep(10)
# driver.get_screenshot_as_file("D:/baidu.png")
# driver.save_screenshot("baidu.png")
print(driver.get_screenshot_as_png())
driver.quit()