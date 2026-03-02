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
    #进入登录
    with allure.step('进入LES登录页'):
        login = LoginPage(browser)
        login.login(LOGIN_URL, USERNAME_XMJL_LQ, PASSWD)
    time.sleep(1)


    # 点击待办处理
    with allure.step('点击待办处理'):
        wk.locator(*allPages.sby_gzt_db_cl).click()

    # 点击处理弹窗确认按钮
    with allure.step('点击处理弹窗确认按钮'):
        wk.locator(*allPages.xmjl_gzt_db_ts_qr).click()

    #进入项目管理页面
        #点击成员配置按钮
    with allure.step('点击成员配置按钮'):
        wk.locator(*allPages.xmgl_cypz).click()
    #进入成员配置页面
        #点击添加
    with allure.step('点击添加'):
        wk.locator(*allPages.xmgl_cypz_tj).click()
        #进入添加页面
            #点击下拉按钮
    with allure.step('点击下拉按钮'):
        wk.locator(*allPages.xmgl_cypz_tj_xl).click()
        #选择第三个人员勾选
    with allure.step('勾选第三个人员'):
        wk.locator(*allPages.xmgl_cypz_tj_03).click()
        #点击确定
    with allure.step('点击确定'):
        wk.locator(*allPages.xmgl_cypz_tj_qd).click()
        #点击返回
    with allure.step('点击返回'):
        wk.locator(*allPages.xmgl_cypz_fh).click()
    #点击检修范围
    with allure.step('点击检修范围按钮'):
        wk.locator(*allPages.xmgl_jxfw).click()

    #进入检修范围页面
        #点击下一页
    # with allure.step('点击下一页'):
    #     wk.locator(*allPages.xmgl_jxfw_xyy).click()
    #     # 点击下一页
    # with allure.step('点击下一页'):
    #     wk.locator(*allPages.xmgl_jxfw_xyy).click()
        #选择第一个法兰点击勾选
    with allure.step('点击勾选第一个法兰'):
        wk.locator(*allPages.xmgl_jxfw_gx_01).click()
        #点击提交
    with allure.step('点击提交'):
        wk.locator(*allPages.xmgl_jxfw_tj).click()
    #弹出确认框
        #点击确定
    with allure.step('点击确定'):
        wk.locator(*allPages.xmgl_jxfw_tj_qr).click()

    # #进行人员配置页面点击项目经理选择框
    # with allure.step("选择项目经理"):
    #     wk.locator(*allPages.fws_fzr_lxqr_xmjl).click()
    #     ActionChains(browser)\
    #         .key_down(Keys.DOWN)\
    #         .key_down(Keys.DOWN)\
    #         .key_down(Keys.ENTER)\
    #         .perform()
    # #点击确认按钮
    # with allure.step('点击确认按钮'):
    #     wk.locator(*allPages.fws_fzr_lxqr_qr).click()