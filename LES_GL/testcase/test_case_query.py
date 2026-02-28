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



    with allure.step('点击查询'):
        wk.locator(*allPages.sku_query).click()

    with allure.step('检查商品SKU是否保存成功'):
        adds = wk.locator(By.XPATH ,"//P[text()='zd-03']" ).text
        # alld = wk.locator(*allPages.sku_num ).text
        assert 'zd-03'== adds