import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

path = r"C:\Program Files\Python313\chromedriver.exe"
ser = Service(executable_path=path)
driver = webdriver.Chrome(service=ser)

driver.get("https://practice.softwaretestingmentor.com/iframe")
time.sleep(3)

# 滚动条处理
js = "window.scrollTo(0, 400)"
driver.execute_script(js)

# frame 处理
iframe = driver.find_element(By.ID, "iframe-frame-1")
driver.switch_to.frame(iframe)
driver.find_element(By.ID, "iframe-name-input").send_keys("111")

# 返回上一个frame
driver.switch_to.default_content()
iframe1 = driver.find_element(By.ID, "internal-iframe")
driver.switch_to.frame(iframe1)
driver.find_element(By.NAME, "iframeName").send_keys("222")

time.sleep(3)