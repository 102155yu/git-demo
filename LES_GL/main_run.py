import os

import pytest

def run():
    pytest.main(['-s', './testcase/test_zzy_01.py', '--alluredir', './result', '--clean-alluredir'])
    # os.system('allure generate ./result/ -o ./report/ --clean')
    os.system('allure generate ./result/ -o ./report_allure/ --clean')


if __name__ == '__main__':
    run()