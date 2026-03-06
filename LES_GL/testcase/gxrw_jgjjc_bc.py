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
@allure.story('填写紧固件检查工序数据')
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
        #紧固件检查页面
        #点击紧固件检查页签
    with allure.step('点击紧固件检查页签'):
        wk.locator(*allPages.app_gxrw_jgjjc).click()
        # 关键等待：给弹窗加载留足够时间（可根据实际情况调整秒数）
        # 点击螺栓螺母照片上传照片
    with allure.step('点击螺栓螺母照片上传照片'):
        wk.locator(*allPages.app_gxrw_jgjjc_lslmzp).click()
        time.sleep(2)
        # 输入图片路径并按回车确认（模拟手动输入文件地址）
    with allure.step('输入图片路径并确认上传'):
            # 输入图片绝对路径，r前缀避免反斜杠转义
        pyautogui.typewrite(r'C:\Users\chens\Pictures\1.jpg', interval=0.1)
            # 连续按3次回车（适配弹窗的确认逻辑）
        pyautogui.press(keys='ENTER', presses=3)
        time.sleep(2)

    # #点击提交按钮提交任务
    # with allure.step('点击提交任务'):
    #     wk.locator(*allPages.app_gxrw_flgp_tj).click()
    #点击保存按钮保存任务
    with allure.step('点击保存任务'):
        wk.locator(*allPages.app_gxrw_jgjjc_bc).click()
        time.sleep(3)
    #点击法兰挂牌页签
    with allure.step('点击页签法兰挂牌'):
        wk.locator(*allPages.app_gxrw_flgp).click()

        # 点击紧固件检查页签
    with allure.step('点击紧固件检查页签'):
        wk.locator(*allPages.app_gxrw_jgjjc).click()

    time.sleep(10)
