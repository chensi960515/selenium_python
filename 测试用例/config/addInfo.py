from selenium import webdriver

from 测试用例.config.indexConfig import INDEX_INFO

INDEX_INFO()

def add(info1,info2,info3):
    wd.find_element_by_css_selector('div .add-one-area button[type="button"]').click()

    inputs = wd.find_elements_by_css_selector('.add-one-area .form-control')

    inputs[0].send_keys(info1)
    inputs[1].send_keys(info2)
    inputs[2].send_keys(info3)

    wd.find_elements_by_css_selector('.add-one-area .btn-xs')[0].click()

def addCustomer(cusname,phone,address):
    wd.find_element_by_css_selector('.sidebar-menu a[href="#/customers"]').click()
    add(cusname,phone,address)

def addMedicion(medname,teal,dectal):
    wd.find_element_by_css_selector('.sidebar-menu a[href = "#/medicines"]').click()
    add(medname,teal,dectal)

addMedicion('青霉素','YP-32342399','青霉素注射液，每支15ml')