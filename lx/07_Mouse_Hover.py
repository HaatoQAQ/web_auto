import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

# 2.打开浏览器（创建浏览器驱动对象）
path = r"C:\Program Files\Python313\chromedriver.exe"
ser = Service(executable_path=path)  # Chrome浏览器驱动服务对象
driver = webdriver.Chrome(service=ser)  # 打开Chrome浏览器

driver.get("https://practice.softwaretestingmentor.com")

driver.find_element(By.LINK_TEXT, "Mouse Hover").click()
ele = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-testid="hover-box-1"]')))
ActionChains(driver).move_to_element(ele).perform()

time.sleep(3)

ele1 = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID, "hover-dropdown-trigger")))
ActionChains(driver).move_to_element(ele1).perform()
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID, "hdd-profile"))).click()
time.sleep(3)

ele2 = driver.find_element(By.XPATH, '//*[@id="img-hover-1"]/div[2]')
ActionChains(driver).move_to_element(ele2).perform()
time.sleep(3)