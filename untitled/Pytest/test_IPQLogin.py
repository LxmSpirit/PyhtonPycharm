#coding=utf-8

import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


accountnumber = 'admin@improve-quality.com'
password = '123456'
loginfocss = '.ant-input.ant-input-lg'#账号和密码的CSS是同一个
logbutcss = '.login-button.ant-btn.ant-btn-primary.ant-btn-lg'#登录按钮的CSS
index = "http://192.168.1.144/homepage/index"

@pytest.mark.usefixtures('open_url')
class Test_Login():

    #pytestmark = pytest.mark.login #整个Test_Login类里面，所有测试用例都有login标签
    #@pytest.mark.smoke
    def test_login_success(self,open_url):
        accnum = open_url.find_elements(By.CSS_SELECTOR, loginfocss)[0]
        pwd = open_url.find_elements(By.CSS_SELECTOR, loginfocss)[1]

        accnum.send_keys(accountnumber)
        pwd.send_keys(password)

        pwd.send_keys(Keys.ENTER)
        time.sleep(5)
        UrlInd = open_url.current_url
        print("test_login_success")
        print(UrlInd)
        assert UrlInd == index


if __name__=='__main__':
    pytest.main(['-s','test_login1.py'])