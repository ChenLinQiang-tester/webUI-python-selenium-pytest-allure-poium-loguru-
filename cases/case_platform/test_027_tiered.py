import allure
import pytest

from selenium.webdriver.common.keys import Keys
from page.page_pf.page_tiered import PageTiered


@allure.feature('27-阶梯计费')
class TestTiered:
    @allure.title("050-创建阶梯计费")
    @pytest.mark.dependency(depends=["platform_login"], scope='session')
    def test_tiered(self, browser_pf):
        page_tiered = PageTiered(browser_pf)
        if len(page_tiered.menus_tiered) == 0:
            page_tiered.menu_billing.click()
        page_tiered.menu_tiered.click()
        page_tiered.btn_create.click()
        page_tiered.sel_type.click()
        page_tiered.sel_type = Keys.ENTER
        # page_tiered.ipt_describe = "文本消息"
        page_tiered.btns_del[-1].click()
        page_tiered.btn_add_tiered.click()
        page_tiered.ipt_0 = "10"
        page_tiered.ipt_1 = "0.02"
        page_tiered.btn_submit.click()
        assert page_tiered.notice.text == "修改成功"
        assert "10" in page_tiered.success_text.text and "0.02" in page_tiered.success_text.text
