import datetime
import random
import allure
import pytest

from cases.case_enterprise.config_ep import RunConfigEp
from page.page_pf.page_agent_manage import PageAgentManage

t = str(datetime.datetime.now()).split('.')[0]


@allure.feature("30-代理商管理")
class TestAgent:
    @allure.title("052-创建个人代理商")
    @pytest.mark.dependency(depends=["platform_login"], scope='session')
    def test_agent_personal(self, browser_pf):
        page_agent_ps = PageAgentManage(browser_pf)
        if len(page_agent_ps.menus_agent_manage) == 0:
            page_agent_ps.menu_agent.click()
        page_agent_ps.menu_agent_manage.click()
        page_agent_ps.btn_create.click()
        page_agent_ps.ipt_name = t + "个人"
        phone = "1" + ''.join(str(i) for i in random.sample(range(0, 10), 10))
        page_agent_ps.ipt_phone = phone
        page_agent_ps.ipt_idNumber = "441522190011110000"
        page_agent_ps.ipt_images = RunConfigEp.img_path + ".png"
        page_agent_ps.ipt_address = "广州市"
        page_agent_ps.ipt_password1 = "Fontdo@agent"
        page_agent_ps.ipt_password2 = "Fontdo@agent"
        page_agent_ps.btn_submit.click()
        assert page_agent_ps.notice.text == "创建成功"
        assert page_agent_ps.agent_name.text == t + "个人"

    @allure.title("053-创建企业代理商")
    @pytest.mark.dependency(depends=["platform_login"], scope='session')
    def test_angent_enterprise(self, browser_pf):
        page_angent_ep = PageAgentManage(browser_pf)
        if len(page_angent_ep.menus_agent_manage) == 0:
            page_angent_ep.menu_agent.click()
        page_angent_ep.menu_agent_manage.click()
        page_angent_ep.btn_create.click()
        page_angent_ep.ipt_ep.click()
        page_angent_ep.ipt_name_ep = t
        page_angent_ep.ipt_idNumber_ep = "123456789123456789"
        page_angent_ep.ipt_images_ep = RunConfigEp.img_path + ".png"
        page_angent_ep.ipt_address_ep = "广州市"
        page_angent_ep.ipt_name = t + "企业"
        phone = "1" + ''.join(str(i) for i in random.sample(range(0, 10), 10))
        page_angent_ep.ipt_phone = phone
        page_angent_ep.ipt_idNumber = "441522190011100000"
        page_angent_ep.ipt_images = RunConfigEp.img_path + ".png"
        page_angent_ep.ipt_password1 = "Fontdo@agent"
        page_angent_ep.ipt_password2 = "Fontdo@agent"
        page_angent_ep.btn_submit.click()
        assert page_angent_ep.notice.text == "创建成功"
        assert page_angent_ep.agent_name.text == t + "企业"
