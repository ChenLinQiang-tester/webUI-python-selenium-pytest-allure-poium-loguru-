from poium import Element, Page, Elements
from cases.case_enterprise.config_ep import RunConfigEp


class PageH5(Page):
    menu_message = Element(xpath='//div[@class="ant-menu-submenu-title"]/span[text()="消息模板"]', describe='消息平台')
    menus_h5 = Elements(xpath='//li//a[text()="H5 页面库"]', describe='判断H5页面库菜单是否存在')
    menu_h5 = Element(xpath='//li//a[text()="H5 页面库"]',  describe='H5页面库菜单')
    create_h5 = Element(css='button[type="button"][class="ant-btn ant-btn-primary"]', describe='新建h5按钮')
    ipt_app = Element(css='span[class="ant-select-selection-search"]>input', describe='选择应用')
    app = Element(css='[class="rc-virtual-list-holder-inner"]>div:nth-child(1)[title="测试应用"]', describe='测试应用')
    ipt_title = Element(id_="title", describe='标题输入框')
    # ipt_describt = Element(css='input[placeholder="在这里填写网页描述 ..."]', describe='描述输入框')
    # ipt_h5 = Element(css='.public-DraftStyleDefault-block', describe='h5编辑框')
    ipt_h5 = Element(css='div[role="textbox"]', describe='h5编辑框')
    # btn_media = Element(xpath='//div[@class="bf-dropdown control-item dropdown bf-emoji-dropdown"]/following-sibling::*[1]//div', describe='选择媒体库按钮')
    btn_media = Element(id_="10-2", describe='选择媒体库按钮')
    # img = Element(css='[alt="'+RunConfigEp.img_name+'.png"]', describe='定位媒体库刚上传的图片')
    img = Element(xpath='//div[text()="'+RunConfigEp.img_name+'.png"]', describe='定位媒体库刚上传的图片')
    # btn_use_img = Element(xpath='//div[@class="ant-drawer-wrapper-body"]//button[text()="使用这个文件"]', describe='文件使用按钮')
    btn_use_img = Element(xpath='//button/span[text()="使用这个文件"]', describe='文件使用按钮')
    # btn_submit = Element(css='button[type="submit"]', describe='提交按钮')
    btn_submit = Element(xpath='//button/span[text()="提 交"]', describe='提交按钮')
    success_notice = Element(xpath='//div[@class="ant-message-notice-content"]/div/span[2]', describe='h5页面创建成功提示')
    h5_title = Element(css='tbody>tr:nth-child(1)>td:nth-child(3)', describe='验证h5创建成功')