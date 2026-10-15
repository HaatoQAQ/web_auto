from script import log

class TestPay:

    def test_01_pay(self,page_pay):
        result = page_pay.pay()
        log.info(f"预期结果{result}")
        page_pay.base_assert("Thank you for your order!",result)

