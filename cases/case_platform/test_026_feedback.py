import allure
import pytest

from cases.case_enterprise.config_ep import RunConfigEp
from page.page_pf.page_feedback import PageFeedback


@allure.feature('26-管理工单')
class TestFeedback:
    @allure.title("049-回复工单")
    @pytest.mark.dependency(depends=["platform_login"], scope='session')
    def test_feedback(self, browser_pf):
        page_feedback = PageFeedback(browser_pf)
        if len(page_feedback.menus_feedback) == 0:
            page_feedback.menu_user.click()
        page_feedback.menu_feedback.click()
        page_feedback.feedback_title[0].click()
        page_feedback.ipt_0 = "回复工单"
        page_feedback.ipt_1 = "密码：123"
        page_feedback.ipt_image = RunConfigEp.img_path+'.png'
        page_feedback.btn_submit.click()
        assert page_feedback.notice.text == "回复成功"
        assert "回复工单" in page_feedback.last_reply.text
