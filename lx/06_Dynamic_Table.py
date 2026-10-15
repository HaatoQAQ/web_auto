import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 2.打开浏览器（创建浏览器驱动对象）
path = r"C:\Program Files\Python313\chromedriver.exe"
ser = Service(executable_path=path)  # Chrome浏览器驱动服务对象
driver = webdriver.Chrome(service=ser)  # 打开Chrome浏览器

driver.get("https://practice.softwaretestingmentor.com")

driver.find_element(By.LINK_TEXT, "Dynamic Table").click()
time.sleep(3)
WebDriverWait(driver,timeout=10).until(EC.visibility_of_element_located((By.ID,"add-row-btn"))).click()


driver.find_element(By.LINK_TEXT,"Pagination Table").click()
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//button[text()="3"]'))).click()

time.sleep(3)

# 上传文件
driver.find_element(By.LINK_TEXT, "File Upload").click()
driver.find_element(By.ID,"uploadFile").send_keys(r"D:\work\面试笔记\面试提.md")

time.sleep(3)

driver.find_element(By.ID, "upload-btn").click()

time.sleep(3)