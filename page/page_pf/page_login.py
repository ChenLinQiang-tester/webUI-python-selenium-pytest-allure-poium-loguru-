from poium import Page, Element, Elements


class PageEnterpriseLogin(Page):
    username = Element(css='input[placeholder="Email"]', describe="邮箱账号")
    password = Element(css="input[type='password']", describe="密码")
    code_ele = "input[type='number']"
    number = Element(css="input[type='number']", describe="图片验证码输入框")
    number_img = Element(css='img[class="captcha-image"]', describe="图片验证码")
    login_btn = Element(css='button[class="ant-btn ant-btn-primary ant-btn-two-chinese-chars"]', describe="登录按钮")
    error_tip = Element(xpath='//div[@class="ant-message-notice-content"]/div/span[2]', describe='错误提示')
    error_tips = Elements(xpath='//div[@class="ant-message-notice-content"]/div/span[2]', describe='判断是否有错误提示')
    email = Element(xpath='//div[@span="19"]//div[@class="ant-space ant-space-horizontal ant-space-align-center"]/div', describe="验证账号")
    reflush_code = Element(css='span[class="ant-input-group-addon"]', describe="刷新验证码")
    know = Element(css='button[type="button"][class="ant-btn ant-btn-primary"]', describe='知道了')