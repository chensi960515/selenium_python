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

wd.find_element_by_css_selector('.sidebar-menu a[href="#/orders"]').click()
wd.find_element_by_css_selector('div .add-one-area button[type="button"]').click()

def ADD_ORDER(order_name,select_cus,select_mer,math):
    name= wd.find_element_by_css_selector('.add-one-area .form-control')
    name.send_keys(order_name)

    # 客户选择 南京中医院2    药品选择 青霉素盒装1    数量填入 100盒
    selectElements = wd.find_elements_by_css_selector('.add-one-area select')

    Select(selectElements[0]).select_by_visible_text(select_cus)
    Select(selectElements[1]).select_by_visible_text(select_mer)

    inputs = wd.find_elements_by_css_selector('.add-one-area input')
    inputs[2].send_keys(math)

    wd.find_elements_by_css_selector('.add-one-area button')[1].click()
    sleep(1)

    orders = wd.find_elements_by_css_selector('.search-result-item')[0].find_elements_by_tag_name('span')

    medicion = wd.find_element_by_css_selector('.search-result-item .search-result-item-field p')

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