from time import sleep

import allure
import pytest
from selenium.webdriver.common.keys import Keys

from page.page_pf.page_sample_intent import PageSampleIntent


@allure.feature("38-行业模板意图")
class TestSampleIntent:
    @pytest.mark.run(order=25)
    @allure.title("62-创建行业模板问答意图")
    @pytest.mark.dependency(depends=["platform_login", "category"], scope="session")
    def test_sample_qa_intent(self, browser_pf):
        page_sample_qa_intent = PageSampleIntent(browser_pf)
        if len(page_sample_qa_intent.menus_intent) == 0:
            page_sample_qa_intent.menu_sample.click()
        page_sample_qa_intent.menus_intent[0].click()
        num = len(page_sample_qa_intent.btn_sel)
        if num != 0:
            for i in range(num):
                page_sample_qa_intent.btn_sel[0].click()
            page_sample_qa_intent.btn_del.click()
            page_sample_qa_intent.btn_ok.click()
        page_sample_qa_intent.btn_qa_intent.click()
        page_sample_qa_intent.ipt_name = "问答意图"
        page_sample_qa_intent.sel_industry.click()
        page_sample_qa_intent.sel_industry = Keys.ENTER
        page_sample_qa_intent.sel_category.click()
        page_sample_qa_intent.category.click()
        page_sample_qa_intent.btn_add_corpus.click()
        page_sample_qa_intent.ipt_corpus = "问答"
        page_sample_qa_intent.btn_add_answer.click()
        page_sample_qa_intent.ipt_answer = "这是一个模板问答意图"
        page_sample_qa_intent.btn_submit.click()
        print(len(page_sample_qa_intent.btn_sel))
        assert page_sample_qa_intent.notice.text == "创建成功"
        assert page_sample_qa_intent.table_first_name.text == "问答意图"
        assert page_sample_qa_intent.table_first_type.text == "问答型"

    @pytest.mark.run(order=26)
    @allure.title("63-创建行业模板任务意图")
    @pytest.mark.dependency(depends=["platform_login", "industry"], scope="session")
    def test_sample_tk_intent(self, browser_pf):
        page_sample_tk_intent = PageSampleIntent(browser_pf)
        if len(page_sample_tk_intent.menus_intent) == 0:
            page_sample_tk_intent.menu_sample.click()
        page_sample_tk_intent.menus_intent[0].click()
        page_sample_tk_intent.btn_task_intent.click()
        page_sample_tk_intent.ipt_name = "任务意图"
        page_sample_tk_intent.sel_industry.click()
        page_sample_tk_intent.sel_industry = Keys.ENTER
        page_sample_tk_intent.sel_category.click()
        page_sample_tk_intent.category.click()
        page_sample_tk_intent.btn_add_corpus.click()
        page_sample_tk_intent.ipt_corpus = "任务"
        page_sample_tk_intent.ipt_function = 'MESSENGER.send("这是一个任务意图")'
        page_sample_tk_intent.btn_submit.click()
        assert page_sample_tk_intent.notice.text == "创建成功"
        assert page_sample_tk_intent.table_first_name.text == "任务意图"
        assert page_sample_tk_intent.table_first_type.text == "任务型"
