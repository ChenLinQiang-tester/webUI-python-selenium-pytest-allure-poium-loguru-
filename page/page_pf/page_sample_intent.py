from poium import Page, Elements, Element


class PageSampleIntent(Page):
    menu_sample = Element(xpath='//div[@class="ant-menu-submenu-title"]/span[text()="行业模板"]', describe='行业模板菜单')
    menus_intent = Elements(css='li[title="意图"]', describe='判断意图子菜单是否存在')
    # 问答意图
    btn_qa_intent = Element(xpath='//button[text()="问答意图"]', describe="问答意图按钮")
    btn_add_answer = Element(xpath='//label[text()="回答"]/../following-sibling::*[1]//button', describe="添加回答按钮")
    ipt_answer = Element(id_='answerTexts_0', describe='回答输入框')
    # 任务意图
    btn_task_intent = Element(xpath='//button[text()="任务意图"]', describe="任务意图按钮")
    ipt_function = Element(css='textarea[placeholder="在这里输入函数 ..."]', describe="函数输入框")
    # 公共
    ipt_name = Element(css='input[placeholder="在这里输入意图名称 ..."]', describe="意图名称输入框")
    sel_industry = Element(id_='applicationId', describe="行业选择框")
    sel_category = Element(id_='categoryId', describe='技能选择框')
    category = Element(xpath='//div[text()="TestCategory"]', describe="选择行业类别")
    # 语料
    btn_add_corpus = Element(xpath='//label[text()="语料"]/../following-sibling::*[1]//button', describe="添加语料按钮")
    ipt_corpus = Element(id_='asks_0', describe="语料输入框")
    btn_submit = Element(css='button[type="submit"]', describe='提交按钮')
    # 验证
    notice = Element(xpath='//div[@class="ant-message-notice-content"]/div/span[2]', describe='h5页面创建成功提示')
    table_first_name = Element(xpath='//tbody/tr[2]/td[3]', describe="第一条表记录意图名称")
    table_first_type = Element(xpath='//tbody/tr[2]/td[6]', describe="第一条表记录意图类型")

    btn_sel = Elements(xpath='//tr/td[text()="TestCategory"]/../td[2]//input[not(@checked)]', describe="选择按钮")
    btn_del = Element(xpath='//button[text()="删除"]', describe="删除按钮")
    btn_ok = Element(xpath='//button/span[text()="确 定"]', describe="确定按钮")