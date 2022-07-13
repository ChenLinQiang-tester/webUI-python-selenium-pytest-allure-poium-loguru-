"""
@author:chen
@data:2021-7-29
"""
import allure
import pytest
from selenium.webdriver import Keys

from poium.common.logging import Logger
from config import RunConfig
from page.page_ep.page_login import PageEnterpriseLogin
from configparser import ConfigParser

from utils.ocrUtils.get_code import get_code

conf = ConfigParser()
conf.read(RunConfig.base_path+'/data/pytest.ini')
login_email = conf["user"]["username"]
login_password = conf["user"]["password"]


@allure.feature('01-登录')
class TestEnterPrise:
    """
    名称：登录企业平台
    步骤：
    1.输入账号
    2.输入密码
    3.勾选服务协议
    4.输入图形验证码并点击登录
    5.关闭登录提示
    6.后置-获取账号余额
    检查点：
    * 检查登录成功页面url是否正确。
    * 检查登录成功页面中邮箱元素文本是否正确。
    """
    @pytest.mark.run(order=1)
    @allure.title('001-登录企业平台')
    @pytest.mark.dependency(name='enterprise_login', scope='session')
    def test_enterprise_login(self, browser, base_url):
        page_ep_login = PageEnterpriseLogin(browser)
        page_ep_login.open(base_url)
        with allure.step("输入账号:{}".format(login_email)):
            page_ep_login.username = login_email
        with allure.step("输入密码:{}".format(login_password)):
            page_ep_login.password = login_password
        with allure.step("勾选服务协议"):
            page_ep_login.agreement.click()
        with allure.step("输入图形验证码并登录验证"):
            while True:
                while True:
                    code_url = page_ep_login.number_img.get_attribute("src")
                    code = get_code(code_url)
                    if len(code) == 6 and code.isdigit():
                        break
                    page_ep_login.reflush_code.click()
                page_ep_login.number = Keys.CONTROL, "a"
                page_ep_login.number = code
                page_ep_login.login_btn.click()
                notice = page_ep_login.notice.text
                if notice == "图形验证码输入有误，请重新输入":
                    continue
                elif notice == "登录成功！":
                    break
                else:
                    Logger().error(notice)
                    assert False, notice
        assert page_ep_login.get_url == "https://5g.fontdo.com/test/enterprise//#/"
        with allure.step("关闭登录提示"):
            page_ep_login.know.click()
        with allure.step("获取断言数据：邮箱账号"):
            email_text = page_ep_login.email.text
        assert email_text == conf["user"]["username"]
        with allure.step("设置缓存-账号余额"):
            self.balance = page_ep_login.balance[0].text.replace(",", "")+page_ep_login.balance[1].text
            conf.set("Balance", "balance", self.balance)
            conf.write(open(RunConfig.base_path+'/data/pytest.ini', 'r+'))


if __name__ == '__main__':
    pytest.main(["-s", "test_001_login.py"])
