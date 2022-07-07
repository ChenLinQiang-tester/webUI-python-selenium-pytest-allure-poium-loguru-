from poium import Page, Element, Elements


class PageOrder(Page):
    menu_billing = Element(xpath='//div[@class="ant-menu-submenu-title"]/span[text()="计费"]', describe='计费菜单')
    menus_order = Elements(css='li[title="订单"]', describe='判断订单子菜单是否存在')
    btn_ok = Element(xpath='//button/span[text()="确 定"]', describe="确定按钮")
    btn_no = Element(xpath='//button/span[text()="取 消"]', describe="取消按钮")
    notice = Element(xpath='//div[@class="ant-message-notice-content"]/div/span[2]', describe='h5页面创建成功提示')
    order_state = Element(xpath='//tr[2]/td[6]/span/span[2]', describe="订单状态")
    # 0 调测
    btn_test = Element(xpath='//tr[2]/td[last()]//button[not(@disabled)]', describe="调测按钮")
    # 1 订单使用详情
    use_detail = Element(xpath='//tr[2]/td[last()]//span[@class="anticon anticon-profile"]', describe="使用明细按钮")
    product_name = Element(xpath='//tbody/tr[2]/td[1]/span', describe='订单名称')
    residue_count = Element(xpath='//tbody/tr[2]/td[6]/span[not(@class)]', describe="商品余量a")
    residue_count_b = Element(xpath='//tbody/tr[1]/td[4]/span', describe="商品余量b")
    detail_product_name = Element(xpath='//tbody/tr[1]/td[1]/span', describe="商品详情中的名称")
    btn_open = Element(xpath='//tr[2]/td[1]/button', describe="展开订单按钮")
    # 2 退款审核
    audit_refund = Element(xpath='//tr[2]/td[last()]//button', describe="退款按钮")
    ipt_refund = Element(css='textarea[placeholder="在这里输入退款说明"]', describe='退款审核输入框')
    menu_passport = Element(xpath='//div[@class="ant-menu-submenu-title"]/span[text()="用户"]', describe='用户菜单')
    menu_enterprise = Element(css='li[title="企业管理"]', describe='判断企业管理子菜单是否存在')
    ipt_search = Element(id_='keyword', describe="企业搜索框")
    balance = Element(xpath='//tr[2]/td[5]/span/span/span', describe="企业余额")
    # 3 修改订单功能
    validCount = Element(id_='validCount', describe="商品余量")
    expire = Element(id_='expire', describe="过期时间")
    ipt_count = Element(id_='count', describe="修改调用次数输入框")
    expireDate = Element(id_='expireDate', describe="商品有效期输入框")
    tomorrow = Element(xpath='//td[@class="ant-picker-cell ant-picker-cell-in-view ant-picker-cell-today"]/following-sibling::*[1]/div', describe="日期选择明天")