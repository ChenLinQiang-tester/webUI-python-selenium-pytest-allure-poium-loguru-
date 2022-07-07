import allure
import pytest


@pytest.mark.skip()
@allure.title("自动化测试结束！")
def test_end():
    print("自动化测试结束！")