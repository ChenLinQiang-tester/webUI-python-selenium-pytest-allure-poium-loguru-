from poium import Page, Element, Elements


class PageIndustry(Page):
    menu_sample = Element(xpath='//div[@class="ant-menu-submenu-title"]/span[text()="行业模板"]', describe='行业模板菜单')
    menus_industry = Elements(css='li[title="行业"]', describe='判断行业子菜单是否存在')
    # 前置
    TEST_del = Elements(xpath='//tbody/tr/td[text()="TestIndustry"]/../td[last()]//a[2]', describe="判断TEST提供商是否存在")
    btn_ok = Element(xpath='//button/span[text()="确 定"]', describe="确认按钮")
    # 执行
    btn_create = Element(xpath='//button[text()="创建"]', describe="创建按钮")
    ipt_name = Element(id_='name', describe="名称输入框")
    btn_submit = Element(xpath='//button[text()="提交"]', describe="提交按钮")
    # 验证
    notice = Element(xpath='//div[@class="ant-message-notice-content"]/div/span[2]', describe='提示')
