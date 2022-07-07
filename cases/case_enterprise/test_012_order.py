import pytest
import allure

from page.page_ep.page_order import PageOrder


@allure.feature("12-我的订单")
class TestOrder:
    @allure.title("029-订单使用明细")
    @pytest.mark.dependency(depends=["enterprise_login"], scope='session')
    def test_order_use_detail(self, browser):
        page_order_use_detail = PageOrder(browser)
        if len(page_order_use_detail.menu_orders) == 0:
            page_order_use_detail.menu_passport.click()
        page_order_use_detail.menu_order.click()
        if len(page_order_use_detail.empty_order) == 0:
            pytest.skip("列表无订单，跳过用例")
        if len(page_order_use_detail.btn_detail) == 0:
            pytest.skip("列表无订单可查看使用详情")
        product_name = page_order_use_detail.product_name[0].text
        page_order_use_detail.btn_detail[0].click()
        assert page_order_use_detail.detail_product_name.text == product_name

    @pytest.mark.run(order=33)
    @allure.title("030-订单申请退款")
    @pytest.mark.dependency(name="refund", depends=["enterprise_login", "test_order"], scope='session')
    def test_order_apply_refund(self, browser):
        # if last_result == 'skipped':
        #     pytest.skip("列表无订单，跳过用例")
        page_order_apply_refund = PageOrder(browser)
        if len(page_order_apply_refund.menu_orders) == 0:
            page_order_apply_refund.menu_passport.click()
        page_order_apply_refund.menu_order.click()
        if len(page_order_apply_refund.btn_refund) == 0:
            pytest.skip("列表无订单可退款")
        page_order_apply_refund.btn_refund[0].click()
        page_order_apply_refund.ipt_refund = '我想退款'
        page_order_apply_refund.btn_confirm_refund.click()
        assert page_order_apply_refund.success_prompt.text == '退款申请已提交。 管理员将在1-3个工作日内对其进行审核。 请耐心等待。'
        # sleep()
        assert page_order_apply_refund.order_status.text == '退款中'

    @allure.title("031-订单重新购买")
    @pytest.mark.dependency(depends=["enterprise_login"], scope='session')
    def test_order_buy_again(self, browser):
        # if last_result == 'skipped':
        #     pytest.skip("列表无订单，跳过用例")
        page_order_buy_again = PageOrder(browser)
        if len(page_order_buy_again.menu_orders) == 0:
            page_order_buy_again.menu_passport.click()
        page_order_buy_again.menu_order.click()
        product_name = page_order_buy_again.product_name_0.text
        page_order_buy_again.btn_reBuy.click()
        if len(page_order_buy_again.product_name_reBuy) != 0:
            assert page_order_buy_again.product_name_reBuy[0].text == product_name
        else:
            assert page_order_buy_again.product_sold_out.text == "此商品已下架"

