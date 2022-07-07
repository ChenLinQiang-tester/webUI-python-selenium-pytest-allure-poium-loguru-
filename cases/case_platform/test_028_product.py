import datetime
from time import sleep

import allure
import pytest
from selenium.webdriver.common.keys import Keys

from cases.case_enterprise.config_ep import RunConfigEp
from page.page_pf.page_product import PageProduct


t = str(datetime.datetime.now()).split('.')[0]


@allure.feature("28-产品管理")
class TestProduct:
    @pytest.mark.run(order=28)
    @allure.title("051-创建产品")
    @pytest.mark.dependency(depends=["platform_login"], scope='session')
    def test_product(self, browser_pf):
        page_product = PageProduct(browser_pf)
        if len(page_product.menus_product) == 0:
            page_product.menu_billing.click()
        page_product.menu_product.click()
        page_product.btn_create.click()
        page_product.sel_type.click()
        page_product.type.click()
        page_product.sel_subType.click()
        page_product.sel_subType = Keys.ENTER
        page_product.ipt_name = t + "能力"
        page_product.ipt_description = "能力调用套餐"
        page_product.ipt_image = RunConfigEp.img_path+".png"
        page_product.ipt_detail = "test product"
        page_product.btn_next[0].click()
        page_product.ipt_validDays = "1"
        page_product.ipt_validCount = "10"
        page_product.ipt_price = "10"
        page_product.btn_add_rule.click()
        page_product.btn_next[1].click()
        # page_product.ipt_availableEp = "测试企业"
        # page_product.ipt_availableEp = Keys.ENTER
        page_product.btn_submit.click()
        assert page_product.notice.text == "创建成功"
        assert page_product.product_name.text == t + "能力"
        page_product.btn_putaway.click()
        sleep(0.5)
        assert page_product.notice.text == "操作成功"
        assert page_product.product_status.text == "使用中"


if __name__ == '__main__':
    pytest.main(['-v', '-k', "019 or 028"])