from selenium import webdriver

#创建webdriverd对象，指明使用chrome浏览器驱动
wd = webdriver.Chrome(r'E:\soft\WebTest\webdrivers\chromedriver.exe')
#调用webdriver对象的get方法，可以让浏览器打开指定网页
wd.get('http://www.baidu.com')

element = wd.find_element_by_id('kw')

element.send_keys('白月黑羽\n')
# wd.start_client()
#wd.quit()