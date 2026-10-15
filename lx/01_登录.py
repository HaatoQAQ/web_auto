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
# 启动时禁用密码泄露检测
options = webdriver.ChromeOptions()
options.add_experimental_option("prefs",{
    "profile.password_manager_leak_detection": False
})

driver = webdriver.Chrome(service=ser, options=options)
# 3.输入网址

driver.get("https://www.saucedemo.com/")
# 全局等待：隐式等待
driver.implicitly_wait(10)
driver.maximize_window()

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
time.sleep(3)
ele = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"login-button")))
ele.click()

app_log = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CLASS_NAME,"app_logo"))).text
assert app_log == "Swag Labs", f"登录失败，预期:Swag Labs , 实际:{app_log}"

time.sleep(3)