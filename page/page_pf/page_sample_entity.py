from poium import Page, Element, Elements


class PageSampleEntity(Page):
    menu_sample = Element(xpath='//div[@class="ant-menu-submenu-title"]/span[text()="行业模板"]', describe='行业模板菜单')
    menus_entity = Elements(css='li[title="实体"]', describe='判断实体子菜单是否存在')
    # 选项实体
    btn_option_entity = Element(xpath='//button[text()="选项实体"]', describe="选项实体按钮")
    ipt_option = Element(css='textarea[placeholder="在这里填写可选项 ..."]', describe="可用选项输入框")
    # 匹配实体
    btn_add = Element(css='button[class="ant-btn ant-btn-dashed ant-btn-icon-only"]', describe="添加实体按钮")
    btn_match_entity = Element(xpath='//button[text()="匹配实体"]', describe="匹配实体按钮")
    ipt_match = Element(css='input[placeholder="在这里输入正则表达式 ..."]', describe="匹配选项输入框")
    # 公共
    ipt_name = Element(css='input[placeholder="在这里填写实体名称 ..."]', describe="实体名称输入框")
    sel_industry = Element(xpath='//label[text()="行业"]/../following-sibling::*[1]//input', describe="行业选择框")
    sel_category = Element(xpath='//label[text()="技能"]/../following-sibling::*[1]//input', describe='技能选择框')
    category = Element(xpath='//div[text()="TestCategory"]', describe="选择行业类别")
    btn_submit = Element(css='button[type="submit"]', describe='提交按钮')
    # 验证
    notice = Element(xpath='//div[@class="ant-message-notice-content"]/div/span[2]', describe='h5页面创建成功提示')
    table_first_name = Element(xpath='//tbody/tr[2]/td[3]', describe="第一条表记录实体名称")
    table_first_type = Element(xpath='//tbody/tr[2]/td[6]', describe="第一条表记录实体类型")

    btn_sel = Elements(xpath='//tr/td[text()="TestCategory"]/../td[2]//input[not(@checked)]', describe="选择按钮")
    btn_del = Element(xpath='//button[text()="删除"]', describe="删除按钮")
    btn_ok = Element(xpath='//button/span[text()="确 定"]', describe="确定按钮")