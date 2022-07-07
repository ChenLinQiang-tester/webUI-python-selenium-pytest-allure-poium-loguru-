from time import sleep

import allure
import pytest

from page.page_pf.page_robot import PageRobot


@allure.feature('24-机器人管理')
class TestRobot:
    @pytest.mark.run(order=18)
    @pytest.mark.dependency(name="audit_robot", depends=["platform_login", "robot"], scope='session')
    @allure.title("045-机器人审核")
    def test_audit_robot(self, browser_pf):
        page_audit_robot = PageRobot(browser_pf)
        if len(page_audit_robot.submenus_robot) == 0:
            page_audit_robot.menu_robot.click()
        page_audit_robot.submenu_robot.click()
        sleep(1)
        page_audit_robot.btn_audit[0].click()
        page_audit_robot.btn_submit.click()
        assert page_audit_robot.notice.text == "审核成功"
        assert page_audit_robot.audit_status[0].text == "审核通过"
