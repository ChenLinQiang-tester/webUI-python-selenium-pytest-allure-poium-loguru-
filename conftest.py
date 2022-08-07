import os
import allure
import pytest

from selenium import webdriver
from selenium.webdriver import Remote
from selenium.webdriver.chrome.options import Options as CH_Options
from selenium.webdriver.firefox.options import Options as FF_Options
from common.config import RunConfig, PathConfig, WebConfig

root_path = PathConfig.root_path
base_url = WebConfig.url


# 项目首页URL
@pytest.fixture(scope='function')
def base_url():
    return base_url


# 控制浏览器启动和关闭
@pytest.fixture(scope='session')
def browser():
    """
    全局定义浏览器驱动
    :return:
    """
    global driver

    if RunConfig.driver_type == "chrome":
        # 本地chrome浏览器
        driver = webdriver.Chrome()
        driver.maximize_window()

    elif RunConfig.driver_type == "firefox":
        # 本地firefox浏览器
        driver = webdriver.Firefox()
        driver.maximize_window()

    elif RunConfig.driver_type == "chrome-headless":
        # chrome headless模式
        chrome_options = CH_Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument("--window-size=1920x1080")
        driver = webdriver.Chrome(options=chrome_options)

    elif RunConfig.driver_type == "firefox-headless":
        # firefox headless模式
        firefox_options = FF_Options()
        firefox_options.headless = True
        driver = webdriver.Firefox(firefox_options=firefox_options)

    elif RunConfig.driver_type == "grid":
        # 通过远程节点运行
        driver = Remote(command_executor='http://localhost:4444/wd/hub',
                        desired_capabilities={
                              "browserName": "chrome",
                        })
        driver.set_window_size(1920, 1080)

    else:
        raise NameError("driver驱动类型定义错误！")

    RunConfig.driver = driver

    # # 所有用例执行接受后关闭浏览器
    yield driver
    driver.quit()
    print("\ntest end!")
    return driver


# # 关闭浏览器
# @pytest.fixture(scope='session', autouse=True)
# def browser_close():
#     yield driver
#     driver.quit()
#     print("\ntest end!")


# 用例调试时调用，跳过登录
@pytest.fixture(scope='session')
def debug_browser():
    """
    定义全局浏览器驱动
    """
    global debug_driver
    if RunConfig.driver_type == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument(r'--user-common-dir=C:\Users\Admin\Desktop\AutoTest\maap_v1\chromeData')
        options.add_argument("--profile-directory=Profile 22")
        debug_driver = webdriver.Chrome(options=options)
    else:
        raise NameError("调试模式需使用Chrome浏览器")
    # 所有用例执行接受后关闭浏览器
    yield debug_driver
    debug_driver.quit()
    print("\ntest end!")
    return debug_driver


# 判断运行结果并处理
@pytest.fixture(autouse=True)
def reset():
    # 控制台打印与用例路径换行
    print()
    yield
    # print("运行结果：" + case_result)
    if case_result != 'passed':
        driver.get(WebConfig.url)
        driver.refresh()


# 调用上一个用例的运行结果
@pytest.fixture(scope='function')
def last_result():
    return case_result


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    hook pytest失败
    :param item:
    :param call:
    :return:
    """
    global case_result
    # 执行所有其他钩子以获取报告对象
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call":
        case_result = rep.outcome
    # 只关注实际失败的测试调用, 不关心setup/teardown
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("../../failures") else "w"
        with open(root_path+"failures", mode) as f:
            if "tmpdir" in item.fixturenames:
                extra = " (%s)" % item.funcargs["tmpdir"]
            else:
                extra = ""
            f.write(rep.nodeid + extra + "\n")
        with allure.step('添加失败截图...'):
            allure.attach(driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)
