from poium import Page, Element, Elements


class PageEnterpriseLogin(Page):
    username = Element(css='input[placeholder="邮箱地址"]', describe="邮箱账号")
    password = Element(css="input[type='password']", describe="密码")
    number = Element(css='input[placeholder="图形验证码"]', describe="图片验证码输入框")
    number_img = Element(css='span>div>img[class="ant-image-img"]', describe="图片验证码")
    agreement = Element(id_='agreement', describe="服务条款")
    notice = Element(xpath='//div[@class="ant-message-notice-content"]/div/span[2]', describe='错误提示')
    email = Element(xpath='//span[@aria-label="mail"]/..', describe="验证账号")
    reflush_code = Element(css='button>span[aria-label="reload"]', describe="刷新验证码")
    login_btn = Element(css='button[type="submit"]', describe="登录按钮")
    know = Element(css='button[type="button"][class="ant-btn ant-btn-primary"]', describe='知道了')
    balance = Elements(xpath='//div[text()="余额"]/../../following-sibling::*/span[2]/span', describe="余额")