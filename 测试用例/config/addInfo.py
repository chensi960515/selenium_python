from selenium.webdriver.support.ui import Select
from time import sleep
from 测试用例.config.indexConfig import INDEX_INFO

wd = INDEX_INFO()

#抽取出添加功能的公共代码块
def ADD(info1,info2,info3):
    wd.find_element_by_css_selector('div .add-one-area button[type="button"]').click()

    inputs = wd.find_elements_by_css_selector('.add-one-area .form-control')

    inputs[0].send_keys(info1)
    inputs[1].send_keys(info2)
    inputs[2].send_keys(info3)

    wd.find_elements_by_css_selector('.add-one-area .btn-xs')[0].click()

#新增客户
def ADD_CUSTOMER(cusname,phone,address):
    """"新增客户

    cusname :客户名
    phone   :练习电话
    address :地址

    """
    wd.find_element_by_css_selector('.sidebar-menu a[href="#/customers"]').click()
    ADD(cusname,phone,address)

#新增药品
def ADD_MEDICION(medname,teal,dectal):
    """新增药品

    medname :药名
    teal    :编号
    dectal  :描述

    """
    wd.find_element_by_css_selector('.sidebar-menu a[href = "#/medicines"]').click()
    ADD(medname,teal,dectal)

#新增订单
def ADD_ORDER(order_name,select_cus,select_mer,math):
    """新增订单

    order_name:订单名称
    select_cus:日期
    select_mer:客户
    math      :药品 * 数量

    """
    wd.find_element_by_css_selector('.sidebar-menu a[href="#/orders"]').click()
    wd.find_element_by_css_selector('div .add-one-area button[type="button"]').click()

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

    return order_list


wd.quit()