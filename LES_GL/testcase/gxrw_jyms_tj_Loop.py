# 应用POM模式实现登录
import time
import pyautogui
import allure
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException

from LES_GL.VAR.BOOKHOUSER_VAR import *
from LES_GL.key_word.keyword import WebKeys
from LES_GL.locate import allPages
from LES_GL.locate.allPages import *
from LES_GL.page.login import *


@allure.epic('LES系统APP端')
@allure.feature('技术员APP页面')
@allure.story('填写简易模式数据')
@allure.title('技术员填写简易工序数据（循环10次）')
@allure.severity('critical')
def test_login02(browser):
    """
        用例编号：test_loin02
            用例标题：技术员填写工序数据（循环10次）
            前置条件：法兰添加了检修范围生成了工序任务
            测试步骤：
                1.登录技术员账号
                2.循环10次执行：
                    a.点击待处理任务
                    b.提交密封面检查、垫片检查、紧固件检查、SOP确认、完工确认工序
            预期结果；每次工序任务提交无报错

    :param browser:
    :return:
    """
    # 窗口最大化操作（核心新增）
    # ========== 新增：窗口最大化 + 按F12键 ==========
    with allure.step('窗口最大化'):
        # 1. 窗口最大化（pyautogui模拟win+向上箭头，适配Windows系统）
        pyautogui.hotkey('win', 'up')

    # 初始化页面对象
    # 实例化Wait
    wait = WebDriverWait(browser, 10)
    wk = WebKeys(browser)
    jyms_executor = GxrwJymsExecutor(browser)
    # 进入登录
    with allure.step('进入APP端'):
        login_app = LoginPage(browser)
        login_app.loginapp(LOGIN_URL_APP, USERNAME_CZG_WS, PASSWD)
        time.sleep(2)

    # 进入定力矩服务，点击工序处理
    with allure.step('点击工序处理'):
        wk.locator(*allPages.app_dljfw_gxcl).click()
        time.sleep(2)

    with allure.step('点击待处理'):
        wk.locator(*allPages.app_dljfw_gxcl_dcl).click()

    # 定义单次任务执行函数（封装核心流程）
    def execute_single_task(cycle_num):
        """执行单次任务流程：点击任务 + 提交所有工序"""
        with allure.step(f'第{cycle_num}次循环 - 点击任务'):
            # 显式等待任务元素可点击，提升稳定性
            wait.until(EC.element_to_be_clickable(allPages.app_dljfw_gxcl_dcl_dj_01)).click()
            time.sleep(2)

        # 提交密封面检查工序
        with allure.step(f'第{cycle_num}次循环 - 提交工序：密封面检查'):
            jyms_executor.execute_full_gxrw_mfmjc_flow()
        # 提交垫片检查工序
        with allure.step(f'第{cycle_num}次循环 - 提交工序：垫片检查'):
            jyms_executor.execute_full_gxrw_dpjc_flow()
        # 提交紧固件检查工序
        with allure.step(f'第{cycle_num}次循环 - 提交工序：紧固件检查'):
            jyms_executor.execute_full_gxrw_jgjjc_flow()
        # 提交SOP确认工序
        with allure.step(f'第{cycle_num}次循环 - 提交工序：SOP确认'):
            jyms_executor.execute_full_gxrw_sopqr_flow()
        # 提交完工确认工序
        with allure.step(f'第{cycle_num}次循环 - 提交工序：完工确认'):
            jyms_executor.execute_full_gxrw_wgqr_flow()

    # 循环10次执行核心任务流程
    for cycle in range(1, 11):
        try:
            execute_single_task(cycle)
            # 可选：每次循环后短暂等待，确保页面恢复至待处理状态（根据实际场景调整）
            time.sleep(2)
        except Exception as e:
            # 捕获单次循环异常，记录日志但不中断后续循环
            allure.attach(
                f'第{cycle}次循环执行失败：{str(e)}',
                name=f'第{cycle}次循环异常',
                attachment_type=allure.attachment_type.TEXT
            )
            print(f"第{cycle}次循环执行失败：{e}")

    time.sleep(10)