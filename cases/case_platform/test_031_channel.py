import allure
import pytest

from selenium.webdriver.common.keys import Keys
from page.page_pf.page_channel import PageChannel


@allure.feature("31-通道配置")
class TestChannel:
    @allure.title("054-创建通道配置")
    @pytest.mark.dependency(depends=["platform_login"], scope='session')
    def test_channel(self, browser_pf):
        page_channel = PageChannel(browser_pf)
        if len(page_channel.menus_channel) == 0:
            page_channel.menu_config.click()
        page_channel.menu_channel.click()
        if len(page_channel.btn_del) != 0:
            page_channel.btn_del[0].click()
            page_channel.btn_ok.click()
        page_channel.btn_create.click()
        page_channel.ipt_id = "TESTC"
        page_channel.ipt_name = "测试通道"
        page_channel.sel_type.click()
        page_channel.sel_type = Keys.ENTER
        page_channel.ipt_msgServerUrl = "http://www.test.com"
        page_channel.btn_submit.click()
        assert page_channel.notice.text == "创建成功"
        assert page_channel.channel_id.text == "TESTC"
