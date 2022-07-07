from poium import Page, Element, Elements


class PageAgentManage(Page):
    menu_agent = Element(xpath='//div[@class="ant-menu-submenu-title"]/span[text()="代理"]', describe='代理')
    menus_agent_manage = Elements(css='li[title="代理商管理"]', describe='判断代理商管理子菜单是否存在')
    menu_agent_manage = Element(css='li[title="代理商管理"]', describe='代理商管理子菜单')
    btn_create = Element(xpath='//button[text()="创建"]', describe="创建按钮")
    # 前置
    old = Element(xpath='//tbody/tr/td[contains(text(),"2021-")]/../td[2]', describe="上次创建的数据")
    btn_del = Element(xpath='//button[text()="删除"]', describe="删除按钮")
    btn_ok = Element(xpath='//button/span[text()="确 定"]', describe="确定删除按钮")
    # 个人
    ipt_name = Element(id_='name', describe="联系人名称输入框")
    ipt_phone = Element(id_='tel', describe="联系人电话输入框")
    ipt_idNumber = Element(id_='idNumber', describe="身份证号码输入框")
    ipt_images = Element(id_='idImages', describe="身份证图片上传框")
    ipt_address = Element(id_='address', describe="地址输入框")
    ipt_password1 = Element(id_='password', describe="密码输入框")
    ipt_password2 = Element(id_='password2', describe="重输密码输入框")
    btn_submit = Element(xpath='//button[text()="提交"]', describe="提交按钮")
    # 企业
    ipt_ep = Element(css='input[value="ENTERPRISE"]', describe="企业选项")
    ipt_name_ep = Element(id_='enterpriseName', describe="公司名称")
    ipt_idNumber_ep = Element(id_='enterpriseIdNumber', describe="统一社会信用代码")
    ipt_images_ep = Element(id_='enterpriseIdImages', describe="营业执照输入框")
    ipt_address_ep = Element(id_='enterpriseAddress', describe="注册地址输入框")
    # 验证
    agent_name = Element(xpath='//tbody/tr[2]/td[5]', describe="代理商对接人姓名")
    notice = Element(xpath='//div[@class="ant-message-notice-content"]/div/span[2]', describe='提示')
