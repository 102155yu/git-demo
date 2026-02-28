import allure
import pytest

from selenium import webdriver

#浏览器预制fix
@pytest.fixture()
def browser():
    #01用例前置操作
    #定义全局变量driver，本文件中其他fix可以共享
    global driver
    driver = webdriver.Chrome()
    #02用例执行，返回driver
    yield driver
    #03 用例后置，关闭浏览器
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport():
    # 获取到用例执行之后的result对象
    out = yield
    """
        setup:
        call: 测试执行中
        teardown:
        wasxfail: 标记失败的用例
    """
    report = out.get_result()

    # 判断call阶段(测试用例的执行阶段），如果你的用例被标记为失败，那么就完成截图
    if report.when == "call":
        xfail = hasattr(report, "wasxfail")
        # report.skipped: 用例跳过
        # report.failed：用例失败
        if (report.skipped and xfail) or (report.failed and not xfail):
            with allure.step("添加失败截图... ..."):
                allure.attach(driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)


