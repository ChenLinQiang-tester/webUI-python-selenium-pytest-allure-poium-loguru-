import os
import allure
import pytest

from selenium import webdriver as webdriver_sel
from selenium.webdriver import Remote
from cases.case_enterprise.config_ep import RunConfigEp
from config import RunConfig


@pytest.fixture(scope='function')
def base_url():
    return RunConfigEp.ep_url


# 启动浏览器
@pytest.fixture(scope='session')
def browser():
    """
    定义全局浏览器驱动
    """
    global driver
    if RunConfig.driver_type == 'chrome':
        # 本地Chrome浏览器
        driver = webdriver_sel.Chrome()
        # 调试
        # options = webdriver_sel.ChromeOptions()
        # options.add_argument(r'--user-data-dir=C:\Users\Admin\Desktop\AutoTest\maap_v1\chromeData')
        # options.add_argument("--profile-directory=Profile 22")
        # driver = webdriver_sel.Chrome(options=options)

        driver.maximize_window()
    elif RunConfig.driver_type == 'firefox':
        # 本地Firefox浏览器
        driver = webdriver_sel.Firefox()
        driver.maximize_window()
    elif RunConfig.driver_type == 'grid':
        # 通过远程节点运行
        driver = Remote(desired_capabilities=webdriver_sel.DesiredCapabilities.FIREFOX.copy())
    else:
        raise NameError("driver驱动类型定义错误")
    # 关闭浏览器
    yield driver
    # driver.quit()
    # print("\ntest end!")
    return driver


# 判断运行结果并处理
@pytest.fixture(autouse=True)
def reset():
    yield
    # print("运行结果：" + case_result)
    if case_result != 'passed':
        driver.get("https://5g.fontdo.com/enterprise//#/")
        driver.refresh()


# 调用上一个用例的运行结果
@pytest.fixture(scope='function')
def last_result():
    return case_result


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    '''
    hook pytest失败
    :param item:
    :param call:
    :return:
    '''
    global case_result
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call":
        case_result = rep.outcome
    # we only look at actual failing test calls, not setup/teardown
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("../../failures") else "w"
        with open(RunConfig.base_path+"/failures", mode) as f:
            # let's also access a fixture for the fun of it
            if "tmpdir" in item.fixturenames:
                extra = " (%s)" % item.funcargs["tmpdir"]
            else:
                extra = ""
            f.write(rep.nodeid + extra + "\n")
        # pic_info = adb_screen_shot()
        with allure.step('添加失败截图...'):
            allure.attach(driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)


"""# 获取用例运行结果
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport():
    global case_result
    # 获取钩子方法的调用结果
    out = yield 
    # 从钩子方法的调用结果中获取测试报告
    report = out.get_result()
    if report.when == "call":
        # print('测试报告：%s' % report)
        # print('步骤：%s' % report.when)
        # print('nodeid：%s' % report.nodeid)
        # print('description:%s' % str(item.function.__doc__))
        # print(('运行结果: %s' % report.outcome))
        case_result = report.outcome
        # if case_result == 'failed':
        #     driver.refresh()"""


"""@pytest.fixture(scope='session', autouse=True)
# @pytest.fixture(scope='session')
def browser_close():
    yield driver
    # driver.quit()
    print("\ntest end!")"""


# 自媒体web端重置页面
# @pytest.fixture(scope='class')
# def reset_mp():
#     print('前置')
#     a = 1
#     yield a
#     print("是否刷新")
    # if case_result == 'failed':
    #     driver.refresh()

# 自媒体web端重置页面
# @pytest.fixture(scope='function')
# def reset_mp(browser):
#     yield driver
#     driver.get(RunConfig.ep_url)
#     driver.refresh()


# 后台管理web端重置页面
# @pytest.fixture(scope='function')
# def reset_mis(browser):
#     yield driver
#     driver.get(RunConfig.pf_url)


# 启动安卓driver
# @pytest.fixture(scope='session')
# def android():
#     """定义全局安卓驱动"""
#     global driver_app
#     desired_caps = dict()
#     desired_caps['platformName'] = 'Android'
#     desired_caps['platformVersion'] = '6.0'
#     desired_caps['deviceName'] = 'leMax2'
#     desired_caps['appPackage'] = 'com.itcast.toutiaoApp'
#     desired_caps['appActivity'] = '.MainActivity'
#     desired_caps['unicodeKeyboard'] = True
#     desired_caps['resetKeyboard'] = True
#     driver_app = webdriver_app.Remote('http://localhost:4723/wd/hub', desired_caps)
#     yield driver_app
#     driver_app.quit()
#     print("\ntest end!")
#     return driver_app


# app重置页面
# @pytest.fixture(scope='function')
# def reset_app(android):
#     yield driver_app
#     if case_result == 'passed':
#         while True:
#             # 判断页面是否有"首页"元素，知道有为止
#             if len(driver_app.find_elements_by_xpath(
#                     '//*[@class="android.widget.ImageView" and contains(@text, "首页")]')) == 1:
#                 # 有：点击
#                 driver_app.find_element_by_xpath('//*[@class="android.widget.ImageView" and contains(@text, "首页")]').click()
#                 break
#             else:
#                 # 没有：返回
#                 driver_app.keyevent(4)
#             sleep(1)
#     # 如果用例失败则重启APP
#     elif case_result == 'failed':
#         driver_app.close_app()
#         driver_app.start_activity('com.itcast.toutiaoApp', '.MainActivity')
#         sleep(6)

