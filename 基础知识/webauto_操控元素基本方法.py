from selenium import webdriver
wd = webdriver.Chrome()
wd.implicitly_wait(10)

wd.get('http://f.python3.vip/webauto/test3.html')

#   清除内容 clear
# element = wd.find_element_by_id('input1')
#
# element.clear()
#
# element.send_keys('白月黑羽')

#获取属性   get_attribute
# element = wd.find_element_by_id('input1')
# classzz = element.get_attribute('value')
# print(classzz)

#获取整个元素对应的HTML  element.get_attribute('outerHTML')
element = wd.find_element_by_id('input1')
print(element.get_attribute('outerHTML'))
#获取某个元素 内部 的HTML文本内容，element.get_attribute('innerHTML')
print(element.get_attribute('innerHTML'))

wd.quit()