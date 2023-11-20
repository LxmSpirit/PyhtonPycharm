#coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

url = "http://192.168.1.144/userlogin/index"#IPQ Platform
url2 = "http://192.168.1.144/homepage/index"
accountnumber = 'admin@improve-quality.com'
password = '123456'
loginfocss = '.ant-input.ant-input-lg'#账号和密码的CSS是同一个
logbutcss = '.login-button.ant-btn.ant-btn-primary.ant-btn-lg'#登录按钮的CSS

headers = webdriver.ChromeOptions()
'''
headers.add_argument("SessionID='b7e114fa-a4b8-4d88-94ca-95ee7b55287f'")
headers.add_argument("StudyID='19bf649e-3c89-ea11-80bb-005056a9fb2f'")
headers.add_argument("TenantID='44b2f206-3789-ea11-80bb-005056a9fb2f'")
headers.add_argument("Access-Token='b7e114fa-a4b8-4d88-94ca-95ee7b55287f'")
headers.add_argument("Authorization='Bearer b7e114fa-a4b8-4d88-94ca-95ee7b55287f'")
headers.add_argument("User-Agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'")

browser = webdriver.Chrome(chrome_options=headers)
'''
browser = webdriver.Chrome()
#browser.add_cookie({'name':'SessionID','value':'b7e114fa-a4b8-4d88-94ca-95ee7b55287f'})
key="SessionID"
value="b7e114fa-a4b8-4d88-94ca-95ee7b55287f"
browser.get(url)
session = browser.get_cookies()
print(session)

browser.add_cookie({'name': 'SessionID', 'value': 'b7e114fa-a4b8-4d88-94ca-95ee7b55287f'})
browser.get('http://192.168.1.144/easycoding/api/Settings/GetSettingsInfo')
#browser.execute_script("return localStorage.setItem('"+key+"', '"+value+"')")
#browser.refresh()