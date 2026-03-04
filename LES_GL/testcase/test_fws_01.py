#应用POM模式实现登录
import time

import allure
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

from LES_GL.VAR.BOOKHOUSER_VAR import *
from LES_GL.key_word.keyword import WebKeys
from LES_GL.locate import allPages
from LES_GL.locate.allPages import *
from LES_GL.page.login import *

@allure.epic('LES系统')
@allure.feature('服务商工作台')
@allure.story('项目立项确认-项目经理指定')
@allure.title('登录彭淦账号完成项目立项确认及项目经理选择')
@allure.severity('critical')
def test_login02(browser):
    """
        用例编号：test_loin02
            用例标题：项目立项确认-项目经理指定
            前置条件：设备员发布计划成功
            测试步骤：
                1.登录彭淦账号
                2.完成服务商工作台待办处理
                3.项目立项确认
                4.项目经理选择确认

            预期结果；项目立项成功，项目经理指定成功

    :param browser:
    :return:
    """
    # 窗口最大化操作（核心新增）
    with allure.step('浏览器窗口最大化'):
        browser.maximize_window()
    #初始化页面对象
    #实例化Wait
    wait = WebDriverWait(browser,10)
    wk = WebKeys(browser)
    #进入登录
    with allure.step('进入LES登录页'):
        login = LoginPage(browser)
        login.login(LOGIN_URL_PC, USERNAME_XMFZR_PG, PASSWD)
    time.sleep(1)


    # 点击待办处理
    with allure.step('点击待办处理'):
        wk.locator(*allPages.sby_gzt_db_cl).click()

    #进入项目立项确认页面，点击下一步
    with allure.step('点击下一步'):
        wk.locator(*allPages.fws_fzr_lxqr_xyb).click()

    #进行人员配置页面点击项目经理选择框
    with allure.step("选择项目经理"):
        wk.locator(*allPages.fws_fzr_lxqr_xmjl).click()
        ActionChains(browser)\
            .key_down(Keys.DOWN)\
            .key_down(Keys.DOWN)\
            .key_down(Keys.ENTER)\
            .perform()
    #点击确认按钮
    with allure.step('点击确认按钮'):
        wk.locator(*allPages.fws_fzr_lxqr_qr).click()