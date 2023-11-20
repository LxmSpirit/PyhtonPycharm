# coding:utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement


#selenium三种等待方式
#为保证脚本运行稳定，需要脚本中添加等待时间

#第一种，强制等待
'''引入time模块，使用time.sleep()'''
#这种方式叫强制等待，不管浏览器是否加载完，程序都要等待3秒，3秒过后才能继续执行代码
#过于死板，影响程序执行速度
#driver = webdriver.Chrome()
#driver.get("http://baidu.com")
'''time.sleep(3)  强制等待3秒再执行下一步'''
#print(driver.current_url)

#第二种，隐形等待
'''通过implicitly_wait()方法，最长30秒'''
#这种方法是在一个时间范围内智能的等待
#如果页面在规定时间内加载完成，则执行下一步，否则一直等待到时间截止
#隐形等待是对整个driver的周期都起作用，所以只需要设置一次即可
#driver = webdriver.Chrome()
'''driver.implicitly_wait(30)'''
#driver.get("http://mail.126.com/")
#print(driver.current_url)

#第三种，显性等待
#通过WebDriverWait类，配合该类的until()和until_not()方法，根据判断条件，灵活等待
#主要意思是：程序每隔xx秒看一眼，如果条件成立，则执行下一步，否则继续等待，知道超过设置的最长时间，然后抛出TimeoutException
'''WebDriverWait(driver, timeout, poll_frequency, ignored_exceptions).until(method, message)'''
    #driver-传入WebDriver实例，即我们上例中的driver
    #timeout-超时时间，等待的最长时间（同时需要考虑隐形等待时间）,隐形和显性都存在时，取二者中较大的
    #poll_frequency-调用until或until_not中的方法的间隔时间，默认是0.5秒
    #ignored_exceptions-忽略的异常，如果在调用until或until_not的过程中抛出这个元组中的异常，则不中断代码，继续等待
    #                               如果抛出的是这个元组外的异常，则中断代码，抛出异常，默认只有NoSearchElementException
    #method-在等待期间，每隔一段时间（指poll_frequency设定的时间）调用这个传入的方法，直到返回值不是false
    #message-如果超时，抛出TimeoutException,将message传入异常
#until--until是当某元素出现或什么条件成立，则继续进行
#until_not--与until相反，是当某元素消失或什么条件不成立，则继续执行，参数与until相同
'''即：WebDriverWait(driver, 超时时长, 调用频率, 忽略异常).until(可执行方法, 超时时返回的信息)'''
#注意：method即可执行方法，一定要是可调用的，即这个对象一定要有call()方法，否则会抛出异常
    #这里可以使用selenium提供的expected_conditions模块中的各种条件，也可以用WebElement的is_displayed()、is_enabled()、is_selected(）方法
    #或者用自己封装的方法都可以
'''excepted_conditions模块'''
'''
1.验证driver.title,是否等于或包含传入的参数
    expected_conditions.title_is
    expected_conditions.title_contains
2.验证元素是否出现，传入的参数都是元组类型的locator(定位器)，如(By.ID,'kw')  
    ！！！此方法只关注元素是否被添加到DOM中，元素不一定可见
    presence_of_element_loacted 只要一个符合条件的元素加载出来就通过
    presence_of_all_elements_loacted 必须所有符合条件的元素都加载出来
3.验证元素是否可见，前两个传入的参数都是元组类型的locator(定位器),第三个传入WebElement,第一个和第三个其实本质是一样的 ？？？  
    ！！！此方法关注元素是否被添加到DOM中并是否可见
        可见代表元素可显示并且宽、高都大于0
    visibility_of_element_located
    invisibility_of_element_located
    visibility_of
4.验证元素中是否含有某段文本，一个判断元素text,一个判断元素的value
    text_to_be_present_in_element
    text_to_be_present_in_element_value
5.验证frame是否可切入，传入的参数是locator元组或者直接传入定位方式：id、name、index或WebElement
    frame_to_be_available_and_switch_to_it
6.验证是否有alert出现
    alert_is_present
7.验证元素是否可以点击，传入的参数是locator(定位器)
    element_to_be_clickable
8.验证元素是否被选中，
    传入的参数第一个WebElement对象，第二个locator元组，
        第三个WebElement对象及状态-相等返回True,否则返回False, 第四个locator以及状态-相等返回True,否则返回False
    element_to_be_selected
    element_located_to_be_selected
    element_selection_state_to_be
    element_located_selection_state_to_be
9.验证元素是否仍在DOM中，传入的参数是WebElement对象，可以用来判断页面是否刷新
    staleness_of
       
'''
'''DOM--当网页被加载时，浏览器会创建页面的文档对象模型（Document Object Model）'''

