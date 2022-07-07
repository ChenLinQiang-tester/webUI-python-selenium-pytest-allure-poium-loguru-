from poium import Element, Page, Elements


class PageUser(Page):
    menu_passport = Element(xpath='//div[@class="ant-menu-submenu-title"]/span[text()="系统配置"]', describe="系统配置菜单")
    menu_user_manage = Element(xpath='//li//a[text()="成员管理"]', describe="成员管理菜单")
    menus_user_manage = Elements(xpath='//li//a[text()="成员管理"]', describe="判断成员管理菜单是否存在")
    btn_create = Element(xpath='//button/span[text()="创建成员"]', describe="创建成员按钮")
    # 清空列表
    btn_delete = Element(xpath='//button/span[text()="删除"]', describe="批量删除按钮")
    sel_all_list = Element(xpath='//tr[1]//input', describe="选中列表所有成员")
    sel_all_lists = Elements(xpath='//tr[1]//input[not(@disabled)]', describe="全选按钮是否可用")
    confirm_delete = Element(xpath='//button/span[text()="确 定"]', describe='确认删除')

    ipt_name = Element(css='input[placeholder="在这里填写成员名称 ..."]', describe="成员名称输入框")
    ipt_phone = Element(css='input[placeholder="在这里填写手机号 ..."]', describe="手机号输入框")
    ipt_email = Element(css='input[placeholder="在这里填写邮件地址 ..."]', describe="邮箱输入框")
    ipt_password = Element(css='input[placeholder="在这里填写密码 ..."]', describe="密码输入框")
    sel_roles = Element(class_name='ant-select-selection-search-input', describe="角色选择框")
    roles = Elements(xpath='//div[@class="rc-virtual-list-holder-inner"]//div[@class="ant-select-item-option-content"]',
                     describe="角色选择")
    btn_submit = Element(css='button[type="submit"]', describe="提交按钮")
