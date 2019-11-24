from selenium import webdriver

wd = webdriver.Chrome()
wd.get('http://f.python3.vip/webauto/test2.html')
#wd.implicitly_wait(5)

element = wd.find_element_by_css_selector("#s_radio input[checked='checked']")
print(element.get_attribute('value'))

wd.find_element_by_css_selector("#s_radio input[value = '小雷老师']").click()

