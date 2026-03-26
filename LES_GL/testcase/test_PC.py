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


@allure.epic('LES系统')#标记大模块 / 系统级的测试范围，通常对应产品的一个大方向
@allure.feature('主要流程')#标记功能模块，是 Epic 下的子分类，用于聚合一类相关功能
@allure.story('检修计划管理')#标记用户故事 / 具体功能点，是 Feature 下更细粒度的业务场景
@allure.title('主要流程验证')#为测试用例设置可读性强的标题，在报告中直接展示，便于快速理解用例目的
@allure.severity('critical')#标记用例优先级 / 严重程度，用于区分测试重点
def test_login02(browser):
    """
        用例编号：test_loin02
            用例标题：主要流程验证
            前置条件：系统为最新状态
            测试步骤：
                1.登录专工账号创建计划
                2.创建完成退出登录
                3.登录设备员下发计划
                4.下发计划成功后退出登录
                5.登录服务商负责人配置项目经理
                6.项目经理创建成功后退出登录
                7.登录项目经理账号进行人员信息配置
                8.项目经理下派具体任务
                9.操作员完成任务
                10.项目经理推送法兰至设备员确认
                11.设备确认检修数据
                12.项目经理上传结项数据进行结项
                13.设备员进行结项审批
                14.审批完成结项完成流程结束

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
    #点击服务过程管理
    with allure.step("点击服务过程管理"):
        wk.locator(*allPages.fwgcgl).click()
    #点击定力矩服务
    with allure.step("点击定力矩服务"):
        wk.locator(*allPages.fwgcgl_dljfw).click()
    #点击任务管理
    with allure.step("点击任务管理"):
        wk.locator(*allPages.rwgl).click()
    #点击任务发布
    with allure.step("点击任务发布"):
        wk.locator(*allPages.rwfb).click()
    time.sleep(3)
    #点击勾选全部任务
    with allure.step("勾选全部"):
        wk.locator(*allPages.rwfb_check_all).click()
    time.sleep(3)
    #点击下派
    with allure.step("点击下派"):
        wk.locator(*allPages.rwfb_xp).click()
    #点击负责人下拉框
    with allure.step("点击负责人选项框"):
        wk.locator(*allPages.rwfb_xp_fzrxxk).click()
        ActionChains(browser) \
            .send_keys("余家傲")\
            .key_down(Keys.DOWN)\
            .key_down(Keys.ENTER)\
            .perform()
    #点击确定
    with allure.step("点击确定"):
        wk.locator(*allPages.rwfb_xp_sure).click()

    time.sleep(10)