from poium import Page, Element, Elements


class PageAllMenu(Page):
    menus = Elements(xpath='//nav/ul/li/*/*[@class="ant-menu-title-content" or @href="#/main/home"]', describe="一级菜单")
    menu_expand = Elements(xpath='//nav/ul/li/*/*[@class="ant-menu-title-content" or @href="#/main/home"]/..', describe="一级菜单菜单是否展开")
    submenus = Elements(xpath='//nav/ul/li/ul[@class="ant-menu ant-menu-sub ant-menu-inline"]/li', describe='二级子菜单')
    submenus3 = Elements(xpath='//ul[@class="ant-menu ant-menu-sub ant-menu-inline"]/li//li', describe='三级子菜单')
    page_notice = Elements(xpath='//div[@class="ant-message-notice-content"]/div/span[2]', describe='判断是否有异常提示')
    page_ = Element(xpath='//div[@class="ant-message-notice-content"]/div/span[2]', describe='h5页面创建成功提示')
    submenus_path_name = Element(xpath='//div[@class="ant-breadcrumb"]/span[3]/span[1]', describe='子菜单路径名称')