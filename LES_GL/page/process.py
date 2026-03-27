import time
from selenium.webdriver import ActionChains ,Keys
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
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException, WebDriverException


class GxrwJymsExecutor:
    """简易模式工序数据填写执行器（封装完整流程）"""

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)
        self.wk = WebKeys(browser)

    #app进入待处理页面
    def execute_full_jrgxcl_flow(self):

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

    # ========== 密封面检查 ==========
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

    # ==========  法兰挂牌  ==========
    def execute_full_gxrw_flgp_flow(self):
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

    # ==========  法兰拆卸  ==========
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

    # ==========  垫片检查  ==========
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

    # ==========  紧固件检查  ==========
    def execute_full_gxrw_jgjjc_flow(self):
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

    # ==========  预装确认  ==========
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

    # ========== SOP确认 ==========
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
                fill_value='600',
                field_name='T1@A Pressure'
            )

            # 填写B压（调用WebKeys中的fill_if_empty方法）
        with allure.step('填写T1B'):
            self.wk.fill_if_empty(
                locator=allPages.app_gxrw_sopqr_T1B,
                fill_value='600',
                field_name='T1@B Pressure'
            )
            with allure.step('点击提交任务'):
                wk.locator(*allPages.app_gxrw_sopqr_tj).click()
                time.sleep(3)

    # ========== 法兰抽检 ==========
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

    # ========== 完工确认 ==========
    def execute_full_gxrw_wgqr_flow(self):  # 完工确认
        # 点击完工确认页签
        with allure.step('点击完工确认页签'):
            self.wk.locator(*allPages.app_gxrw_wgqr).click()


        # #点击提交按钮提交任务
        with allure.step('点击提交任务'):
            self.wk.locator(*allPages.app_gxrw_wgqr_tj).click()

            time.sleep(3)

    # ========== 法兰校核 ==========
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

        #     # 点击签字
        # with allure.step('点击签字'):
        #     self.wk.locator(*allPages.app_gxrw_fljh_qm).click()
        #     # 调整成手机模式
        # with allure.step('调整成手机模式'):
        #
        #     pyautogui.press("F12")
        #     time.sleep(2)
        #     pyautogui.hotkey('ctrl', 'shift', 'm')
        #     time.sleep(2)
        #     # 定位签字框
        #     # 定位签字框（Canvas）并在正中间绘制“王”字
        # with allure.step("在签字框正中间绘制“王”字"):
        #     try:
        #         # 步骤1：移动到签字框中心，激活绘制区域
        #         pyautogui.moveTo(SIGN_CENTER_X, SIGN_CENTER_Y, duration=0.5)
        #         pyautogui.click()  # 激活Canvas
        #         time.sleep(0.5)
        #
        #         # 步骤2：绘制“王”字（以中心为基准）
        #         # 第一横：中心向左→向右
        #         pyautogui.mouseDown(x=SIGN_CENTER_X - STROKE_LEN, y=SIGN_CENTER_Y - STROKE_LEN)
        #         pyautogui.moveTo(x=SIGN_CENTER_X + STROKE_LEN, y=SIGN_CENTER_Y - STROKE_LEN, duration=0.2)
        #         pyautogui.mouseUp()
        #         time.sleep(0.2)
        #
        #         # 中间竖：中心向上→向下
        #         pyautogui.mouseDown(x=SIGN_CENTER_X, y=SIGN_CENTER_Y - STROKE_LEN)
        #         pyautogui.moveTo(x=SIGN_CENTER_X, y=SIGN_CENTER_Y + STROKE_LEN, duration=0.2)
        #         pyautogui.mouseUp()
        #         time.sleep(0.2)
        #
        #         # 第二横：中心向左→向右
        #         pyautogui.mouseDown(x=SIGN_CENTER_X - STROKE_LEN, y=SIGN_CENTER_Y)
        #         pyautogui.moveTo(x=SIGN_CENTER_X + STROKE_LEN, y=SIGN_CENTER_Y, duration=0.2)
        #         pyautogui.mouseUp()
        #         time.sleep(0.2)
        #
        #         allure.attach(
        #             f"绘制完成：中心坐标({SIGN_CENTER_X},{SIGN_CENTER_Y})，笔画长度{STROKE_LEN}",
        #             "绘制结果",
        #             allure.attachment_type.TEXT
        #         )
        #     except Exception as e:
        #         allure.attach(f"绘制失败：{str(e)}", "错误信息", allure.attachment_type.TEXT)
        #         raise
        #     # 停留查看绘制效果
        #     # 切换电脑模式，定位保存按钮点击保存
        # with allure.step("点击签字框中的保存"):
        #     pyautogui.press("F12")
        #     time.sleep(2)
        #     self.wk.locator(*allPages.app_gxrw_fljh_qm_qmk_bc).click()
        #
        #     # 点击保存，保存签名
        # with allure.step("点击保存，保存签名"):
        #
        #     self.wk.locator(*allPages.app_gxrw_fljh_bc).click()
            # 点击提交按钮保存任务
        with allure.step('点击保存任务'):
            self.wk.locator(*allPages.app_gxrw_fljh_bc).click()
        #点击提交按钮提交任务
        with allure.step('点击提交任务'):
            self.wk.locator(*allPages.app_gxrw_fljh_tj).click()

    # ========== 螺栓抽检 ==========
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

    # 点击成员配置按钮
    def execute_full_PM_cypz_flow(self):
        #点击成员配置按钮
        # 点击成员配置按钮
        with allure.step('点击成员配置按钮'):
            self.wk.locator(*allPages.xmgl_cypz).click()
        # 进入成员配置页面
        # 点击添加
        with allure.step('点击添加'):
            self.wk.locator(*allPages.xmgl_cypz_tj).click()
            # 进入添加页面
            # 点击下拉按钮
        with allure.step('点击下拉按钮'):
            self.wk.locator(*allPages.xmgl_cypz_tj_xl).click()
            # 全选
        with allure.step('全选'):
            self.wk.locator(*allPages.xmgl_cypz_tj_qx).click()
            # 点击确定
        with allure.step('点击确定'):
            self.wk.locator(*allPages.xmgl_cypz_tj_qd).click()
            # 点击返回
        with allure.step('点击返回'):
            self.wk.locator(*allPages.xmgl_cypz_fh).click()
    #推送设备员确认
    def execute_full_PM_tssbyqr_flow(self):
        # 进入项目页面点击推送设备员确认
        with allure.step('进入项目页面点击推送设备员确认'):
            self.wk.locator(*allPages.xmgl_tssby).click()
        # 点击推送按钮
        with allure.step('点击推送按钮'):
            self.wk.locator(*allPages.xmgl_tssby_ts).click()

        # 勾选法兰进行推送
        with allure.step('勾选法兰'):
            self.wk.locator(*allPages.xmgl_tssby_ts_qx).click()

        # 点击确定
        with allure.step('点击确定'):
            self.wk.locator(*allPages.xmgl_tssby_ts_qd).click()

        # 点击返回推送成功
        with allure.step('点击返回推送成功'):
            self.wk.locator(*allPages.xmgl_tssby_fh).click()

    # 配置检修范围
    def execute_full_PM_pzjxfw_flow(self):
        #配置检修范围
        # 点击检修范围
        with allure.step('点击检修范围按钮'):
            self.wk.locator(*allPages.xmgl_jxfw).click()
            time.sleep(3)

            # 勾选全部法兰
            with allure.step('点击勾选全部法兰'):
                self.wk.locator(*allPages.xmgl_jxfw_gx_qx).click()
                time.sleep(2)

            # ====================== 循环翻页勾选（只做勾选，不提交！）======================
            max_pages = 50  # 最多翻50页，防止卡死
            current_page = 0

            while current_page < max_pages:
                try:
                    # 获取选中条数
                    selected_text = self.wk.locator(*allPages.xmgl_jxfw_selected_count).text
                    selected_count = int(selected_text.replace('已选中', '').replace('条数据', ''))
                    allure.attach(f"第{current_page + 1}页选中：{selected_count}条", "数据", allure.attachment_type.TEXT)

                    # 本页无数据 → 翻页
                    if selected_count == 0:
                        with allure.step(f"第{current_page + 1}页无数据，翻下一页"):
                            # JS 点击下一页（永不报错）
                            next_ele = self.wk.locator(*allPages.xmgl_jxfw_xyy)
                            self.browser.execute_script("arguments[0].click();", next_ele)
                            time.sleep(3)

                            # 翻页后重新勾选
                            self.wk.locator(*allPages.xmgl_jxfw_gx_qx).click()
                            time.sleep(2)
                            current_page += 1
                    else:
                        # 有数据，退出循环
                        break

                except Exception as e:
                    allure.attach(f"异常：{str(e)}", "错误", allure.attachment_type.TEXT)
                    break

            # ====================== 【循环结束】才提交！======================
            with allure.step(f'已选中{selected_count}条数据，点击提交'):
                self.wk.locator(*allPages.xmgl_jxfw_tj).click()
                time.sleep(2)

            # 点击确认框确定
            with allure.step('点击确认弹窗确定'):
                self.wk.locator(*allPages.xmgl_jxfw_tj_qr).click()
                time.sleep(2)

            # 点击返回
            with allure.step('点击返回'):
                self.wk.locator(*allPages.xmgl_jxfw_fh).click()

    # 新建服务商
    def execute_full_zg_fwsgl_flow(self):
        #新建服务商
        #添加服务商
        with allure.step('点击添加按钮'):
            self.wk.locator(*allPages.jcsjgl_fwsgl_tj).click()

        #填写服务商名称
        with allure.step('填写服务商名称'):
            self.wk.locator(*allPages.jcsjgl_fwsgl_tj_fwsmc).send_keys("源城测绘")

        #填写服务商简称
        with allure.step('填写服务商简称'):
            self.wk.locator(*allPages.jcsjgl_fwsgl_tj_fwsjc).send_keys("YCCH")

        #填写服务商类型
        with allure.step('填写服务商类型'):
            self.wk.locator(*allPages.jcsjgl_fwsgl_tj_fwslx).click()
            ActionChains(self.browser) \
                .key_down(Keys.DOWN) \
                .key_down(Keys.ENTER) \
                .click()\
                .perform()


        #选择服务范围
        with allure.step('选择服务范围'):
            self.wk.locator(*allPages.jcsjgl_fwsgl_tj_fwfw).click()
            ActionChains(self.browser) \
                .key_down(Keys.DOWN) \
                .key_down(Keys.ENTER) \
                .click()\
                .perform()

        #填写负责人
        with allure.step('填写负责人'):
            self.wk.locator(*allPages.jcsjgl_fwsgl_tj_fzr).send_keys("李学谦")

        #填写联系方式
        with allure.step('填写联系方式'):
            self.wk.locator(*allPages.jcsjgl_fwsgl_tj_lxfs).send_keys('18911773995')

        #点击确认
        with allure.step('点击确认'):
            self.wk.locator(*allPages.jcsjgl_fwsgl_tj_qd).click()

        #专工下发计划
    def execute_full_zg_xfjh_flow(self):
        # 定位服务计划管理
        with allure.step('定位服务计划管理菜单'):
            self.wk.locator(*allPages.fwjh).click()

        # 点击定力矩服务计划菜单
        with allure.step('点击定力矩服务计划菜单'):
            self.wk.locator(*allPages.fwjh_dljfwjh).click()

        # 点击添加定力矩服务计划
        with allure.step('点击添加定力矩服务计划'):
            self.wk.locator(*allPages.fwjh_dljfwjh_tj).click()

            # ---------- 核心改造：使用计数器生成唯一计划名称 ----------
        with allure.step('输入计划名称（计数器生成唯一名称）'):
            # 调用计数器自增方法，获取最新值
            counter_value = self.wk.increment_counter()
            # 拼接唯一名称（前缀可自定义）
            plan_name = f"测试扫码查看预紧力-web-yja-{counter_value}"
            # 输入计划名称
            self.wk.locator(*allPages.fwjh_dljfwjh_jhmc).send_keys(plan_name)
            # 打印日志，方便调试
            allure.attach(f"生成的计划名称：{plan_name}", "计划名称", allure.attachment_type.TEXT)
            # ---------- 计数器改造结束 ----------

        # 选择检修类型
        with allure.step("选择检修类型"):
            self.wk.locator(*allPages.fwjh_dljfwjh_jxlx).click()
            # 通过classname定位到仓库的下拉框
            ActionChains(self.browser) \
                .key_down(Keys.DOWN) \
                .key_down(Keys.ENTER) \
                .perform()
        # 选择开始时间
        with allure.step("选择开始时间"):
            self.wk.locator(*allPages.fwjh_dljfwjh_kssj).click()
            ActionChains(self.browser) \
                .key_down(Keys.DOWN) \
                .key_down(Keys.RIGHT) \
                .key_down(Keys.ENTER) \
                .perform()
        # 选择结束时间
        with allure.step("选择结束时间"):
            self.wk.locator(*allPages.fwjh_dljfwjh_jssj).click()
            ActionChains(self.browser) \
                .key_down(Keys.DOWN) \
                .key_down(Keys.DOWN) \
                .key_down(Keys.DOWN) \
                .key_down(Keys.RIGHT) \
                .key_down(Keys.ENTER) \
                .perform()

        # 点击保存
        with allure.step("保存"):
            self.wk.locator(*allPages.fwjh_dljfwjh_bc).click()

        # 添加检修范围
        with allure.step("点击添加，添加检修范围"):
            self.wk.locator(*allPages.fwjh_dljfwjh_jxfwpz_tj).click()

        # 选择服务商
        with allure.step("选择服务商:北京源城"):
            self.wk.locator(*allPages.fwjh_dljfwjh_jxfwpz_fws).click()
            ActionChains(self.browser) \
                .key_down(Keys.DOWN) \
                .key_down(Keys.ENTER) \
                .perform()

        # 选择装置
        with allure.step("选择装置:55万吨"):
            self.wk.locator(*allPages.fwjh_dljfwjh_jxfwpz_zz).click()
            ActionChains(self.browser) \
                .send_keys('55万吨') \
                .key_down(Keys.DOWN) \
                .key_down(Keys.ENTER) \
                .perform()

        # 填写计划检修量
        with allure.step("选择装置:55万吨"):
            self.wk.locator(*allPages.fwjh_dljfwjh_jxfwpz_jhjxl).send_keys("50")

        # 选择服务模式
        with allure.step("选择服务模式：简易模式"):
            self.wk.locator(*allPages.fwjh_dljfwjh_jxfwpz_fwms).click()
            ActionChains(self.browser) \
                .key_down(Keys.DOWN) \
                .key_down(Keys.DOWN) \
                .key_down(Keys.DOWN) \
                .key_down(Keys.ENTER) \
                .perform()
        # 点击确认保存检修范围
        with allure.step("点击确认保存检修范围"):
            self.wk.locator(*allPages.fwjh_dljfwjh_jxfwpz_qd).click()
        time.sleep(3)
        # 点击下派
        with allure.step("点击下派"):
            self.wk.locator(*allPages.fwjh_dljfwjh_xp).click()
        time.sleep(3)

