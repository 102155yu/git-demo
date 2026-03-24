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
@allure.story('配置项目信息')
@allure.title('项目经理配置项目信息')
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
        login.login(LOGIN_URL_PC, USERNAME_XMJL_LQ, PASSWD)
    time.sleep(1)

    #进入项目管理详情页面
    with allure.step('进入项目管理详情页面'):
        mj.execute_full_xmgl_xq_flow()

    #进入项目管理详情页面
    with allure.step('点击上传结项材料'):
        wk.locator(*allPages.xmgl_jx_scjxzl).click()

