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

# 新增通用函数：等待元素可交互 + 无值则填写
def fill_if_empty(wait, wk, locator, fill_value, field_name):
    """
    :param wait: WebDriverWait实例
    :param wk: WebKeys实例
    :param locator: 元素定位器（元组）
    :param fill_value: 要填写的值
    :param field_name: 字段名称（用于报告/日志）
    """
    try:
        # 等待元素可交互（最长10秒），解决"未加载完成/不可交互"问题
        ele = wait.until(
            EC.element_to_be_clickable(locator)
        )
        # 聚焦到输入框（解决遮挡/未激活问题）
        ele.click()
        # 获取输入框当前值（兼容value属性/文本内容）
        current_value = ele.get_attribute('value') or ele.text or ''
        current_value = current_value.strip()

        if not current_value:
            # 清空原有空值（避免输入叠加）+ 输入值
            ele.clear()
            ele.send_keys(fill_value)
            allure.attach(f'{field_name}为空，已填写{fill_value}', '操作说明')
        else:
            allure.attach(f'{field_name}已有值：{current_value}，无需填写', '操作说明')
    except TimeoutException:
        allure.attach(f'{field_name}元素超时未加载，跳过填写', '异常说明')
        raise  # 抛出异常，让用例失败（也可根据需求改为continue）
    except ElementNotInteractableException:
        allure.attach(f'{field_name}元素不可交互，跳过填写', '异常说明')
        raise
@allure.epic('LES系统APP端')
@allure.feature('技术员APP页面')
@allure.story('填写SOP确认工序数据')
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
    with allure.step('窗口最大化'):
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
        time.sleep(2)
    #跳转至工序任务页面
        #SOP确认页面
        #点击SOP确认页签
    with allure.step('点击页签SOP确认'):
        wk.locator(*allPages.app_gxrw_sopqr).click()
        time.sleep(3)
        #点击工具类型
    with allure.step('选择工具类型'):
        wk.locator(*allPages.app_gxrw_sopqr_gjlx).click()
        time.sleep(2)
        # ActionChains(browser) \
        #     .key_down(Keys.ENTER) \
        #     .perform()
        #选择工具类型
    with allure.step('选择工具类型'):
        wk.locator(*allPages.app_gxrw_sopqr_gjlx_yyfq).click()
        time.sleep(10)
    #     点击完成
        #点击工具型号
        #选择工具型号
        #点击完成
        #填写工具数量
        #填写工具数量
    with allure.step('填写工具数量'):
        wk.locator(*allPages.app_gxrw_sopqr_gjsl).send_keys('2')
        #填写摩擦系数
    # with allure.step('填写摩擦系数'):
    #     wk.locator(*allPages.app_gxrw_sopqr_mcxs).send_keys('0.1')
    #     #填写A压
    # with allure.step('填写A压'):
    #     wk.locator(*allPages.app_gxrw_sopqr_Ay).send_keys('0.1')
    #     #填写B压
    # with allure.step('填写B压'):
    #     wk.locator(*allPages.app_gxrw_sopqr_By).send_keys('0.1')

    # #点击提交按钮提交任务
    # with allure.step('点击提交任务'):
    #     wk.locator(*allPages.app_gxrw_flgp_tj).click()
    # ========== 核心修复：使用通用函数处理字段填写 ==========
    # 处理摩擦系数
    with allure.step('填写摩擦系数（无值时填写）'):
        fill_if_empty(
            wait=wait,
            wk=wk,
            locator=allPages.app_gxrw_sopqr_mcxs,
            fill_value='0.1',
            field_name='摩擦系数'
        )

        # 处理A压
    with allure.step('填写T1@A（无值时填写）'):
        fill_if_empty(
            wait=wait,
            wk=wk,
            locator=allPages.app_gxrw_sopqr_T1A,
            fill_value='0.1',
            field_name='A压'
        )

        # 处理B压
    with allure.step('填写T1@B（无值时填写）'):
        fill_if_empty(
            wait=wait,
            wk=wk,
            locator=allPages.app_gxrw_sopqr_T1B,
            fill_value='0.1',
            field_name='B压'
        )

    #点击保存按钮保存任务
    with allure.step('点击保存任务'):
        wk.locator(*allPages.app_gxrw_sopqr_bc).click()
        time.sleep(3)
    #点击法兰挂牌页签
    with allure.step('点击页签法兰挂牌'):
        wk.locator(*allPages.app_gxrw_flgp).click()

        # 点击SOP确认页签
    with allure.step('点击页签SOP确认'):
        wk.locator(*allPages.app_gxrw_yzqr).click()

    time.sleep(10)
