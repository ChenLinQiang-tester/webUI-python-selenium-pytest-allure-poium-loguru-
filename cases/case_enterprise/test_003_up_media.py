import pytest
import allure

from time import sleep
from page.page_ep.page_media import PageMedia
from config_ep import RunConfigEp


@allure.feature("03-媒体库")
class TestUpMedia:
    @pytest.mark.run(order=6)
    @allure.title("003-媒体库上传图片")
    @pytest.mark.dependency(depends=["enterprise_login"], name="up_media", scope='session')
    def test_up_media(self, browser):
        page_media = PageMedia(browser)
        if len(page_media.menu_medias) == 0:
            page_media.menu_message.click()
        page_media.menu_media.click()
        page_media.btn_up.click()
        page_media.ipt_up.send_keys(RunConfigEp.img_path +".png")
        page_media.btn_x.click()
        sleep(1)
        assert RunConfigEp.img_name+'.png' == page_media.file[0].text


if __name__ == '__main__':
    pytest.main(["-v", "-s", "ignore:Module already imported:pytest.PytestWarning", "-k", "001 or 003"])
