import allure
import pytest

from selenium.webdriver.common.keys import Keys
from page.page_pf.page_category import PageCategory


@allure.feature("35-行业类别")
class TestCategory:
    @pytest.mark.run(order=21)
    @allure.title("058-创建行业类别")
    @pytest.mark.dependency(name="category", depends=["platform_login", "industry"], scope='session')
    def test_create_category(self, browser_pf):
        page_category = PageCategory(browser_pf)
        if len(page_category.menus_industry) == 0:
            page_category.menu_sample.click()
        page_category.menus_industry[0].click()
        page_category.btn_create.click()
        page_category.ipt_name = "TestCategory"
        page_category.sel_industry.click()
        page_category.sel_industry = Keys.ENTER
        page_category.btn_submit.click()
        assert page_category.notice.text == "创建成功"
        assert page_category.category_name.text == "TestCategory"
