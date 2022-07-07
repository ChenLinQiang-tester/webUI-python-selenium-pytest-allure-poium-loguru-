from time import sleep

import allure
import pytest
from configparser import ConfigParser

from selenium.webdriver.common.keys import Keys
from page.page_pf.page_application import PageApplication
from config import RunConfig

conf = ConfigParser()


@allure.feature('20-应用管理')
class TestApplication:
    @pytest.mark.run(order=4)
    @allure.title('040-审核应用')
    @pytest.mark.dependency(depends=['platform_login', "chatbot"], scope='session')
    def test_audit_app(self, browser_pf):
        conf.read(RunConfig.base_path + '/data/pytest.ini')
        app_name = conf["app"]["name"]
        page_audit_app = PageApplication(browser_pf)
        if len(page_audit_app.menus_app) == 0:
            page_audit_app.menu_message.click()
        page_audit_app.menu_app.click()
        page_audit_app.btn_audit(app_name).click()
        page_audit_app.btn_confirm.click()
        sleep(1)
        # assert page_audit_app.notice.text == "审核成功"
        assert page_audit_app.audit_status(app_name).text == "新增-通过"

    @pytest.mark.run(order=5)
    @allure.title('041-配置应用通道')
    @pytest.mark.dependency(depends=['platform_login', "chatbot"], scope='session')
    def test_set_channel(self, browser_pf):
        conf.read(RunConfig.base_path + '/data/pytest.ini')
        app_name = conf["app"]["name"]
        page_set_channel = PageApplication(browser_pf)
        if len(page_set_channel.menus_app) == 0:
            page_set_channel.menu_message.click()
        page_set_channel.menu_app.click()
        page_set_channel.set_channel(app_name).click()
        page_set_channel.binding_channel.click()
        page_set_channel.channel_type.click()
        page_set_channel.channel_type = Keys.ENTER
        page_set_channel.ipt_chatbotId = app_name
        page_set_channel.ipt_appId = "123"
        page_set_channel.ipt_token = "123"
        channel = page_set_channel.channel.text
        page_set_channel.btn_submit[-1].click()
        sleep(1)
        # assert page_set_channel.notice.text == "配置成功"
        assert page_set_channel.channel_name(app_name).text == channel


if __name__ == '__main__':
    pytest.main(["-v", "-s", "-k", "019 or 020"])