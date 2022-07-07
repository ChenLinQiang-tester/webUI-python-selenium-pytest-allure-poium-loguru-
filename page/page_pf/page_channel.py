from poium import Page, Element, Elements


class PageChannel(Page):
    menu_config = Element(xpath='//div[@class="ant-menu-submenu-title"]/span[text()="配置管理"]', describe='配置管理')
    menus_channel = Elements(css='li[title="通道配置"]', describe='判断通道配置子菜单是否存在')
    menu_channel = Element(css='li[title="通道配置"]', describe='通道配置子菜单')
    btn_del = Elements(xpath='//tbody/tr/td[text()="TESTC"]/../td[last()]//a[2]', describe='删除按钮')
    btn_ok = Element(xpath='//button/span[text()="确 定"]', describe="确认按钮")
    btn_create = Element(xpath='//button[text()="创建"]', describe="创建按钮")
    ipt_id = Element(id_='id', describe="通道编码输入框")
    ipt_name = Element(css='input[placeholder="在这里输入名称 ..."]', describe="通道名称输入框")
    sel_type = Element(id_='channelType', describe="通道类型选择框")
    # ipt_version = Element(id_='version', describe="版本输入框")
    ipt_msgServerUrl = Element(id_='msgServerUrl', describe="消息服务器地址输入框")
    btn_submit = Element(xpath='//button[text()="提交"]', describe="提交按钮")
    notice = Element(xpath='//div[@class="ant-message-notice-content"]/div/span[2]', describe='提示')
    channel_id = Element(xpath='//tbody/tr[2]/td[2]', describe="通道编码")



