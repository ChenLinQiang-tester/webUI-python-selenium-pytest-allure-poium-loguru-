import pytest
import allure
import datetime

from selenium.webdriver.common.keys import Keys
from page.page_ep.page_template_robot import PageTemplateRobot
from page.page_ep.page_my_robot import PageMyRobot
from page.page_ep.page_robot_entity import PageRobotEntity
from page.page_ep.page_robot_intent import PageRobotIntent
from time import sleep

t = str(datetime.datetime.now()).split('.')[0]


@allure.feature("10-聊天机器人管理")
class TestRobot:
    @pytest.mark.run(order=27)
    @allure.title("021-从模板创建机器人")
    @pytest.mark.dependency(depends=["enterprise_login", "industry"], scope='session')
    def test_create_template_robot(self, browser):
        page_create_template_robot = PageTemplateRobot(browser)
        if len(page_create_template_robot.menu_template_robots) == 0:
            page_create_template_robot.menu_robot.click()
        page_create_template_robot.menu_template_robot.click()
        page_create_template_robot.first_template.click()
        robot_name = page_create_template_robot.first_template.text
        page_create_template_robot.btn_create.click()
        page_create_template_robot.btn_next_step.click()
        page_create_template_robot.btn_save.click()
        assert page_create_template_robot.success_prompt.text == "导入应用模板完成！"
        page_create_template_robot.menu_my_robot.click()
        list_robot_names = [i.text for i in page_create_template_robot.list_robot_name]
        # print(list_robot_names)
        assert robot_name in list_robot_names

    @pytest.mark.run(order=12)
    @allure.title("022-创建我的机器人")
    @pytest.mark.dependency(name="robot", depends=["chatbot"], scope='session')
    def test_create_my_robot(self, browser):
        page_create_my_robot = PageMyRobot(browser)
        if len(page_create_my_robot.menu_my_robots) == 0:
            page_create_my_robot.menu_robot.click()
        page_create_my_robot.menu_my_robot.click()
        page_create_my_robot.btn_create.click()
        page_create_my_robot.ipt_name = t + "机"
        page_create_my_robot.ipt_nickname = "小test"
        page_create_my_robot.ipt_describe = "autoTest"
        page_create_my_robot.sel_app.click()
        page_create_my_robot.sel_first.click()
        page_create_my_robot.btn_submit.click()
        assert page_create_my_robot.success_prompt.text == "创建成功"
        sleep(1)
        assert page_create_my_robot.first_robot_name.text == t + "机"

    @pytest.mark.run(order=13)
    @allure.title("023-创建机器人选项实体")
    @pytest.mark.dependency(depends=["robot"], scope='session')
    def test_robot_option_entity(self, browser):
        page_robot_option_entity = PageRobotEntity(browser)
        if len(page_robot_option_entity.menu_robot_entitys) == 0:
            page_robot_option_entity.menu_robot.click()
        page_robot_option_entity.menu_robot_entity.click()
        page_robot_option_entity.btn_option_entity.click()
        page_robot_option_entity.ipt_name = t + " option"
        page_robot_option_entity.sel_robot.click()
        page_robot_option_entity.sel_first.click()
        page_robot_option_entity.ipt_option = "张三\n李四\n王五"
        page_robot_option_entity.btn_submit.click()
        assert page_robot_option_entity.success_prompt.text == "创建成功"
        assert page_robot_option_entity.table_first_name.text == t + " option"
        assert page_robot_option_entity.table_first_type.text == "选项实体"

    @pytest.mark.run(order=14)
    @allure.title("024-创建机器人匹配实体")
    @pytest.mark.dependency(depends=["robot"], scope='session')
    def test_robot_match_entity(self, browser):
        page_robot_match_entity = PageRobotEntity(browser)
        if len(page_robot_match_entity.menu_robot_entitys) == 0:
            page_robot_match_entity.menu_robot.click()
        page_robot_match_entity.menu_robot_entity.click()
        page_robot_match_entity.btn_match_entity.click()
        page_robot_match_entity.ipt_name = t + " match"
        page_robot_match_entity.sel_robot.click()
        page_robot_match_entity.sel_first.click()
        page_robot_match_entity.ipt_match = r"1\d{10}"
        page_robot_match_entity.btn_submit.click()
        assert page_robot_match_entity.success_prompt.text == "创建成功"
        assert page_robot_match_entity.table_first_name.text == t + " match"
        assert page_robot_match_entity.table_first_type.text == "匹配实体"

    @pytest.mark.run(order=15)
    @allure.title("025-创建机器人问答意图")
    @pytest.mark.dependency(name="intent1", depends=["robot"], scope='session')
    def test_robot_qa_intent(self, browser):
        page_robot_qa_intent = PageRobotIntent(browser)
        if len(page_robot_qa_intent.menu_robot_intents) == 0:
            page_robot_qa_intent.menu_robot.click()
        page_robot_qa_intent.menu_robot_intent.click()
        page_robot_qa_intent.btn_qa_intent.click()
        page_robot_qa_intent.ipt_name = t + " 问答"
        page_robot_qa_intent.ipt_robot.click()
        page_robot_qa_intent.sel_first_robot.click()
        page_robot_qa_intent.btn_add_corpus.click()
        page_robot_qa_intent.ipt_corpus = "问答"
        page_robot_qa_intent.btn_add_answer.click()
        page_robot_qa_intent.ipt_answer = "这是一个问答意图"
        page_robot_qa_intent.btn_submit.click()
        # assert page_robot_qa_intent.notice.text == "创建成功"
        sleep(1)
        assert page_robot_qa_intent.table_first_name.text == t + " 问答"
        assert page_robot_qa_intent.table_first_type.text == "问答型"

    @pytest.mark.run(order=16)
    @allure.title("026-创建机器人任务意图-流程编排")
    @pytest.mark.dependency(name="intent2", depends=["robot"], scope='session')
    def test_robot_task1_intent(self, browser):
        page_robot_task1_intent = PageRobotIntent(browser)
        if len(page_robot_task1_intent.menu_robot_intents) == 0:
            page_robot_task1_intent.menu_robot.click()
        page_robot_task1_intent.menu_robot_intent.click()
        page_robot_task1_intent.btn_task_intent.click()
        page_robot_task1_intent.ipt_name = t + " 流程编排"
        page_robot_task1_intent.ipt_robot.click()
        page_robot_task1_intent.ipt_robot = Keys.ENTER
        page_robot_task1_intent.btn_add_corpus.click()
        page_robot_task1_intent.ipt_corpus = "流程编排"
        page_robot_task1_intent.btn_procedure.click()
        page_robot_task1_intent.add_node.click()
        page_robot_task1_intent.template_node.click()
        page_robot_task1_intent.sel_0_template.click()
        page_robot_task1_intent.sel_0_template = Keys.ENTER
        page_robot_task1_intent.btn_submit.click()
        # assert page_robot_task1_intent.notice.text == "创建成功"
        sleep(1)
        assert page_robot_task1_intent.table_first_name.text == t + " 流程编排"
        assert page_robot_task1_intent.table_first_type.text == "任务型"

    @pytest.mark.run(order=17)
    @allure.title("027-创建机器人任务意图-云函数")
    @pytest.mark.dependency(name="intent3", depends=["robot"], scope='session')
    def test_robot_task2_intent(self, browser):
        page_robot_task2_intent = PageRobotIntent(browser)
        if len(page_robot_task2_intent.menu_robot_intents) == 0:
            page_robot_task2_intent.menu_robot.click()
        page_robot_task2_intent.menu_robot_intent.click()
        page_robot_task2_intent.btn_task_intent.click()
        page_robot_task2_intent.ipt_name = t + " 云函数"
        page_robot_task2_intent.ipt_robot.click()
        page_robot_task2_intent.ipt_robot = Keys.ENTER
        page_robot_task2_intent.btn_add_corpus.click()
        page_robot_task2_intent.ipt_corpus = "云函数"
        page_robot_task2_intent.ipt_function = 'MESSENGER.send("这是一个云函数意图")'
        page_robot_task2_intent.btn_submit.click()
        # assert page_robot_task2_intent.notice.text == "创建成功"
        sleep(1)
        assert page_robot_task2_intent.table_first_name.text == t + " 云函数"
        assert page_robot_task2_intent.table_first_type.text == "任务型"
