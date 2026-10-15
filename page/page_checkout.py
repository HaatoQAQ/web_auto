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

    def add_information(self):
        """填写个人信息"""
        self.base_input(self.first_name_input,"aodong")
        self.base_input(self.last_name_input,"zhong")
        self.base_input(self.phone_input,"13000000001")

    def submit_information(self):
        self.base_click(self.submit_btn)
        