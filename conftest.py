import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from page.page_login import PageLogin
from page.page_inventory import PageInventory
from config import BASE_URL


@pytest.fixture()
def browser():
    path = r"C:\Program Files\Python313\chromedriver.exe"
    ser = Service(executable_path=path)  # Chrome浏览器驱动服务对象
    # 启动时禁用密码泄露检测
    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", {
        "profile.password_manager_leak_detection": False
    })

    driver = webdriver.Chrome(service=ser, options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)

    yield driver
    driver.quit()


@pytest.fixture()
def page_login(browser):
    """登录界面"""
    page = PageLogin(browser)
    page.open_url(BASE_URL)
    page.login("standard_user", "secret_sauce")
    return page

@pytest.fixture()
def page_inventory(page_login):
    """基于已登录的状态，返回PageInventory对象"""
    return PageInventory(page_login.driver)