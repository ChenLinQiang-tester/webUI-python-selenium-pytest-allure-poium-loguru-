from time import sleep

import allure

from page.page_pf.page_notices import PageNotices


@allure.feature("39-系统通知")
class TestPfNotices:
    @allure.title("查看管理平台通知")
    def test_check_pf_notices(self, browser_pf):
        page_pf_notices = PageNotices(browser_pf)
        if len(page_pf_notices.menus_notices) == 0:
            page_pf_notices.menu_account.click()
        page_pf_notices.menus_notices[0].click()
        sleep(1)
        page_pf_notices.notice_1.click()
        assert len(page_pf_notices.notice_content) == 1
        assert page_pf_notices.notice_status.get_attribute("class") == "ant-badge-status-dot ant-badge-status-default"