#设备员确认计划 发布计划
    def execute_full_sby_fbjh_flow(self):
        # 点击待办处理
        with allure.step('点击待办处理'):
            self.wk.locator(*allPages.sby_gzt_db_cl).click()

        # 点击处理弹窗确认按钮
        with allure.step('点击处理弹窗确认按钮'):
            self.wk.locator(*allPages.sby_gzt_db_cl_qr).click()

        # 发布专工的计划
        with allure.step("点击发布计划"):
            self.wk.locator(*allPages.sby_gzt_db_cl_fb).click()

        # 点击提示确认
        with allure.step("点击提示确认"):
            self.wk.locator(*allPages.sby_gzt_db_cl_fb_qd).click()

#服务商负责人添加项目经理
    def execute_full_fws_tjxmjl_flow(self):
        # 点击待办处理
        with allure.step('点击待办处理'):
            self.wk.locator(*allPages.sby_gzt_db_cl).click()

        # 进入项目立项确认页面，点击下一步
        with allure.step('点击下一步'):
            self.wk.locator(*allPages.fws_fzr_lxqr_xyb).click()

        # 进行人员配置页面点击项目经理选择框
        with allure.step("选择项目经理"):
            self.wk.locator(*allPages.fws_fzr_lxqr_xmjl).click()
            ActionChains(self.browser) \
                .key_down(Keys.DOWN) \
                .key_down(Keys.ENTER) \
                .perform()
        # 点击确认按钮
        with allure.step('点击确认按钮'):
            self.wk.locator(*allPages.fws_fzr_lxqr_qr).click()


