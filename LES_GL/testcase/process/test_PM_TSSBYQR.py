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
from LES_GL.page.process import *


@allure.epic('LES系统')
@allure.feature('项目经理工作台')
@allure.story('推送设备员确认')
@allure.title('推送设备员确认')
@allure.severity('critical')
def test_login02(browser):
    """
        用例编号：test_loin02
            用例标题：项目经理配置项目信息
            前置条件：服务商负责人配置完成项目经理
            测试步骤：
                1.登录项目经理账号
                2.点击工作台待办处理
                3.项目配置项目成员
                4.添加法兰进入检修范围
                5.提交至设备员确认

            预期结果；项目成员配置成功，法兰添加成功

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
    mj = GxrwJymsExecutor(browser)
    #进入登录
    with allure.step('进入LES登录页'):
        login = LoginPage(browser)
        login.login(LOGIN_URL_PC, USERNAME_XMJL_PM, PASSWD)
    time.sleep(1)

    #服务过程管理菜单
    with allure.step('服务过程管理菜单'):
        wk.locator(*allPages.fwgcgl).click()
    #点击定力矩服务菜单
    with allure.step('点击定力矩服务菜单'):
        wk.locator(*allPages.fwgcgl_dljfw).click()
    # 点击项目管理菜单
    with allure.step('点击项目管理菜单'):
        wk.locator(*allPages.fwgcgl_dljfw_xmgl).click()
    #进入项目管理页面点击查看按钮
    with allure.step('进入项目管理页面点击查看按钮'):
        wk.locator(*allPages.fwgcgl_dljfw_xmgl_ck).click()

    #进入项目页面点击推送设备员确认
    with allure.step('进入项目页面点击推送设备员确认'):
        wk.locator(*allPages.xmgl_tssby).click()
    #点击推送按钮
    with allure.step('点击推送按钮'):
        wk.locator(*allPages.xmgl_tssby_ts).click()

    #勾选法兰进行推送
    with allure.step('勾选法兰'):
        wk.locator(*allPages.xmgl_tssby_ts_qx).click()

    #点击确定
    with allure.step('点击确定'):
        wk.locator(*allPages.xmgl_tssby_ts_qd).click()

    #点击返回推送成功
    with allure.step('点击返回推送成功'):
        wk.locator(*allPages.xmgl_tssby_fh).click()



