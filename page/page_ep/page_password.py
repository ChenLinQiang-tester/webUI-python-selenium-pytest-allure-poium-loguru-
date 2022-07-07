from poium import Element, Page, Elements


class PagePassword(Page):
    menu_passport = Element(xpath='//div[@class="ant-menu-submenu-title"]/span[text()="账号配置"]', describe="账号配置菜单")
    menu_password = Element(xpath='//li//a[text()="修改密码"]', describe="修改密码菜单")
    menus_password = Elements(xpath='//li//a[text()="修改密码"]', describe="判断修改密码菜单是否存在")
    ipt_old_password = Element(css='input[placeholder="在这里输入原密码 ..."]', describe="原密码输入框")
    ipt_new_password = Element(css='input[placeholder="在这里输入新密码 ..."]', describe="新密码输入框")
    ipt_again_password = Element(css='input[placeholder="在这里重输密码 ..."]', describe="重输密码输入框")
    btn_submit = Element(css='button[type="submit"]', describe="提交按钮")
    success_notice = Element(xpath='//div[@class="ant-message-notice-content"]/div/span[2]', describe="修改成功提示")