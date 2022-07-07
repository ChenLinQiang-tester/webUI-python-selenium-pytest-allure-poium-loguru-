from poium import Element, Page, Elements


class PageMessage(Page):
    # 开头
    menu_message = Element(xpath='//div[@class="ant-menu-submenu-title"]/span[text()="消息模板"]', describe='消息模板')
    menus_template = Elements(xpath='//li//a[text()="我的模板"]', describe='判断消息模板菜单是否存在')
    menu_template = Element(xpath='//li//a[text()="我的模板"]', describe='消息模板菜单')
    btn_yes = Element(xpath='//button/span[text()="确 定"]', describe='确定按钮')
    btn_submit = Element(xpath='//button/span[text()="提交审核"]', describe='提交按钮')
    # create_message = Element(css='button[class="ant-btn ant-btn-primary"]', describe='创建消息模板')
    create_message = Element(xpath='//button/span[text()="创建"]', describe='创建消息模板')
    ipt_contentType = Element(xpath='//form[@class="ant-form ant-form-vertical"]//input[@id="contentType"]', describe='消息类型')
    sel_contentType = Element(css='[title="5G 消息"]', describe="消息类型选择5G消息")
    ipt_app = Element(xpath='//form[@class="ant-form ant-form-vertical"]//input[@id="applicationId"]', describe='应用选择框')
    sel_app = Element(css='[title="测试应用"]', describe='选择应用')
    # 结尾
    ipt_modeName = Element(css='input[placeholder="填写模板名称"]', describe='模板名称')
    btn_make = Element(xpath='//button/span[text()="消息制作器"]', describe='消息制作器按钮')
    # first_mode = Element(xpath='//div[@class="ant-row content--2ounj"]/div[1]//span[@class="title--WjcNL"]', describe='列表第一个模板')
    first_mode = Element(xpath='//div[@class="ant-row content--rNUrj"]/div[1]//span[@class="title--O7gZZ"]', describe='列表第一个模板')
    success_notice = Element(xpath='//div[@class="ant-message-notice-content"]/div/span[2]', describe='h5页面创建成功提示')

    # 文本消息模板
    btn_text = Element(xpath='//div[@id="MessageMaker"]/div[1]/div[2]', describe='文本消息按钮')
    ipt_text = Element(xpath='//div[@style="text-align: center;"]//textarea', describe='文本消息输入框')
    # 图片消息模板
    btn_picture = Element(xpath='//div[@class="ant-col ant-col-8"]/div[3]/span[@type="picture"]', describe='图片消息按钮')
    display_picture = Element(xpath='//div[@style="text-align: center;"]/div/div', describe='图片展示框')
    ipt_picture = Element(xpath='//tbody/tr[2]//input', describe='图片路径输入框')
    ipt_picture_xpath = '//tbody/tr[2]//input'
    # 语音消息模板
    btn_audio = Element(xpath='//div[@class="ant-col ant-col-8"]/div[4]/span[@type="audio"]', describe='语音消息按钮')
    display_audio = Element(css='div[style="text-align: center;"]>audio', describe='语音展示框')
    ipt_audio = Element(xpath='//tbody/tr//input', describe='语音路径输入框')
    ipt_audio_xpath = '//tbody/tr//input'
    # 视频消息模板
    btn_video = Element(xpath='//div[@class="ant-col ant-col-8"]/div[5]/span[@type="video-camera"]', describe='视频消息按钮')
    # 卡片消息模板
    btn_minus_square = Element(xpath='//div[@class="ant-col ant-col-8"]/div[6]/span[@type="minus-square"]', describe='卡片消息按钮')
    display_btn = Element(xpath='//*[@id="rc-tabs-0-panel-MAAP"]/div/div/div/div/div[2]/button[1]', describe='编辑卡片图片按钮')
    btn_media = Element(xpath='//tbody/tr[2]/td[3]//input/following-sibling::*[1]', describe='媒体库入口按钮')
    imgs = Elements(xpath='//div[text()="媒体库"]/../../following::*[1]//img', describe="媒体库第一个图片")
    btn_use_img = Element(xpath='//button[text()="使用这个文件"]', describe="【使用这个文件】按钮")
    ipt_square_img = Element(xpath='//tbody/tr[2]//input', describe="卡片图片路径输入框")
    ipt_square_img_xpath = '//tbody/tr[2]//input'
    ipt_square_title = Element(css='input[value="标题"]', describe='卡片标题输入框')
    ipt_square_describe = Element(css='textarea[placeholder="在这输入描述"]', describe='卡片描述输入框')
    btn_square_memu = Element(css='button[type="button"][class="ant-btn ant-btn-dashed"]', describe='添加卡片按钮')
    square_memu_reply = Element(xpath='//span[text()="回复信息" and @class="ant-menu-title-content"]', describe='卡片回复按钮')
    # 卡片轮播图模板
    btn_switcher = Element(xpath='//div[@class="ant-col ant-col-8"]/div[7]/span[@type="switcher"]', describe='卡片消息按钮')
    btn_add = Element(xpath='//div[@id="rc-tabs-3-panel-MAAP"]/div/div/button[2]', describe='添加多卡片')
    # H5卡片模板
    btn_h5 = Element(xpath='//div[@class="ant-col ant-col-8"]/div[8]/span[@type="html5"]', describe='h5卡片消息按钮')
    # H5卡片轮播图模板
    btn_h5s = Element(xpath='//div[@class="ant-col ant-col-8"]/div[9]/div[text()="H5 卡片轮播"]', describe='h5卡片轮播图按钮')
    # 地理位置模板
    btn_location = Element(xpath='//div[@class="ant-col ant-col-8"]/div[10]/div[text()="地理位置"]', describe="地理位置按钮")
    btn_change_location = Element(xpath='//button[text()="修改位置"]', describe='修改位置按钮')
    ipt_location = Element(xpath='//input[@placeholder="输入一个地名"]', describe='位置输入框')
    first_location = Element(xpath='//ul/li[@class="poibox"][1]', describe='搜索的第一个位置')
    btn_use_location = Element(xpath='//button/span[text()="使用这个"]', describe='“使用这个”位置按钮')
    # 浮动按钮
    btn_float_menu = Element(xpath='//div[@class="ant-col ant-col-8"]/div[11]/div[text()="浮动菜单"]', describe='浮动菜单按钮')
    btn_add_float_menu = Element(xpath='//div[@id="rc-tabs-0-panel-MAAP"]/div/div[2]/span', describe='添加浮动菜单按钮')
    sel_float_reply = Element(xpath='//li[@data-menu-id="rc-menu-uuid-21990-3-reply"]', describe="浮动菜单-回复信息")
    # btn_float_3x = Element(xpath='//span[@class="ant-tag ant-tag-has-color" and text()="拨打电话"]/span', describe='删掉拨打电话按钮')
