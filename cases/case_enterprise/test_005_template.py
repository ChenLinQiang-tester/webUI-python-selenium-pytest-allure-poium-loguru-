import allure
import pytest
import datetime

from time import sleep
from selenium.webdriver.common.keys import Keys
from page.page_ep.page_message import PageMessage

t = str(datetime.datetime.now()).split('.')[0]


@allure.feature("05-消息模板")
class TestTemplate:
    # 公共步骤
    def public_step(self, driver, mode_name):
        driver = PageMessage(driver)
        if len(driver.menus_template) == 0:
            driver.menu_message.click()
        driver.menu_template.click()
        driver.create_message.click()
        driver.ipt_contentType.click()
        driver.sel_contentType.click()
        driver.ipt_app.click()
        driver.ipt_app = Keys.ENTER
        driver.ipt_modeName = mode_name
        driver.btn_make.click()

    @allure.title("005-创建文本模板")
    @pytest.mark.dependency(depends=["enterprise_login"], scope='session')
    def test_mk_text_message(self, browser):
        mk_text_message = PageMessage(browser)
        self.public_step(browser, t + ' 文本')
        mk_text_message.btn_text.click()
        mk_text_message.ipt_text = t
        mk_text_message.btn_yes.click()
        mk_text_message.btn_submit.click()
        sleep(1)
        assert mk_text_message.success_notice.text == "创建成功"
        assert mk_text_message.first_mode.text == t + ' 文本'

    @allure.title("006-创建图片模板")
    @pytest.mark.dependency(depends=["enterprise_login"], scope="session")
    def test_mk_img_message(self, browser):
        mk_img_message = PageMessage(browser)
        self.public_step(browser, t + '图片')
        mk_img_message.btn_picture.click()
        mk_img_message.display_picture.click()
        sleep(1)
        browser.find_element_by_xpath(mk_img_message.ipt_picture_xpath).send_keys(Keys.CONTROL, 'a')
        mk_img_message.ipt_picture.send_keys('https://oss.fontdo.com/66562870577464289.jpg')
        mk_img_message.btn_yes.click()
        mk_img_message.btn_submit.click()
        sleep(1)
        assert mk_img_message.success_notice.text == "创建成功"
        assert mk_img_message.first_mode.text == t + '图片'

    @allure.title("007-创建语音模板")
    @pytest.mark.dependency(depends=["enterprise_login"], scope="session")
    def test_mk_audio_message(self, browser):
        mk_audio_message = PageMessage(browser)
        self.public_step(browser, t + " 语音")
        mk_audio_message.btn_audio.click()
        mk_audio_message.display_audio.click()
        sleep(1)
        browser.find_element_by_xpath(mk_audio_message.ipt_audio_xpath).send_keys(Keys.CONTROL, 'a')
        mk_audio_message.ipt_audio.send_keys("https://oss.fontdo.com/66562870577464291.mp3")
        mk_audio_message.btn_yes.click()
        mk_audio_message.btn_submit.click()
        sleep(1)
        assert mk_audio_message.success_notice.text == "创建成功"
        assert mk_audio_message.first_mode.text == t+" 语音"

    @allure.title("008-创建视频模板")
    @pytest.mark.dependency(depends=['enterprise_login'], scope="session")
    def test_mk_video_message(self, browser):
        mk_video_message = PageMessage(browser)
        self.public_step(browser, t + " 视频")
        mk_video_message.btn_video.click()
        mk_video_message.btn_yes.click()
        mk_video_message.btn_submit.click()
        sleep(1)
        assert mk_video_message.success_notice.text == "创建成功"
        assert mk_video_message.first_mode.text == t+" 视频"

    @allure.title("009-创建卡片模板")
    @pytest.mark.run(order=10)
    # @pytest.mark.dependency(name="template", depends=['enterprise_login', "up_media"], scope="session")
    def test_mk_minus_square_message(self, browser):
        mk_minus_square_message = PageMessage(browser)
        self.public_step(browser, t + " 单卡片")
        mk_minus_square_message.btn_minus_square.click()
        # mk_minus_square_message.display_btn.click()
        # sleep(1)
        # mk_minus_square_message.btn_media.click()
        # mk_minus_square_message.imgs[0].click()
        # mk_minus_square_message.btn_use_img.click()
        # mk_minus_square_message.btn_media.click()
        # browser.find_element_by_xpath(mk_minus_square_message.ipt_square_img_xpath).send_keys(Keys.CONTROL, 'a')
        # mk_minus_square_message.ipt_square_img.send_keys("https://oss.fontdo.com/66562870577464289.jpg")
        mk_minus_square_message.ipt_square_title.send_keys("test1")
        mk_minus_square_message.ipt_square_describe.send_keys("test2")
        mk_minus_square_message.btn_square_memu.click()
        mk_minus_square_message.square_memu_reply.click()
        mk_minus_square_message.btn_yes.click()
        mk_minus_square_message.btn_submit.click()
        sleep(1)
        assert mk_minus_square_message.success_notice.text == "创建成功"
        assert mk_minus_square_message.first_mode.text == t+" 单卡片"

    @allure.title("010-创建卡片轮播图模板")
    @pytest.mark.dependency(depends=['enterprise_login'], scope="session")
    def test_mk_switcher_message(self, browser):
        mk_switcher_message = PageMessage(browser)
        self.public_step(browser, t + " 多卡片")
        mk_switcher_message.btn_switcher.click()
        mk_switcher_message.btn_add.click()
        mk_switcher_message.btn_yes.click()
        mk_switcher_message.btn_submit.click()
        sleep(1)
        assert mk_switcher_message.success_notice.text == "创建成功"
        assert mk_switcher_message.first_mode.text == t+" 多卡片"

    @allure.title('011-创建h5卡片模板')
    @pytest.mark.dependency(depends=['enterprise_login'], scope="session")
    def test_mk_h5_message(self, browser):
        mk_h5_message = PageMessage(browser)
        self.public_step(browser, t + " 单h5卡片")
        mk_h5_message.btn_h5.click()
        mk_h5_message.btn_yes.click()
        mk_h5_message.btn_submit.click()
        sleep(1)
        assert mk_h5_message.success_notice.text == "创建成功"
        assert mk_h5_message.first_mode.text == t+" 单h5卡片"

    @allure.title('012-创建h5卡片轮播图模板')
    @pytest.mark.dependency(depends=['enterprise_login'], scope="session")
    def test_mk_h5s_message(self, browser):
        mk_h5s_message = PageMessage(browser)
        self.public_step(browser, t + " 多h5卡片")
        mk_h5s_message.btn_h5s.click()
        mk_h5s_message.btn_add.click()
        mk_h5s_message.btn_yes.click()
        mk_h5s_message.btn_submit.click()
        sleep(1)
        assert mk_h5s_message.success_notice.text == "创建成功"
        assert mk_h5s_message.first_mode.text == t+" 多h5卡片"

    @allure.title('013-创建位置消息模板')
    @pytest.mark.dependency(depends=['enterprise_login'], scope='session')
    def test_mk_location_message(self, browser):
        mk_location_message = PageMessage(browser)
        self.public_step(browser, t + " 位置")
        mk_location_message.btn_location.click()
        mk_location_message.btn_change_location.click()
        mk_location_message.ipt_location.send_keys("万胜围")
        mk_location_message.ipt_location.click()
        mk_location_message.first_location.click()
        mk_location_message.btn_use_location.click()
        mk_location_message.btn_yes.click()
        mk_location_message.btn_submit.click()
        sleep(1)
        assert mk_location_message.success_notice.text == "创建成功"
        assert mk_location_message.first_mode.text == t+" 位置"

    @allure.title('014-创建浮动按钮消息模板')
    @pytest.mark.dependency(depends=['enterprise_login'], scope='session')
    def test_mk_float_menu(self, browser):
        mk_float_menu = PageMessage(browser)
        self.public_step(browser, t + " 浮动按钮")
        mk_float_menu.btn_text.click()
        mk_float_menu.btn_float_menu.click()
        mk_float_menu.btn_add_float_menu.click()
        mk_float_menu.sel_float_reply.click()
        mk_float_menu.btn_yes.click()
        mk_float_menu.btn_submit.click()
        sleep(1)
        assert mk_float_menu.success_notice.text == "创建成功"
        assert mk_float_menu.first_mode.text == t+" 浮动按钮"


if __name__ == '__main__':
    pytest.main(["-v", "-k", "001 or test_mk_minus_square_message"])