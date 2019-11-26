from selenium import webdriver
from time import sleep
driver = webdriver.Firefox(firefox_profile=r'C:\Users\zz\AppData\Roaming\Mozilla\Firefox\Profiles\zxplr12b.default')
wd = webdriver.Chrome()
driver.get("http://www.baidu.com")

# sleep(1)
# driver.get("http://www.biying.com")
# sleep(1)
# driver.back()
# sleep(1)
# driver.forward()
# sleep(1)
# driver.refresh()

