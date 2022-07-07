from poium import Element, Page, Elements


class PageGroupSend(Page):
    menu_message = Element(xpath='//div[@class="ant-menu-submenu-title"]/span[text()="消息发送"]', describe='消息平台')
    menu_group_send = Element(xpath='//li//a[text()="在线发送"]', describe='群发助手菜单')
    menu_group_sends = Elements(xpath='//li//a[text()="在线发送"]', describe='判断群发助手菜单是否存在')
    ipt_task_name = Element(css='input[placeholder="请填写任务名称 ..."]', describe="任务名称输入框")
    ipt_chatbot = Element(css='#applicationId', describe='选择应用')
    ipt_channel = Element(css='#channelId', describe='消息通道输入框')
    channel_PRIV = Element(css='div[title="模拟器"]', describe='选择模拟器通道')
    ipt_object = Element(css='textarea[placeholder="每行一个手机号，或以空格分开 ..."]', describe='输入发送的号码')
    btn_submit = Element(css='button[type="submit"]', describe='提交按钮')
    first_task = Element(xpath='//tbody/tr[2]/td[2]', describe='任务列表第一个任务')
    task_state = Element(xpath='//tbody/tr[2]/td[5]', describe='任务状态')
    # 页面新元素
    template_message = Element(id_='rc-tabs-0-tab-BATCH_MESSAGE', describe="选择模板消息")
    sel_template = Element(id_='batchMessage_templateId', describe="模板选择框")
    template = Element(xpath='//*[contains(text(),"单卡片")]', describe="选择单卡片模板")
