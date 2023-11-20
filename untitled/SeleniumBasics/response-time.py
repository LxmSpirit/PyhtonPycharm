from selenium import webdriver
import time

'''
Web页面响应时间探测工具
打开一个页面，并统计页面各项耗时【页面响应时间，重定向时间，DNS解析时间，页面渲染时间，白屏等待时间】
可以用于统计某些页面的耗时
目前统计的是fireFox的数据
后续可以把耗时输出到文件里，用以统计耗时数据
'''


def gettime(page, url):
    page.append(url)
    # 请求到响应时间=responseStart 服务器开始响应的时间requestStart 发起请求的时间
    page.append(driver.execute_script("return performance.timing.responseStart") - driver.execute_script(
        "return performance.timing.requestStart"))
    # 重定向时间=redirectStart 重定向开始时间-redirectEnd 重定向结束时间
    page.append(driver.execute_script("return performance.timing.redirectStart") - driver.execute_script(
        "return performance.timing.redirectEnd"))
    # DNS解析时间=domainLookupStart 查询DNS的开始时间-domainLookupEnd 查询DNS的结束时间
    page.append(driver.execute_script("return performance.timing.domainLookupEnd") - driver.execute_script(
        "return performance.timing.domainLookupStart"))
    # 页面渲染时间=domComplete 从图中看是dom渲染完成时间-domLoading 从图中看是开始渲染dom的时间
    page.append(driver.execute_script("return performance.timing.domComplete") - driver.execute_script(
        "return performance.timing.domLoading"))
    # 白屏时间=responseStart 服务器开始响应的时间-navigationStart 加载起始时间
    page.append(driver.execute_script("return performance.timing.responseStart") - driver.execute_script(
        "return performance.timing.navigationStart"))
    return page


if __name__ == '__main__':
    url = "http://www.baidu.com"
    filepath = "time12.csv"
    str1 = "被测页面,页面响应时间,重定向时间,DNS解析时间,页面渲染时间,白屏等待时间"+ "\n"
    page = []
    # 初始化一个浏览器
    driver = webdriver.Chrome()

    '''
    以下是各种详细时间点的获取方式
    # navigationStart 加载起始时间
    page.append(driver.execute_script("return performance.timing.navigationStart"))
    # redirectStart 重定向开始时间（如果发生了HTTP重定向，每次重定向都和当前文档同域的话，就返回开始重定向的fetchStart的值。其他情况，则返回0）
    page.append(driver.execute_script("return performance.timing.redirectStart"))
    # redirectEnd 重定向结束时间（如果发生了HTTP重定向，每次重定向都和当前文档同域的话，就返回最后一次重定向接受完数据的时间。其他情况则返回0）
    page.append(driver.execute_script("return performance.timing.redirectEnd"))
    # fetchStart 浏览器发起资源请求时，如果有缓存，则返回读取缓存的开始时间
    page.append(driver.execute_script("return performance.timing.fetchStart"))
    # domainLookupStart 查询DNS的开始时间。如果请求没有发起DNS请求，如keep-alive，缓存等，则返回fetchStart
    page.append(driver.execute_script("return performance.timing.domainLookupStart"))
    # domainLookupEnd 查询DNS的结束时间。如果没有发起DNS请求，同上
    page.append(driver.execute_script("return performance.timing.domainLookupEnd"))
    # connectStart 开始建立TCP请求的时间。如果请求是keep-alive，缓存等，则返回domainLookupEnd(secureConnectionStart) 如果在进行TLS或SSL，则返回握手时间
    page.append(driver.execute_script("return performance.timing.connectStart"))
    # connectEnd 完成TCP链接的时间。如果是keep-alive，缓存等，同connectStart
    page.append(driver.execute_script("return performance.timing.connenctEnd"))
    # responseStart 服务器开始响应的时间
    page.append(driver.execute_script("return performance.timing.responseStart"))
    # requestStart 发起请求的时间
    page.append(driver.execute_script("return performance.timing.requestStart"))
    # domLoading 从图中看是开始渲染dom的时间，具体未知
    page.append(driver.execute_script("return performance.timing.domLoading"))
    # domComplete 从图中看是dom渲染完成时间，具体未知
    page.append(driver.execute_script("return performance.timing.domComplete"))
    # loadEventStart 触发load的时间，如没有则返回0
    page.append(driver.execute_script("return performance.timing.loadEventStart"))
    # loadEventEnd load事件执行完的时间，如没有则返回0
    page.append(driver.execute_script("return performance.timing.loadEventEnd "))'''
    # 窗口最大化
    driver.maximize_window()
    time.sleep(1)
    # 打开页面
    driver.get(url)
    time.sleep(1)
    timeStatistical = open(filepath, "a+")
    i = 2
    timeStatistical.write(str1)
    while i > 0:
        try:
            driver.refresh()
            page = gettime(page, url)
            #map(lambda x: str(x), page)将lambda x: str(x) 这个函数作用到每个page的元素中
            pageStr = list(map(lambda x: str(x), page))
            print(pageStr)
            #",".join(pageStr)  将pageStr通过,分割
            str = ",".join(pageStr) + "\r\n"
            print(str)
            timeStatistical.write(str)
        except Exception as e:
            print(e)
        i = i - 1
    timeStatistical.close()
    #driver.close()