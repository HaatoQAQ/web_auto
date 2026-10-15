from base.base import BasePage
from config import BASE_URL
from selenium.webdriver.common.by import By
from tools import DriverTools
import time


class PageLogin(BasePage):

    def __init__(self, driver, timeout=10):
        super().__init__(driver,10)
        self.username = (By.ID, "user-name")
        self.password = (By.ID, "password")
        self.login_button = (By.ID,"login-button")
        self.success_result = (By.CLASS_NAME, "app_logo")
        self.fail_result = (By.CLASS_NAME, "error-button")

    def open_url(self,url_path):
        self.driver.get(url_path)

    def login(self, username, password):
        self.base_input(self.username,username)
        self.base_input(self.password,password)
        self.base_click(self.login_button)

    def get_success_result(self):
        return self.fd_element(self.success_result).text
        # return self.base_assert_text(self.app_log,"Swag Labs")

    def get_fail_result(self):
        return self.fd_element(self.fail_result).text


if __name__ == '__main__':
    login = PageLogin(DriverTools.get_driver())
    login.open_url(BASE_URL)
    login.login("standard_user","secret_sauce")
    time.sleep(3)
