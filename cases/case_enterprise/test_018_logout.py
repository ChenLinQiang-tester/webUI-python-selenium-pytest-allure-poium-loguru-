import allure
import pytest

from cases.case_enterprise.config_ep import RunConfigEp
from page.page_ep.page_home import PageHome


@allure.feature("18-退出登录")
class TestLogout:
    @pytest.mark.dependency(depends=["enterprise_login"], scope='session')
    @allure.title("039-退出登录")
    def test_logout(self, browser):
        page_logout = PageHome(browser)
        page_logout.user.click()
        page_logout.btn_logout.click()
        page_logout.btn_confirm_logout.click()
        assert page_logout.get_url == RunConfigEp.ep_url
        if len(page_logout.btn_login) == 0:
            assert False, "无登录按钮，页面出错"


if __name__ == '__main__':
    pytest.main(["-v", "-s", "-k", "001 or 018"])