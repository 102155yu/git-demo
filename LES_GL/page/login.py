import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as ec
import pyautogui
from LES_GL.key_word.keyword import WebKeys
from LES_GL.locate.allPages import *
from LES_GL.VAR.BOOKHOUSER_VAR import LOGIN_URL_APP, USERNAME_CZG_YJA, PASSWD
from LES_GL.key_word.keyword import WebKeys
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

    def fill_if_empty(wait, wk, locator, fill_value, field_name):
        """
        :param wait: WebDriverWait实例
        :param wk: WebKeys实例
        :param locator: 元素定位器（元组）
        :param fill_value: 要填写的值
        :param field_name: 字段名称（用于报告/日志）
        """
        try:
            # 等待元素可交互（最长10秒），解决"未加载完成/不可交互"问题
            ele = wait.until(
                EC.element_to_be_clickable(locator)
            )
            # 聚焦到输入框（解决遮挡/未激活问题）
            ele.click()
            # 获取输入框当前值（兼容value属性/文本内容）
            current_value = ele.get_attribute('value') or ele.text or ''
            current_value = current_value.strip()

            if not current_value:
                # 清空原有空值（避免输入叠加）+ 输入值
                ele.clear()
                ele.send_keys(fill_value)
                allure.attach(f'{field_name}为空，已填写{fill_value}', '操作说明')
            else:
                allure.attach(f'{field_name}已有值：{current_value}，无需填写', '操作说明')
        except TimeoutException:
            allure.attach(f'{field_name}元素超时未加载，跳过填写', '异常说明')
            raise  # 抛出异常，让用例失败（也可根据需求改为continue）
        except ElementNotInteractableException:
            allure.attach(f'{field_name}元素不可交互，跳过填写', '异常说明')
            raise
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

    # def execute_full_gxrw_flgp_flow(self):
    #
    # def execute_full_gxrw_flcx_flow(self):
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
    # def execute_full_gxrw_yzqr_flow(self):
    # def execute_full_gxrw_sopqr_flow(self):
    #     def fill_if_empty(wait, wk, locator, fill_value, field_name):
    #         """
    #         :param wait: WebDriverWait实例
    #         :param wk: WebKeys实例
    #         :param locator: 元素定位器（元组）
    #         :param fill_value: 要填写的值
    #         :param field_name: 字段名称（用于报告/日志）
    #         """
    #         try:
    #             # 等待元素可交互（最长10秒），解决"未加载完成/不可交互"问题
    #             ele = wait.until(
    #                 EC.element_to_be_clickable(locator)
    #             )
    #             # 聚焦到输入框（解决遮挡/未激活问题）
    #             ele.click()
    #             # 获取输入框当前值（兼容value属性/文本内容）
    #             current_value = ele.get_attribute('value') or ele.text or ''
    #             current_value = current_value.strip()
    #
    #             if not current_value:
    #                 # 清空原有空值（避免输入叠加）+ 输入值
    #                 ele.clear()
    #                 ele.send_keys(fill_value)
    #                 allure.attach(f'{field_name}为空，已填写{fill_value}', '操作说明')
    #             else:
    #                 allure.attach(f'{field_name}已有值：{current_value}，无需填写', '操作说明')
    #         except TimeoutException:
    #             allure.attach(f'{field_name}元素超时未加载，跳过填写', '异常说明')
    #             raise  # 抛出异常，让用例失败（也可根据需求改为continue）
    #         except ElementNotInteractableException:
    #             allure.attach(f'{field_name}元素不可交互，跳过填写', '异常说明')
    #             raise
    #     # ========== 7. SOP确认 ==========
    #     # 点击SOP确认页签
    #     with allure.step('点击页签SOP确认'):
    #         self.wk.locator(*allPages.app_gxrw_sopqr).click()
    #         time.sleep(3)
    #         # 点击工具类型
    #     with allure.step('选择工具类型'):
    #         self.wk.locator(*allPages.app_gxrw_sopqr_gjlx).click()
    #         time.sleep(2)
    #         # ActionChains(browser) \
    #         #     .key_down(Keys.ENTER) \
    #         #     .perform()
    #         # 选择工具类型
    #     with allure.step('选择工具类型'):
    #         self.wk.locator(*allPages.app_gxrw_sopqr_gjlx_yyfq).click()
    #         time.sleep(10)
    #     #     点击完成
    #     # 点击工具型号
    #     # 选择工具型号
    #     # 点击完成
    #     # 填写工具数量
    #     # 填写工具数量
    #     with allure.step('填写工具数量'):
    #         self.wk.locator(*allPages.app_gxrw_sopqr_gjsl).send_keys('2')
    #         # 填写摩擦系数
    #     # with allure.step('填写摩擦系数'):
    #     #     wk.locator(*allPages.app_gxrw_sopqr_mcxs).send_keys('0.1')
    #     #     #填写A压
    #     # with allure.step('填写A压'):
    #     #     wk.locator(*allPages.app_gxrw_sopqr_Ay).send_keys('0.1')
    #     #     #填写B压
    #     # with allure.step('填写B压'):
    #     #     wk.locator(*allPages.app_gxrw_sopqr_By).send_keys('0.1')
    #
    #     # #点击提交按钮提交任务
    #     # with allure.step('点击提交任务'):
    #     #     wk.locator(*allPages.app_gxrw_flgp_tj).click()
    #     # ========== 核心修复：使用通用函数处理字段填写 ==========
    #     # 处理摩擦系数
    #     with allure.step('填写摩擦系数（无值时填写）'):
    #         fill_if_empty(
    #             wait=wait,
    #             wk=wk,
    #             locator=allPages.app_gxrw_sopqr_mcxs,
    #             fill_value='0.1',
    #             field_name='摩擦系数'
    #         )
    #
    #         # 处理A压
    #     with allure.step('填写T1@A（无值时填写）'):
    #         fill_if_empty(
    #             wait=wait,
    #             wk=wk,
    #             locator=allPages.app_gxrw_sopqr_T1A,
    #             fill_value='0.1',
    #             field_name='A压'
    #         )
    #
    #         # 处理B压
    #     with allure.step('填写T1@B（无值时填写）'):
    #         fill_if_empty(
    #             wait=wait,
    #             wk=wk,
    #             locator=allPages.app_gxrw_sopqr_T1B,
    #             fill_value='0.1',
    #             field_name='B压'
    #         )
    #
    # def execute_full_gxrw_flcj_flow(self):
    # def execute_full_gxrw_wgqr_flow(self):
    # def execute_full_gxrw_fljh_flow(self):
    # def execute_full_gxrw_lscj_flow(self):