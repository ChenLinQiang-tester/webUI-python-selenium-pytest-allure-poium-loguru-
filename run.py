import os
import sys
import time
import pytest

from os.path import join
from shutil import copyfile
from config import RunConfig


now_time = time.strftime("%Y-%m-%d %H.%M.%S", time.localtime())
with open(RunConfig.base_path+'/tool/code_file/img_name.txt', 'w') as f:
        f.write(now_time)

report_path = join(RunConfig.base_path, "allure-report")  # 测试报告路径
cases_path = join(RunConfig.base_path, "cases")           # 测试用例路径
html_path = join(report_path, 'html')                     # 测试报告html文件夹路径

sys.path.insert(0, RunConfig.base_path)  # 将项目路径添加到系统

pytest.main(["-v", "-s", '-k', "001",
             # "--reruns=0",
             "--reruns-delay=2",
             "--alluredir="+report_path,
             "--clean-alluredir"])
# 复制测试环境信息到测试报告目录下
copyfile(RunConfig.base_path+"/data/environment.properties", RunConfig.base_path+"/allure-report/environment.properties")
os.system('allure generate '+report_path +' --clean -o '+html_path)  # -o 参数是将报告内容保存到指定的文件夹下 -c接目录，清理上次的报告数据
