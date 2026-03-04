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
@allure.feature('设备员审核检修范围')
@allure.story('设备员查看检修范围并确认')
@allure.title('设备员登录账号查看项目经理提交的检修范围并确认')
@allure.severity('critical')
def test_login02(browser):
    """
        用例编号：test_loin02
            用例标题：设备员审核检修范围
            前置条件：项目经理提交检修范围至设备员
            测试步骤：
                1.登录设备员账号
                2.点击设备员工作台待办处理
                3.跳转至检修范围添加确认
                4.勾选同意的法兰点击同意
                5.检修范围确认结束

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
        login.login(LOGIN_URL_PC, USERNAME_sby_55, PASSWD)
    time.sleep(1)


    # 点击待办处理
    with allure.step('点击待办处理'):
        wk.locator(*allPages.sby_gzt_db_cl).click()

    #进入检修范围添加确认页面
    with allure.step('点击驳回'):#不勾选内容情况下点击驳回会同意所有选项
        wk.locator(*allPages.sby_gzt_db_jxfwqr_bh).click()

    #点击确认按钮
    with allure.step('点击确认按钮'):
        wk.locator(*allPages.sby_gzt_db_jxfwqr_bh_qr).click()