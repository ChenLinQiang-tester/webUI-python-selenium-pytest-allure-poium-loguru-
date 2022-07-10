from os.path import dirname, abspath, join

base_path = dirname(abspath(__file__))


class RunConfig:
    """
    自媒体web端运行测试配置
    """
    # 要运行的测试用例的目录或文件
    cases_path = join(base_path, 'scripts')
    # 配置浏览器驱动类型
    driver_type = 'chrome'
    # 失败重跑次数
    rerun = 2
    # 当达到最大失败数时，停止执行
    max_fail = '5'
    # 报告路径
    report_path = join(base_path, 'allure-report')
    # 接收浏览器驱动
    driver = None
    # 项目路径
    base_path = base_path
    # 企业平台登录url
    ep_url = "https://5G.fontdo.com/test/enterprise//#/login"
    # 管理平台登录URL
    pf_url = ""

    def set_rerun(self, num):
        self.rerun = num


if __name__ == '__main__':
    test = RunConfig()
    print(test.cases_path)
    print(test.report_path)
