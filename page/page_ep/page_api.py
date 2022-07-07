from poium import Element, Page, Elements


class PageApi(Page):
    menu_message = Element(xpath='//div[@class="ant-menu-submenu-title"]/span[text()="开发者选项"]', describe='消息平台')
    menu_api = Element(xpath='//li//a[text()="API定义"]', describe='API定义菜单')
    menus_api = Elements(xpath='//li//a[text()="API定义"]', describe='判断是否API定义菜单是否存在')
    btn_create_api = Element(xpath='//button[text()="创建 API 定义"]', describe='创建API定义按钮')
    ipt_api_name = Element(css='#name', describe='API名称输入框')
    ipt_url = Element(css='#url', describe='URL输入框')
    sel_method = Element(css='#method', describe='id下拉框')
    post = Element(css='div[title="POST"]', describe='选择post请求方法')
    sel_content_type = Element(xpath='//div[@class="ant-col ant-col-7"]/div[4]//div[@class="ant-select-selector"]', describe='内容类型下拉框')
    app_json = Element(css='div[title="application/json"]', describe="选择application/json类型")
    ipt_body = Element(css='textarea[class="ant-input"]', describe='body输入框')
    btn_add_output = Element(xpath='//div[@class="ant-col ant-col-10"]//button[@class="ant-btn ant-btn-dashed ant-btn-icon-only ant-btn-block"]', describe="添加output按钮")
    ipt_outputs_key = Element(css='#outputs_0_key', describe="outputs_key输入框")
    ipt_outputs_path = Element(css='#outputs_0_path', describe="outputs_path输入框")
    sel_outputs_type = Element(css='#outputs_0_type', describe="outputs_type下拉框")
    string = Element(css='div[title="string"]', describe="选择string类型")
    btn_submit = Element(css='button[type="submit"]', describe='提交按钮')
    first_list = Element(xpath='//tbody/tr[2]/td[3]', describe='列表第一个api定义')


