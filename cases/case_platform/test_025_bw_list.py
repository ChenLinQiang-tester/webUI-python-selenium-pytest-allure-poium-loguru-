import allure
import pytest
import datetime

from page.page_pf.page_access_list import PageAccessList
from time import sleep

t = str(datetime.datetime.now()).split(' ')[0]


@allure.feature("25-黑白名单管理")
class TestBlackWhiteList:
    @allure.title("046-开启创建黑名单")
    @pytest.mark.dependency(depends=["platform_login"], scope='session')
    def test_black_list(self, browser_pf):
        page_black_list = PageAccessList(browser_pf)
        if len(page_black_list.menu_bw_lists) == 0:
            page_black_list.menu_message.click()
        page_black_list.menu_bw_list.click()
        page_black_list.btn_black_on.click()
        if len(page_black_list.btn_yess) != 0:
            page_black_list.btn_yes.click()
        page_black_list.btn_create_black.click()
        page_black_list.ipt_black_list_name = t
        page_black_list.ipt_phone = "13030303330"
        page_black_list.btn_submit.click()
        sleep(1)
        assert page_black_list.first_list.text == t

    @allure.title("047-开启创建白名单")
    @pytest.mark.dependency(depends=["platform_login"], scope='session')
    def test_white_list(self, browser_pf):
        page_white_list = PageAccessList(browser_pf)
        if page_white_list.menu_bw_lists == 0:
            page_white_list.menu_message.click()
        page_white_list.menu_bw_list.click()
        page_white_list.btn_white_on.click()
        if len(page_white_list.btn_yess) != 0:
            page_white_list.btn_yes.click()
        page_white_list.btn_create_white.click()
        page_white_list.ipt_white_list_name = t
        page_white_list.ipt_phone = "13030303333"
        page_white_list.btn_submit.click()
        sleep(1)
        assert page_white_list.first_list.text == t

    @allure.title("048-不开启黑白名单")
    @pytest.mark.dependency(depends=["platform_login"], scope='session')
    def test_close_list(self, browser_pf):
        page_close_list = PageAccessList(browser_pf)
        if page_close_list.menu_bw_lists == 0:
            page_close_list.menu_message.click()
        page_close_list.menu_bw_list.click()
        page_close_list.btn_list_close.click()
        if len(page_close_list.btn_yess) != 0:
            page_close_list.btn_yes.click()
        assert page_close_list.close_list.text == "暂无数据"
