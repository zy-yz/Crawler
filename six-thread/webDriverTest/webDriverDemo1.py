# # encoding= utf-8
#
# from selenium import webdriver
#
# driver_path = r''
#
# driver = webdriver.Chrome(executable_path=driver_path)
#
# driver.get('http://www.baidu.com')
#
# print(driver.page_source)

# coding=utf-8
from selenium import webdriver
import time

wd = webdriver.Chrome()
wd.get("https://www.baidu.com")    # 打开百度浏览器
wd.find_element_by_id("kw").send_keys("selenium")   # 定位输入框并输入关键字

wd.find_element_by_id("su").click()   #点击[百度一下]搜索
time.sleep(3)   #等待3秒
# wd.quit()   #退出浏览器
# 关闭浏览器
#wd.close()