from poium import Element, Page, Elements


class PageMyRobot(Page):
    menu_robot = Element(xpath='//div[@class="ant-menu-submenu-title"]/span[text()="聊天机器人"]', describe="聊天机器人菜单")
    menu_my_robot = Element(xpath='//li//a[text()="我的机器人"]', describe="我的机器人菜单")
    menu_my_robots = Elements(xpath='//li//a[text()="我的机器人"]', describe="判断我的机器人菜单是否存在")
    btn_create = Element(xpath='//button[text()="创建机器人"]', describe="创建机器人按钮")
    ipt_name = Element(css='input[placeholder="在这里填写机器人名称 ..."]', describe="机器人名称输入框")
    ipt_nickname = Element(css='input[placeholder="在这里填写昵称 ..."]', describe="机器人昵称输入框")
    ipt_describe = Element(css='textarea[placeholder="在这里填写描述 ..."]', describe="机器人描述输入框")
    sel_app = Element(css='span[class="ant-select-selection-search"]', describe="应用选择框")
    sel_first = Element(css='div[class="rc-virtual-list-holder-inner"]>div:nth-child(1)', describe="选择第一个应用")
    btn_submit = Element(css='button[type="submit"]', describe='提交按钮')
    # 验证
    success_prompt = Element(xpath='//span[text()="创建成功"]', describe='创建成功提示')
    first_robot_name = Element(xpath='//tbody/tr[2]/td[3]/a', describe='列表第一条机器人信息')

