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
    # ========== 关键：适配你屏幕的坐标（根据截图调整） ==========
    # 步骤1：运行代码到“调整成手机模式”后暂停，手动获取以下坐标：
    # 1. 签字框绿色框的中心坐标（鼠标移到中心，看PyAutoGUI坐标：pyautogui.position()）
    SIGN_CENTER_X = 600  # 替换为你屏幕的实际X坐标（示例：180）
    SIGN_CENTER_Y = 800  # 替换为你屏幕的实际Y坐标（示例：400）
    # 2. 笔画长度（绿色框宽度的1/4，避免越界）
    STROKE_LEN = 30  # 可根据实际调整（示例：30px）
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
    #输入项目名称  2026年03月流程测试1-1北京源诚
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
        wk.locator(*allPages.app_gxrw_fljh_njz).send_keys(2)
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
        # 定位签字框（Canvas）并在正中间绘制“王”字
    with allure.step("在签字框正中间绘制“王”字"):
        try:
            # 步骤1：移动到签字框中心，激活绘制区域
            pyautogui.moveTo(SIGN_CENTER_X, SIGN_CENTER_Y, duration=0.5)
            pyautogui.click()  # 激活Canvas
            time.sleep(0.5)

            # 步骤2：绘制“王”字（以中心为基准）
            # 第一横：中心向左→向右
            pyautogui.mouseDown(x=SIGN_CENTER_X - STROKE_LEN, y=SIGN_CENTER_Y - STROKE_LEN)
            pyautogui.moveTo(x=SIGN_CENTER_X + STROKE_LEN, y=SIGN_CENTER_Y - STROKE_LEN, duration=0.2)
            pyautogui.mouseUp()
            time.sleep(0.2)

            # 中间竖：中心向上→向下
            pyautogui.mouseDown(x=SIGN_CENTER_X, y=SIGN_CENTER_Y - STROKE_LEN)
            pyautogui.moveTo(x=SIGN_CENTER_X, y=SIGN_CENTER_Y + STROKE_LEN, duration=0.2)
            pyautogui.mouseUp()
            time.sleep(0.2)

            # 第二横：中心向左→向右
            pyautogui.mouseDown(x=SIGN_CENTER_X - STROKE_LEN, y=SIGN_CENTER_Y)
            pyautogui.moveTo(x=SIGN_CENTER_X + STROKE_LEN, y=SIGN_CENTER_Y, duration=0.2)
            pyautogui.mouseUp()
            time.sleep(0.2)

            allure.attach(
                f"绘制完成：中心坐标({SIGN_CENTER_X},{SIGN_CENTER_Y})，笔画长度{STROKE_LEN}",
                "绘制结果",
                allure.attachment_type.TEXT
            )
        except Exception as e:
            allure.attach(f"绘制失败：{str(e)}", "错误信息", allure.attachment_type.TEXT)
            raise
        # 停留查看绘制效果
        # 切换电脑模式，定位保存按钮点击保存
    with allure.step("点击签字框中的保存"):
        pyautogui.press("F12")
        time.sleep(2)
        wk.locator(*allPages.app_gxrw_fljh_qm_qmk_bc).click()

        # 点击保存，保存签名
    with allure.step("点击保存，保存签名"):

        wk.locator(*allPages.app_gxrw_fljh_bc).click()

    # #点击提交按钮提交任务
    # with allure.step('点击提交任务'):
    #     wk.locator(*allPages.app_gxrw_wgqr_tj).click()
    #点击保存按钮保存任务
    # with allure.step('点击保存任务'):
    #     wk.locator(*allPages.app_gxrw_mfmjc_bc).click()
    #     time.sleep(3)
    #点击法兰挂牌页签
    with allure.step('点击页签法兰挂牌'):
        wk.locator(*allPages.app_gxrw_flgp).click()

        # 点击法兰校核页签
    with allure.step('点击法兰校核页签'):
        wk.locator(*allPages.app_gxrw_fljh).click()

    time.sleep(10)
