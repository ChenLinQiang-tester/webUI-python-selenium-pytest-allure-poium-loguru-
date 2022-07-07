from time import sleep

import allure
import pytest
import configparser

from selenium.webdriver.common.keys import Keys

from cases.case_enterprise.config_ep import RunConfigEp
from page.page_ep.page_password import PagePassword
from config import RunConfig
from page.page_ep.page_login import PageEnterpriseLogin
from tool.get_code import get_code
from selenium import webdriver


conf = configparser.ConfigParser()
conf.read(RunConfig.base_path+'/data/pytest.ini')
password = conf["user"]["password"]


@allure.feature("16-修改密码")
class TestPassword:
    @pytest.mark.dependency(depends=["enterprise_login"], scope='session')
    @allure.title("037-修改密码")
    def test_change_password(self, browser, base_url):
        page_change_password = PagePassword(browser)
        if len(page_change_password.menus_password) == 0:
            page_change_password.menu_passport.click()
        page_change_password.menu_password.click()
        page_change_password.ipt_old_password = password
        if password == "Fontdo@test":
            page_change_password.ipt_new_password = "Fontdo@test123"
            page_change_password.ipt_again_password = "Fontdo@test123"
            page_change_password.btn_submit.click()
            assert page_change_password.success_notice.text == "修改成功"
            conf.set("user", "password", "Fontdo@test123")
            conf.write(open(RunConfig.base_path+'/data/pytest.ini', 'r+'))
        else:
            page_change_password.ipt_new_password = "Fontdo@test"
            page_change_password.ipt_again_password = "Fontdo@test"
            page_change_password.btn_submit.click()
            assert page_change_password.success_notice.text == "修改成功"
            conf.set("user", "password", "Fontdo@test")
            conf.write(open(RunConfig.base_path + '/data/pytest.ini', 'r+'))
        # 登录验证
        if RunConfig.driver_type == 'chrome':
            # 本地Chrome浏览器
            driver = webdriver.Chrome()
            driver.maximize_window()
        elif RunConfig.driver_type == 'firefox':
            # 本地Firefox浏览器
            driver = webdriver.Firefox()
            driver.maximize_window()
        else:
            raise NameError("driver驱动类型定义错误")
        page_ep_login = PageEnterpriseLogin(driver)
        page_ep_login.get(base_url)
        page_ep_login.username = conf["user"]["username"]
        page_ep_login.password = conf["user"]["password"]
        while True:
            while True:
                code_url = page_ep_login.number_img.get_attribute("src")
                code = get_code(code_url)
                print(code)
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
            if page_ep_login.get_url == RunConfigEp.login_success_url:
                break
        page_ep_login.know.click()
        assert page_ep_login.email.text == 'chenlq@fontdo.com'
        driver.close()


if __name__ == '__main__':
    pytest.main(["-v", "-k", "001 or 016"])
