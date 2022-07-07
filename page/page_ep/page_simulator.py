from poium import Page, Element, Elements


class PageSimulator(Page):
    btn_simulator = Element(css='[class="block--13xVL"]>button[class="ant-btn ant-btn-text ant-btn-icon-only"]',
                            describe='模拟器按钮')
    iframe = Element(tag="iframe", describe="模拟器iframe")
    sel_app = Elements(css='[class="van-cell van-cell--clickable van-cell--center"]', describe="所有应用")
    enter_chat = Element(css='button[class="detail-content-action van-button van-button--info van-button--normal van-button--block"]',
                         describe="进入聊天")
    ipt_chat = Element(css='textarea[placeholder="在这里输入"]', describe="聊天输入框")
    btn_send = Element(css='button[class="van-button van-button--info van-button--normal im-action-button white square"]',
                       describe="发送按钮")
    message_content = Elements(css='[class="message"]>div', describe='消息内容')
    btn_close = Element(css='span[class="anticon anticon-poweroff"]', describe="关闭按钮")
    # ipt = Element(css='input[placeholder="请输入搜索关键字"]')