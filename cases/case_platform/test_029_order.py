import datetime
from configparser import ConfigParser
from time import sleep

import allure
import pytest

from config import RunConfig
from page.page_pf.page_order import PageOrder

t = str(datetime.date.today()+datetime.timedelta(days=1))


@allure.feature("29-订单管理")
class TestBillingOrder:
    @pytest.mark.run(order=30)
    @allure.title("完成订单调测")
    @pytest.mark.dependency(name="test_order", depends=["platform_login", "buy_product"], scope='session')
    def test_order_test(self, browser_pf):
        page_order = PageOrder(browser_pf)
        if len(page_order.menus_order) == 0:
            page_order.menu_billing.click()
        page_order.menus_order[0].click()
        page_order.btn_test.click()
        page_order.btn_ok.click()
        assert page_order.notice.text == "操作完成，产品已激活使用。"
        assert page_order.order_state.text == "使用中"

    @pytest.mark.run(order=31)
    @allure.title("订单使用明细")
    @pytest.mark.dependency(depends=["platform_login", "test_order"], scope='session')
    def test_order_use(self, browser_pf):
        page_order = PageOrder(browser_pf)
        if len(page_order.menus_order) == 0:
            page_order.menu_billing.click()
        page_order.menus_order[0].click()
        page_order.btn_open.click()
        name = page_order.product_name.text
        count = page_order.residue_count.text
        page_order.use_detail.click()
        assert page_order.detail_product_name.text == name
        assert page_order.residue_count_b.text == count

    @pytest.mark.run(order=32)
    @allure.title("订单条数修改")
    @pytest.mark.dependency(depends=["platform_login", "test_order"], scope='session')
    def test_order_edit(self, browser_pf):
        page_order = PageOrder(browser_pf)
        if len(page_order.menus_order) == 0:
            page_order.menu_billing.click()
        page_order.menus_order[0].click()
        page_order.btn_test.click()
        validCount = page_order.validCount.get_attribute("value")
        page_order.ipt_count = "10"
        page_order.expireDate.click()
        page_order.tomorrow.click()
        page_order.btn_ok.click()
        assert page_order.notice.text == "修改成功"
        page_order.btn_test.click()
        assert page_order.validCount.get_attribute("value") == str(int(validCount)+10)
        assert t in page_order.expire.get_attribute("value")
        page_order.btn_no.click()

    @pytest.mark.run(order=34)
    @allure.title("订单退款审核")
    @pytest.mark.dependency(depends=["platform_login", "refund"], scope='session')
    def test_audit_refund(self, browser_pf):
        page_order = PageOrder(browser_pf)
        if len(page_order.menus_order) == 0:
            page_order.menu_billing.click()
        page_order.menus_order[0].click()
        page_order.audit_refund.click()
        page_order.ipt_refund = "同意退款"
        page_order.btn_ok.click()
        assert page_order.notice.text == "处理成功"
        assert page_order.order_state.text == "已退款"
        page_order.menu_passport.click()
        page_order.menu_enterprise.click()
        page_order.ipt_search = "chenlq@fontdo.com"
        sleep(1)
        conf = ConfigParser()
        conf.read(RunConfig.base_path + '/data/pytest.ini')
        assert str(float(page_order.balance.text)-float(conf["Balance"]["price"])) == conf["Balance"]["balance"]
        conf.set("Balance", "balance", page_order.balance.text)
        conf.write(open(RunConfig.base_path + '/data/pytest.ini', 'r+'))
