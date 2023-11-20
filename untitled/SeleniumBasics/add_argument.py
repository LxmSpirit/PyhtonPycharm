#加载配置启动浏览器
#用Chrome地址栏输入chrome://version/，查看自己的“个人资料路径”，
# 然后在浏览器启动时，调用这个配置文件，代码如下：

from selenium import webdriver

option = webdriver.ChromeOptions()
#注意''前有r
option.add_argument(r'- -user-data-dir=C:\Users\user\AppData\Local\Google\Chrome\User Data')#用户自己的数据目录即个人资料路径
driver=webdriver.Chrome(chrome_options=option)