base_url = "http://www.baidu.com"
driver = webdriver.Chrome()
driver.implicitly_wait(5)
#()代表tuple，元组数据类型
locator = (By.ID,'kw')
driver.get(base_url)


'''判断title,返回布尔值'''
#res1 = WebDriverWait(driver,10).until(EC.title_is(u"百度一下，你就知道"))
#u后面字符串以 Unicode 格式 进行编码，一般用在中文字符串前面，防止因为源码储存格式问题，导致再次使用时出现乱码。
#PS：不是仅仅是针对中文, 可以针对任何的字符串，代表是对字符串进行。一般英文字符在使用各种编码下,，基本都可以正常解析, 所以一般不带u。
#print(type(res1))
#print('判断title-title_is: '+str(res1))


'''判断title,返回布尔值'''
#res1 = WebDriverWait(driver,10).until(EC.title_contains(u"百度一下"))
#print(type(res1))
#print('判断title-title_contains: '+str(res1))

'''判断元素是否加到了dom树里，并不代表元素一定可见'''
#resl = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,'kw')))
#print(type(res1))
#print('判断presence_of_element_located: '+str(res1))


'''判断元素是否加到了dom树里，并且可见，可见代表元素可显示且宽和高都大于0'''
#resl = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,'kw')))
#print(type(resl))
#print('判断visibility_of_element_located: '+str(res1))

'''判断元素是否可见，可见就返回这个元素'''
#res1 = WebDriverWait(driver,10).until(EC.visibility_of(driver.find_element(By.ID,'su')))
#print(type(resl))
#print('判断find_element1: '+str(res1))
#res1 = WebDriverWait(driver,10).until(EC.visibility_of(driver.find_element(by=By.ID,value='su')))
#print(type(resl))
#print('判断find_element2: '+str(res1))

'''判断是否至少有一个元素存在于dom树中，如果定位到就返回列表'''
#res1pre = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'.mnav')))
#print(type(res1pre))
#print('判断presence_of_all_elements_located: '+str(res1pre))

'''判断是否至少有一个元素再页面中可见，如果定位到就返回列表'''
#reslvis = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'.mnav')))
#print(type(reslvis))
#print('判断visibility_of_any_elements_located: '+str(reslvis))

'''判断元素中是否包含了预期的字符串，返回布尔值'''
#resl = WebDriverWait(driver,10).until(EC.text_to_be_present_in_element((By.XPATH,"//*[@id='u1']/a[8]"),u'设置'))
#try:
   # resltext = WebDriverWait(driver, 30).until(EC.text_to_be_present_in_element((By.XPATH, "//*[@id='u1']"), u'设置'))
    #print(type(resltext))
   # print('判断text_to_be_present_in_element: ' + str(resltext))
#except Exception as e:
   # print('fail''')

'''判断元素的属性值中是否包含了预期的字符串，返回布尔值'''
#restextv = WebDriverWait(driver,10).until(EC.text_to_be_present_in_element_value((By.CSS_SELECTOR,'#su'),u'百度一下'))
#print(type(restextv))
#print('判断text_to_be_present_in_element_value: '+str(restextv))

'''判断frame是否可以switch进去，如果可以，返回True并且switch进去，否则返回false'''
#driverframe = webdriver.Chrome()
#driverframe.get("http://mail.126.com/")
#resframe = WebDriverWait(driverframe,10).until(EC.frame_to_be_available_and_switch_to_it((By.NAME,'')))
#resframe = WebDriverWait(driverframe,10).until(EC.frame_to_be_available_and_switch_to_it((By.ID,'x-URS-iframe1650780547636.7676')))#会超时
#print(type(resframe))
#print('判断frame_to_be_available_and_switch_to_it: '+str(resframe))
#driverframe.close()

'''判断元素是否存在于dom或不可见，如果可见返回True,不可见返回这个元素'''
#使用场景：不同角色登录系统后，页面按身份展示模块或按钮等
######resinv = WebDriverWait(driver,10).until(EC.invisibility_of_element_located((By.CSS_SELECTOR,'#swfEveryCookieWrap')))#这是不可见###不确定
#resinv1 = WebDriverWait(driver,30).until(EC.invisibility_of_element_located((By.ID,'s_is_result_css')))#这是不可见，通过style="display:none;"确定
#resinv2 = WebDriverWait(driver,30).until(EC.invisibility_of_element_located((By.ID,'s_kw_wrap')))#这是可见
#print(type(resinv1))
#print(type(resinv2))
#print('判断invisibility_of_element_located不可见: '+str(resinv1))
#print('判断invisibility_of_element_located可见: '+str(resinv2))

