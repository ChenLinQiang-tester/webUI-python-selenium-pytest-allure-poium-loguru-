import allure
import pytest

# from cases.case_platform.config_pf import RunConfigPf
from page.page_pf.page_home import PageHome


@allure.feature("41-退出登录")
class TestLogout:
    @pytest.mark.dependency(depends=["platform_login"], scope='session')
    @allure.title("登出管理平台")
    def test_logout_pf(self, browser_pf):
        page_logout = PageHome(browser_pf)
        page_logout.user.click()
        page_logout.btn_logout.click()
        page_logout.btn_confirm_logout.click()
        # assert page_logout.get_url == RunConfigPf.pf_url
        assert page_logout.get_url == "https://test.fontdo.com/platform/?#/login"
        if len(page_logout.btn_login) == 0:
            assert False, "无登录按钮，页面出错"


if __name__ == '__main__':
    pytest.main(["-v", "-s", "-k", "019 or 041"])