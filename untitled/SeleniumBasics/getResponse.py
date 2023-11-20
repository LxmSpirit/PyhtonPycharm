from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

ca = DesiredCapabilities.CHROME
ca["goog:loggingPrefs"] = {"performance": "ALL"}
driver = webdriver.Chrome(desired_capabilities=ca)
driver.get("http://192.168.1.144/userlogin/index")
logs = driver.get_log("performance")
print(logs)