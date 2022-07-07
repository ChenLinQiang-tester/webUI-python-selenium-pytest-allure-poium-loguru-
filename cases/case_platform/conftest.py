import os
from time import sleep

import allure
import pytest

from selenium import webdriver
from selenium.webdriver import Remote
from config import RunConfig
from config_pf import RunConfigPf


# 定义测试环境
@pytest.fixture(scope='function')
def base_url():
    return RunConfigPf.pf_url


# 启动浏览器
@pytest.fixture(scope='session')
def browser_pf():
    """
    定义全局浏览器驱动
    """
    global driver
    if RunConfig.driver_type == 'chrome':
        # 本地Chrome浏览器
        driver = webdriver.Chrome()
        driver.maximize_window()
    elif RunConfig.driver_type == 'firefox':
        # 本地Firefox浏览器
        driver = webdriver.Firefox()
        driver.maximize_window()
    elif RunConfig.driver_type == 'grid':
        # 通过远程节点运行
        driver = Remote(desired_capabilities=webdriver.DesiredCapabilities.FIREFOX.copy())
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
        driver.get("https://test.fontdo.com/platform/#/main/home")
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
