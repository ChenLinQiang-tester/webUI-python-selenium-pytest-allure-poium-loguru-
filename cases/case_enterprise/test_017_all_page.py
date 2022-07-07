from time import sleep

import allure
import pytest

from page.page_ep.page_all_menu import PageAllMenu

data = [(0, 0, 99),
        (1, 0, 99), (1, 1, 99), (1, 2, 99), (1, 3, 99), (1, 4, 99), (1, 5, 99), (1, 6, 99), (1, 7, 99), (1, 8, 0), (1, 8, 1), (1, 9, 99), (1, 10, 99), (1, 11, 2), (1, 11, 3), (1, 12, 99), (1, 13, 99),
        (2, 0, 99), (2, 1, 99), (2, 2, 99), (2, 3, 99), (2, 4, 99),
        (3, 0, 99), (3, 1, 99), (3, 2, 99), (3, 3, 99), (3, 4, 99),
        (4, 0, 99), (4, 1, 99), (4, 2, 99), (4, 3, 99), (4, 4, 99), (4, 5, 99), (4, 6, 99), (4, 7, 99), (4, 8, 99), (4, 9, 99),
        (5, 0, 99), (5, 1, 99)]


@allure.feature("17-检查功能页面")
class TestAllPage:
    def public_case(self, driver, n, m, o):
        all_page = PageAllMenu(driver)
        menu = all_page.menus[n]
        if n != 0:
            if all_page.menu_expand[n].get_attribute("aria-expanded") == "false":
                # all_page.menus[n-1].click()
                # sleep(1)
                # menu.click()
                menu.click()
                sleep(1)
                all_page.submenus[-1].click()
                sleep(1)
            submenu = all_page.submenus[m]
            submenu.click()
            if o != 99:
                submenu3 = all_page.submenus3[o]
                submenu3.click()
                assert submenu3.get_attribute("title") in all_page.submenus_path_name.text or all_page.submenus_path_name.text[:3] in submenu3.get_attribute("title")
                if len(all_page.page_notice) != 0:
                    assert False, all_page.page_notice[0].text
            else:
                assert submenu.get_attribute("title") in all_page.submenus_path_name.text or all_page.submenus_path_name.text[:3] in submenu.get_attribute("title")
                if len(all_page.page_notice) != 0:
                    assert False, all_page.page_notice[0].text
        else:
            menu.click()
            if len(all_page.page_notice) != 0:
                assert False, all_page.page_notice[0].text

    @pytest.mark.dependency(depends=["enterprise_login"], scope='session')
    @pytest.mark.parametrize("n,m,o", data)
    @allure.title("038-检查所有功能页面")
    def test_menu(self, browser, last_result, n, m, o):
        if last_result != "passed":
            sleep(2)
        self.public_case(browser, n, m, o)


if __name__ == '__main__':
    pytest.main(["-v", "-s", "-k", "001 or 017"])