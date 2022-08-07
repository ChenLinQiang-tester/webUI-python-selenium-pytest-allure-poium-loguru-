import os
import time

import pytest
from shutil import copyfile

from common.config import PathConfig
from utils.dateUtils.get_date import GetDate

now_time = GetDate().get_now_time("%Y-%m-%d_%H-%M_%S")

root_path = PathConfig.root_path  # 项目根路径
cases_path = PathConfig.case_path  # 测试用例路径
common_path = PathConfig.common_path  # 公共文件路径
report_path = os.path.join(PathConfig.report_path, now_time)  # 测试报告路径
html_path = os.path.join(report_path, 'html')  # 测试报告html文件夹路径

now_time = time.strftime("%Y-%m-%d %H.%M.%S", time.localtime())

pytest.main(["-v", "-s",
             "--reruns-delay=2",
             r"--alluredir=" + report_path,
             "--clean-alluredir"])

# 复制测试环境信息到测试报告目录下
copyfile(common_path + "/environment.properties", report_path + "/environment.properties")
os.system('allure generate ' + report_path + ' --clean -o ' + html_path)  # -o 参数是将报告内容保存到指定的文件夹下 -c接目录，清理上次的报告数据