#设备员通过检修数据确认(项目经理推送法兰)
    def execute_full_sby_jxsjqr_flow(self):
        # 点击待办
        with allure.step('点击待办'):
            self.wk.locator(*allPages.sby_gzt_db_cl).click()

        # 点击确认
        with allure.step('点击确认跳转至详情页'):
            self.wk.locator(*allPages.sby_gzt_db_cl_qr).click()

        # 点击全选
        with allure.step('点击全选'):
            self.wk.locator(*allPages.fwgcgl_jxsjqr_qx).click()

        # 点击通过
        with allure.step('点击通过'):
            self.wk.locator(*allPages.fwgcgl_jxsjqr_tg).click()
        # 点击确定
        with allure.step('点击确定'):
            self.wk.locator(*allPages.fwgcgl_jxsjqr_qd).click()

#进入项目管理页面流程
    def execute_full_xmgl_xq_flow(self):
        # 服务过程管理菜单
        with allure.step('服务过程管理菜单'):
            self.wk.locator(*allPages.fwgcgl).click()
        # 点击定力矩服务菜单
        with allure.step('点击定力矩服务菜单'):
            self.wk.locator(*allPages.fwgcgl_dljfw).click()
        # 点击项目管理菜单
        with allure.step('点击项目管理菜单'):
            self.wk.locator(*allPages.fwgcgl_dljfw_xmgl).click()
        # 进入项目管理页面点击查看按钮
        with allure.step('进入项目管理页面点击查看按钮'):
            self.wk.locator(*allPages.fwgcgl_dljfw_xmgl_ck).click()

