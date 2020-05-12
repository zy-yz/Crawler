# coding=utf-8
from selenium import webdriver
import time

# wd = webdriver.Chrome()
# wd.get("https://www.baidu.com")    # 打开百度浏览器
#
# inputTag = wd.find_elements_by_css_selector(".quickdelete-wrap >input")[0]
# print(inputTag)
# inputTag.send_keys('python')

# 操作checkbox
# driver = webdriver.Chrome()
# driver.get("https://www.douban.com/")
#
# rememberBtn = driver.find_element_by_id('account-form-remember')
# rememberBtn.click()
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")

# 一部分链式操作
# inputTag = driver.find_element_by_id('kw')
# submitTag = driver.find_element_by_id('su')
#
# actions = ActionChains(driver)
# actions.move_to_element(inputTag)
# actions.send_keys_to_element(inputTag,'python')
# actions.move_to_element(submitTag)
# actions.click(submitTag)
# actions.perform()

# 获取所有的cookie
# for cookie in driver.get_cookies():
#     print(cookie)
#
# # 根据cookie的key获取value
# value= driver.get_cookie('BAIDUID')
# print(value)
#
# # 删掉所有的cookie
# # driver.delete_all_cookies()
#
# # 删掉某个cookie
# driver.delete_cookie('BAIDUID')

# 等待20s，如果还没有找到这个就抛出异常，
# 因为都是动态加载数据，所以等待一下
driver.implicitly_wait(20)
driver.find_element_by_id("dfdfd")

# 这个可以添加条件
WebDriverWait(driver,10).until(
    expected_conditions.presence_of_element_located((By.ID,'fadfdaf'))
)
