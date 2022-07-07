from configparser import ConfigParser
from time import sleep

import pytest
import allure

from selenium.webdriver.common.keys import Keys
from config import RunConfig
from page.page_ep.page_mall import PageMall


@allure.feature("11-商城")
class TestRobot:
    @pytest.mark.run(order=29)
    @allure.title("028-购买商品")
    @pytest.mark.dependency(depends=["enterprise_login"], name='buy_product', scope='session')
    def test_buy_product(self, browser):
        conf = ConfigParser()
        conf.read(RunConfig.base_path + '/data/pytest.ini')
        page_buy_product = PageMall(browser)
        if len(page_buy_product.menus_mall) == 0:
            page_buy_product.menu_passport.click()
        page_buy_product.menu_mall.click()
        page_buy_product.list_product_1[0].click()
        price = page_buy_product.price.text.replace("￥", "")
        page_buy_product.btn_buy.click()
        page_buy_product.ipt_name = "小测"
        page_buy_product.ipt_phone = "13030303330"
        page_buy_product.btn_submit.click()
        # 企业账户余额不足
        if len(page_buy_product.exception_prompt) != 0:
            sleep(0.5)
            if page_buy_product.exception_prompt[0].text == "企业账户余额不足":
                pytest.skip("企业账户余额不足")
            else:
                assert False, "异常提示"
        assert page_buy_product.success_prompt.text == "支付成功"
        page_buy_product.copy_order_id.click()
        page_buy_product.btn_confirm_order.click()
        page_buy_product.ipt_order_id = Keys.CONTROL, "v"
        assert page_buy_product.get_order_id.get_attribute("title") == page_buy_product.ipt_order_id1.get_attribute("value")
        page_buy_product.menu_home.click()
        balance = page_buy_product.balance[0].text.replace(",", "")+page_buy_product.balance[1].text
        assert str(float(balance)+float(price)) == conf["Balance"]["balance"]
        conf.set("Balance", "balance", balance)
        conf.set("Balance", "price", price)
        conf.write(open(RunConfig.base_path + '/data/pytest.ini', 'r+'))
