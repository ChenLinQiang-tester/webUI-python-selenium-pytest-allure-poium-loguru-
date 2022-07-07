from poium import Page, Element, Elements


class PageHome(Page):
    user = Element(css='section[class="ant-dropdown-trigger account--t-YEs"]', describe="顶部栏-用户名称")
    btn_logout = Element(xpath='//span[text()="退出登录"]', describe="退出登录按钮")
    btn_confirm_logout = Element(xpath='//button/span[text()="确 定"]', describe="确认注销登录按钮")
    btn_login = Elements(xpath='//button[text()="登录"]', describe="登录按钮")
