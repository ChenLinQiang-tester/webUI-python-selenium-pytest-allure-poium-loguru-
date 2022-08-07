from poium import Page, Element


class LoginPage(Page):
    login_a = Element(link_text="登录", describe="主页登录入口")
    username_input = Element(css='#loginDialog input[name="username"]', describe="登录用户名输入框")
    password_input = Element(css='#loginDialog input[name="password"]', describe="登录密码输入框")
    login_span = Element(xpath='//span[.="登录" and @class="btn save"]', describe="登录按钮")
    username_span = Element(css='.account>a[href="/user/lg/index"]', describe="登录后主页显示的用户名")