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

@allure.epic('LES系统')
@allure.feature('登录')
@allure.story('典型场景')
@allure.title('主流程完成')
@allure.severity('critical')
def test_login02(browser):
    """
        用例编号：test_loin02
            用例标题：登录
            前置条件：登录
            测试步骤：
                1登录进入首页

            预期结果；登录成功

    :param browser:
    :return:
    """
    #初始化页面对象
    #实例化Wait
    wait = WebDriverWait(browser,10)
    wk = WebKeys(browser)
    #进入登录
    with allure.step('进入LES登录页'):
        login = LoginPage(browser)
        login.login(LOGIN_URL, USERNAME_zg_YJA, PASSWD)
    time.sleep(1)

    #定位服务计划管理
    with allure.step('定位服务计划管理菜单'):

        wk.locator(*allPages.fwjh).click()

    # 点击定力矩服务计划菜单
    with allure.step('点击定力矩服务计划菜单'):
        wk.locator(*allPages.fwjh_dljfwjh).click()

    #点击添加定力矩服务计划
    with allure.step('点击添加定力矩服务计划'):

        wk.locator(*allPages.fwjh_dljfwjh_tj).click()

    #输入计划名称
    with allure.step('输入计划名称'):

        wk.locator(*allPages.fwjh_dljfwjh_jhmc).send_keys("源诚服务-web-yu-2")
    #选择检修类型
    with allure.step("选择检修类型"):

        wk.locator(*allPages.fwjh_dljfwjh_jxlx).click()
        # 通过classname定位到仓库的下拉框
        ActionChains(browser) \
            .key_down(Keys.DOWN) \
            .key_down(Keys.ENTER) \
            .perform()
    #选择开始时间
    with allure.step("选择开始时间"):
        wk.locator(*allPages.fwjh_dljfwjh_kssj).click()
        ActionChains(browser) \
            .key_down(Keys.DOWN) \
            .key_down(Keys.RIGHT)\
            .key_down(Keys.ENTER)\
            .perform()
    #选择结束时间
    with allure.step("选择结束时间"):
        wk.locator(*allPages.fwjh_dljfwjh_jssj).click()
        ActionChains(browser) \
            .key_down(Keys.DOWN) \
            .key_down(Keys.DOWN) \
            .key_down(Keys.DOWN) \
            .key_down(Keys.RIGHT)\
            .key_down(Keys.ENTER)\
            .perform()

    #点击保存
    with allure.step("保存"):
        wk.locator(*allPages.fwjh_dljfwjh_bc).click()

    #添加检修范围
    with allure.step("点击添加，添加检修范围"):
        wk.locator(*allPages.fwjh_dljfwjh_jxfwpz_tj).click()

    #选择服务商
    with allure.step("选择服务商:北京源城"):
        wk.locator(*allPages.fwjh_dljfwjh_jxfwpz_fws).click()
        ActionChains(browser) \
            .key_down(Keys.DOWN) \
            .key_down(Keys.ENTER) \
            .perform()

    #选择装置
    with allure.step("选择装置:55万吨"):
        wk.locator(*allPages.fwjh_dljfwjh_jxfwpz_zz).click()
        ActionChains(browser) \
            .send_keys('55万吨') \
            .key_down(Keys.DOWN) \
            .key_down(Keys.ENTER) \
            .perform()

    #填写计划检修量
    with allure.step("选择装置:55万吨"):
        wk.locator(*allPages.fwjh_dljfwjh_jxfwpz_jhjxl).send_keys("50")

    #选择服务模式
    with allure.step("选择服务模式：简易模式"):
        wk.locator(*allPages.fwjh_dljfwjh_jxfwpz_fwms).click()
        ActionChains(browser) \
            .key_down(Keys.DOWN) \
            .key_down(Keys.DOWN) \
            .key_down(Keys.DOWN) \
            .key_down(Keys.ENTER) \
            .perform()
    #点击确认保存检修范围
    with allure.step("点击确认保存检修范围"):
        wk.locator(*allPages.fwjh_dljfwjh_jxfwpz_qd).click()

    #点击下派
    with allure.step("点击下派"):
        wk.locator(*allPages.fwjh_dljfwjh_xp).click()


