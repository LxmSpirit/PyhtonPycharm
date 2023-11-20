import pytest
from selenium import webdriver
import time

@pytest.fixture
def open_url():
    #前置
    url = "http://192.168.1.144/userlogin/index"  # IPQ Platform
    browser = webdriver.Chrome()
    browser.get(url)
    time.sleep(3)
    yield browser #yield之前代码是前置，之后代码是后置
    #后置
    time.sleep(3)
    #browser.quit()
