from base.base import BasePage
from selenium.webdriver.common.by import By

class PageCheckout(BasePage):
    """结算信息页"""

    def __init__(self, driver, timeout=10):
        super().__init__(driver)
        self.first_name_input = (By.ID,"first-name")
        self.last_name_input = (By.ID,"last-name")
        self.phone_input = (By.ID,"postal-code")
        self.submit_btn = (By.NAME,"continue")
        self.pay_page = (By.CLASS_NAME,"title")

    def add_information(self,first_name,last_name,phone):
        """填写个人信息"""
        self.base_input(self.first_name_input,first_name)
        self.base_input(self.last_name_input,last_name)
        self.base_input(self.phone_input,phone)

    def submit_information(self):
        self.base_click(self.submit_btn)
        return self.fd_element(self.pay_page).text