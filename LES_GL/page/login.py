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
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException


#以页面或组件为单位，封装常用的行为代码和页面元素定位代码
class LoginPage(WebKeys):
    # #登录操作
    # def login(self,url,username,passwd):
    #     self.open(url)
    #     #实例化Wait
    #     wait = WebDriverWait(self.driver,5)
    #     #根据‘登录LES_GL’作为等待条件
    #     # wait.until(ec.text_to_be_present_in_element((By.XPATH,'//div'),"欢迎登陆"))
    #
    #     #登录操作
    #     #01进行用户登录
    #     self.locator(*page_login_user).send_keys(username)
    #     self.locator(*page_login_indexPwd).send_keys(passwd)
    #     self.locator(*page_login_loginBtn).click()
    # 打开登录页面（仅负责加载登录URL）
    def open_login_page(self, url):
        """
        打开指定的登录页面URL
        :param url: 登录页面的地址
        """
        self.open(url)
        # 实例化Wait（保持原有等待逻辑，可根据需要扩展）
        wait = WebDriverWait(self.driver, 5)
        # 可选：添加登录页面加载完成的等待条件（如原注释的“欢迎登陆”文本）
        # wait.until(ec.text_to_be_present_in_element((By.XPATH,'//div'),"欢迎登陆"))

    # 输入账号密码并执行登录（需先调用open_login_page打开页面）
    def input_credential_and_login(self, username, passwd):
        """
        输入账号密码并点击登录按钮
        :param username: 登录用户名
        :param passwd: 登录密码
        """
        # 01 输入用户名
        self.locator(*page_login_user).send_keys(username)
        # 02 输入密码
        self.locator(*page_login_indexPwd).send_keys(passwd)
        # 03 点击登录按钮
        self.locator(*page_login_loginBtn).click()

    # 兼容原有逻辑的整合方法（可选保留，方便老代码调用）
    def login(self, url, username, passwd):
        self.open_login_page(url)
        self.input_credential_and_login(username, passwd)
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

