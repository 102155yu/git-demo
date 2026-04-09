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


# 封装核心业务流程为独立函数（便于循环调用）
def execute_main_process(browser):
    """
    封装检修计划管理的核心业务流程
    :param browser: 浏览器驱动实例
    """
    # 初始化页面对象
    wait = WebDriverWait(browser, 10)
    wk = WebKeys(browser)
    LES = GxrwJymsExecutor(browser)

    try:
        with allure.step('进入LES登录页（专工账号）'):
            login = LoginPage(browser)
            login.login(LOGIN_URL_PC, USERNAME_zg_YJA, PASSWD)
        # 替换硬编码sleep为显式等待（更稳定）
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        with allure.step('退出登录（专工账号）'):
            LES.execute_full_log_out_flow()

        with allure.step('进入APP端（设备员账号）'):
            login_app = LoginPage(browser)
            login_app.loginapp(LOGIN_URL_APP, USERNAME_CZG_YJA, PASSWD)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        with allure.step("进入任务页面"):
            LES.execute_full_jrgxcl_flow()

        with allure.step("做标准工序任务"):
            LES.execute_full_standard_mode_flow()

        with allure.step("查看已完成项目是否提交成功"):
            LES.execute_full_verification_flow()

        allure.attach("第{}次执行成功".format(execution_count), "执行结果", allure.attachment_type.TEXT)

    except Exception as e:
        # 捕获异常并记录到Allure报告
        allure.attach(f"执行失败：{str(e)}", "异常信息", allure.attachment_type.TEXT)
        raise e  # 抛出异常，不中断整体循环（也可根据需求调整）


@allure.epic('LES系统')  # 标记大模块 / 系统级的测试范围，通常对应产品的一个大方向
@allure.feature('主要流程')  # 标记功能模块，是 Epic 下的子分类，用于聚合一类相关功能
@allure.story('检修计划管理')  # 标记用户故事 / 具体功能点，是 Feature 下更细粒度的业务场景
@allure.title('主要流程验证（循环执行10遍）')  # 为测试用例设置可读性强的标题
@allure.severity('critical')  # 标记用例优先级 / 严重程度
def test_login02(browser):
    """
        用例编号：test_loin02
            用例标题：主要流程验证（循环执行10遍）
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
    :param browser: 浏览器驱动（由pytest-fixture传入）
    :return:
    """
    # 窗口最大化（前置操作）
    with allure.step('浏览器窗口最大化'):
        browser.maximize_window()

    # 定义循环次数
    total_executions = 5
    global execution_count  # 全局变量，用于记录当前执行次数

    # 循环执行核心流程
    for execution_count in range(1, total_executions + 1):
        with allure.step(f'开始执行第{execution_count}次核心流程'):
            execute_main_process(browser)
            # 每次执行后短暂等待（避免系统压力过大，可根据实际调整）
            time.sleep(2)

    # 最终等待（便于观察结果，可根据需求删除）
    time.sleep(5)