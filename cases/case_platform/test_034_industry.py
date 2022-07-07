from time import sleep

import allure
import pytest

from page.page_pf.page_industry import PageIndustry


@allure.feature("34-行业模板")
class TestIndustry:
    @pytest.mark.run(order=20)
    @allure.title("057-创建行业模板")
    @pytest.mark.dependency(name="industry", depends=["platform_login"], scope='session')
    def test_create_industry(self, browser_pf):
        page_industry = PageIndustry(browser_pf)
        if len(page_industry.menus_industry) == 0:
            page_industry.menu_sample.click()
        page_industry.menus_industry[0].click()
        # if len(page_industry.TEST_del) != 0:
        sleep(1)
        for i in range(len(page_industry.TEST_del)):
            page_industry.TEST_del[i].click()
            page_industry.btn_ok.click()
            sleep(1)

        page_industry.btn_create.click()
        page_industry.ipt_name = "TestIndustry"
        page_industry.btn_submit.click()
        sleep(0.5)
        assert page_industry.notice.text == "创建成功"
        assert len(page_industry.TEST_del) == 1
