import pytest
import allure
import datetime

from selenium.webdriver.common.keys import Keys
from page.page_ep.page_group_send import PageGroupSend

t = str(datetime.datetime.now()).split('.')[0]


@pytest.mark.run(order=12)
@allure.feature("07-群发助手")
class TestGroupSend:
    @pytest.mark.dependency(depends=["enterprise_login"], scope='session')
    @allure.title("018-模拟器通道群发")
    def test_group_send(self, browser):
        page_group_send = PageGroupSend(browser)
        if len(page_group_send.menu_group_sends) == 0:
            page_group_send.menu_message.click()
        page_group_send.menu_group_send.click()
        page_group_send.ipt_task_name = t + " 群发"
        page_group_send.ipt_chatbot.click()
        page_group_send.ipt_chatbot = Keys.ENTER
        page_group_send.ipt_channel.click()
        page_group_send.channel_PRIV.click()
        page_group_send.ipt_object = "13030303330 15050505550"
        page_group_send.template_message.click()
        page_group_send.sel_template.click()
        page_group_send.template.click()
        # page_group_send.sel_template = Keys.ENTER
        page_group_send.btn_submit.click()
        assert page_group_send.first_task.text == t + " 群发"
        assert page_group_send.task_state.text == "已完成"
