from poium import Page, Element, Elements


class PageProduct(Page):
    menu_billing = Element(xpath='//div[@class="ant-menu-submenu-title"]/span[text()="计费"]', describe='计费')
    menus_product = Elements(css='li[title="产品管理"]', describe='判断产品管理子菜单是否存在')
    menu_product = Element(css='li[title="产品管理"]', describe='产品管理子菜单')
    btn_create = Element(xpath='//button[text()="创建商品"]', describe="创建商品按钮")
    sel_type = Element(id_='type', describe="商品类别选择框")
    type = Element(xpath='//div[@class="ant-select-item-option-content" and text()="能力调用"]', describe="能力调用类型")
    sel_subType = Element(id_="subType", describe="商品类型选择框")
    ipt_name = Element(css='input[placeholder="在这里输入商品名称"]', describe="商品名称输入框")
    ipt_description = Element(id_="description", describe="商品描述输入框")
    ipt_image = Element(id_='mainImageUrls', describe="商品图片上传框")
    ipt_detail = Element(css='div[class="notranslate public-DraftEditor-content"]', describe="商品详情")
    btn_next = Elements(xpath='//button[text()="下一步"]', describe="下一步按钮")
    ipt_validDays = Element(id_='availableDays', describe="商品有效期输入框")
    ipt_validCount = Element(id_='validCount', describe="商品条数输入框")
    ipt_price = Element(id_="price", describe="商品价格输入框")
    btn_add_rule = Element(xpath='//button[text()="添加"]', describe="添加按钮")
    btn_submit = Element(xpath='//button[text()="提交"]', describe="提交按钮")
    ipt_availableEp = Element(id_='validEnterpriseIds', describe="可用企业输入框")
    notice = Element(xpath='//div[@class="ant-message-notice-content"]/div/span[2]', describe='修改成功提示')
    product_name = Element(xpath='//tbody/tr[2]/td[2]', describe="表格商品名称")
    btn_putaway = Element(xpath='//tbody/tr[2]/td[last()]/div[@class="ant-space ant-space-horizontal ant-space-align-center"]/div[1]',
                          describe="上架按钮")
    product_status = Element(xpath='//tbody/tr[2]/td[5]//span[@class="ant-badge-status-text"]', describe="表格商品状态")
