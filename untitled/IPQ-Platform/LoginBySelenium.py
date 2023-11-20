#coding=utf-8
#Ctrl+B,看源码
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time




url = "http://test.improve-quality.com/userlogin/index"#IPQ Platform
#url2 = "http://192.168.1.144/homepage/index"
accountnumber = 'admin@improve-quality.com'
password = '123456'
loginfocss = '.ant-input.ant-input-lg'#账号和密码的CSS是同一个
logbutcss = '.login-button.ant-btn.ant-btn-primary.ant-btn-lg'#登录按钮的CSS

'''#将浏览器最大化显示'''
#browser.maximize_window()
'''#浏览器设置窗口大小'''
#browser.set_window_size(1500,1000)#宽480，高800

#实现登录操作
browser = webdriver.Chrome()
browser.get(url)
accnum = browser.find_elements(By.CSS_SELECTOR,loginfocss)[0]
pwd = browser.find_elements(By.CSS_SELECTOR,loginfocss)[1]

accnum.send_keys(accountnumber)
pwd.send_keys(password)

#Url_Login = str(browser.current_url())
#获取当前URL地址
UrlLogin=browser.current_url
print(UrlLogin)
print('######################################################登录操作')

'''#方法一：通过点击登录按钮'''
#logbut = browser.find_element(By.CSS_SELECTOR,logbutcss)
#logbut.click()

'''#方法二：通过键盘回车键'''
pwd.send_keys(Keys.ENTER)
time.sleep(5)

#获取sessionid
sessionid = browser.session_id
print(sessionid)

#获取当前URL地址
UrlInd=browser.current_url
print(UrlInd)
time.sleep(3)
session = browser.get_cookies()
print(session)
print('######################################################222222222')
time.sleep(5)
sessionid2 = browser.session_id
print(sessionid2)

antcardbut = browser.find_element(By.CSS_SELECTOR,'.link-button')

antcardbut.click()
time.sleep(10)


