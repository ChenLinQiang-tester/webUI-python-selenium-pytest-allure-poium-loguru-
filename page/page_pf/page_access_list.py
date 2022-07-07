from poium import Element, Page, Elements


class PageAccessList(Page):
    # 前
    menu_message = Element(xpath='//div[@class="ant-menu-submenu-title"]/span[text()="消息平台"]', describe='消息平台')
    menu_bw_list = Element(css='li[title="黑白名单"]', describe='黑白名单菜单')
    menu_bw_lists = Elements(css='li[title="黑白名单"]', describe='判断黑白名单菜单是否存在')
    # 启动黑白名单
    btn_black_on = Element(xpath='//span[text()="启用黑名单"]', describe='启用黑名单按钮')
    btn_white_on = Element(xpath='//span[text()="启用白名单"]', describe='启用白名单按钮')
    # 创建黑白名单
    btn_create_black = Element(xpath='//button[text()="创建黑名单"]', describe='创建黑名单按钮')
    btn_create_white = Element(xpath='//button[text()="创建白名单"]', describe='创建白名单按钮')
    ipt_black_list_name = Element(xpath='//input[@placeholder="在这里填写黑名单名称 ..."]', describe='黑名单名称输入框')
    ipt_white_list_name = Element(xpath='//input[@placeholder="在这里填写白名单名称 ..."]', describe='白名单名称输入框')
    ipt_phone = Element(xpath='//textarea[@placeholder="每行一个手机号，或以空格分开 ..."]', describe='手机号输入框')
    btn_submit = Element(xpath='//button[@type="submit"]', describe='名单提交按钮')
    # 关闭黑白名单
    btn_list_close = Element(xpath='//span[text()="不启用"]', describe='不启用黑白名单')
    # 后
    first_list = Element(xpath='//tbody/tr[2]/td[3]', describe='名单第一位')
    close_list = Element(xpath='//div[@class="ant-empty-description"]', describe="列表暂无数据")
    btn_yes = Element(xpath='//button/span[text()="确 定"]', describe='确定开启按钮')
    btn_yess = Elements(xpath='//button/span[text()="确 定"]', describe='判断是否已开启')
