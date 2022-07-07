from poium import Element, Page, Elements


class PageOrder(Page):
    menu_passport = Element(xpath='//div[@class="ant-menu-submenu-title"]/span[text()="消息商城"]', describe="消息商城菜单")
    menu_order = Element(xpath='//li//a[text()="我的订单"]', describe='我的订单菜单')
    menu_orders = Elements(xpath='//li//a[text()="我的订单"]', describe='判断我的订单菜单是否存在')
    empty_order = Elements(class_name='ant-pagination-total-text', describe='判断订单是否为空')
    # 三个功能
    btn_detail = Elements(xpath='//span[@class="anticon anticon-profile"]', describe='使用详情功能')
    btn_refund = Elements(xpath='//button[@class="ant-btn ant-btn-link" and not(@disabled)]', describe='申请退款功能')
    btn_reBuy = Element(xpath='//tbody/tr[2]//span[@class="anticon anticon-transaction"]', describe='第一个订单重新购买功能')
    # 1 订单使用详情
    product_name = Elements(xpath='//span[@class="anticon anticon-profile"]/../../../preceding-sibling::*[7]', describe='订单名称')
    detail_product_name = Element(xpath='//tbody/tr[1]/td[1]/span')
    # 2 订单退款
    ipt_refund = Element(css='textarea[placeholder="在这里填写退款原因"]', describe='退款原因输入框')
    btn_confirm_refund = Element(xpath='//button/span[text()="确 定"]', describe='确定退款按钮')
    success_prompt = Element(xpath='//div[@class="ant-message-notice"]//span[2]', describe='退款成功提示')
    order_status = Element(xpath='//tbody/tr[2]/td[7]', describe='退款状态')
    # 3 订单重新购买
    product_name_0 = Element(xpath='//tbody/tr[2]/td[3]', describe='第一个订单名称')
    product_name_reBuy = Elements(xpath='//article[@class="ant-typography"]/h4', describe='重新购买页面订单名称')
    product_sold_out = Element(class_name='ant-result-title', describe="此商品已下架")




