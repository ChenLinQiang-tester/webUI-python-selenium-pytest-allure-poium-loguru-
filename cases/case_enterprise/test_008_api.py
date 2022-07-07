import pytest
import allure
import datetime

from page.page_ep.page_api import PageApi
from time import sleep

t = str(datetime.datetime.now()).split('.')[0]


@allure.feature("08-API定义")
class TestApi:
    @allure.title("019-创建API定义")
    @pytest.mark.dependency(depends=["enterprise_login"], scope='session')
    def test_create_api(self, browser):
        page_create_api = PageApi(browser)
        if len(page_create_api.menus_api) == 0:
            page_create_api.menu_message.click()
        page_create_api.menu_api.click()
        page_create_api.btn_create_api.click()
        page_create_api.ipt_api_name = t + " 获取token"
        page_create_api.ipt_url = "https://test.fontdo.com/messenger/developer/v1/tokens"
        page_create_api.sel_method.click()
        page_create_api.post.click()
        page_create_api.sel_content_type.click()
        page_create_api.app_json.click()
        page_create_api.ipt_body = '{"appId": "bc615177-1638-43dd-ab42-a74c4a683ec5","appSecret": "5f1eabf8b21343a8af42f7ebf6364c7e"}'
        page_create_api.btn_add_output.click()
        page_create_api.ipt_outputs_key = "access_token"
        page_create_api.ipt_outputs_path = "access_token"
        page_create_api.sel_outputs_type.click()
        page_create_api.string.click()
        page_create_api.btn_submit.click()
        sleep(1)
        assert page_create_api.first_list.text == t + " 获取token"