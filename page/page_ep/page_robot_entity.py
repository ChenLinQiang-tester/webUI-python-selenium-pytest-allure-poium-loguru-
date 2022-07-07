from poium import Element, Page, Elements


class PageRobotEntity(Page):
    menu_robot = Element(xpath='//div[@class="ant-menu-submenu-title"]/span[text()="聊天机器人"]', describe="聊天机器人菜单")
    menu_robot_entity = Element(xpath='//li//a[text()="我的实体"]', describe="实体菜单")
    menu_robot_entitys = Elements(xpath='//li//a[text()="我的实体"]', describe="判断实体菜单是否存在")
    # 选项实体
    btn_option_entity = Element(xpath='//button/span[text()="选项实体"]', describe="选项实体按钮")
    ipt_option = Element(css='textarea[placeholder="在这里填写选项"]', describe="可用选项输入框")
    # 匹配实体
    btn_match_entity = Element(xpath='//button/span[text()="匹配实体"]', describe="匹配实体按钮")
    ipt_match = Element(css='input[placeholder="在这里填写正则表达式"]', describe="匹配选项输入框")
    # 公共
    ipt_name = Element(css='input[placeholder="输入实体名称"]', describe="实体名称输入框")
    sel_robot = Element(xpath='//span[text()="选填" and @class="ant-select-selection-placeholder"]/..', describe="机器人选择框")
    sel_first = Element(css='div[class="rc-virtual-list-holder-inner"]>div:nth-child(1)', describe='选择第一个机器人')
    btn_submit = Element(css='button[type="submit"]', describe='提交按钮')
    # 验证
    success_prompt = Element(xpath='//span[text()="创建成功"]', describe='创建成功提示')
    table_first_name = Element(xpath='//tbody/tr[2]/td[4]', describe="第一条表记录实体名称")
    table_first_type = Element(xpath='//tbody/tr[2]/td[6]', describe="第一条表记录实体类型")
