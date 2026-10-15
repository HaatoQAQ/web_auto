import time
from pickletools import optimize

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui

path = r"C:\Program Files\Python313\chromedriver.exe"
ser = Service(executable_path=path)

# 启动时禁用密码泄露检测
options = webdriver.ChromeOptions()
options.add_experimental_option("prefs",{
    "profile.password_manager_leak_detection": False
})

driver = webdriver.Chrome(service=ser, options=options)

driver.maximize_window()

driver.get("https://www.saucedemo.com/")

time.sleep(3)
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
# time.sleep(3)
driver.find_element(By.ID, "login-button").click()
time.sleep(5)

# 处理弹窗，方法一：使用 JavaScript alert,但这个弹窗是Chrome的原生对话窗，不是网页的Js alert 不能正常捕捉
# ActionChains(driver).send_keys(Keys.ENTER).perform()

# 方法二：使用pyautogui这类自动化库去点击，可以正常实现，但不稳定，依赖屏幕分辨率和焦点状态。如果浏览器不在前台、或者切了窗口，就会失败
# pyautogui.press('enter')

# 方法三：启动时禁用密码泄露检测

# 查看商品信息
driver.find_element(By.LINK_TEXT, "Sauce Labs Backpack").click()

time.sleep(10)