import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from page.page_login import PageLogin
from page.page_inventory import PageInventory
from page.page_cart import  PageCart
from page.page_checkout import PageCheckout
from page.page_pay import PagePay
from config import (BASE_URL,DRIVER_PATH)
import os


@pytest.fixture()
def browser():
    # 让 Selenium 自动处理驱动
    # ser = Service(executable_path=DRIVER_PATH)  # Chrome浏览器驱动服务对象
    # 启动时禁用密码泄露检测
    options = webdriver.ChromeOptions()

    # CI 环境用无头模式
    if os.getenv("CI"):
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
    else:
        options.add_argument("--start-maximized")

    options.add_experimental_option("prefs", {
        "profile.password_manager_leak_detection": False
    })

    # driver = webdriver.Chrome(service=ser, options=options)
    driver = webdriver.Chrome(options=options)
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

@pytest.fixture()
def page_cart(page_inventory):
    page_inventory.add_shopping_cart()
    page_inventory.enter_shopping_cart()
    return PageCart(page_inventory.driver)


@pytest.fixture()
def page_checkout(page_cart):
    page_cart.checkout()
    return PageCheckout(page_cart.driver)


@pytest.fixture()
def page_pay(page_checkout):
    page_checkout.add_information("li","si","13000000001")
    page_checkout.submit_information()
    return PagePay(page_checkout.driver)