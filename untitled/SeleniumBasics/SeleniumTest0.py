# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

#Headless Chrome 是 Chrome 浏览器的无界面形态，可以在不打开浏览器的前提下，使用所有 Chrome 支持的特性运行你的程序。
# 相比于现代浏览器，Headless Chrome 更加方便测试 web 应用，获得网站的截图，做爬虫抓取信息等。

chrome_options = webdriver.ChromeOptions()
#使用headless无界面浏览器模式
chrome_options.add_argument('- -headless')#增加无界面选项
chrome_options.add_argument('- -disable-gpu')#不加该选项，定位会出现问题
#加载配置启动浏览器
chrome_options.add_argument(r'--user-data-dir=C:\Users\user\AppData\Local\Google\Chrome\User Data')#用户自己的数据目录即个人资料路径
#'--user-data-dir=C:\Users\Administrator\AppData\Local\Google\Chrome\User Data'
#- -user-data-dir=C:\Users\user\AppData\Local\Google\Chrome\User Data'

#启动浏览器，获取网页源代码
browser = webdriver.Chrome(chrome_options = chrome_options)
mainUrl = "https://www.taobao.com/"
browser.get(mainUrl)
print(f"browser text = {browser.page_source}")
browser.quit()