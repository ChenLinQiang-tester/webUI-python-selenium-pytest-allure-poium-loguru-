from poium import Element, Page, Elements


class PageTemplate(Page):
    menu_message = Element(xpath='//div[@class="ant-menu-submenu-title"]/span[text()="消息平台"]', describe='消息平台菜单')
    menus_template = Elements(css='li[title="模板审核"]', describe='判断模板审核子菜单是否存在')
    menu_template = Element(css='li[title="模板审核"]', describe='模板审核子菜单')
    btn_audit = Elements(xpath='//tr/td[contains(text(),"单卡片")]/../td[last()]//a[1]', describe="模板审核按钮")
    btn_submit = Element(css='button[class="ant-btn ant-btn-primary"]', describe="审核提交按钮")
    notice = Element(xpath='//div[@class="ant-message-notice-content"]/div/span[2]', describe='审核成功提示')
    audit_status = Elements(xpath='//tr/td[contains(text(),"单卡片")]/../td[6]/span', describe="模板审核状态")
