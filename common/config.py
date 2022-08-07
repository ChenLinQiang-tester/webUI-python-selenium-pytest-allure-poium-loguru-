import os


class WebConfig:
    """
    web项目配置
    """
    # 测试web地址
    url = "https://wanandroid.com/index"
    # 登录用户名
    username = "chenlq"
    # 登录密码
    password = "chenlq@2022"


class RunConfig:
    """
    运行配置
    """
    # 配置浏览器驱动类型(chrome/firefox/chrome-headless/firefox-headless)
    driver_type = 'chrome-headless'
    # 失败重跑次数
    rerun = 2
    # 当达到最大失败数时，停止执行
    max_fail = '5'
    # 接收浏览器驱动（不需要修改）
    driver = None


class PathConfig:
    """
    框架路径配置
    """
    _SLASH = os.sep
    # 项目路径
    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # 用例路径
    case_path = os.path.join(root_path, 'cases' + _SLASH)
    # 缓存路径
    cache_path = os.path.join(root_path, 'cache' + _SLASH)
    # 日志路径
    log_path = os.path.join(root_path, 'log' + _SLASH)
    # 测试报告路径
    report_path = os.path.join(root_path, 'allure-report' + _SLASH)
    # 公共配置路径
    common_path = os.path.join(root_path, 'common' + _SLASH)


if __name__ == '__main__':
    test = PathConfig()
    print("log:", test.log_path)
