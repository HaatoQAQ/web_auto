import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, select

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

# select1 = Select(driver.find_element(By.CLASS_NAME,"product_sort_container"))

"""css 查找方式"""
# 按 id 查找(#) #username ; 对应 <input id="username"> ; find_element(By.CSS_SELECTOR, "#username");
# select1 = Select(driver.find_element(By.CSS_SELECTOR, "#"))

# 按class查找(.) ; <button class="login_btn"> ; find_element(By.CSS_SELECTOR, ".login_btn") ; 有多个class时，用点连起来， .btn.primary.large
# select1 = Select(driver.find_element(By.CSS_SELECTOR, ".product_sort_container"))

# 按属性值找([属性=值]); [name="username"]; find_element(By.CSS_SELECTOR, '[name="username"]');
# select1 = Select(driver.find_element(By.CSS_SELECTOR, '[aria-label="Sort products"]'))

# 按路径找
# select1 = Select(driver.find_element(By.CSS_SELECTOR, "#header_container > div.header_secondary_container > div > span > select"))

"""xpath"""
# 按属性查找(@属性); //input[@name="username"]
select1 = Select(driver.find_element(By.XPATH, '//select[@aria-label="Sort products"]'))

# 按文字查找; //input[text()="username"]
# select1 = Select(driver.find_element(By.XPATH, '//select[text()=""]'))

time.sleep(3)
# select1.select_by_index(1) # 下表
# select1.select_by_value("za") # value 属性值
select1.select_by_visible_text("Price (low to high)") # 文本

time.sleep(5)

