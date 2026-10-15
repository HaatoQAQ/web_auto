from base.base import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class PageInventory(BasePage):
    """商品信息页面"""

    def __init__(self, driver, timeout=10):
        super().__init__(driver)
        self.check_details = (By.LINK_TEXT,"Sauce Labs Backpack")
        self.quit_details = (By.ID,"back-to-products")
        self.add_cart = (By.ID,"add-to-cart-sauce-labs-backpack")
        self.remove_cart = (By.ID, "remove-sauce-labs-backpack")
        self.enter_cart = (By.CLASS_NAME, "shopping_cart_link")
        self.quit_cart = (By.NAME,"continue-shopping")
        self.sort = (By.XPATH,'//select[@aria-label="Sort products"]')
        self.inventory_page = (By.XPATH,'//*[@id="header_container"]/div[2]/span')


    def check_the_details(self):
        """查看物品详情"""
        self.base_click(self.check_details)
        return self.fd_element(self.quit_details).text

    def quit_the_details(self):
        self.base_click(self.quit_details)
        return self.fd_element(self.inventory_page).text

    def add_shopping_cart(self):
        self.base_click(self.add_cart)
        return self.fd_element(self.remove_cart).text

    def remove_shopping_cart(self):
        self.base_click(self.remove_cart)
        return self.fd_element(self.add_cart).text

    def enter_shopping_cart(self):
        self.base_click(self.enter_cart)
        return self.fd_element(self.quit_cart).text

    def quit_shopping_cart(self):
        self.base_click(self.quit_cart)
        return self.fd_element(self.inventory_page).text

    def sort_details(self,text=None,index=None,value=None):
        """商品排序"""
        self.base_select_list(self.sort,index=index)
        return Select(self.fd_element(self.sort)).options[1].text