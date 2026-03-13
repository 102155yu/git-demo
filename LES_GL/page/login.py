import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as ec
import pyautogui
from LES_GL.key_word.keyword import WebKeys
from LES_GL.locate.allPages import *
from LES_GL.VAR.BOOKHOUSER_VAR import LOGIN_URL_APP, USERNAME_CZG_YJA, PASSWD
from LES_GL.key_word.keyword import *
from LES_GL.locate import allPages
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException


#以页面或组件为单位，封装常用的行为代码和页面元素定位代码
class LoginPage(WebKeys):
    #登录操作
    def login(self,url,username,passwd):
        self.open(url)
        #实例化Wait
        wait = WebDriverWait(self.driver,5)
        #根据‘登录LES_GL’作为等待条件
        # wait.until(ec.text_to_be_present_in_element((By.XPATH,'//div'),"欢迎登陆"))

        #登录操作
        #01进行用户登录
        self.locator(*page_login_user).send_keys(username)
        self.locator(*page_login_indexPwd).send_keys(passwd)
        self.locator(*page_login_loginBtn).click()

    #登录APP操作
    def loginapp(self, url, username, passwd):
        self.open(url)
            # 实例化Wait
        wait = WebDriverWait(self.driver, 10)
            # 根据‘登录LES_GL’作为等待条件
            # wait.until(ec.text_to_be_present_in_element((By.XPATH,'//div'),"欢迎登陆"))

            # 登录操作
            # 01进行用户登录
        self.locator(*page_login_user_app).click()
        time.sleep(3)
        self.locator(*page_login_user_app).send_keys(username)
        self.locator(*page_login_indexPwd_app).click()
        self.locator(*page_login_indexPwd_app).send_keys(passwd)
        time.sleep(3)
        self.locator(*page_login_loginBtn_app).click()
        # 根据username出现在首页作为等待条件，确保首页正常出现
        # wait.until(ec.text_to_be_present_in_element((By.LINK_TEXT, username), username))
