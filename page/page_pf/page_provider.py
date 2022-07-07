from poium import Page, Element, Elements


class PageProvider(Page):
    menu_config = Element(xpath='//div[@class="ant-menu-submenu-title"]/span[text()="配置管理"]', describe='配置管理')
    menus_provider = Elements(css='li[title="码号提供商"]', describe='判断码号提供商子菜单是否存在')
    # 前置
    TEST_del = Elements(xpath='//tbody/tr/td[text()="TESTc"]/../td[last()]//a[2]', describe="判断TEST提供商是否存在")
    btn_ok = Element(xpath='//button/span[text()="确 定"]', describe="确认按钮")
    # 执行
    btn_create = Element(xpath='//button[text()="创建"]', describe="创建按钮")
    ipt_code = Element(id_='code', describe="提供商码号输入框")
    ipt_providerId = Element(id_='providerId', describe="提供商账号输入框")
    ipt_providerName = Element(id_='providerName', describe="提供商名称输入框")
    sel_cspId = Element(id_='cspId', describe="归属CSP选择框")
    sel_type = Element(id_='type', describe="提供商类型")
    sel_status = Element(xpath='//div[@class="ant-drawer-body"]//input[@id="status"]', describe="状态")
    btn_submit = Element(xpath='//button[text()="提交"]', describe="提交按钮")
    # 验证
    notice = Element(xpath='//div[@class="ant-message-notice-content"]/div/span[2]', describe='提示')
