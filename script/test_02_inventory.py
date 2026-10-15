from script import log

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
        except AssertionError:
            log.error(f"断言错误：预期 Back to products 实际 {result}")
            raise

    def test_02_quit_the_details(self,page_inventory):

        page_inventory.check_the_details()

        result = page_inventory.quit_the_details()
        log.info(f"预期结果{result}")
        try:
            assert result == "Products"
        except AssertionError:
            log.error(f"断言错误: 预期 Products 实际 {result}")
            raise


    def test_03_add_shopping_cart(self,page_inventory):
        result = page_inventory.add_shopping_cart()
        log.info(f"预期结果{result}")
        page_inventory.base_assert("Remove",result)


    def test_04_remove_shopping_cart(self,page_inventory):
        page_inventory.add_shopping_cart()
        result = page_inventory.remove_shopping_cart()
        log.info(f"预期结果{result}")
        page_inventory.base_assert("Add to cart",result)


    def test_05_enter_shopping_cart(self,page_inventory):
        result = page_inventory.enter_shopping_cart()
        log.info(f"预期结果{result}")
        page_inventory.base_assert("Continue Shopping",result)


    def test_06_quit_shopping_cart(self,page_inventory):
        page_inventory.enter_shopping_cart()
        result = page_inventory.quit_shopping_cart()
        log.info(f"预期结果{result}")
        page_inventory.base_assert("Products",result)


    def test_07_sort_details(self,page_inventory):
        result = page_inventory.sort_details(index=1)
        log.info(f"预期结果{result}")
        page_inventory.base_assert("Name (Z to A)",result)