import allure
import pytest

from page.page_pf.page_template import PageTemplate


@allure.feature('21-模板审核')
class TestAuditTemplate:
    @pytest.mark.run(order=11)
    @allure.title('042-模板审核')
    @pytest.mark.dependency(depends=["platform_login", "template"], scope='session')
    def test_audit_template(self, browser_pf):
        page_audit_template = PageTemplate(browser_pf)
        if len(page_audit_template.menus_template) == 0:
            page_audit_template.menu_message.click()
        page_audit_template.menu_template.click()
        page_audit_template.btn_audit[0].click()
        page_audit_template.btn_submit.click()
        assert page_audit_template.notice.text == "审核成功"
        assert page_audit_template.audit_status[0].text == "通过"
