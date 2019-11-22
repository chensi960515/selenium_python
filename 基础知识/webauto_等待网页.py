from selenium import webdriver
wd = webdriver.Chrome()
#设置最大等待时间
#周期性（每隔半秒钟）重新寻找该元素，直到该元素找到，或者超出指定最大等待时长，这时才 抛出异常  或者  空列表
wd.implicitly_wait(10)

wd.get('http://www.baidu.com')

element = wd.find_element_by_id('kw')
element.send_keys('白月黑羽\n')

#等待两秒
# from time import sleep
# sleep(2)

element2 = wd.find_element_by_id('2')
print(element2.text)

wd.quit()