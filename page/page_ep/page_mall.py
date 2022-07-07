from poium import Element, Page, Elements


class PageMall(Page):
    menu_passport = Element(xpath='//div[@class="ant-menu-submenu-title"]/span[text()="消息商城"]', describe="消息商城菜单")
    menu_mall = Element(xpath='//li//a[text()="产品列表"]', describe="产品列表")
    menus_mall = Elements(xpath='//li//a[text()="产品列表"]', describe="判断产品列表是否存在")
    menu_home = Element(css='li[title="主页"]', describe="主页菜单")
    balance = Elements(xpath='//div[text()="余额"]/following-sibling::*/span[2]/span', describe="余额")
    # 商城页面
    list_product_1 = Elements(xpath='//div[contains(text(),"能力") and @class="ant-card-meta-title"]', describe="商城第一个能力调用商品")
    # 商品详情页面
    btn_buy = Element(xpath='//button/span[text()="立即购买"]', describe='立即购买按钮')
    price = Element(tag="strong", describe="商品价格")
    # 支付页面
    ipt_name = Element(id_='name', describe='名称输入框')
    ipt_phone = Element(id_='number', describe='手机号码输入框')
    btn_submit = Element(xpath='//button[text()="确认支付"]', describe='确认支付按钮')
    success_prompt = Element(class_name='ant-result-title', describe='支付成功提示')
    exception_prompt = Elements(xpath='//div[@class="ant-message-notice-content"]/div/span[2]', describe="判断异常提示")
    copy_order_id = Element(css='span[aria-label="copy"]', describe='复制订单号')
    btn_confirm_order = Element(xpath='//button[text()="确认订单"]', describe='确认订单按钮')
    # 订单页面
    ipt_order_id = Element(id_='orderId', describe='订单编号输入框')
    ipt_order_id1 = Element(id_='orderId', describe='订单编号输入框')
    get_order_id = Element(xpath='//tbody/tr[2]/td[2]', describe='搜索到的订单id')