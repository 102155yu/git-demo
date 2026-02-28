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
@allure.feature('设备员审核计划')
@allure.story('典型场景')
@allure.title('设备员审核计划')
@allure.severity('critical')
def test_login02(browser):
    """
        用例编号：test_loin02
            用例标题：设备员审核计划
            前置条件：专工下派计划成功
            测试步骤：
                1登录进入首页
                2.定位待办处理
                3.点击处理
                4.进入计划页面点击发布
                5.发布成功

            预期结果；设备员发布计划成功

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
        login.login(LOGIN_URL, USERNAME_sby_55, PASSWD)
    time.sleep(1)


    # 点击待办处理
    with allure.step('点击待办处理'):
        wk.locator(*allPages.sby_gzt_db_cl).click()

    #点击处理弹窗确认按钮
    with allure.step('点击处理弹窗确认按钮'):

        wk.locator(*allPages.sby_gzt_db_cl_qr).click()


    #发布专工的计划
    with allure.step("点击发布计划"):

        wk.locator(*allPages.sby_gzt_db_cl_fb).click()
