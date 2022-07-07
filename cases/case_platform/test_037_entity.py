from time import sleep

import allure
import pytest

from selenium.webdriver.common.keys import Keys
from page.page_pf.page_sample_entity import PageSampleEntity


@allure.feature("37-行业模板实体")
class TestEntity:
    @pytest.mark.run(order=23)
    @allure.title("60-创建行业模板选项实体")
    @pytest.mark.dependency(depends=["platform_login", "category"], scope="session")
    def test_sample_option_entity(self, browser_pf):
        page_sample_option_entity = PageSampleEntity(browser_pf)
        if len(page_sample_option_entity.menus_entity) == 0:
            page_sample_option_entity.menu_sample.click()
        page_sample_option_entity.menus_entity[0].click()
        num = len(page_sample_option_entity.btn_sel)
        if num != 0:
            for i in range(num):
                page_sample_option_entity.btn_sel[0].click()
            page_sample_option_entity.btn_del.click()
            page_sample_option_entity.btn_ok.click()
        page_sample_option_entity.btn_option_entity.click()
        page_sample_option_entity.ipt_name = "option"
        page_sample_option_entity.sel_industry.click()
        page_sample_option_entity.sel_industry = Keys.ENTER
        page_sample_option_entity.sel_category.click()
        page_sample_option_entity.category.click()
        page_sample_option_entity.ipt_option = "张三\n李四\n王五"
        page_sample_option_entity.btn_submit.click()
        # assert page_sample_option_entity.notice.text == "创建成功"
        assert page_sample_option_entity.table_first_name.text == "option"
        assert page_sample_option_entity.table_first_type.text == "选项型"

    @pytest.mark.run(order=24)
    @allure.title("61-创建行业模板匹配实体")
    @pytest.mark.dependency(depends=["platform_login", "industry"], scope="session")
    def test_sample_match_entity(self, browser_pf):
        page_sample_match_entity = PageSampleEntity(browser_pf)
        if len(page_sample_match_entity.menus_entity) == 0:
            page_sample_match_entity.menu_sample.click()
        page_sample_match_entity.menus_entity[0].click()
        page_sample_match_entity.btn_match_entity.click()
        page_sample_match_entity.ipt_name = "match"
        page_sample_match_entity.sel_industry.click()
        page_sample_match_entity.sel_industry = Keys.ENTER
        page_sample_match_entity.sel_category.click()
        page_sample_match_entity.category.click()
        page_sample_match_entity.btn_add.click()
        page_sample_match_entity.ipt_match = r"1\d{10}"
        page_sample_match_entity.btn_submit.click()
        assert page_sample_match_entity.notice.text == "创建成功"
        assert page_sample_match_entity.table_first_name.text == "match"
        assert page_sample_match_entity.table_first_type.text == "匹配型"