'''判断元素是否可见并且是enable的，代表可点击'''
#rescli = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='u1']")))
#rescli = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='s-usersetting-top']")))
#print(type(rescli))
#print('判断element_to_be_clickable: '+str(rescli))
#driver.find_element(By.XPATH, "//*[@id='s-usersetting-top']").click()

'''等待元素从dom树中移除'''#X
#未找到例子
#WebDriverWait(driver,10).until(EC.staleness_of(driver.find_element()))

'''判断元素是否被选中，一般用在下拉列表'''
'''注意：下拉列表是指
<select name="">
<option value=" ">选项1</option>
<option value=" ">选项2</option>
</select>
这种类型 其他情况会显示找不到元素
'''#X
#driver.find_element(By.XPATH, "//*[@id='s-usersetting-top']").click()
#usersetting = driver.find_element_by_id("s-usersetting-top")
#usersetting2 = driver.find_element_by_xpath("//*[@id='s-user-setting-menu']//*[@class='s-user-setting-pfmenu']//*[@class='setpref first']//*[@class='set']")
#usersetting2 = driver.find_element_by_xpath("//span[@class='set']")
#driver.find_element_by_xpath("//*[@id='s-usersetting-top']").click()
#usersetting3 = driver.find_element_by_xpath("//*[@class='s-user-setting-pfmenu']")#//a//span
#usersetting4 = driver.find_element_by_xpath("//div//a[contains(@class,'setp')]")#//a//span
#usersetting4 = driver.find_element_by_css_selector("a[class='setpref first']")#//a//span
#usersetting4 = driver.find_element_by_xpath("//*[@class='setpref first']")
#usersetting5 = driver.find_element_by_xpath("//*[@class='set']")
#print(usersetting)
#print(usersetting2)
#print(usersetting3)
#print(usersetting3.get_attribute('outerHTML'))
#print(usersetting4)
#print(usersetting4.get_attribute('outerHTML'))
#print(usersetting5)
#print(usersetting5.get_attribute('outerHTML'))
#usersetting.click()
#a = usersetting4.is_enabled()
#print(a)
#usersetting4.click()
#ECselect = EC.element_to_be_selected(driver.find_element_by_xpath("//*[@class='setpref first']"))
#print(type(ECselect))
#print(ECselect)
#ressele = WebDriverWait(driver,30).until(ECselect)
#ressele = WebDriverWait(driver,40).until(ECselect)
#ressele = EC.element_to_be_selected(driver.find_element_by_id("s-usersetting-top"))
#ressele2 = EC.element_to_be_selected(driver.find_element_by_xpath("//*[@id='nr']//option[1]"))
#ressele = WebDriverWait(driver,10).until(EC.element_to_be_selected(driver.find_element(By.XPATH,"//*[@id='nr']//option[1]")))
#print(type(ressele))
#print('判断element_to_be_selected: '+str(ressele))
#print('判断element_to_be_selected2: '+str(ressele2))
#driver.find_element(By.XPATH, "//*[@id='s-usersetting-top']").click()
#driver2 = webdriver.Chrome()
#driver2.get('https://blog.csdn.net/m0_59742894/article/details/121666621')
#a = driver2.find_element_by_link_text('足迹')
#print(a)
#print(a.get_attribute('outerHTML'))
#a.click()
#b = driver2.find_element_by_xpath("//*[@class ='hotArticle-list']//a[1]")
#print(b)
#print(b.get_attribute("outerHTML"))
#print(EC.element_to_be_selected(b))
#ressele = WebDriverWait(driver,10).until(EC.element_to_be_selected(b))

'''判断元素选中状态是否符合预期'''#X
#ressta = WebDriverWait(driver,10).until(EC.element_selection_state_to_be(driver.find_element())
#print(type(ressta))
#print('判断text_to_be_present_in_element_value: '+str(ressta))

'''判断元素选中状态是否符合预期'''#X
#WebDriverWait(driver,10).until(EC.element_located_selection_state_to_be())

'''判断页面上是否存在alert,如果有就切换到alert并返回alert的内容'''#X
#instance = WebDriverWait(driver,10).until(EC.alert_is_present)
#print(instance)

driver.close()













