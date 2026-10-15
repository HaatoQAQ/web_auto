import pytest

from tools import read_json
from script import log


class TestCheckout:

    @pytest.mark.parametrize("first_name,last_name,phone", read_json("user_data.json"))
    def test_01_add_information(self,page_checkout,first_name,last_name,phone):
        page_checkout.add_information(first_name,last_name,phone)


    def test_02_submit_information(self,page_checkout):
        page_checkout.add_information("li","si","13000000001")
        result = page_checkout.submit_information()
        log.info(f"预期结果{result}")
        page_checkout.base_assert("Checkout: Overview",result)