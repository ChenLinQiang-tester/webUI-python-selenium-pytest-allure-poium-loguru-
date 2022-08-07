import allure
import pytest

from page.login_page import LoginPage
from common.config import WebConfig


@allure.feature("登录")
class TestLogin:
    @allure.title("登录"+WebConfig.username)
    def test_login(self, browser):
        page = LoginPage(browser)
        with allure.step("打开首页"):
            page.open(WebConfig.url)
        with allure.step("点击打开登录页面"):
            page.login_a.click()
        with allure.step("输入用户名"):
            page.username_input = WebConfig.username
        with allure.step("输入密码"):
            page.password_input = WebConfig.password
        with allure.step("点击登录按钮"):
            page.login_span.click()
        with allure.step("断言主页顶部栏用户名"):
            assert page.username_span.text == WebConfig.username


if __name__ == '__main__':
    pytest.main(["-s", "test_login.py"])
