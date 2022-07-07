import pytest
import allure
import datetime

from selenium.webdriver.common.keys import Keys
from page.page_ep.page_feedback import PageFeedback
from config_ep import RunConfigEp

t = str(datetime.datetime.now()).split('.')[0]


@allure.feature("13-工单")
class TestFeedback:
    @allure.title("032-提交工单")
    @pytest.mark.dependency(depends=["enterprise_login"], scope="session")
    def test_submit_feedback(self, browser):
        page_submit_feedback = PageFeedback(browser)
        if len(page_submit_feedback.menu_feedbacks) == 0:
            page_submit_feedback.menu_passport.click()
        page_submit_feedback.menu_feedback.click()
        page_submit_feedback.btn_feedback.click()
        page_submit_feedback.ipt_title = t + "单"
        page_submit_feedback.sel_type.click()
        page_submit_feedback.sel_type = Keys.ENTER
        page_submit_feedback.sel_degree.click()
        page_submit_feedback.sel_degree = Keys.ENTER
        page_submit_feedback.sel_scope.click()
        page_submit_feedback.sel_scope = Keys.ENTER
        page_submit_feedback.ipt_question = "怎么创建应用"
        page_submit_feedback.ipt_secret_information = "密码：123"
        page_submit_feedback.ipt_image = RunConfigEp.img_path+".png"
        page_submit_feedback.btn_submit.click()
        assert page_submit_feedback.success_notice.text == "提交成功"
        assert page_submit_feedback.first_feedback_title.text == t + "单"
