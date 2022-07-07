from poium import Element, Page, Elements


class PageApplication(Page):
    menu_message = Element(xpath='//div[@class="ant-menu-submenu-title"]/span[text()="消息平台"]', describe='消息平台')
    menus_app = Elements(css='li[title="应用管理"]',  describe='判断应用管理菜单是否存在')
    menu_app = Element(css='li[title="应用管理"]',  describe='应用管理')
    btn_confirm = Element(css='button[class="ant-btn ant-btn-primary"]', describe='通过审核确认按钮')
    binding_channel = Element(xpath='//div[text()="绑定通道"]', describe="绑定通道选项")
    channel_type = Element(id_='channelId', describe='选择通道类型')
    ipt_chatbotId = Element(id_='serviceCode', describe="chatbotId输入框")
    ipt_appId = Element(id_='appId', describe="appId输入框")
    ipt_token = Element(id_='token', describe="token输入框")
    btn_submit = Elements(css='button[class="ant-btn ant-btn-primary"]', describe="确定通道配置")
    # 验证
    channel = Element(xpath='//input[@id="channelId"]/../following-sibling::*[1]', describe="验证通道")
    notice = Element(xpath='//div[@class="ant-message-notice-content"]/div/span[2]', describe='审核提示')

    def btn_audit(self, name):
        return Element(xpath='//td[text()="'+name+'"]/following-sibling::*[last()]//span[@aria-label="file-search"]',
                       describe=name+'应用审核')

    def audit_status(self, name):
        return Element(xpath='//td[text()="'+name+'"]/following-sibling::*[2]/span', describe="审核成功状态：新增-通过")

    def set_channel(self, name):
        return Element(xpath='//td[text()="'+name+'"]/following-sibling::*[4]/a', describe="设置通道")

    def channel_name(self, name):
        return Element(xpath='//td[text()="'+name+'"]/following-sibling::*[4]/span[2]/span', describe="已设置的通道名称")