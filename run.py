import os
import pytest

if __name__ == '__main__':
    pytest.main(['-vs'])
    # # 生成allure报告
    # pytest.main(['-vs', '--reruns=2', './testcase', '--allure dir', './temp', '--clean-allure dir'])
    # os.system("allure generate ./temp -o ./report --clean")