#项目经理上传结项资料
    def execute_full_xmgl_scjxzl_flow(self):
        # 进入项目管理详情页面
        with allure.step('点击上传结项材料'):
            self.wk.locator(*allPages.xmgl_jx_scjxzl).click()
        # 进入上传页面，点击上传框
        with allure.step('点击上传框'):
            self.wk.locator(*allPages.xmgl_jx_jxclsc).click()
            time.sleep(2)
            pyautogui.typewrite(r'C:\Users\chens\Pictures\1.jpg', interval=0.1)
            pyautogui.press(keys='ENTER', presses=3)
            time.sleep(3)
        # 点击确定保存上传文件
        with allure.step('点击确定保存上传文件'):
            self.wk.locator(*allPages.xmgl_jx_jxclsc_qd).click()
            time.sleep(3)
        # 点击“其他过程材料页签”
        with allure.step('点击“其他过程材料页签”'):
            self.wk.locator(*allPages.xmgl_jx_jxclsq_yq).click()

        # 点击上传框上传
        with allure.step('点击上传框上传'):
            self.wk.locator(*allPages.xmgl_jx_qtgczlsc).click()
            time.sleep(2)
            pyautogui.typewrite(r'C:\Users\chens\Pictures\1.jpg', interval=0.1)
            pyautogui.press(keys='ENTER', presses=3)
            time.sleep(3)
        # 点击确定按钮
        with allure.step('点击确定按钮'):
            self.wk.locator(*allPages.xmgl_jx_qtgczlsc_qd).click()
            time.sleep(2)
        # 点击退出按钮
        with allure.step('点击“点击退出按钮”'):
            self.wk.locator(*allPages.xmgl_jx_x).click()

    # 项目经理点击结项
    def execute_full_xmgl_jx_flow(self):
        # 点击结项按钮
        with allure.step('点击结项按钮'):
            self.wk.locator(*allPages.xmgl_jx).click()

        # 点击结项确定按钮
        with allure.step('点击结项确定按钮'):
            self.wk.locator(*allPages.xmgl_jx_qd).click()

