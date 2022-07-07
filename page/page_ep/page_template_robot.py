from poium import Element, Page, Elements


class PageTemplateRobot(Page):
    menu_robot = Element(xpath='//div[@class="ant-menu-submenu-title"]/span[text()="聊天机器人"]', describe="聊天机器人菜单")
    menu_template_robot = Element(xpath='//li//a[text()="机器人模板"]', describe="机器人模板菜单")
    menu_template_robots = Elements(xpath='//li//a[text()="机器人模板"]', describe="判断机器人模板菜单是否存在")
    first_template = Element(xpath='//tbody/tr[1]/td[3]', describe="选择第一个机器人模板")
    btn_create = Element(xpath='//button[text()="从模板创建机器人"]', describe="创建模板机器人按钮")
    btn_next_step = Element(xpath='//button[text()="下一步"]', describe="下一步按钮")
    btn_save = Element(xpath='//button[text()="保存"]', describe='保存按钮')
    # 验证
    success_prompt = Element(xpath='//div[text()="导入应用模板完成！"]', describe='创建成功提示')
    menu_my_robot = Element(css='li[title="我的机器人"]', describe="我的机器人菜单")
    # first_robot_name = Element(xpath='//tbody/tr[2]/td[3]/a', describe='列表第一条机器人信息')
    list_robot_name = Elements(xpath='//tbody/tr/td[3]', describe="列表第一页所有机器人名称")