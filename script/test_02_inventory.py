from time import time

from script import log
from unittest import result

from page.page_inventory import PageInventory
from tools import DriverTools
import time

class TestInventory:

    def test_01_check_the_details(self,page_inventory):
        #测试数据
        #测试方法
        result = page_inventory.check_the_details()
        #预期结果
        log.info(f"预期结果{result}")
        #断言
        try:
            assert result == "Back to products"
        except:
            log.error(f"断言错误：预期 Back to products 实际 {result}")
            raise

    def test_02_quit_the_details(self,page_inventory):
        result = page_inventory.quit_the_details()