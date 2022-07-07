from poium import Element, Page, Elements


class PageApplication(Page):
    menu_message = Element(xpath='//div[@class="ant-menu-submenu-title"]/span[text()="应用管理"]', describe='应用管理')
    menu_applications = Elements(xpath='//li//a[text()="我的应用"]', describe='判断我的应用菜单是否存在')
    menu_application = Element(xpath='//li//a[text()="我的应用"]', describe='我的应用菜单')
    create_application = Element(xpath='//*[text()="注册新应用" or text()="创建应用"]')
    ipt_logo = Element(css='input[accept="image/*"]')
    ipt_name = Element(css='#name')
    ipt_location = Element(id_='rc_select_0')
    location = Element(css='ul[class="ant-cascader-menu"]>li:nth-child(1)')
    ipt_autograph = Element(css='#autograph')
    ipt_industry = Element(css='#issueIndustry')
    industry = Element(css='div[title="民生"]')
    ipt_phoneWhiteList = Element(css='#phoneWhiteList')
    ipt_descript = Element(css='#description')
    btn_submit = Element(xpath='//button[text()="提交"]')
    btn_success_x = Element(css='button[aria-label="Close"]')
    success_text = Element(css='.ant-result-title')
    app_name = Element(css='tbody[class="ant-table-tbody"]>tr:nth-child(2)>td:nth-child(3)')