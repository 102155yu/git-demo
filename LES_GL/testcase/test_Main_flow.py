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
    LES = GxrwJymsExecutor(browser)
    #进入登录
    with allure.step('进入LES登录页'):
        login = LoginPage(browser)
        login.login(LOGIN_URL_PC, USERNAME_zg_YJA, PASSWD)
    time.sleep(1)

    with allure.step("专工下发计划"):
        LES.execute_full_zg_Plan_flow()

    with allure.step('退出登录'):
        LES.execute_full_log_out_flow()

    with allure.step("登录设备员账号"):
        login = LoginPage(browser)
        login.input_credential_and_login(USERNAME_sby_80, PASSWD)

    with allure.step("设备员确认计划 发布计划"):
        LES.execute_full_sby_fbjh_flow()

    with allure.step('退出登录'):
        LES.execute_full_log_out_flow()

    with allure.step("登录服务商负责人账号"):
        login = LoginPage(browser)
        login.input_credential_and_login(USERNAME_XMFZR_PG, PASSWD)

    with allure.step("服务商负责人添加项目经理"):
        LES.execute_full_fws_tjxmjl_flow()

    with allure.step('退出登录'):
        LES.execute_full_log_out_flow()

    with allure.step("登录项目经理账号"):
        login = LoginPage(browser)
        login.input_credential_and_login(USERNAME_XMJL_LQ, PASSWD)

    with allure.step("进入项目管理页面"):
        LES.execute_full_xmgl_xq_flow()

    with allure.step("成员配置添加所有成员进项目"):
        LES.execute_full_PM_cypz_flow()

    with allure.step("添加法兰到检修范围"):
        LES.execute_full_PM_pzjxfw_flow()

    with allure.step('退出登录'):
        LES.execute_full_log_out_flow()

    with allure.step("登录设备员账号"):
        login = LoginPage(browser)
        login.input_credential_and_login(USERNAME_sby_80, PASSWD)

    with allure.step("设备员通过检修数据确认"):
        LES.execute_full_sby_jxsjqr_flow()

    with allure.step('退出登录'):
        LES.execute_full_log_out_flow()

    with allure.step("登录项目经理账号"):
        login = LoginPage(browser)
        login.input_credential_and_login(USERNAME_XMJL_LQ, PASSWD)

    with allure.step('下派任务'):
        LES.execute_full_xmjl_xprw_flow()

    with allure.step("完成后关闭浏览器"):
        LES.close_browser(delay=3)

    with allure.step('进入APP端'):
        login_app = LoginPage(browser)
        login_app.loginapp(LOGIN_URL_APP, USERNAME_CZG_YJA, PASSWD)

        time.sleep(2)

    with allure.step("进入任务页面"):
        LES.execute_full_jrgxcl_flow()


    with allure.step("做标准工序任务"):
        LES.execute_full_xmjl_xprw_flow()

    with allure.step("完成后关闭浏览器"):
        LES.close_browser(delay=3)

    with allure.step('登录项目经理账号'):
        login = LoginPage(browser)
        login.login(LOGIN_URL_PC, USERNAME_XMJL_LQ, PASSWD)
    time.sleep(1)

    with allure.step("项目经理推送法兰至装置员"):
        LES.execute_full_PM_tssbyqr_flow()


    with allure.step('退出登录'):
        LES.execute_full_log_out_flow()

    with allure.step("登录设备员账号"):
        login = LoginPage(browser)
        login.input_credential_and_login(USERNAME_sby_80, PASSWD)


    with allure.step("设备员通过检修数据审核"):
        LES.execute_full_sby_jxsjqr_flow()

    with allure.step('退出登录'):
        LES.execute_full_log_out_flow()

    with allure.step("登录项目经理账号"):
        login = LoginPage(browser)
        login.input_credential_and_login(USERNAME_XMJL_LQ, PASSWD)

    with allure.step('上传结项资料'):
        LES.execute_full_xmgl_scjxzl_flow()

    with allure.step('点击结项申请'):
        LES.execute_full_xmgl_jx_flow()


    with allure.step('退出登录'):
        LES.execute_full_log_out_flow()

    with allure.step("登录设备员账号"):
        login = LoginPage(browser)
        login.input_credential_and_login(USERNAME_sby_80, PASSWD)

    with allure.step('设备员审批结项通过'):
        LES.execute_full_sby_jx_pass_flow()


    time.sleep(10)