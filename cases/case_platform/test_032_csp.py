import datetime
import allure
import pytest

from selenium.webdriver.common.keys import Keys
from page.page_pf.page_csp import PageCsp

t = str(datetime.datetime.now()).split('.')[0]


@allure.feature("32-CSP配置")
class TestCsp:
    @allure.title("055-创建CSP配置")
    @pytest.mark.dependency(depends=["platform_login"], scope='session')
    def test_csp(self, browser_pf):
        page_csp = PageCsp(browser_pf)
        if len(page_csp.menus_csp) == 0:
            page_csp.menu_config.click()
        page_csp.menu_csp.click()
        if len(page_csp.TEST_del) != 0:
            page_csp.TEST_del[0].click()
            page_csp.btn_ok.click()
        page_csp.btn_create.click()
        page_csp.ipt_name = t+"CSP"
        page_csp.ipt_account = "4321"
        page_csp.ipt_appId = "1234"
        page_csp.ipt_secret = "1234"
        page_csp.ipt_token = "123"
        page_csp.execute_script('document.getElementsByClassName("ant-drawer-body")[0].scrollTop=800')
        page_csp.sel_region.click()
        page_csp.guangdong.click()
        page_csp.guangzhou.click()
        page_csp.sel_carrier.click()
        page_csp.sel_carrier = Keys.ENTER
        page_csp.sel_status.click()
        page_csp.sel_status = Keys.ENTER
        page_csp.ipt_serverRoot = "0"
        page_csp.ipt_version = "v1"
        page_csp.ipt_domain = "0"
        page_csp.sel_channelId.click()
        page_csp.sel_channelId = Keys.ENTER
        page_csp.btn_submit.click()
        assert page_csp.notice.text == "创建成功"
        assert page_csp.csp_name.text == t+"CSP"

