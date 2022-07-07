from poium import Element, Page, Elements


class PageMedia(Page):
    menu_message = Element(xpath='//div[@class="ant-menu-submenu-title"]/span[text()="消息模板"]', describe='消息模板菜单')
    menu_medias = Elements(xpath='//li//a[text()="媒体库"]', describe='判断媒体库菜单是否存在')
    menu_media = Element(xpath='//li//a[text()="媒体库"]', describe='媒体库菜单')
    btn_up = Element(xpath='//button/span[text()="上传文件"]', describe='上传文件按钮')
    ipt_up = Element(css='input[type="file"]', describe="传入验证码图片")
    btn_x = Element(css='button[aria-label="Close"]', describe="关闭上传框按钮")
    file = Element(css='[class="ant-row"]>div:nth-child(1)>div>img', describe="验证媒体文件")
