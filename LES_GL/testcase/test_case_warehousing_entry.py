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

@allure.epic('一件代发海外仓')
@allure.feature('海外仓--新建商品SKU')
@allure.story('典型场景')
@allure.title('新增商品SKU')
@allure.severity('critical')
def test_login03(browser):
    """
        用例编号：test_loin02
            用例标题：新增入库单
            前置条件：登录
            测试步骤：
                1登录进入首页
                2进入入库单管理页面
                3点击新增
                4填写新增内容
                5点击保存
            预期结果；跳转对应新增页面，保存成功后页面出现新保存的入库单

    :param browser:
    :return:
    """
    #初始化页面对象
    #实例化Wait
    wait = WebDriverWait(browser,10)
    wk = WebKeys(browser)
    #进入登录
    with allure.step('进入LES_GL登录页'):
        login =LoginPage(browser)
        login.login(LOGIN_URL,USERNAME,PASSWD)

    time.sleep(3)


    #点击菜单入库单
    with allure.step('点击入库单'):
        wk.locator(*allPages.menu_warehousing_entry).click()

    #点击入库单管理菜单
    with allure.step('点击入库单管理'):
        wk.locator(*allPages.menu_warehousing_entry_manage).click()

    #点击新增按钮
    with allure.step('点击新增'):
        wk.locator(*allPages.warehousing_entry_newly_added).click()


    #定位时间
    with allure.step('填写时间'):
        wk.locator(*allPages.warehousing_entry_time).send_keys('2024-09-05')

    #定位送货类型
    with allure.step('填写送货类型：散货'):
        wk.locator(*allPages.warehousing_entry_add_shlx).click()
        ActionChains(browser) \
            .key_down(Keys.ARROW_DOWN) \
            .key_down(Keys.ENTER) \
            .perform()

    #填写送达方式
    with allure.step('填写送达方式：快递'):
        wk.locator(*allPages.warehousing_entry_add_sdfs).click()
        ActionChains(browser) \
            .key_down(Keys.ARROW_DOWN) \
            .key_down(Keys.ENTER) \
            .perform()

    #填写入库数量
    with allure.step('填写入库箱子数量'):
        wk.locator(*allPages.warehousing_entry_add_rksl).send_keys("10")

    #选择入库仓库
    with allure.step('选着入库仓库'):
        wk.locator(*allPages.warehousing_entry_add_rkck).click()
        ActionChains(browser) \
            .send_keys('US-') \
            .key_down(Keys.ARROW_DOWN) \
            .key_down(Keys.ENTER) \
            .perform()

    #填写客户参考号
    with allure.step('填写客户参考号'):
        wk.locator(*allPages.warehousing_entry_add_khckh).send_keys("05261176")

    #添加商品
    with allure.step('添加商品'):
        wk.locator(*allPages.warehousing_entry_add_zjsp).click()


    time.sleep(5)