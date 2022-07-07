"""
@author:chen
@data:2021-7-29
"""
import allure
import pytest

from time import sleep
from selenium.webdriver.common.keys import Keys
from config import RunConfig
from page.page_pf.page_login import PageEnterpriseLogin
from tool.get_code import get_code
from config_pf import RunConfigPf
from configparser import ConfigParser

conf = ConfigParser()
conf.read(RunConfig.base_path+'/data/pytest.ini')


@allure.feature('19-登录管理平台')
class TestEnterPrise:
    """登录管理平台"""
    @pytest.mark.run(order=2)
    @allure.title('040-登录管理平台')
    @pytest.mark.dependency(name='platform_login', depends=["enterprise_login"], scope='session')
    def test_platform_login(self, browser_pf, base_url):
        page_ep_login = PageEnterpriseLogin(browser_pf)
        page_ep_login.get(base_url)
        page_ep_login.username = conf["root"]["username"]
        page_ep_login.password = conf["root"]["password"]
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
                if page_ep_login.error_tip.text != "图片验证码不正确。":
                    assert False, page_ep_login.error_tip.text
            if page_ep_login.get_url == RunConfigPf.login_success_url:
                break
        assert page_ep_login.email.text == conf["root"]["username"]


if __name__ == '__main__':
    pytest.main(["-v", "-s", "-k", "019"])