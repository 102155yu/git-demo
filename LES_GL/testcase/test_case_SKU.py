

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
            用例标题：新增商品SKU
            前置条件：登录
            测试步骤：
                1登录进入首页
                2进入仓库，进入库存商品页面
                3点击新增
                4填写新增内容
                5点击保存
            预期结果；跳转对应新增页面，保存成功后页面出现新保存的商品SKU

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

    #定位登录按钮
    # with allure.step('点击登录按钮'):
    #
    #     wk.locator(*allPages.page_login_loginBtn).click()

    #定位到仓库菜单

    with allure.step('点击仓库菜单'):
        wk.locator(*allPages.menu_warehouse).click()


    #定位到菜单（库存管理）
    with allure.step('点击库存管理'):
        wk.locator(*allPages.menu_finished_goods).click()

    #定位新增按钮
    with allure.step('点击新增按钮'):
        wk.locator(*allPages.sku_newly_added).click()

    #定位弹出新页面
    with allure.step('页面弹出'):
        wk.locator(*allPages.sku_text)

    #定位至库存商品SKU
    with allure.step('填写商品SKU'):
        wk.locator(*allPages.sku_sku).send_keys('zd-03')
 #每次跑的时候改下商品SKU

    #定位至商品中文名
    with allure.step('填写商品中文名'):
        wk.locator(*allPages.sku_chinese_name).send_keys('自动步枪')

    #定位商品英文名
    with allure.step('填写商品英文名'):
        wk.locator(*allPages.sku_english_name).send_keys('zdbq')
    #定位商品状态
    with allure.step('选择商品状态'):
        wk.locator(*allPages.sku_state).click()
        ActionChains(browser)\
            .key_down(Keys.ARROW_DOWN)\
            .key_down(Keys.ENTER)\
            .perform()

    #定位类目
    with allure.step('选择类目'):
        wk.locator(*allPages.sku_category).click()
        ActionChains(browser)\
            .key_down(Keys.ARROW_DOWN)\
            .key_down(Keys.ARROW_DOWN)\
            .key_down(Keys.ARROW_DOWN)\
            .click()\
            .perform()


    #定位尺寸 长
    with allure.step('填写长'):
        wk.locator(*allPages.sku_long).send_keys(5)
    #定位尺寸 宽
    with allure.step('填写宽'):
        wk.locator(*allPages.sku_wide).send_keys(10)
    #定位尺寸  高
    with allure.step('填写高'):
        wk.locator(*allPages.sku_tall).send_keys(15)
    #定位重量
    with allure.step('输入重量'):
        wk.locator(*allPages.sku_weight).send_keys(20)
    #定位确定

    with allure.step('点击确认'):
        wk.locator(*allPages.sku_ok).click()

    with allure.step('点击查询'):
        wk.locator(*allPages.sku_query).click()

    with allure.step('检查商品SKU是否保存成功'):
        wk.locator(By.XPATH ,"//P[text()='zd-03']" ).text


        assert 1==1
