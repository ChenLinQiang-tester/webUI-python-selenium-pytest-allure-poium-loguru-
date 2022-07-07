from poium import Element, Page, Elements


class PageAddressBook(Page):
    menu_message = Element(xpath='//div[@class="ant-menu-submenu-title"]/span[text()="用户管理"]', describe='应用管理菜单')
    menu_user = Element(xpath='//li//a[text()="我的用户"]', describe='我的用户-二级菜单')
    menus_user = Elements(xpath='//li//a[text()="用户"]', describe='判断用户菜单是否存在')
    # menu_address_book = Element(css='li[title="通讯录"]', describe="通讯录-三级菜单")
    # menus_address_book = Elements(css='li[title="通讯录"]', describe="判断通讯录-三级菜单是否存在")
    btn_create_contacts = Element(xpath='//button[text()="创建联系人"]', describe='创建联系人')
    ipt_name = Element(css='input[placeholder="请填写联系人名称 ..."]', describe="联系人名称输入框")
    ipt_phone = Element(css='textarea[placeholder="每行一个手机号，或以空格分开 ..."]', describe='手机号输入框')
    btn_submit = Element(css='button[type="submit"]', describe='提交按钮')
    first_list_name = Element(xpath='//tbody/tr[2]/td[3]', describe='列表第一个联系人名称')
    first_list_phone = Element(xpath='//tbody/tr[2]/td[5]', describe='列表第一个联系人号码')



