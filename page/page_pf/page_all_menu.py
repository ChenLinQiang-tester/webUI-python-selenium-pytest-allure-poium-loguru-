from poium import Page, Element, Elements


class PageAllMenu(Page):
    menus = Elements(xpath='//li/*/*[@class="ant-menu-title-content" or @href="#/main/home"]', describe="一级菜单")
    menu_expand = Elements(xpath='//li/*/*[@class="ant-menu-title-content" or @href="#/main/home"]/..', describe="一级菜单菜单是否展开")
    else_expand = Elements(xpath='//li/div[@aria-expanded="true"]', describe="判断是否有其他菜单展开")
    submenus = Elements(xpath='//ul[@class="ant-menu ant-menu-sub ant-menu-inline"]/li', describe='子菜单')
    page_notice = Elements(xpath='//div[@class="ant-message-notice-content"]/div/span[2]', describe='判断是否有异常提示')
    page_ = Element(xpath='//div[@class="ant-message-notice-content"]/div/span[2]', describe='h5页面创建成功提示')
    submenus_path_name = Element(xpath='//div[@class="ant-breadcrumb"]/span[3]/span[1]', describe='子菜单路径名称')