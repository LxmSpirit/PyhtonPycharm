#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

url = "https://www.imedidata.com/"#IPQ Platform
accountnumber = 'wangjunyi1'
password = '@Wjy98061519'
loginfocss = 'form-control form-control-lg'#账号和密码的CSS是同一个
logbutcss = 'onex-btn form_button__oHaYF onex-btn--default btn btn-primary btn-md'#登录按钮的CSS

browser = webdriver.Chrome()
'''将浏览器最大化显示'''
#browser.maximize_window()
'''浏览器设置窗口大小'''
browser.set_window_size(1500,1000)#宽480，高800

'''浏览器前进后退'''
#browser.forward()
#browser.back()

'''键盘事件'''
'''通过send_keys()调用按键'''

#实现登录操作
browser.get(url)
accnum = browser.find_elements(By.CSS_SELECTOR,loginfocss)[0]
pwd = browser.find_elements(By.CSS_SELECTOR,loginfocss)[1]
print(accnum)
print(pwd)

accnum.send_keys(accountnumber)
pwd.send_keys(password)

'''方法一：通过点击登录按钮'''
#logbut = browser.find_element(By.CSS_SELECTOR,logbutcss)
#logbut.click()

'''方法二：通过键盘回车键'''
pwd.send_keys(Keys.ENTER)

'''键盘组合键的用法'''
#ctrl+a 全选内容
#accnum.send_keys(Keys.CONTROL,'a')
#ctrl+x 剪切内容
#accnum.send_keys(Keys.CONTROL,'x')