# 设备员审批通过（法兰添加检修范围）
    def execute_full_sby_jx_pass_flow(self):
        # 点击待办处理
        with allure.step('点击待办处理'):
            self.wk.locator(*allPages.sby_gzt_db_cl).click()

        # 进入检修范围添加确认页面
        with allure.step('点击驳回'):  # 不勾选内容情况下点击驳回会同意所有选项
            self.wk.locator(*allPages.sby_gzt_db_jxfwqr_bh).click()

        # 点击确认按钮
        with allure.step('点击确认按钮'):
            self.wk.locator(*allPages.sby_gzt_db_jxfwqr_bh_qr).click()
        time.sleep(5)
#关闭浏览器
    def close_browser(self, delay=0):
        """
        封装关闭浏览器的通用方法
        :param delay: 延迟关闭时间（秒），默认0秒
        """
        with allure.step(f"延迟{delay}秒后关闭浏览器"):
            if delay > 0:
                time.sleep(delay)
            try:
                self.browser.quit()
                allure.attach(f"延迟{delay}秒后，浏览器已成功关闭", "关闭结果", allure.attachment_type.TEXT)
            except WebDriverException as e:
                error_msg = f"延迟{delay}秒后关闭浏览器失败：{str(e)}"
                allure.attach(error_msg, "关闭结果（异常）", allure.attachment_type.TEXT)
                print(f"【警告】{error_msg}")
            finally:
                self.browser = None
    #退出登录
    def execute_full_log_out_flow(self):
        # 点击个人信息框
        with allure.step('点击个人信息框'):
            self.wk.locator(*allPages.sy_Personal_information_box).click()

        # 点击退出登录
        with allure.step('点击退出登录'):
            self.wk.locator(*allPages.sy_log_out).click()
        time.sleep(6)
