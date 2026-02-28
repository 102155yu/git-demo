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

@allure.epic('一件代发海外仓')
@allure.feature('海外仓--下订单')
@allure.story('典型场景')
@allure.title('新增订单')
@allure.severity('critical')
def test_login02(browser):
    """
        用例编号：test_loin02
            用例标题：新增订单
            前置条件：登录
            测试步骤：
                1登录进入首页
                2进入全部订单页面
                3点击新建订单
                4填写新增内容
                5点击保存
            预期结果；跳转对应新增页面，保存成功后页面出现新保存的订单

    :param browser:
    :return:
    """
    #初始化页面对象
    #实例化Wait
    wait = WebDriverWait(browser,10)
    wk = WebKeys(browser)
    #进入登录
    with allure.step('进入LES_GL登录页'):
        login = LoginPage(browser)
        login.login(LOGIN_URL, USERNAME, PASSWD)
    time.sleep(3)

    #定位登录按钮
    with allure.step('定位登录按钮'):

        wk.locator(*allPages.page_login_loginBtn).click()

    #定位订单菜单
    with allure.step('定位订单菜单'):

        wk.locator(*allPages.menu_order_for_goods).click()

    #定位全部菜单
    with allure.step('定位全部菜单'):

        wk.locator(*allPages.menu_all_orders).click()

    #等待新建按钮
    # wait.until(EC.visibility_of_element_located(new_built))
    # 定位新建菜单
    with allure.step('定位新建菜单'):

        wk.locator(*allPages.new_built).click()
    #等待新增页面弹出
    with allure.step('新增页面弹出'):
        wk.locator(*allPages.now_cjbi)

    #定位仓库下拉框
    # wait.until(EC.visibility_of_element_located((By.XPATH , '//*[@id="app"]/div/div[2]/div[2]/section/div/form/div[3]/p')))
    with allure.step('定位仓库下拉框'):

        wk.locator(*allPages.now_warehouse).click()
    # 通过classname定位到仓库的下拉框
        ActionChains(browser) \
            .send_keys('US-') \
            .key_down(Keys.ARROW_DOWN) \
            .key_down(Keys.ENTER) \
            .perform()

    # 通过键盘输入CS点击下一个点击回车键
    with allure.step('通过键盘输入CS点击下一个点击回车键'):

        wk.locator(*allPages.now_bqdzlx).click()
        #通过相对路径定位至标签地址类型
        ActionChains(browser) \
            .key_down(Keys.ARROW_DOWN) \
            .key_down(Keys.ENTER) \
            .perform()
    # 通过键盘点击下一个点击回车键
    #点击添加商品按钮进入添加商品页面
    with allure.step('点击添加商品按钮进入添加商品页面'):

        wk.locator(*allPages.now_tjsp).click()
    #点击添加按钮，添加商品sku
    with allure.step('点击添加按钮'):

        wk.locator(*allPages.now_tianjia).click()
    #定位收件人模块（姓名）
    with allure.step('定位收件人模块（姓名）输入cs'):
        wk.locator(*allPages.now_name).send_keys('cs')
        # el = wk.driver.find_element(By.XPATH, '(//input[@type="text"])[9]').send_keys('cs')
    #定位州省地区
    with allure.step('定位州省地区输入（湖北）'):
        wk.locator(*allPages.now_area).send_keys('湖北')
        # el = wk.driver.find_element(By.XPATH, '(//input[@type="text"])[11]').send_keys('湖北')
    #定位城市
    with allure.step('定位城市输入（武汉）'):
        wk.locator(*allPages.now_city).send_keys('武汉')
        # el = wk.driver.find_element(By.XPATH, '(//input[@type="text"])[12]').send_keys('武汉')
    #定位联系电话
    with allure.step('定位联系电话输入13711111111'):
        wk.locator(*allPages.now_number).send_keys('13711111111')
        # el = wk.driver.find_element(By.XPATH, '(//input[@type="text"])[13]').send_keys('13711111111')
    #定位邮政编码
    with allure.step('定位邮政编码输入11'):
        wk.locator(*allPages.now_postal_code).send_keys('11')
        # el = wk.driver.find_element(By.XPATH, '(//input[@type="text"])[14]').send_keys('11')
    #定位目的地
    with allure.step('目的地输入（中国）'):
        wk.locator(*allPages.now_destination).click()
        # el = wk.driver.find_element(By.XPATH, '(//input[@type="text"])[10]').click()
        ActionChains(browser) \
            .send_keys("中国") \
            .key_down(Keys.ARROW_DOWN) \
            .key_down(Keys.ENTER) \
            .perform()

    # 定位地址输入框1
    with allure.step('地址输入框1输入（中国）'):
        wk.locator(*allPages.now_address_1).click()
        # el = wk.driver.find_element(By.XPATH, "//div[@class='el-textarea']").click()
        ActionChains(browser) \
            .send_keys("中国") \
            .perform()

        #定位点击确定
    with allure.step('点击确定'):
        wk.locator(*allPages.now_ok).click()
        # el = wk.driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/section/div/div[2]/button[3]').click()


