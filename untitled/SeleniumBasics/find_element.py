#coding=utf-8
from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("http://www.baidu.com")
#########百度输入框的定位方式########
#<input id="kw" name="wd" class="s_ipt" value="" maxlength="255" autocomplete="off">
'''通过id方式定位√'''
#browser.find_element_by_id("kw").send_keys("selenium")
'''通过name方式定位√'''
#browser.find_element_by_name("wd").send_keys("selenium")
'''通过tag name方式定位'''
''' 总结--标签不唯一不常用
   tag_name定位方法
    1. 当页面中有唯一的标签的时候,可以使用
       driver.find_element_by_tag_name("标签名")
    2. 当有多个标签相同的元素时,使用
        driver.find_element_by_tag_name("标签名")
        默认定位的是第一个标签名
    3. 当有多个标签相同的元素时,使用
        driver.find_elements_by_tag_name("标签名")
        得到所有标签相同的元素,使用列表遍历的形式,对具体的元素做操作'''
#browser.find_elements_by_tag_name("input").send_keys("selenium")
'''input_eles = browser.find_elements_by_tag_name("input")
print(len(input_eles))
for i in input_eles:
    print(i.get_attribute("outerHTML"))

span_eles = browser.find_elements_by_tag_name("span")
print(len(span_eles))
for j in span_eles:
    print(j.get_attribute("outerHTML"))

form_eles = browser.find_elements_by_tag_name("form")
print(len(form_eles))
for k in form_eles:
     print(k.get_attribute("outerHTML"))'''
'''通过class name方式定位'''
#browser.find_element_by_class_name("s_ipt").send_keys("selenium")
'''通过CSS方式定位'''
#browser.find_element_by_css_selector("#kw").send_keys("selenium")
'''通过xpath方式定位'''
browser.find_element_by_xpath("//input[@id='kw']").send_keys("selenium")
####################################
browser.find_element_by_id("su").click()
time.sleep(10)
browser.quit()
