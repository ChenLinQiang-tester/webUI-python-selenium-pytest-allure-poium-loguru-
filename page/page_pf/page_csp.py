from poium import Page, Element, Elements


class PageCsp(Page):
    menu_config = Element(xpath='//div[@class="ant-menu-submenu-title"]/span[text()="配置管理"]', describe='配置管理')
    menus_csp = Elements(css='li[title="CSP 配置"]', describe='判断CSP配置子菜单是否存在')
    menu_csp = Element(css='li[title="CSP 配置"]', describe='CSP配置子菜单')
    btn_create = Element(xpath='//button[text()="创建"]', describe="创建按钮")
    ipt_name = Element(css='input[placeholder="在这里输入名称 ..."]', describe="名称输入框")
    ipt_account = Element(id_='account', describe="CSP编号输入框")
    ipt_appId = Element(id_='appId', describe="CSP账号输入框")
    ipt_secret = Element(id_='secret', describe="密码输入框")
    ipt_token = Element(id_='token', describe="令牌输入框")
    sel_region = Element(css='input[id="regionCode"]', describe="地区选择框")
    guangdong = Element(css='li[title="广东"]', describe="广东")
    guangzhou = Element(css='li[title="广州"]', describe="广州")
    sel_carrier = Element(id_='carrier', describe="运营商选择框")
    sel_status = Element(xpath='//div[@class="ant-drawer-body"]//input[@id="status"]', describe="状态选择框")
    ipt_serverRoot = Element(id_='serverRoot', describe="对接根地址输入框")
    ipt_version = Element(id_='version', describe="版本号输入框")
    ipt_domain = Element(id_='domain', describe="域名输入框")
    sel_channelId = Element(id_='channelId', describe="通道选择框")
    btn_submit = Element(xpath='//button[text()="提交"]', describe="提交按钮")
    # 验证
    notice = Element(xpath='//div[@class="ant-message-notice-content"]/div/span[2]', describe='提示')
    csp_name = Element(xpath='//tbody/tr[2]/td[2]', describe="数据表csp名称")
    TEST_del = Elements(xpath='//tbody/tr/td[text()="TESTC"]/../td[last()]//a[2]', describe="判断TESTC通道类型是否存在")
    btn_ok = Element(xpath='//button/span[text()="确 定"]', describe="确认按钮")



