from selenium import webdriver
from time import sleep

wd = webdriver.Chrome()
wd.get('http://127.0.0.1/mgr/sign.html')

wd.implicitly_wait(5)

wd.find_element_by_id('username').send_keys('byhy')
wd.find_element_by_id('password').send_keys('88888888')

wd.find_element_by_xpath('//button').click()

wd.find_element_by_xpath('//a[contains(@href,"#/orders")]').click()

while True:
    # 修改全局等待时间，以免找不到元素，等待时间较长
    wd.implicitly_wait(1)
    delButtons = wd.find_elements_by_xpath('//label')

    # 再改回原来的等待时间
    wd.implicitly_wait(5)

    # 没有删除按钮，说明已经全部删除了
    if not delButtons:
        break

    delButtons[0].click()
    wd.switch_to.alert.accept()

    sleep(1)



