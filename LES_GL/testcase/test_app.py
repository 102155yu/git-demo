#应用POM模式实现登录
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
from LES_GL.page.process import GxrwJymsExecutor


@allure.epic('LES系统APP端')
@allure.feature('技术员APP页面')
@allure.story('填写标准工序数据')
@allure.title('技术员填写标准工序数据')
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
    # ========== 新增：窗口最大化 + 按F12键 ==========
    with allure.step('窗口最大化'):
        # 1. 窗口最大化（pyautogui模拟win+向上箭头，适配Windows系统）
        pyautogui.hotkey('win', 'up')

    #初始化页面对象
    #实例化Wait
    wait = WebDriverWait(browser,10)
    wk = WebKeys(browser)
    jyms_executor = GxrwJymsExecutor(browser)
    #进入登录
    with allure.step('进入APP端'):
        login_app = LoginPage(browser)
        login_app.loginapp(LOGIN_URL_APP, USERNAME_CZG_YJA, PASSWD)

        time.sleep(2)
    #进入定力矩服务，点击工序处理
    with allure.step('点击工序处理'):
        wk.locator(*allPages.app_dljfw_gxcl).click()

        time.sleep(2)
    # #选择对应项目
    # with allure.step('点击项目名称'):
    #     wk.locator(*allPages.app_gxcl_xmmc).click()
    #     time.sleep(2)
    # #输入项目名称
    # with allure.step('选择项目'):
    #     wk.locator(*allPages.app_gxcl_xmmc_srk).click()
    #     time.sleep(2)
    with allure.step('点击待处理'):
        wk.locator(*allPages.app_dljfw_gxcl_dcl).click()

    # #进入待处理页面点击任务
    # with allure.step('点击任务'):
    #     wk.locator(*allPages.app_dljfw_gxcl_dcl_dj_01).click()
    #     time.sleep(2)
    # #跳转至工序任务页面
    #     #SOP确认页面
    # with allure.step('提交工序：SOP确认'):
    #     jyms_executor.execute_full_gxrw_sopqr_flow()
    # 循环执行20次SOP确认提交流程
    for i in range(3):
        with allure.step(f'第{i + 1}次执行：点击任务'):
            # 每次循环都重新定位任务元素，避免元素失效
            try:
                task_element = wait.until(
                    EC.element_to_be_clickable(allPages.app_dljfw_gxcl_dcl_dj_01)
                )
                task_element.click()
                time.sleep(2)
            except (TimeoutException, ElementNotInteractableException) as e:
                allure.attach(f"第{i + 1}次点击任务失败: {str(e)}", name="错误信息",
                              attachment_type=allure.attachment_type.TEXT)
                continue

        # 跳转至工序任务页面
        # SOP确认页面
        with allure.step(f'第{i + 1}次执行：提交工序：SOP确认'):
            try:
                jyms_executor.execute_full_gxrw_sopqr_flow()
                allure.attach(f"第{i + 1}次SOP确认提交成功", name="执行结果",
                              attachment_type=allure.attachment_type.TEXT)
            except Exception as e:
                allure.attach(f"第{i + 1}次SOP确认提交失败: {str(e)}", name="错误信息",
                              attachment_type=allure.attachment_type.TEXT)
                # 失败后可以选择继续下一次循环或退出
                continue

        # 每次提交后等待，确保页面稳定后再进行下一次操作
        time.sleep(2)

    time.sleep(10)
