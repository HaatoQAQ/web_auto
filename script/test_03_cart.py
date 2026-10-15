from script import log

class TestCart:

    def test_01_remove_things(self,page_cart):
        page_cart.remove_things()


    def test_02_checkout(self,page_cart):
        result = page_cart.checkout()
        log.info(f"预期结果{result}")
        page_cart.base_assert("Checkout: Your Information",result)

