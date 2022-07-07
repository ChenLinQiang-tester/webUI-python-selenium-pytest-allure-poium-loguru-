import allure
import pytest

from page.page_pf.page_page import PagePage


@allure.feature('23-H5页面审核')
class TestAuditPage:
    @allure.title("044-H5页面审核")
    @pytest.mark.run(order=9)
    @pytest.mark.dependency(depends=["platform_login"], scope='session')
    def test_audit_page(self, browser_pf):
        page_audit_page = PagePage(browser_pf)
        if len(page_audit_page.menus_page) == 0:
            page_audit_page.menu_message.click()
        page_audit_page.menu_page.click()
        page_audit_page.btn_audit[0].click()
        page_audit_page.btn_submit.click()
        assert page_audit_page.notice.text == "审核成功"
        assert page_audit_page.audit_status[0].text == "通过"
