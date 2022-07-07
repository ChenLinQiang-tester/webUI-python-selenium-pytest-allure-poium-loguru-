import allure
import pytest

from page.page_ep.page_simulator import PageSimulator
from time import sleep


@allure.feature("15-模拟器")
class TestSimulator:
    @pytest.mark.run(order=19)
    @pytest.mark.dependency(depends=["audit_robot", "intent1", "intent2", "intent3"], scope="session")
    @allure.title("036-模拟器聊天")
    def test_simulator_chat(self, browser):
        page_simulator_chat = PageSimulator(browser)
        browser.refresh()
        page_simulator_chat.btn_simulator.click()
        iframe = browser.find_element_by_tag_name("iframe")
        page_simulator_chat.switch_to_frame(iframe)
        sleep(1)
        page_simulator_chat.sel_app[-1].click()
        page_simulator_chat.enter_chat.click()
        page_simulator_chat.ipt_chat = "问答"
        sleep(1)
        page_simulator_chat.btn_send.click()
        sleep(1)
        assert page_simulator_chat.message_content[2].text == "问答"
        assert page_simulator_chat.message_content[3].text == "这是一个问答意图"
        page_simulator_chat.ipt_chat = "云函数"
        page_simulator_chat.btn_send.click()
        sleep(1)
        assert page_simulator_chat.message_content[4].text == "云函数"
        assert page_simulator_chat.message_content[5].text == "这是一个云函数意图"
        page_simulator_chat.ipt_chat = "流程编排"
        page_simulator_chat.btn_send.click()
        sleep(1)
        assert page_simulator_chat.message_content[6].text == "流程编排"
        assert page_simulator_chat.message_content[7].get_attribute("class") == "card flexbox-v l"
        page_simulator_chat.switch_to_default_content()
        page_simulator_chat.btn_close.click()
