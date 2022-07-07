import configparser

import pytest
import allure
import datetime

from page.page_ep.page_application import PageApplication
from config_ep import RunConfigEp
from config import RunConfig


def t():
    return str(datetime.datetime.now()).split('.')[0]


@allure.feature('02-应用')
class TestCreateChatbot:
    @pytest.mark.run(order=3)
    @pytest.mark.dependency(name="chatbot", depends=["enterprise_login"], scope='session')
    @allure.title('002-创建应用')
    def test_create_chatbot(self, browser):
        t_ = t()
        page_application = PageApplication(browser)
        if len(page_application.menu_applications) == 0:
            page_application.menu_message.click()
        page_application.menu_application.click()
        page_application.create_application.click()
        page_application.ipt_logo.send_keys(RunConfig.base_path+'/tool/code_file/'+RunConfigEp.img_name +".png")
        page_application.ipt_name = t_
        page_application.ipt_location.send_keys("广州")
        page_application.location.click()
        page_application.ipt_autograph.send_keys('test')
        page_application.ipt_industry.click()
        page_application.industry.click()
        page_application.ipt_phoneWhiteList.send_keys('1')
        page_application.ipt_descript.send_keys('2')
        page_application.btn_submit.click()
        assert page_application.success_text.text == '您的应用已提交审核！'
        page_application.btn_success_x.click()
        assert page_application.app_name.text == t_
        conf = configparser.ConfigParser()
        conf.read(RunConfig.base_path+'/data/pytest.ini')
        conf.set("app", "name", t_)
        conf.write(open(RunConfig.base_path + '/data/pytest.ini', 'r+'))


if __name__ == '__main__':
    pytest.main(["-v", "-s", "-k", "001 or test_002_create_chatbot.py"])