#专工下发计划
    def execute_full_zg_Plan_flow(self):
        # 定位服务计划管理
        with allure.step('定位服务计划管理菜单'):
            self.wk.locator(*allPages.fwjh).click()

        # 点击定力矩服务计划菜单
        with allure.step('点击定力矩服务计划菜单'):
            self.wk.locator(*allPages.fwjh_dljfwjh).click()

        # 点击添加定力矩服务计划
        with allure.step('点击添加定力矩服务计划'):
            self.wk.locator(*allPages.fwjh_dljfwjh_tj).click()

            # ---------- 核心改造：使用计数器生成唯一计划名称 ----------
        with allure.step('输入计划名称（计数器生成唯一名称）'):
            # 调用计数器自增方法，获取最新值
            counter_value = self.wk.increment_counter()
            # 拼接唯一名称（前缀可自定义）
            plan_name = f"测试扫码查看预紧力-web-yja-{counter_value}"
            # 输入计划名称
            self.wk.locator(*allPages.fwjh_dljfwjh_jhmc).send_keys(plan_name)
            # 打印日志，方便调试
            allure.attach(f"生成的计划名称：{plan_name}", "计划名称", allure.attachment_type.TEXT)
            # ---------- 计数器改造结束 ----------

        # 选择检修类型
        with allure.step("选择检修类型"):
            self.wk.locator(*allPages.fwjh_dljfwjh_jxlx).click()
            # 通过classname定位到仓库的下拉框
            ActionChains(self.browser) \
                .key_down(Keys.DOWN) \
                .key_down(Keys.ENTER) \
                .perform()
        # 选择开始时间
        with allure.step("选择开始时间"):
            self.wk.locator(*allPages.fwjh_dljfwjh_kssj).click()
            ActionChains(self.browser) \
                .key_down(Keys.DOWN) \
                .key_down(Keys.RIGHT) \
                .key_down(Keys.ENTER) \
                .perform()
        # 选择结束时间
        with allure.step("选择结束时间"):
            self.wk.locator(*allPages.fwjh_dljfwjh_jssj).click()
            ActionChains(self.browser) \
                .key_down(Keys.DOWN) \
                .key_down(Keys.DOWN) \
                .key_down(Keys.DOWN) \
                .key_down(Keys.RIGHT) \
                .key_down(Keys.ENTER) \
                .perform()

        # 点击保存
        with allure.step("保存"):
            self.wk.locator(*allPages.fwjh_dljfwjh_bc).click()

        # 添加检修范围
        with allure.step("点击添加，添加检修范围"):
            self.wk.locator(*allPages.fwjh_dljfwjh_jxfwpz_tj).click()

        # 选择服务商
        with allure.step("选择服务商:北京源城"):
            self.wk.locator(*allPages.fwjh_dljfwjh_jxfwpz_fws).click()
            ActionChains(self.browser) \
                .key_down(Keys.DOWN) \
                .key_down(Keys.ENTER) \
                .perform()

        # 选择装置
        with allure.step("选择装置:55万吨"):
            self.wk.locator(*allPages.fwjh_dljfwjh_jxfwpz_zz).click()
            ActionChains(self.browser) \
                .send_keys('55万吨') \
                .key_down(Keys.DOWN) \
                .key_down(Keys.ENTER) \
                .perform()

        # 填写计划检修量
        with allure.step("选择装置:55万吨"):
            self.wk.locator(*allPages.fwjh_dljfwjh_jxfwpz_jhjxl).send_keys("200")

        # 选择服务模式
        with allure.step("选择服务模式：简易模式"):
            self.wk.locator(*allPages.fwjh_dljfwjh_jxfwpz_fwms).click()
            ActionChains(self.browser) \
                .key_down(Keys.UP) \
                .key_down(Keys.ENTER) \
                .perform()
        # 点击确认保存检修范围
        with allure.step("点击确认保存检修范围"):
            self.wk.locator(*allPages.fwjh_dljfwjh_jxfwpz_qd).click()
        time.sleep(60)
        # 点击下派
        with allure.step("点击下派"):
            self.wk.locator(*allPages.fwjh_dljfwjh_xp).click()
        time.sleep(3)

