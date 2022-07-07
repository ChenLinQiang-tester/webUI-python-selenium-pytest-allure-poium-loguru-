from poium import Page, Element, Elements


class PageTiered(Page):
    menu_billing = Element(xpath='//div[@class="ant-menu-submenu-title"]/span[text()="计费"]', describe='计费')
    menus_tiered = Elements(css='li[title="阶梯计费"]', describe='判断阶梯计费子菜单是否存在')
    menu_tiered = Element(css='li[title="阶梯计费"]', describe='阶梯计费子菜单')
    btn_create = Element(xpath='//button[text()="创建阶梯计费"]', describe="创建阶梯计费按钮")
    sel_type = Element(id_='rc_select_0', describe="消息类型下拉框")
    ipt_describe = Element(xpath='//label[text()="消息描述"]/../following-sibling::*[1]//input', describe="消息描述输入框")
    btns_del = Elements(css='span[class="anticon anticon-delete"]', describe="删除按钮")
    btn_add_tiered = Element(xpath='//button[text()="创建计费阶梯"]', describe='创建计费阶梯按钮')
    ipt_0 = Element(xpath='//input[@class="ant-input-number-input" and @value=""]', describe='短信条数输入框')
    ipt_1 = Element(xpath='//div/input[@class="ant-input" and @value=""]', describe='费用输入框')
    btn_submit = Element(css='button[class="ant-btn ant-btn-primary ant-btn-two-chinese-chars"]', describe="提交按钮")
    notice = Element(xpath='//div[@class="ant-message-notice-content"]/div/span[2]', describe='修改成功提示')
    success_text = Element(xpath='//tbody/tr/td[text()="文本消息"]/following-sibling::*[1]/div/div[last()]',
                           describe="验证数据内容")
