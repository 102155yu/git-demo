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
@allure.feature('登录')
@allure.story('典型场景')
@allure.title('专工创建计划')
@allure.severity('critical')
def test_login02(browser):
    """
        用例编号：test_loin02
            用例标题：登录
            前置条件：登录
            测试步骤：
                1登录进入首页
                2.选择服务计划管理菜单
                3.点击定力矩服务计划菜单
                4.点击添加定力矩服务计划
                5.下派成功

            预期结果；专工建立计划下派成功

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
    jy = GxrwJymsExecutor(browser)

    #进入登录
    with allure.step('进入LES登录页'):
        login = LoginPage(browser)
        login.login(LOGIN_URL_PC, USERNAME_zg_YJA, PASSWD)
    time.sleep(1)

    #定位基础数据管理
    with allure.step('定位基础数据管理'):

        wk.locator(*allPages.jcsjgl).click()

    # 点击服务商管理
    with allure.step('点击服务商管理'):
        wk.locator(*allPages.jcsjgl_fwsgl).click()

    #添加服务商
    with allure.step('添加服务商'):
        jy.execute_full_zg_fwsgl_flow()


