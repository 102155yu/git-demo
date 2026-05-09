import os

import pytest

def run():
    pytest.main(['-v','-s', # -v 显示详细日志 -s 显示打印信息
                 './testcase/test_sby_main_process.py',#测试用例路径
                 '--alluredir',
                 './result',
                 '--clean-alluredir' #清理上次测试结果  每次是最新的数据 固定代码
                 ])
    # os.system('allure generate ./result/ -o ./report/ --clean')
    os.system('allure generate ./result/ -o ./report_allure/ --clean') #固定代码


if __name__ == '__main__':
    run()

