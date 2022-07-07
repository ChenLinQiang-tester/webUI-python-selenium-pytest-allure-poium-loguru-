from poium import Element, Page, Elements


class PageFeedback(Page):
    menu_user = Element(xpath='//div[@class="ant-menu-submenu-title"]/span[text()="用户"]', describe='用户')
    menus_feedback = Elements(css='li[title="工单"]', describe='判断工单子菜单是否存在')
    menu_feedback = Element(css='li[title="工单"]', describe='工单子菜单')
    feedback_title = Elements(xpath='//tr/td/a[contains(text(),"工单")]', describe='工单标题')
    ipt_0 = Element(id_='contents', describe='问题输入框')
    ipt_1 = Element(id_='secretContents', describe='机密信息输入框')
    btn_submit = Element(css='button[class="ant-btn ant-btn-primary ant-btn-two-chinese-chars"]', describe="提交工单按钮")
    ipt_image = Element(id_='images', describe="图片上传框")
    notice = Element(xpath='//div[@class="ant-message-notice-content"]/div/span[2]', describe='回复成功提示')
    last_reply = Element(xpath='//div[@class="ant-drawer-body"]/div[last()]/div[2]')

