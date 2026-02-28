#应用POM模式实现登录
import time

from LES_GL.VAR.BOOKHOUSER_VAR import *
from LES_GL.page.login import LoginPage



def test_login02(browser):
    #初始化页面对象
    login = LoginPage(browser)
    login.login(LOGIN_URL,USERNAME,PASSWD)
    time.sleep(3)