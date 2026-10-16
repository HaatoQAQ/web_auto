from os import remove

from base.base import BasePage
from selenium.webdriver.common.by import By

class PageCart(BasePage):
    """购物车页面"""

    def __init__(self, driver, timeout=10):
        super().__init__(driver)
        self.remove_btn = (By.NAME,"remove-sauce-labs-backpack")
        self.checkout_btn = (By.CSS_SELECTOR,'[data-test="checkout"]')
        self.checkout_page = (By.CSS_SELECTOR,'[data-test="title"]')

    def remove_things(self):
        """删除物品"""
        self.base_click(self.remove_btn)

    def checkout(self):
        self.base_click(self.checkout_btn)
        return self.fd_element(self.checkout_page).text