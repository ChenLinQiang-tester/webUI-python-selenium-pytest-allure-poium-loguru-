import allure
import pytest

from cases.case_enterprise.config_ep import RunConfigEp
from page.page_pf.page_media import PageMedia


@allure.feature('22-媒体审核')
class TestAuditMedia:
    @allure.title("043-媒体审核")
    @pytest.mark.run(order=7)
    @pytest.mark.dependency(depends=["platform_login", "up_media"], scope='session')
    def test_audit_media(self, browser_pf):
        page_audit_media = PageMedia(browser_pf)
        if len(page_audit_media.menus_media) == 0:
            page_audit_media.menu_message.click()
        page_audit_media.menu_media.click()
        page_audit_media.btn_audit(RunConfigEp.img_name).click()
        page_audit_media.btn_submit.click()
        assert page_audit_media.notice.text == "审核成功"
        assert page_audit_media.media_status(RunConfigEp.img_name).text == "通过"
