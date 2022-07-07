from poium import Page, Element, Elements


class PageSampleTemplate(Page):
    menu_sample = Element(xpath='//div[@class="ant-menu-submenu-title"]/span[text()="行业模板"]', describe='行业模板菜单')
    menus_template = Elements(css='li[title="模板"]', describe='判断模板子菜单是否存在')
    # 执行
    btn_create = Element(xpath='//button[text()="创建"]', describe="创建按钮")
    ipt_name = Element(id_='name', describe="名称输入框")
    sel_industry = Element(id_='applicationId', describe="行业选择框")
    sel_category = Element(id_='categoryId', describe="模板类别选择框")
    category = Element(xpath='//div[text()="TestCategory"]', describe="选择行业类别")
    btn_maker = Element(xpath='//button[text()="消息制作器"]', describe="消息制作器按钮")
    # 消息制作器
    btn_minus_square = Element(xpath='//div[@class="ant-col ant-col-8"]/div[6]/span[@type="minus-square"]',
                               describe='卡片消息按钮')
    display_btn = Element(xpath='//button[@type="button" and @class="ant-btn ant-btn-circle ant-btn-sm"][1]',
                          describe='编辑卡片按钮')
    ipt_square_img = Element(xpath='//tbody/tr[2]//span/span/input', describe="卡片图片路径输入框")
    ipt_square_img_xpath = '//tbody/tr[2]//input'
    ipt_square_title = Element(css='input[value="标题"]', describe='卡片标题输入框')
    ipt_square_describe = Element(css='textarea[placeholder="在这输入描述"]', describe='卡片描述输入框')
    btn_square_memu = Element(css='button[type="button"][class="ant-btn ant-btn-dashed"]', describe='添加卡片按钮')
    square_memu_reply = Element(xpath='//span[text()="回复信息" and @class="ant-menu-title-content"]', describe='卡片回复按钮')
    btn_ok = Element(xpath='//button/span[text()="确 定"]', describe='确定按钮')
    btn_submit = Element(xpath='//button[text()="提交"]', describe='提交按钮')
    # 验证
    notice = Element(xpath='//div[@class="ant-message-notice-content"]/div/span[2]', describe='h5页面创建成功提示')
    template_name = Element(xpath='//tr[2]/td[3]', describe="验证模板名称")