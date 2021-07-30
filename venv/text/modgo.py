from selenium import webdriver
from time import *

a=1
start_time=time()
while a<6:
    driver = webdriver.Chrome()
    driver.get("http://www.modgo.pro")
    a+=1
    driver.quit()
end_time = time()
run_time = end_time - start_time
print(run_time)