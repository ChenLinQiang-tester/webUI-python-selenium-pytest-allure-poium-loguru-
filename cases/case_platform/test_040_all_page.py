from time import sleep

import allure
import pytest

from page.page_pf.page_all_menu import PageAllMenu

data = [(0, 0,),
        (1, 0), (1, 1), (1, 2), (1, 3), (1, 4),
        (2, 0), (2, 1), (2, 2), (2, 3), (2, 4),
        (3, 0),
        (4, 0), (4, 1), (4, 2), (4, 3),
        (5, 0),
        (6, 0), (6, 1), (6, 2), (6, 3), (6, 4),
        (7, 0), (7, 1), (7, 2), (7, 3), (7, 4),
        (8, 0), (8, 1)]


@allure.feature("40-检查管理平台功能页面")
class TestAllPfPage:
    def public_case(self, driver, n, m):
        all_page = PageAllMenu(driver)
        menu = all_page.menus[n]
        if n != 0:
            if all_page.menu_expand[n].get_attribute("aria-expanded") == "false":
            #     # all_page.menus[n-1].click()
            #     # sleep(1)
            #     if len(all_page.else_expand) == 0:
                menu.click()
                sleep(1)
                all_page.submenus[-1].click()
                sleep(1)
            submenu = all_page.submenus[m]
            submenu.click()
            if n == 4 and m == 1:
                assert "计费商品" == all_page.submenus_path_name.text
            elif n == 7 and m == 1:
                assert "类目（服务、技能）" == all_page.submenus_path_name.text
            elif n == 2 and m == 3:
                assert "页面审核" in all_page.submenus_path_name.text
            else:
                assert submenu.get_attribute("title") in all_page.submenus_path_name.text or all_page.submenus_path_name.text[:3] in submenu.get_attribute("title")
            if len(all_page.page_notice) != 0:
                assert False, all_page.page_notice[0].text
        else:
            menu.click()
            if len(all_page.page_notice) != 0:
                assert False, all_page.page_notice[0].text

    @pytest.mark.dependency(depends=["platform_login"], scope='session')
    @pytest.mark.parametrize("n,m", data)
    @allure.title("检查所有功能页面")
    def test_pf_menu(self, browser_pf, last_result, n, m):
        if last_result != "passed":
            sleep(2)
        self.public_case(browser_pf, n, m)


if __name__ == '__main__':
    pytest.main(["-v", "-s", "-k", "019 or 040"])