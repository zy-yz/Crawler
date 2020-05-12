# encoding= utf-8
from selenium import webdriver


# 使用代理
options = webdriver.ChromeOptions()
options.add_argument("--proxy-server=http://121.196.205.196:8888")

driver = webdriver.Chrome(chrome_options=options)
driver.get("https://www.baidu.com/")

driver.execute_script("window.open('https://www.douban.com/')")
driver.switch_to_window(driver.window_handles[1])

print(driver.current_url)
print(driver.page_source)

# 虽然在窗口切换了页面，但是driver没有切换
# 所以应该使用driver.switch_to_window来切换到指定窗口
# driver.window_handlers来取出聚集地几个窗口