#在定位元素时，发现class name是有多个class组合的复合类，中间以空格隔开
#通过一下方式处理：
#class属性唯一但是有空格，选择空格两边唯一的
#若空格隔开的class不唯一可以通过索引进行定位
#   self.driver.find_elements_by_class_name('table-dragColumn')[0]
#通过css方法进行定位（空格以 . 代替）
#前面加（.）空格地方用点（.）来代替
#self.driver.find_element_by_css_selector('.dtb-style-1.table-dragColumns').click()
#包含整个类
#self.driver.find_element_by_css_selector('class="dtb-style-1 table-dragColumns').click()

# coding:utf-8
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://mail.126.com/")
#隐性等待，在开头设置过之后，整个的程序运行过程中都会有效
#隐性等待设置了一个时间，在一段时间内网页是否加载完成，如果完成了，就进行下一步；在设置的时间内没有加载完成，则会报超时加载。
driver.implicitly_wait(10)
#页面包含frame/iframe标签，需要先切换到该frame标签，再去定位属于这个frame的元素   ps:HTML5中不支持frame标签
#如果要再去定位其他frame的元素，需要回到该frame的上级，定位到要选择的frame,不过为了保险起见，可以回到整个页面的主frame,然后再去选择其他frame
#.switch_to_frame("XXX") XXX为frame的id或name或通过find_element_by_XXX找到的frame元素
#.switch_to_default_content() 回到当前页面的原始页面，即可以退出当前的frame
#switch_to还可以识别Window和alert
driver.switch_to.frame("")
#id="x-URS-iframe1650523305951.9116"
'''
input_eles = driver.find_elements_by_tag_name("input")
print(len(input_eles))
for i in input_eles:
    print(i.get_attribute("outerHTML"))
'''
'''
<input data-placeholder="邮箱帐号或手机号码" name="email" data-type="email" data-loginname="loginEmail" data-required="true" 
class="j-inputtext dlemail j-nameforslide" type="text" autocomplete="off" tabindex="1" spellcheck="false" 
id="auto-id-1650524468285" placeholder="邮箱帐号或手机号码" style="width: 200px;">

<input data-placeholder="输入密码" name="password" maxlength="50" data-required="true" 
class="j-inputtext dlpwd" type="password" autocomplete="new-password" data-max-length="50" tabindex="2" spellcheck="false" 
id="auto-id-1650524468288" placeholder="输入密码">
'''

#方法一：取单个class属性
#driver.find_element_by_class_name("dlemail").send_keys("yoyo")
#driver.find_element_by_class_name("dlpwd").send_keys("12333")

#方法二：定位一组取下标定位（乃下策，不推荐） 注意：要使用find_elements 有S
#driver.find_elements_by_class_name("j-inputtext")[0].send_keys("yoyo")
#driver.find_elements_by_class_name("j-inputtext")[1].send_keys("12333")

#方法三：css定位
#driver.find_element_by_css_selector(".j-inputtext.dlemail").send_keys("yoyo")
#driver.find_element_by_css_selector(".j-inputtext.dlpwd").send_keys("12333")

#方法四：取单个css属性也是可以的
#driver.find_element_by_css_selector(".dlemail").send_keys("yoyo")
#driver.find_element_by_css_selector(".dlpwd").send_keys("12333")

#方法五：直接包含空格的CSS属性定位 注意格式：标签[属性='值'] 其中值要写全，属性是唯一的，那么标签名可以不用写
driver.find_element_by_css_selector("input[class='j-inputtext dlemail j-nameforslide']").send_keys("yoyo")
driver.find_element_by_css_selector("input[class='j-inputtext dlpwd']").send_keys("12333")


