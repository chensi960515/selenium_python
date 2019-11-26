from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep


driver = webdriver.Firefox()
driver.get('file:///E:/soft/WebTest/demo.html')
driver.implicitly_wait(5)

driver.switch_to.default_content()

#select框
select = Select(driver.find_element_by_xpath('//select[@name="select"]'))
#select.select_by_value('2')
select.select_by_visible_text('Audi')

#单选框redio
driver.find_element_by_xpath("//div[@id='radio']/input[2]").click()

#CheckBox
#先选择之前已经默认选择的复选框
driver.find_elements_by_xpath('')

