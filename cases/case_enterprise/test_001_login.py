"""
@author:chen
@data:2021-7-29
"""
from time import sleep

import allure
import pytest
from selenium.webdriver import Keys

from cases.case_enterprise.config_ep import RunConfigEp
from config import RunConfig
from page.page_ep.page_login import PageEnterpriseLogin
from configparser import ConfigParser

from utils.ocrUtils.get_code import get_code

conf = ConfigParser()
conf.read(RunConfig.base_path+'/data/pytest.ini')


@allure.feature('01-登录')
class TestEnterPrise:
    """登录企业平台"""
    @pytest.mark.run(order=1)
    @allure.title('001-登录企业平台')
    @pytest.mark.dependency(name='enterprise_login', scope='session')
    def test_enterprise_login(self, browser, base_url):
        page_ep_login = PageEnterpriseLogin(browser)
        page_ep_login.get(base_url)

        def accout():
            page_ep_login.username = conf["user"]["username"]
            page_ep_login.password = conf["user"]["password"]
        with allure.step("step2：输入密码"):
        page_ep_login.agreement.click()
        while True:
            while True:
                code_url = page_ep_login.number_img.get_attribute("src")
                code = get_code(code_url)
                if len(code) == 6 and code.isdigit():
                    break
                page_ep_login.reflush_code.click()
            page_ep_login.number = Keys.CONTROL, 'a'
            page_ep_login.number = code
            page_ep_login.login_btn.click()
            sleep(1)
            if len(page_ep_login.error_tips) != 0:
                if page_ep_login.error_tip.text != "图形验证码输入有误，请重新输入":
                    # assert False, page_ep_login.error_tip.text
                    print(page_ep_login.error_tip.text)
                    break
            if page_ep_login.get_url == RunConfigEp.login_success_url:
                break
        page_ep_login.know.click()
        assert page_ep_login.email.text == conf["user"]["username"]
        balance = page_ep_login.balance[0].text.replace(",", "")+page_ep_login.balance[1].text
        conf.set("Balance", "balance", balance)
        conf.write(open(RunConfig.base_path+'/data/pytest.ini', 'r+'))


if __name__ == '__main__':
    pytest.main(["-s", "test_001_login.py"])