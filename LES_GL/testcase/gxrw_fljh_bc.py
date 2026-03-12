#应用POM模式实现登录
import time
import pyautogui
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
@allure.story('填写法兰校核工序数据')
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
    # ========== 新增：窗口最大化 + 按F12键 ==========
    with allure.step('窗口最大化并按下F12键'):
        # 1. 窗口最大化（pyautogui模拟win+向上箭头，适配Windows系统）
        pyautogui.hotkey('win', 'up')

    #初始化页面对象
    #实例化Wait
    wait = WebDriverWait(browser,10)
    wk = WebKeys(browser)
    #进入登录
    with allure.step('进入APP端'):
        login_app = LoginPage(browser)
        login_app.loginapp(LOGIN_URL_APP, USERNAME_CZG_YJA, PASSWD)

        time.sleep(2)
    #进入定力矩服务，点击工序处理
    with allure.step('点击工序处理'):
        wk.locator(*allPages.app_dljfw_gxcl).click()

        time.sleep(2)
    #选择对应项目
    with allure.step('点击项目名称'):
        wk.locator(*allPages.app_gxcl_xmmc).click()
        time.sleep(2)
    #输入项目名称
    with allure.step('选择项目'):
        wk.locator(*allPages.app_gxcl_xmmc_srk).click()
        time.sleep(2)
    with allure.step('点击待处理'):
        wk.locator(*allPages.app_dljfw_gxcl_dcl).click()

    #进入待处理页面点击任务
    with allure.step('点击任务'):
        wk.locator(*allPages.app_dljfw_gxcl_dcl_dj_01).click()

    #跳转至工序任务页面
        #法兰校核页面
        #点击法兰校核页签
    with allure.step('点击法兰校核页签'):
        wk.locator(*allPages.app_gxrw_fljh).click()
        # 关键等待：给弹窗加载留足够时间（可根据实际情况调整秒数）
        #点击输入工具数量
    with allure.step('点击输入工具数量'):
        wk.locator(*allPages.app_gxrw_fljh_gjsl).send_keys(2)
        #点击输入扭矩值
    with allure.step('点击输入扭矩值'):
        wk.locator(*allPages.app_gxrw_fljh_njz).click()
        #点击输入平行公差
    with allure.step('点击输入平行公差'):
        wk.locator(*allPages.app_gxrw_fljh_pxgc).click()
        # 平行公差填写
    with allure.step('平行公差填写'):
        wk.locator(*allPages.app_gxrw_fljh_pxgc_qd).click()

        #点击签字
    with allure.step('点击签字'):
        wk.locator(*allPages.app_gxrw_fljh_qm).click()
        #调整成手机模式
    with allure.step('调整成手机模式'):

        pyautogui.press("F12")
        time.sleep(2)
        pyautogui.hotkey('ctrl', 'shift', 'm')
        time.sleep(2)
        #定位签字框
    with allure.step("定位签字框"):
        wk.locator(*allPages.app_gxrw_fljh_qm_qmk).click()
        clickable = browser.find_element(By.ID,"click")
        ActionChains(browser)\
            .click(clickable)\
            .move_by_offset(13,15)\
            .perform()
        time.sleep(5)


    # #点击提交按钮提交任务
    # with allure.step('点击提交任务'):
    #     wk.locator(*allPages.app_gxrw_wgqr_tj).click()
    #点击保存按钮保存任务
    with allure.step('点击保存任务'):
        wk.locator(*allPages.app_gxrw_mfmjc_bc).click()
        time.sleep(3)
    #点击法兰挂牌页签
    with allure.step('点击页签法兰挂牌'):
        wk.locator(*allPages.app_gxrw_flgp).click()

        # 点击法兰校核页签
    with allure.step('点击法兰校核页签'):
        wk.locator(*allPages.app_gxrw_fljh).click()

    time.sleep(10)
