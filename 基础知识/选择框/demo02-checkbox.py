from selenium import webdriver

wd = webdriver.Chrome()
wd.get('http://f.python3.vip/webauto/test2.html')
wd.implicitly_wait(5)

#先选中已经选择的复选框
elements = wd.find_elements_by_css_selector('#s_checkbox input[checked="checked"]')

#再次点击已经选中的复选框,保证都是未选中的状态
for element in elements:
    element.click()

wd.find_element_by_css_selector('#s_checkbox input[value="小雷老师"]').click()