from poium import Element, Page, Elements


class PageRobotIntent(Page):
    menu_robot = Element(xpath='//div[@class="ant-menu-submenu-title"]/span[text()="聊天机器人"]', describe="聊天机器人菜单")
    menu_robot_intent = Element(xpath='//li//a[text()="我的意图"]', describe="意图菜单")
    menu_robot_intents = Elements(xpath='//li//a[text()="我的意图"]', describe="判断意图菜单是否存在")
    # 问答意图
    btn_qa_intent = Element(xpath='//button[text()="问答意图"]', describe="问答意图按钮")
    btn_add_answer = Element(xpath='//label[text()="回答"]/../following-sibling::*[1]//button', describe="添加回答按钮")
    ipt_answer = Element(id_='answerTexts_0', describe='回答输入框')
    # 任务意图
    btn_task_intent = Element(xpath='//button[text()="任务意图"]', describe="任务意图按钮")
    btn_procedure = Element(css='label[class="ant-radio-button-wrapper"]', describe="流程编排按钮")
    add_node = Element(xpath='//ul[@class="ant-timeline"]/../div//button', describe="添加节点按钮")
    template_node = Element(xpath='//span[text()="模板节点"]', describe="选择模板节点")
    sel_0_template = Element(id_='procedure_nodes_0_payloadId', describe="第一个模板节点选择框")
    ipt_function = Element(css='textarea[placeholder="在这里输入函数 ..."]', describe="函数输入框")
    # 公共
    ipt_name = Element(css='input[placeholder="在这里输入意图名称 ..."]', describe="意图名称输入框")
    ipt_robot = Element(xpath='//label[@title="机器人"]/../following-sibling::*[1]//input', describe="机器人选择框")
    sel_first_robot = Element(css='div[class="rc-virtual-list-holder-inner"]>div:nth-child(1)', describe='选择第一个机器人')
    btn_add_corpus = Element(xpath='//label[text()="语料"]/../following-sibling::*[1]//button', describe="添加语料按钮")
    ipt_corpus = Element(id_='asks_0', describe="语料输入框")
    btn_submit = Element(css='button[type="submit"]', describe='提交按钮')
    # 验证
    notice = Element(xpath='//div[@class="ant-message-notice-content"]/div/span[2]', describe='h5页面创建成功提示')
    table_first_name = Element(xpath='//tbody/tr[2]/td[4]', describe="第一条表记录意图名称")
    table_first_type = Element(xpath='//tbody/tr[2]/td[6]', describe="第一条表记录意图类型")
