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
