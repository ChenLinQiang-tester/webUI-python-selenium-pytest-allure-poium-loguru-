import pytest
import allure
import datetime

from selenium.webdriver.common.keys import Keys
from page.page_ep.page_h5 import PageH5

t = str(datetime.datetime.now()).split('.')[0]


@allure.feature("04-H5页面")
class TestCreateH5:
    @pytest.mark.run(order=8)
    @allure.title("004-创建H5页面")
    # @pytest.mark.dependency(depends=["enterprise_login", "up_media"], scope='session')
    def test_create_h5(self, browser):
        create_h5 = PageH5(browser)
        if len(create_h5.menus_h5) == 0:
            create_h5.menu_message.click()
        create_h5.menu_h5.click()
        create_h5.create_h5.click()
        create_h5.ipt_app.click()
        create_h5.ipt_app = Keys.ENTER
        create_h5.ipt_title = t+' H5标题'
        create_h5.ipt_h5.send_keys('1234')
        create_h5.btn_media.click()
        create_h5.img.click()
        create_h5.btn_use_img.click()
        create_h5.btn_submit.click()
        assert create_h5.success_notice.text == '创建成功'
        assert create_h5.h5_title.get_attribute('title') == t+' H5标题'


if __name__ == '__main__':
    pytest.main(["-v", "-s", "-k", "debug or 004"])