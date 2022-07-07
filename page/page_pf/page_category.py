from poium import Page, Element, Elements


class PageCategory(Page):
    menu_sample = Element(xpath='//div[@class="ant-menu-submenu-title"]/span[text()="行业模板"]', describe='行业模板菜单')
    menus_industry = Elements(css='li[title="类别（技能）"]', describe='判断类别（技能）子菜单是否存在')
    # 执行
    btn_create = Element(xpath='//button[text()="创建"]', describe="创建按钮")
    ipt_name = Element(id_='name', describe="名称输入框")
    sel_industry = Element(id_='applicationId', describe="行业选择框")
    btn_submit = Element(xpath='//button[text()="提交"]', describe="提交按钮")
    # 验证
    notice = Element(xpath='//div[@class="ant-message-notice-content"]/div/span[2]', describe='提示')
    category_name = Element(xpath='//tbody/tr[2]/td[2]', describe="类别名称")
