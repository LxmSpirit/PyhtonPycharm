from selenium import webdriver

#启动浏览器
driver = webdriver.Chrome()
driver.get('http://baidu.com')
print(f"browser text = {driver.page_source}")
driver.quit()

