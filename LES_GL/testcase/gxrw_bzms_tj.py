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

    #进入待处理页面点击任务
    with allure.step('点击任务'):
        wk.locator(*allPages.app_dljfw_gxcl_dcl_dj_01).click()
        time.sleep(2)
    #跳转至工序任务页面
        #SOP确认页面
        #点击SOP确认页签
    with allure.step('提交工序：法兰挂牌'):
        jyms_executor.execute_full_gxrw_flgp_flow()
    with allure.step('提交工序：法兰拆卸'):
        jyms_executor.execute_full_gxrw_flcx_flow()
    with allure.step('提交工序：密封面检查'):
        jyms_executor.execute_full_gxrw_mfmjc_flow()
    with allure.step('提交工序：垫片检查'):
        jyms_executor.execute_full_gxrw_dpjc_flow()
    with allure.step('提交工序：紧固件检查'):
        jyms_executor.execute_full_gxrw_jgjjc_flow()
    with allure.step('提交工序：预装确认'):
        jyms_executor.execute_full_gxrw_yzqr_flow()
    with allure.step('提交工序：SOP确认'):
        jyms_executor.execute_full_gxrw_sopqr_flow()
    with allure.step('提交工序：法兰抽检'):
        jyms_executor.execute_full_gxrw_flcj_flow()
    with allure.step('提交工序：完工确认'):
        jyms_executor.execute_full_gxrw_wgqr_flow()
    with allure.step('提交工序：法兰校核'):
        jyms_executor.execute_full_gxrw_fljh_flow()
    with allure.step('提交工序：螺栓抽检'):
        jyms_executor.execute_full_gxrw_lscj_flow()

    time.sleep(10)
