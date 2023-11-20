#coding=utf-8
#Ctrl+B,看源码
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

''''''
'''鼠标事件'''
#需要引入ActionChains类
'''常用方法'''
#perform()  执行所有ActionChains 中存储的行为
#context_click()  右击
#double_click()  双击
#drag_and_drop() 拖动
#move_to_element() 鼠标悬停

'''鼠标双金示例'''
#定位到要双击的元素
#aaa = driver.find_element_by_xpath("XXX")
#对定位到的元素执行鼠标双击操作
#ActionChains(driver).double_click(aaa).perform()

'''鼠标拖放示例'''
#定位元素的原位置
#element = driver.find_element_by_name("source")
#定位元素要移动到的目标位置
#target = driver.find_element_by_name("target")
#执行元素的移动操作
#ActionChains(driver).drag_and_drop(element,target).perform()

url = "http://192.168.1.144/userlogin/index"#IPQ Platform
url2 = "http://192.168.1.144/homepage/index"
accountnumber = 'admin@improve-quality.com'
password = '123456'
loginfocss = '.ant-input.ant-input-lg'#账号和密码的CSS是同一个
logbutcss = '.login-button.ant-btn.ant-btn-primary.ant-btn-lg'#登录按钮的CSS

'''
headers = webdriver.ChromeOptions()
headers.add_argument("SessionID='b7e114fa-a4b8-4d88-94ca-95ee7b55287f'")
headers.add_argument("StudyID='19bf649e-3c89-ea11-80bb-005056a9fb2f'")
headers.add_argument("TenantID='44b2f206-3789-ea11-80bb-005056a9fb2f'")
headers.add_argument("Access-Token='b7e114fa-a4b8-4d88-94ca-95ee7b55287f'")
headers.add_argument("Authorization='Bearer b7e114fa-a4b8-4d88-94ca-95ee7b55287f'")
headers.add_argument("User-Agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'")
browser = webdriver.Chrome(chrome_options=headers)
browser.get('http://192.168.1.144/easycoding/api/Settings/GetSettingsInfo')
'''


'''#将浏览器最大化显示'''
#browser.maximize_window()
'''#浏览器设置窗口大小'''
#browser.set_window_size(1500,1000)#宽480，高800

'''#浏览器前进后退'''
#browser.forward()
#browser.back()

'''#键盘事件'''
'''#通过send_keys()调用按键'''

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
print('######################################################11111111111111')
print(browser.page_source)

'''#方法一：通过点击登录按钮'''
#logbut = browser.find_element(By.CSS_SELECTOR,logbutcss)
#logbut.click()

'''#方法二：通过键盘回车键'''
pwd.send_keys(Keys.ENTER)
time.sleep(5)
'''
hand = browser.window_handles
print(hand)
print(browser.title)
time.sleep(5)

'''


#问题：登录页面跳转后如何定位元素
#可以试试页面刷新后 如何获取页面
'''
#重新新建driver更换地址--Index页面     失败
browser2 = webdriver.Chrome()
browser2.set_window_size(1500,1000)#宽480，高800
browser2.get(url2)
print(browser2.window_handles)
print(browser2.title)

'''
#Url_Index = browser.current_url()
#UrlIndex = browser.current_url()
#print(UrlIndex)

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
#print(browser.page_source)#已经进入到http://192.168.1.144/homepage/index页面
'''
#重新链接当前地址
ca = DesiredCapabilities.CHROME
ca["goog:loggingPrefs"] = {"performance": "ALL"}
driver = webdriver.Chrome(desired_capabilities=ca)
driver.get(UrlInd)
logs = driver.get_log("performance")
print(logs)
'''
print('######################################################33333333333')
time.sleep(5)
sessionid2 = browser.session_id
print(sessionid2)
#print(browser.page_source)

antcardbut = browser.find_element(By.CSS_SELECTOR,'.link-button')
print(antcardbut.get_attribute("outerHTML"))

antcardbut.click()
time.sleep(10)

#
#browser.execute_script("return localStorage.setItem('"+'SessionID'+"', '"+sessionid+"')")
#print('execute_script')

#antcardbut = browser.find_element(By.CSS_SELECTOR,'.ant-btn.ant-btn-primary')
#print(antcardbut.get_attribute("outerHTML"))
'''
#antcardbut2 = browser.find_elements(By.TAG_NAME,'button')
#print(antcardbut2)
#for a in antcardbut2:
#    print(a.get_attribute("outerHTML"))
'''

#antcardbut = browser2.find_element(By.CSS_SELECTOR,'.ant-btn.ant-btn-primary')
#antcardbut2 = browser2.find_elements(By.CSS_SELECTOR,"button[class='ant-btn.ant-btn-primary']")
#antcardbut = browser.find_elements(By.CSS_SELECTOR,"div[class = 'ant-pro-grid-content']")
#print(antcardbut)
#print(antcardbut.get_attribute("outerHTML"))
#print(antcardbut2)
#for a in antcardbut2:
#    print(a.get_attribute("outerHTML"))


#antcardbut.click()

