from base.base import BasePage
from selenium.webdriver.common.by import By

class PagePay(BasePage):
    """结算"""

    def __init__(self, driver, timeout=10):
        super().__init__(driver)
        self.pay_btn = (By.CSS_SELECTOR,".btn.btn_action.btn_medium.cart_button")
        self.assert_pay = (By.XPATH,'//h2[@data-test="complete-header"]')

    def pay(self):
        self.base_click(self.pay_btn)
        return self.fd_element(self.assert_pay).text
