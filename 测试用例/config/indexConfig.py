from selenium import webdriver

def INDEX_INFO(self):
    wd = webdriver.Chrome()
    wd.implicitly_wait(5)

    wd.get('http://127.0.0.1/mgr/sign.html')

    # 根据 ID 选择元素，并且输入字符串
    wd.find_element_by_id('username').send_keys('byhy')
    wd.find_element_by_id('password').send_keys('88888888')

    # 点击登录
    wd.find_element_by_tag_name('button').click()

    return wd
