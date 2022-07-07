import allure
import pytest
from selenium.webdriver.common.keys import Keys

from page.page_pf.page_sample_template import PageSampleTemplate


@allure.feature("36-行业消息模板")
class TestSampleTemplate:
    @pytest.mark.run(order=22)
    @allure.title("059-创建行业消息模板")
    @pytest.mark.dependency(depends=["platform_login", "category"], scope="session")
    def test_sample_template(self, browser_pf):
        page_sample_template = PageSampleTemplate(browser_pf)
        if len(page_sample_template.menus_template) == 0:
            page_sample_template.menu_sample.click()
        page_sample_template.menus_template[0].click()
        page_sample_template.btn_create.click()
        page_sample_template.ipt_name = "TestTemplate"
        page_sample_template.sel_industry.click()
        page_sample_template.sel_industry = Keys.ENTER
        page_sample_template.sel_category.click()
        page_sample_template.category.click()
        page_sample_template.btn_maker.click()
        page_sample_template.btn_minus_square.click()
        page_sample_template.display_btn.click()
        page_sample_template.ipt_square_img.click()
        page_sample_template.ipt_square_img = Keys.CONTROL, "a"
        page_sample_template.ipt_square_img = "https://oss.fontdo.com/66562870577463576.png"
        page_sample_template.ipt_square_title = "title"
        page_sample_template.ipt_square_describe = "describe"
        page_sample_template.btn_square_memu.click()
        page_sample_template.square_memu_reply.click()
        page_sample_template.btn_ok.click()
        page_sample_template.btn_submit.click()
        assert page_sample_template.notice.text == "创建成功"
        assert page_sample_template.template_name.text == "TestTemplate"
