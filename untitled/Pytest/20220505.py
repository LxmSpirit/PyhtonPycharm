from selenium import webdriver
import time



#前置
url = "http://192.168.1.144/userlogin/index"  # IPQ Platform
browser = webdriver.Chrome()
browser.get(url)
time.sleep(10)