class GxrwJymsExecutor:
    """简易模式工序数据填写执行器（封装完整流程）"""

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)
        self.wk = WebKeys(browser)

    def execute_full_jrgxcl_flow(self):
        """执行完整的简易模式工序数据填写流程（与原用例逻辑完全一致）"""

        # ========== 进入定力矩服务-工序处理-待处理 ==========
        # 点击工序处理
        self.wk.locator(*allPages.app_dljfw_gxcl).click()
        time.sleep(2)
        # 点击待处理
        self.wk.locator(*allPages.app_dljfw_gxcl_dcl).click()
        time.sleep(2)
        # 点击第一个待处理任务
        self.wk.locator(*allPages.app_dljfw_gxcl_dcl_dj_01).click()
        time.sleep(2)

    def execute_full_gxrw_mfmjc_flow(self):
        # ========== 4. 密封面检查 ==========
        # 点击密封面检查页签
        self.wk.locator(*allPages.app_gxrw_mfmjc).click()
        time.sleep(1)
        # 上传密封面照片
        self.wk.locator(*allPages.app_gxrw_mfmjc_mfmzp).click()
        time.sleep(2)
        pyautogui.typewrite(r'C:\Users\chens\Pictures\1.jpg', interval=0.1)
        pyautogui.press(keys='ENTER', presses=3)
        time.sleep(2)
        # 提交任务
        self.wk.locator(*allPages.app_gxrw_mfmjc_tj).click()
        time.sleep(3)

    def execute_full_gxrw_flgp_flow(self):
        # 法兰挂牌页面
        # 点击法兰挂牌页签
        with allure.step('点击页签法兰挂牌'):
            self.wk.locator(*allPages.app_gxrw_flgp).click()
            # 关键等待：给弹窗加载留足够时间（可根据实际情况调整秒数）
            # 点击法兰挂牌照片上传照片
        with allure.step('点击法兰挂牌照片'):
            self.wk.locator(*allPages.app_gxrw_flgp_flgpzp).click()
            time.sleep(2)
            # 输入图片路径并按回车确认（模拟手动输入文件地址）
        with allure.step('输入图片路径并确认上传'):
            # 输入图片绝对路径，r前缀避免反斜杠转义
            pyautogui.typewrite(r'C:\Users\chens\Pictures\1.jpg', interval=0.1)
            # 连续按3次回车（适配弹窗的确认逻辑）
            pyautogui.press(keys='ENTER', presses=3)
            time.sleep(2)
        # 填写层级
        with allure.step('点击填写层级'):
            self.wk.locator(*allPages.app_gxrw_flgp_cj).send_keys('1')


        # 点击保存按钮保存任务
        with allure.step('点击保存任务'):
            self.wk.locator(*allPages.app_gxrw_flgp_bc).click()

        #点击提交按钮提交任务
        with allure.step('点击提交任务'):
            self.wk.locator(*allPages.app_gxrw_flgp_tj).click()
    def execute_full_gxrw_flcx_flow(self):
        # 法兰拆卸页面
        # 点击法兰拆卸页签
        with allure.step('点击页签法兰拆卸'):
            self.wk.locator(*allPages.app_gxrw_flcx).click()
            # 关键等待：给弹窗加载留足够时间（可根据实际情况调整秒数）
            # 点击法兰拆卸工具数量
        with allure.step('点击法兰拆卸工具数量'):
            self.wk.locator(*allPages.app_gxrw_flcx_cxgjsl).send_keys('1')
            # 点击法兰拆卸拉伸力
        with allure.step('点击法兰拆卸拉伸力'):
            self.wk.locator(*allPages.app_gxrw_flcx_cxlsl).send_keys('1000')
            # 点击拆卸后照片
        with allure.step('点击拆卸后照片'):
            self.wk.locator(*allPages.app_gxrw_flcx_cxhzp).click()
            time.sleep(2)
            # 输入图片路径并按回车确认（模拟手动输入文件地址）
        with allure.step('输入图片路径并确认上传'):
            # 输入图片绝对路径，r前缀避免反斜杠转义
            pyautogui.typewrite(r'C:\Users\chens\Pictures\1.jpg', interval=0.1)
            # 连续按3次回车（适配弹窗的确认逻辑）
            pyautogui.press(keys='ENTER', presses=3)
            time.sleep(2)
        # 填写施工人员
        with allure.step('点击填写施工人员'):
            self.wk.locator(*allPages.app_gxrw_flcx_sgry).send_keys('余家傲')

            time.sleep(2)

        # 点击保存按钮保存任务
        with allure.step('点击保存任务'):
            self.wk.locator(*allPages.app_gxrw_flcx_bc).click()
            time.sleep(3)
        # #点击提交按钮提交任务
        with allure.step('点击提交任务'):
            self.wk.locator(*allPages.app_gxrw_flgp_tj).click()
    def execute_full_gxrw_dpjc_flow(self):
        # ========== 5. 垫片检查 ==========
        # 点击垫片检查页签
        self.wk.locator(*allPages.app_gxrw_dpjc).click()
        time.sleep(1)
        # 上传垫片照片
        self.wk.locator(*allPages.app_gxrw_dpjc_dpzp).click()
        time.sleep(2)
        pyautogui.typewrite(r'C:\Users\chens\Pictures\1.jpg', interval=0.1)
        pyautogui.press(keys='ENTER', presses=3)
        time.sleep(2)
        # 上传垫片规格铭牌
        self.wk.locator(*allPages.app_gxrw_dpjc_dpgemp).click()
        time.sleep(2)
        pyautogui.typewrite(r'C:\Users\chens\Pictures\2.jpg', interval=0.1)
        pyautogui.press(keys='ENTER', presses=3)
        time.sleep(2)
        # 提交任务
        self.wk.locator(*allPages.app_gxrw_flgp_tj).click()
        time.sleep(3)
    def execute_full_gxrw_jgjjc_flow(self):
        # ========== 6. 紧固件检查 ==========
        # 点击紧固件检查页签
        self.wk.locator(*allPages.app_gxrw_jgjjc).click()
        time.sleep(1)
        # 上传螺栓螺母照片
        self.wk.locator(*allPages.app_gxrw_jgjjc_lslmzp).click()
        time.sleep(2)
        pyautogui.typewrite(r'C:\Users\chens\Pictures\1.jpg', interval=0.1)
        pyautogui.press(keys='ENTER', presses=3)
        time.sleep(2)
        # 提交任务
        self.wk.locator(*allPages.app_gxrw_flgp_tj).click()
        time.sleep(3)
    def execute_full_gxrw_yzqr_flow(self):
        # 预装确认页面
        # 点击预装确认页签
        with allure.step('点击页签预装确认'):
            self.wk.locator(*allPages.app_gxrw_yzqr).click()
            # 关键等待：给弹窗加载留足够时间（可根据实际情况调整秒数）

            # 点击紧固照片
        with allure.step('点击紧固照片'):
            self.wk.locator(*allPages.app_gxrw_yzqr_jgzp).click()
            time.sleep(2)
            # 输入图片路径并按回车确认（模拟手动输入文件地址）
        with allure.step('输入图片路径并确认上传'):
            # 输入图片绝对路径，r前缀避免反斜杠转义
            pyautogui.typewrite(r'C:\Users\chens\Pictures\1.jpg', interval=0.1)
            # 连续按3次回车（适配弹窗的确认逻辑）
            pyautogui.press(keys='ENTER', presses=3)
            time.sleep(2)

        # #点击提交按钮提交任务
        with allure.step('点击提交任务'):
            self.wk.locator(*allPages.app_gxrw_yzqr_tj).click()
    def execute_full_gxrw_sopqr_flow(self):
    # 新增通用函数：等待元素可交互 + 无值则填写


    # ========== 核心封装：SOP确认独立函数 ==========

        """
        独立封装的SOP确认环节逻辑，可被其他用例直接调用
        :param browser: selenium的webdriver实例（由pytest夹具传入）
        :return: None
        """
        # 初始化依赖对象
        wait = WebDriverWait(self.browser, 10)
        wk = WebKeys(self.browser)

        # SOP确认核心步骤
        with allure.step('点击页签SOP确认'):
            wk.locator(*allPages.app_gxrw_sopqr).click()
            time.sleep(3)
        with allure.step('选择工具类型'):
            wk.locator(*allPages.app_gxrw_sopqr_gjlx).click()
            time.sleep(2)
        with allure.step('选择工具类型（液压风枪）'):
            wk.locator(*allPages.app_gxrw_sopqr_gjlx_yyfq).click()
            time.sleep(10)
        with allure.step('填写工具数量'):
            wk.locator(*allPages.app_gxrw_sopqr_gjsl).send_keys('2')

        # # 通用函数填充字段
        # with allure.step('填写摩擦系数（无值时填写）'):
        #     fill_if_empty(
        #         wait=wait,
        #         wk=wk,
        #         locator=allPages.app_gxrw_sopqr_mcxs,
        #         fill_value='0.1',
        #         field_name='摩擦系数'
        #     )
        # with allure.step('填写T1@A（无值时填写）'):
        #     fill_if_empty(
        #         wait=wait,
        #         wk=wk,
        #         locator=allPages.app_gxrw_sopqr_T1A,
        #         fill_value='0.1',
        #         field_name='A压'
        #     )
        # with allure.step('填写T1@B（无值时填写）'):
        #     fill_if_empty(
        #         wait=wait,
        #         wk=wk,
        #         locator=allPages.app_gxrw_sopqr_T1B,
        #         fill_value='0.1',
        #         field_name='B压'
        #     )
    # 填写摩擦系数（调用WebKeys中的fill_if_empty方法）

        with allure.step('填写摩擦系数'):
            self.wk.fill_if_empty(
                locator=allPages.app_gxrw_sopqr_mcxs,
                fill_value='0.1',
                field_name='摩擦系数'
            )

            # 填写A压（调用WebKeys中的fill_if_empty方法）
        with allure.step('填写T1A'):
            self.wk.fill_if_empty(
                locator=allPages.app_gxrw_sopqr_T1A,
                fill_value='0.1',
                field_name='T1@A Pressure'
            )

            # 填写B压（调用WebKeys中的fill_if_empty方法）
        with allure.step('填写T1B'):
            self.wk.fill_if_empty(
                locator=allPages.app_gxrw_sopqr_T1B,
                fill_value='0.1',
                field_name='T1@B Pressure'
            )
            with allure.step('点击提交任务'):
                wk.locator(*allPages.app_gxrw_sopqr_tj).click()
                time.sleep(3)
    def execute_full_gxrw_flcj_flow(self):
        # 法兰抽检页面
        # 点击法兰抽检页签
        with allure.step('点击页签法兰抽检'):
            self.wk.locator(*allPages.app_gxrw_flcj).click()
            # 关键等待：给弹窗加载留足够时间（可根据实际情况调整秒数）
            # 点击紧固压力
        with allure.step('点击紧固压力'):
            self.wk.locator(*allPages.app_gxrw_flcj_jgyl).send_keys(2)
            # 点击抽检前照片
        with allure.step('点击抽检前照片'):
            self.wk.locator(*allPages.app_gxrw_flcj_cjqzp).click()
            time.sleep(2)
            # 输入图片路径并按回车确认（模拟手动输入文件地址）
        with allure.step('输入图片路径并确认上传'):
            # 输入图片绝对路径，r前缀避免反斜杠转义
            pyautogui.typewrite(r'C:\Users\chens\Pictures\1.jpg', interval=0.1)
            # 连续按3次回车（适配弹窗的确认逻辑）
            pyautogui.press(keys='ENTER', presses=3)
            time.sleep(2)

            # 点击抽检公差
        with allure.step('点击抽检公差'):
            self.wk.locator(*allPages.app_gxrw_flcj_cjgc).click()
            # 点击抽检公差确定
        with allure.step('点击抽检公差确定'):
            self.wk.locator(*allPages.app_gxrw_flcj_cjgc_qd).click()
            # 点击校验公差1
        with allure.step('点击校验公差1'):
            self.wk.locator(*allPages.app_gxrw_flcj_jygc).click()
            # time.sleep(2)
            # 点击校验公差1确定
        with allure.step('点击校验公差1确定'):
            self.wk.locator(*allPages.app_gxrw_flcj_jygc_qd).click()
            # 点击校验公差2
        with allure.step('点击校验公差2'):
            self.wk.locator(*allPages.app_gxrw_flcj_jygc_2).click()
            # time.sleep(2)
            # 点击校验公差2确定
        with allure.step('点击校验公差2确定'):
            self.wk.locator(*allPages.app_gxrw_flcj_jygc_qd_2).click()

            # 点击抽检过程照片
        with allure.step('点击抽检过程照片'):
            self.wk.locator(*allPages.app_gxrw_flcj_cjgczp).click()
            time.sleep(2)
            # 输入图片路径并按回车确认（模拟手动输入文件地址）
        with allure.step('输入图片路径并确认上传'):
            # 输入图片绝对路径，r前缀避免反斜杠转义
            pyautogui.typewrite(r'C:\Users\chens\Pictures\1.jpg', interval=0.1)
            # 连续按3次回车（适配弹窗的确认逻辑）
            pyautogui.press(keys='ENTER', presses=3)
        # #点击提交按钮提交任务
        # with allure.step('点击提交任务'):
        #     wk.locator(*allPages.app_gxrw_flgp_tj).click()
        # 点击保存按钮保存任务
        with allure.step('点击保存任务'):
            self.wk.locator(*allPages.app_gxrw_flcj_bc).click()
            time.sleep(3)
        # #点击提交按钮提交任务
        with allure.step('点击提交任务'):
            self.wk.locator(*allPages.app_gxrw_flcj_tj).click()

    def execute_full_gxrw_wgqr_flow(self):  # 完工确认
        # 点击完工确认页签
        with allure.step('点击完工确认页签'):
            self.wk.locator(*allPages.app_gxrw_wgqr).click()
            # 关键等待：给弹窗加载留足够时间（可根据实际情况调整秒数）
            # 点击垫片照片上传垫片照片
        with allure.step('点击垫片照片'):
            self.wk.locator(*allPages.app_gxrw_wgqr_dpzp).click()
            time.sleep(2)
            # 输入图片路径并按回车确认（模拟手动输入文件地址）
        with allure.step('输入图片路径并确认上传'):
            # 输入图片绝对路径，r前缀避免反斜杠转义
            pyautogui.typewrite(r'C:\Users\chens\Pictures\1.jpg', interval=0.1)
            # 连续按3次回车（适配弹窗的确认逻辑）
            pyautogui.press(keys='ENTER', presses=3)
            time.sleep(2)

        # #点击提交按钮提交任务
        with allure.step('点击提交任务'):
            self.wk.locator(*allPages.app_gxrw_wgqr_tj).click()

            time.sleep(3)
    def execute_full_gxrw_fljh_flow(self):    # 法兰校核
        # ========== 关键：适配你屏幕的坐标（根据截图调整） ==========
        # 步骤1：运行代码到“调整成手机模式”后暂停，手动获取以下坐标：
        # 1. 签字框绿色框的中心坐标（鼠标移到中心，看PyAutoGUI坐标：pyautogui.position()）
        SIGN_CENTER_X = 600  # 替换为你屏幕的实际X坐标（示例：180）
        SIGN_CENTER_Y = 800  # 替换为你屏幕的实际Y坐标（示例：400）
        # 2. 笔画长度（绿色框宽度的1/4，避免越界）
        STROKE_LEN = 30  # 可根据实际调整（示例：30px）
        # 窗口最大化操作（核心新增）
        # ========== 新增：窗口最大化 + 按F12键 ==========

        # 法兰校核页面
        # 点击法兰校核页签
        with allure.step('点击法兰校核页签'):
            self.wk.locator(*allPages.app_gxrw_fljh).click()
            # 关键等待：给弹窗加载留足够时间（可根据实际情况调整秒数）
            # 点击输入工具数量
        with allure.step('点击输入工具数量'):
            self.wk.locator(*allPages.app_gxrw_fljh_gjsl).send_keys(2)
            # 点击输入扭矩值
        with allure.step('点击输入扭矩值'):
            self.wk.locator(*allPages.app_gxrw_fljh_njz).send_keys(2)
            # 点击输入平行公差
        with allure.step('点击输入平行公差'):
            self.wk.locator(*allPages.app_gxrw_fljh_pxgc).click()
            # 平行公差填写
        with allure.step('平行公差填写'):
            self.wk.locator(*allPages.app_gxrw_fljh_pxgc_qd).click()

            # 点击签字
        with allure.step('点击签字'):
            self.wk.locator(*allPages.app_gxrw_fljh_qm).click()
            # 调整成手机模式
        with allure.step('调整成手机模式'):

            pyautogui.press("F12")
            time.sleep(2)
            pyautogui.hotkey('ctrl', 'shift', 'm')
            time.sleep(2)
            # 定位签字框
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
            self.wk.locator(*allPages.app_gxrw_fljh_qm_qmk_bc).click()

            # 点击保存，保存签名
        with allure.step("点击保存，保存签名"):

            self.wk.locator(*allPages.app_gxrw_fljh_bc).click()
            # 点击提交按钮保存任务
        with allure.step('点击保存任务'):
            self.wk.locator(*allPages.app_gxrw_fljh_bc).click()
        #点击提交按钮提交任务
        with allure.step('点击提交任务'):
            self.wk.locator(*allPages.app_gxrw_fljh_tj).click()
    def execute_full_gxrw_lscj_flow(self):
        # 螺栓抽检页面
        # 点击螺栓抽检页签
        with allure.step('点击螺栓抽检页签'):
            self.wk.locator(*allPages.app_gxrw_lscj).click()
            # 关键等待：给弹窗加载留足够时间（可根据实际情况调整秒数）

        with allure.step("填写实际施工值"):
            self.wk.locator(*allPages.app_gxrw_lscj_sjsgz).send_keys(20)

        # 点击保存按钮保存任务
        with allure.step('点击保存任务'):
            self.wk.locator(*allPages.app_gxrw_lscj_bc).click()
            # #点击提交按钮提交任务
        with allure.step('点击提交任务'):
            self.wk.locator(*allPages.app_gxrw_lscj_tj).click()