from poium import Element, Page, Elements


class PageMedia(Page):
    menu_message = Element(xpath='//div[@class="ant-menu-submenu-title"]/span[text()="消息平台"]', describe='消息平台')
    menus_media = Elements(css='li[title="媒体审核"]', describe='判断媒体审核菜单是否存在')
    menu_media = Element(css='li[title="媒体审核"]', describe='媒体审核菜单')
    btn_submit = Element(css='button[class="ant-btn ant-btn-primary"]', describe="审核提交按钮")
    notice = Element(xpath='//div[@class="ant-message-notice-content"]/div/span[2]', describe='审核成功提示')

    def media_status(self, name):
        return Element(xpath='//span[text()="'+name+'.png"]/../../following-sibling::*[4]/span', describe="媒体审核状态")

    def btn_audit(self, name):
        return Element(xpath='//span[text()="'+name+'.png"]/../../following-sibling::*[last()]//span[@aria-label="file-search"]', describe="审核按钮")