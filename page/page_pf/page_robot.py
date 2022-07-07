from poium import Element, Page, Elements


class PageRobot(Page):
    menu_robot = Element(xpath='//div[@class="ant-menu-submenu-title"]/span[text()="聊天机器人"]', describe='聊天机器人菜单')
    submenus_robot = Elements(css='li[title="机器人管理"]', describe='判断H5页面审核子菜单是否存在')
    submenu_robot = Element(css='li[title="机器人管理"]', describe='机器人管理子菜单')
    btn_audit = Elements(xpath='//tr/td[contains(text(),"机") and contains(text(),"-")]/../td[last()]//a[1]/span', describe="审核按钮")
    btn_submit = Element(css='button[class="ant-btn ant-btn-primary"]', describe="审核提交按钮")
    notice = Element(xpath='//div[@class="ant-message-notice-content"]/div/span[2]', describe='审核成功提示')
    audit_status = Elements(xpath='//tr/td[contains(text(),"机器人")]/../td[6]/span', describe="机器人审核状态")