#项目经理下派任务
    def execute_full_xmjl_xprw_flow(self):
        # 点击服务过程管理
        with allure.step("点击服务过程管理"):
            self.wk.locator(*allPages.fwgcgl).click()
        # 点击定力矩服务
        with allure.step("点击定力矩服务"):
            self.wk.locator(*allPages.fwgcgl_dljfw).click()
        # 点击任务管理
        with allure.step("点击任务管理"):
            self.wk.locator(*allPages.rwgl).click()
        # 点击任务发布
        with allure.step("点击任务发布"):
            self.wk.locator(*allPages.rwfb).click()
        time.sleep(3)
        # 点击勾选全部任务
        with allure.step("勾选全部"):
            self.wk.locator(*allPages.rwfb_check_all).click()
        time.sleep(3)
        # 点击下派
        with allure.step("点击下派"):
            self.wk.locator(*allPages.rwfb_xp).click()
        # 点击负责人下拉框
        with allure.step("点击负责人选项框"):
            self.wk.locator(*allPages.rwfb_xp_fzrxxk).click()
            ActionChains(self.browser) \
                .send_keys("余家傲") \
                .key_down(Keys.DOWN) \
                .key_down(Keys.ENTER) \
                .perform()
        # 点击确定
        with allure.step("点击确定"):
            self.wk.locator(*allPages.rwfb_xp_sure).click()


#"""服务模式"""
#标准模式

    def execute_full_standard_mode_flow(self):
    # 填写法兰挂牌工序任务
        with allure.step('提交工序：法兰挂牌'):
            self.execute_full_gxrw_flgp_flow()
            # 填写法兰拆卸工序任务
        with allure.step('提交工序：法兰拆卸'):
            self.execute_full_gxrw_flcx_flow()
            # 填写密封面检查工序任务
        with allure.step('提交工序：密封面检查'):
            self.execute_full_gxrw_mfmjc_flow()
            # 填写垫片检查工序任务
        with allure.step('提交工序：垫片检查'):
            self.execute_full_gxrw_dpjc_flow()
            # 填写紧固件检查工序任务
        with allure.step('提交工序：紧固件检查'):
            self.execute_full_gxrw_jgjjc_flow()
            # 填写预装确认工序任务
        with allure.step('提交工序：预装确认'):
            self.execute_full_gxrw_yzqr_flow()
            # 填写SOP确认工序任务
        with allure.step('提交工序：SOP确认'):
            self.execute_full_gxrw_sopqr_flow()
            # 填写法兰抽检工序任务
        with allure.step('提交工序：法兰抽检'):
            self.execute_full_gxrw_flcj_flow()
            # 填写完工确认工序任务
        with allure.step('提交工序：完工确认'):
            self.execute_full_gxrw_wgqr_flow()
            # 填写法兰校核工序任务
        with allure.step('提交工序：法兰校核'):
            self.execute_full_gxrw_fljh_flow()
            # 填写螺栓抽检工序任务
        with allure.step('提交工序：螺栓抽检'):
            self.execute_full_gxrw_lscj_flow()
        time.sleep(5)

# """验证APP任务提交是否完成"""
    def execute_full_verification_flow(self):
        with allure.step("点击已完成"):

