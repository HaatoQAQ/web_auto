import pytest

from page.page_login import PageLogin
from config import (USERNAME,PASSWORD,BASE_URL)
from script import log
from tools import DriverTools
from datetime import datetime

class TestLogin:

    def setup_method(self):
        """前置"""
        self.driver = DriverTools.get_driver()
        self.page_login = PageLogin(self.driver)
        self.page_login.open_url(BASE_URL)

    def teardown_method(self):
        """后置"""
        DriverTools.quit_driver()

    def test_01_login(self):
        """登录成功"""
        self.page_login.login("standard_user","secret_sauce")
        result = self.page_login.get_success_result()
        log.info(f"登录结果{result}")
        try:
            assert result == "Swag Labs"
        except AssertionError:
            log.error(f"断言失败：预期 Swag Labs，实际 {result}")
            raise  # 关键：重新抛出，让 pytest 知道用例失败了

    users=[("standard_user","secret_sauce"),("visual_user","secret_sauce")]
    @pytest.mark.parametrize("username,password",users)
    def test_02_login(self,username,password):
        """登录成功"""
        self.page_login.login(username,password)
        result = self.page_login.get_success_result()
        log.info(f"登录结果 {result}")
        try:
            assert result == "Swag Labs"
        except AssertionError:
            log.error(f"断言失败：预期 Swag Labs， 实际 {result}")
            raise


    def test_03_login_fail_username_error(self):
        self.page_login.login("standard_use","secret_sauce")
        result = self.page_login.get_fail_result()
        log.info(f"登录结果{result}")
        try:
            assert result == "Epic sadface: Username and password do not match any user in this service"
        except AssertionError:
            log.error(f"断言失败：预期 Epic sadface: Username and password do not match any user in this service , 实际 {result}")
            self.page_login.get_shot(datetime.now().strftime("%Y%m%d_%H%M%S") + ".png")
            raise

    def test_04_login_fail_password_error(self):
        self.page_login.login("standard_user","secret_sau")
        result = self.page_login.get_fail_result()
        log.info(f"登录结果{result}")
        try:
            assert result == "Epic sadface: Username and password do not match any user in this service"
        except AssertionError:
            log.error(f"断言失败：预期 Epic sadface: Username and password do not match any user in this service , 实际 {result}")
            self.page_login.get_shot(datetime.now().strftime("%Y%m%d_%H%M%S") + ".png")
            raise