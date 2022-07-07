from poium import Element, Page, Elements


class PageFeedback(Page):
    menu_passport = Element(xpath='//div[@class="ant-menu-submenu-title"]/span[text()="系统配置"]', describe="我的帐号菜单")
    menu_feedback = Element(xpath='//li//a[text()="工单服务"]', describe='工单菜单')
    menu_feedbacks = Elements(xpath='li[title="工单服务"]', describe='判断工单菜单是否存在')
    btn_feedback = Element(xpath='//button[text()="提交工单"]', describe='提交工单按钮')
    ipt_title = Element(xpath='//form[@class="ant-legacy-form ant-legacy-form-horizontal"]/div[1]//input', describe="工单标题输入框")
    sel_type = Element(xpath='//form[@class="ant-legacy-form ant-legacy-form-horizontal"]/div[2]//input', describe="工单类型选择框")
    sel_degree = Element(xpath='//form[@class="ant-legacy-form ant-legacy-form-horizontal"]/div[3]//input', describe="工单紧急程度选择框")
    sel_scope = Element(xpath='//form[@class="ant-legacy-form ant-legacy-form-horizontal"]/div[4]//input', describe="工单范围选择框")
    ipt_question = Element(css='textarea[placeholder="在这里详细描述您的问题 ..."]', describe="工单问题输入框")
    ipt_secret_information = Element(css='textarea[placeholder="在这里输入机密信息，如 密码、appId、appSecret 等 ..."]', describe="工单机密信息输入框")
    ipt_image = Element(css='input[accept="image/*"]', describe="上传图片框")
    btn_submit = Element(css='button[type="submit"]', describe='提交工单按钮')
    success_notice = Element(xpath='//div[@class="ant-message-notice"]//span[2]', describe="工单提交成功提示")
    first_feedback_title = Element(xpath='//tbody/tr[last()]/td[3]', describe="列表第一工单标题")


