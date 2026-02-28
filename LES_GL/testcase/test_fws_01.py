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
@allure.feature('服务商设置项目经理')
@allure.story('典型场景')
@allure.title('服务商设备之项目经理')
@allure.severity('critical')
def test_login02(browser):
    """
        用例编号：test_loin02
            用例标题：服务商设置项目经理
            前置条件：装置员发布计划
            测试步骤：
                1.登录进入首页
                2.查看待办信息
                3.点击待办处理
                4.进入项目立项确认
                5.确认检修范围点击下一步
                6.选择项目经理
                7.点击确认
                8.项目经理指定完成

            预期结果；项目经理设置成功

    :param browser:
    :return:
    """
    # 窗口最大化操作（核心新增）
    with allure.step('浏览器窗口最大化'):
        browser.maximize_window()
    #初始化页面对象
    #实例化Wait
    wait = WebDriverWait(browser,10)
    wk = WebKeys(browser)

    #进入登录
    with allure.step('进入LES登录页'):
        login = LoginPage(browser)
        login.login(LOGIN_URL, USERNAME_XMFZR_PG, PASSWD)
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

        # ---------- 核心改造：使用计数器生成唯一计划名称 ----------
    with allure.step('输入计划名称（计数器生成唯一名称）'):
            # 调用计数器自增方法，获取最新值
        counter_value = wk.increment_counter()
            # 拼接唯一名称（前缀可自定义）
        plan_name = f"源诚服务-web-yja-{counter_value}"
            # 输入计划名称
        wk.locator(*allPages.fwjh_dljfwjh_jhmc).send_keys(plan_name)
            # 打印日志，方便调试
        allure.attach(f"生成的计划名称：{plan_name}", "计划名称", allure.attachment_type.TEXT)
        # ---------- 计数器改造结束 ----------

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
    time.sleep(3)
    #点击下派
    with allure.step("点击下派"):
        wk.locator(*allPages.fwjh_dljfwjh_xp).click()
    time.sleep(3)
    # with allure.step("后置校验：验证计划名称展示在页面中"):
    #     try:
    #         # 1. 返回计划列表页
    #         wk.locator(*allPages.fwjh_dljfwjh).click()
    #         # 2. 校验计划名称是否存在于页面
    #         is_text_exist = wk.check_text_in_page(plan_name, timeout=15)
    #         # 3. 断言（核心：用例成败的关键判断）
    #         assert is_text_exist, f"创建的计划名称【{plan_name}】未在页面中展示！"
    #         # 4. 报告附加校验结果（成功）
    #         allure.attach(f"校验通过：计划名称【{plan_name}】已在页面展示", "校验结果", allure.attachment_type.TEXT)
    #     except AssertionError as e:
    #         # 断言失败时，强制写入失败信息到Allure
    #         allure.attach(f"校验失败：{str(e)}", "校验结果", allure.attachment_type.TEXT)
    #         raise  # 重新抛出异常，保证用例标记为失败