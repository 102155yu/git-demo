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

@allure.epic('LES系统APP端')
@allure.feature('技术员APP页面')
@allure.story('填写工序数据')
@allure.title('技术员填写工序数据')
@allure.severity('critical')
def test_login02(browser):
    """
        用例编号：test_loin02
            用例标题：技术员填写工序数据
            前置条件：法兰添加了检修范围生成了工序任务
            测试步骤：
                1.登录技术员账号
                2.填写对应工序任务信息
                3.提交工序任务
                4.完成工序任务

            预期结果；工序任务提交无报错

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