import pytest
import allure
import datetime

from page.page_ep.page_address_book import PageAddressBook
from time import sleep

t = str(datetime.datetime.now()).split('.')[0]


@allure.feature("09-通讯录")
class TestAddressBook:
    @allure.title("020-创建联系人")
    @pytest.mark.dependency(depends=["enterprise_login"], scope='session')
    def test_create_contacts(self, browser):
        page_create_contacts = PageAddressBook(browser)
        if len(page_create_contacts.menus_user) == 0:
            page_create_contacts.menu_message.click()
        page_create_contacts.menu_user.click()
        # page_create_contacts.menu_address_book.click()
        page_create_contacts.btn_create_contacts.click()
        page_create_contacts.ipt_name = t + " 张三"
        page_create_contacts.ipt_phone.send_keys("13030303330")
        page_create_contacts.btn_submit.click()
        sleep(1)
        assert page_create_contacts.first_list_name.text == t + " 张三"
        assert page_create_contacts.first_list_phone.text == "13030303330"


if __name__ == '__main__':
    pytest.main(["-v", "-k", "001 or 009"])
