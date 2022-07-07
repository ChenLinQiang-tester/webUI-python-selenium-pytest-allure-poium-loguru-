import pytest
import allure

from page.page_ep.page_user import PageUser

data = [("运营", "13000000000", "1@qq.com", "Fontdo@test", 0, "033-创建运营人员"),
        ("开发", "14000000000", "2@qq.com", "Fontdo@test", 1, "034-创建开发人员"),
        ("财务", "15000000000", "3@qq.com", "Fontdo@test", 2, "035-创建财务人员")]


@allure.feature("14-成员管理")
class TestUser:
    @pytest.mark.dependency(depends=["enterprise_login"], scope='session')
    @pytest.mark.parametrize('name, phone, email, password, role, title', data)
    @allure.title("{title}")
    def test_create_user(self, browser, name, phone, email, password, role, title):
        page_create_user = PageUser(browser)
        if len(page_create_user.menus_user_manage) == 0:
            page_create_user.menu_passport.click()
        page_create_user.menu_user_manage.click()
        if role == 0 and len(page_create_user.sel_all_lists) != 0:
            page_create_user.sel_all_list.click()
            page_create_user.btn_delete.click()
            page_create_user.confirm_delete.click()
        page_create_user.btn_create.click()
        page_create_user.ipt_name = name
        page_create_user.ipt_phone = phone
        page_create_user.ipt_email = email
        page_create_user.ipt_password = password
        page_create_user.sel_roles.click()
        page_create_user.roles[role].click()
        page_create_user.btn_submit.click()


if __name__ == '__main__':
    pytest.main(["-v", "-s", "-k", "001 or 014"])