from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep

from 测试用例.config.libConfig import CHECK_POINT

wd = webdriver.Chrome()
wd.implicitly_wait(5)

wd.get('http://127.0.0.1/mgr/sign.html')

# 根据 ID 选择元素，并且输入字符串
wd.find_element_by_id('username').send_keys('byhy')
wd.find_element_by_id('password').send_keys('88888888')

# 点击登录
wd.find_element_by_tag_name('button').click()


def add(info1, info2, info3):
    wd.find_element_by_css_selector(
        'div .add-one-area button[type="button"]').click()

    inputs = wd.find_elements_by_css_selector('.add-one-area .form-control')

    inputs[0].send_keys(info1)
    inputs[1].send_keys(info2)
    inputs[2].send_keys(info3)

    wd.find_elements_by_css_selector('.add-one-area .btn-xs')[0].click()


def addCustomer(cusname, phone, address):
    wd.find_element_by_css_selector(
        '.sidebar-menu a[href="#/customers"]').click()
    add(cusname, phone, address)


def addOrMedicion(medname, teal, dectal):
    wd.find_element_by_css_selector(
        '.sidebar-menu a[href = "#/medicines"]').click()
    add(medname, teal, dectal)


# 在系统中添加3种药品
addOrMedicion('青霉素盒装1', 'YP-32342341', '青霉素注射液，每支15ml，20支装')
sleep(1)
addOrMedicion('青霉素盒装2', 'YP-32342342', '青霉素注射液，每支15ml，30支装')
sleep(1)
addOrMedicion('青霉素盒装3', 'YP-32342343', '青霉素注射液，每支15ml，40支装')
sleep(1)
# 在系统中添加3个客户
addCustomer('南京中医院1', '2551867851', '江苏省-南京市-秦淮区-汉中路-501')
sleep(1)
addCustomer('南京中医院2', '2551867852', '江苏省-南京市-秦淮区-汉中路-502')
sleep(1)
addCustomer('南京中医院3', '2551867853', '江苏省-南京市-秦淮区-汉中路-503')

wd.find_element_by_css_selector('.sidebar-menu a[href="#/orders"]').click()
wd.find_element_by_css_selector(
    'div .add-one-area button[type="button"]').click()

name = wd.find_element_by_css_selector('.add-one-area .form-control')
name.send_keys('南京中医院订单001')

# 客户选择 南京中医院2    药品选择 青霉素盒装1    数量填入 100盒
selectElements = wd.find_elements_by_css_selector('.add-one-area select')

Select(selectElements[0]).select_by_visible_text('南京中医院2')
Select(selectElements[1]).select_by_visible_text('青霉素盒装1')

inputs = wd.find_elements_by_css_selector('.add-one-area input')
inputs[2].send_keys('100')

wd.find_elements_by_css_selector('.add-one-area button')[0].click()
sleep(1)

orders = wd.find_elements_by_css_selector(
    '.search-result-item')[0].find_elements_by_tag_name('span')

medicion = wd.find_element_by_css_selector(
    '.search-result-item .search-result-item-field p')

order_list = [order_info.text for order_info in orders]
order_list.append(medicion.text)
del order_list[2:4]
print(order_list)

CHECK_POINT('订单信息是否和输入的一致',order_list == [
        '订单：',
        '南京中医院订单001',
        '客户：',
        '南京中医院2',
        '药品：',
        '青霉素盒装1 * 100'])

wd.quit()