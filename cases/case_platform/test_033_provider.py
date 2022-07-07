import allure
import pytest

from selenium.webdriver.common.keys import Keys
from page.page_pf.page_provider import PageProvider


@allure.feature("33-码号提供商")
class TestProvider:
    @allure.title("056-创建码号提供商")
    @pytest.mark.dependency(depends=["platform_login"], scope='session')
    def test_create_provider(self, browser_pf):
        page_provider = PageProvider(browser_pf)
        if len(page_provider.menus_provider) == 0:
            page_provider.menu_config.click()
        page_provider.menus_provider[0].click()
        if len(page_provider.TEST_del) != 0:
            page_provider.TEST_del[0].click()
            page_provider.btn_ok.click()
        page_provider.btn_create.click()
        page_provider.ipt_code = '777'
        page_provider.ipt_providerId = '888'
        page_provider.ipt_providerName = "TESTc"
        page_provider.sel_cspId.click()
        page_provider.sel_cspId = Keys.ENTER
        page_provider.sel_type.click()
        page_provider.sel_type = Keys.ENTER
        page_provider.sel_status.click()
        page_provider.sel_status = Keys.ENTER
        page_provider.btn_submit.click()
        assert page_provider.notice.text == "创建成功"
        assert len(page_provider.TEST_del) == 1
