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
@allure.story('填写工序数据')
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
        # 短暂等待窗口最大化完成
        time.sleep(1)
        # 2. 按下F12键（可根据需要调整为presses=n实现多次按）
        pyautogui.press('f12')
    #初始化页面对象
    #实例化Wait
    wait = WebDriverWait(browser,10)
    wk = WebKeys(browser)
    #进入登录
    with allure.step('进入APP端'):
        loginapp = LoginPage(browser)
        loginapp.login(LOGIN_URL_APP, USERNAME_CZG_YJA, PASSWD)
    time.sleep(1)


    #进入定力矩服务，点击工序处理
    with allure.step('点击工序处理'):
        wk.locator(*allPages.app_dljfw_gxcl).click()

    # 点击领取工序任务
    with allure.step('点击勾选任务'):
        wk.locator(*allPages.app_dljfw_gxcl_dql_dj_01).click()

    #点击领取按钮
    with allure.step('点击领取按钮'):
        wk.locator(*allPages.app_dljfw_gxcl_dlq_lq).click()

    #等待1分钟点击“待处理”
    time.sleep(60)
    with allure.step('点击待处理'):
        wk.locator(*allPages.app_dljfw_gxcl_dcl).click()

    #进入待处理页面点击任务
    with allure.step('点击任务'):
        wk.locator(*allPages.app_dljfw_gxcl_dcl_dj_01).click()

    #跳转至工序任务页面
        #密封面页面
    #点击提交密封面照片
    with allure.step('点击密封面照片'):
        wk.locator(*allPages.app_gxrw_mfmjc_mfmzp).click()
        # 关键等待：给弹窗加载留足够时间（可根据实际情况调整秒数）
    time.sleep(3)

        # 输入图片路径并按回车确认（模拟手动输入文件地址）
    with allure.step('输入图片路径并确认上传'):
            # 输入图片绝对路径，r前缀避免反斜杠转义
        pyautogui.typewrite(r'C:\Users\chens\Pictures\1.jpg', interval=0.1)
            # 连续按3次回车（适配弹窗的确认逻辑）
        pyautogui.press(keys='ENTER', presses=3)
    #点击提交按钮提交任务
    with allure.step('点击提交任务'):
        wk.locator(*allPages.app_gxrw_mfmjc_tj).click()

    #
    # #进入项目管理页面
    #     #点击成员配置按钮
    # with allure.step('点击成员配置按钮'):
    #     wk.locator(*allPages.xmgl_cypz).click()
    # #进入成员配置页面
    #     #点击添加
    # with allure.step('点击添加'):
    #     wk.locator(*allPages.xmgl_cypz_tj).click()
    #     #进入添加页面
    #         #点击下拉按钮
    # with allure.step('点击下拉按钮'):
    #     wk.locator(*allPages.xmgl_cypz_tj_xl).click()
    #     #选择第三个人员勾选
    # with allure.step('勾选第三个人员'):
    #     wk.locator(*allPages.xmgl_cypz_tj_03).click()
    #     #点击确定
    # with allure.step('点击确定'):
    #     wk.locator(*allPages.xmgl_cypz_tj_qd).click()
    #     #点击返回
    # with allure.step('点击返回'):
    #     wk.locator(*allPages.xmgl_cypz_fh).click()
    # #点击检修范围
    # with allure.step('点击检修范围按钮'):
    #     wk.locator(*allPages.xmgl_jxfw).click()
    #
    # #进入检修范围页面
    #     #点击下一页
    # # with allure.step('点击下一页'):
    # #     wk.locator(*allPages.xmgl_jxfw_xyy).click()
    # #     # 点击下一页
    # # with allure.step('点击下一页'):
    # #     wk.locator(*allPages.xmgl_jxfw_xyy).click()
    #     #选择第一个法兰点击勾选
    # with allure.step('点击勾选第一个法兰'):
    #     wk.locator(*allPages.xmgl_jxfw_gx_01).click()
    #     #点击提交
    # with allure.step('点击提交'):
    #     wk.locator(*allPages.xmgl_jxfw_tj).click()
    # #弹出确认框
    #     #点击确定
    # with allure.step('点击确定'):
    #     wk.locator(*allPages.xmgl_jxfw_tj_qr).click()
    #
    # # #进行人员配置页面点击项目经理选择框
    # # with allure.step("选择项目经理"):
    # #     wk.locator(*allPages.fws_fzr_lxqr_xmjl).click()
    # #     ActionChains(browser)\
    # #         .key_down(Keys.DOWN)\
    # #         .key_down(Keys.DOWN)\
    # #         .key_down(Keys.ENTER)\
    # #         .perform()
    # # #点击确认按钮
    # # with allure.step('点击确认按钮'):
    # #     wk.locator(*allPages.fws_fzr_lxqr_qr).click()