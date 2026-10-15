import time

from faker.providers.person import or_IN
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

path = r"C:\Program Files\Python313\chromedriver.exe"
ser = Service(executable_path=path)
driver = webdriver.Chrome(service=ser)

driver.get("https://www.bilibili.com")
driver.find_element(By.LINK_TEXT, "国创").click()
time.sleep(3)
handles = driver.window_handles
print("handles=", handles)
# -1 默认找最新的窗口
driver.switch_to.window(handles[-1])
driver.find_element(By.LINK_TEXT, "追番人数").click()

time.sleep(5)