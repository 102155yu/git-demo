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
from LES_GL.page.process import GxrwJymsExecutor


@allure.epic('LES系统')
@allure.feature('项目经理工作台')
@allure.story('配置项目信息')
@allure.title('项目经理配置项目信息')
@allure.severity('critical')
def test_login02(browser):
    """
        用例编号：test_loin02
            用例标题：项目经理配置项目信息
            前置条件：服务商负责人配置完成项目经理
            测试步骤：
                1.登录项目经理账号
                2.点击工作台待办处理
                3.项目配置项目成员
                4.添加法兰进入检修范围
                5.提交至设备员确认

            预期结果；项目成员配置成功，法兰添加成功

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
    LES = GxrwJymsExecutor(browser)
    #进入登录
    with allure.step('进入LES登录页'):
        login = LoginPage(browser)
        login.login(LOGIN_URL_PC, USERNAME_XMJL_LQ, PASSWD)
    time.sleep(1)


    # 点击待办处理
    with allure.step('进入项目管理详情'):
        LES.execute_full_xmgl_xq_flow()
    #点击检修范围
    with allure.step('点击检修范围按钮'):
        wk.locator(*allPages.xmgl_jxfw).click()
        time.sleep(3)

        # 勾选全部法兰
        with allure.step('点击勾选全部法兰'):
            wk.locator(*allPages.xmgl_jxfw_gx_qx).click()
            time.sleep(2)

        # ====================== 循环翻页勾选（只做勾选，不提交！）======================
        max_pages = 50  # 最多翻50页，防止卡死
        current_page = 0

        while current_page < max_pages:
            try:
                # 获取选中条数
                selected_text = wk.locator(*allPages.xmgl_jxfw_selected_count).text
                selected_count = int(selected_text.replace('已选中', '').replace('条数据', ''))
                allure.attach(f"第{current_page + 1}页选中：{selected_count}条", "数据", allure.attachment_type.TEXT)

                # 本页无数据 → 翻页
                if selected_count == 0:
                    with allure.step(f"第{current_page + 1}页无数据，翻下一页"):
                        # JS 点击下一页（永不报错）
                        next_ele = wk.locator(*allPages.xmgl_jxfw_xyy)
                        browser.execute_script("arguments[0].click();", next_ele)
                        time.sleep(3)

                        # 翻页后重新勾选
                        wk.locator(*allPages.xmgl_jxfw_gx_qx).click()
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
            wk.locator(*allPages.xmgl_jxfw_tj).click()
            time.sleep(2)

        # 点击确认框确定
        with allure.step('点击确认弹窗确定'):
            wk.locator(*allPages.xmgl_jxfw_tj_qr).click()
            time.sleep(2)

        # 点击返回
        with allure.step('点击返回'):
            wk.locator(*allPages.xmgl_jxfw_fh).click()
