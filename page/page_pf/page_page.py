from poium import Element, Page, Elements


class PagePage(Page):
    menu_message = Element(xpath='//div[@class="ant-menu-submenu-title"]/span[text()="消息平台"]', describe='消息平台菜单')
    menus_page = Elements(css='li[title="H5页面审核"]', describe='判断H5页面审核子菜单是否存在')
    menu_page = Element(css='li[title="H5页面审核"]', describe='H5页面审核子菜单')
    btn_audit = Elements(xpath='//tr/td[contains(text(),"H5标题")]/../td[last()]//a[1]/span', describe="H5审核按钮")
    btn_submit = Element(css='button[class="ant-btn ant-btn-primary"]', describe="审核提交按钮")
    notice = Element(xpath='//div[@class="ant-message-notice-content"]/div/span[2]', describe='审核成功提示')
    audit_status = Elements(xpath='//tr/td[contains(text(),"H5标题")]/../td[6]/span', describe="H5审核状态")
