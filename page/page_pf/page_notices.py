from poium import Page, Element, Elements


class PageNotices(Page):
    menu_account = Element(xpath='//div[@class="ant-menu-submenu-title"]/span[text()="账号"]', describe='账号菜单')
    menus_notices = Elements(css='li[title="通知"]', describe='判断通知子菜单是否存在')
    notice_1 = Element(xpath='//tr[2]/td[1]', describe="第一条通知展开按钮")
    notice_content = Elements(xpath='//tr[@class="ant-table-expanded-row ant-table-expanded-row-level-1"]//*[contains(text(),"【蜂动科技")]', describe="通知展开内容")
    notice_status = Element(xpath='//tr[2]/td[3]/span/span/span[1]')
