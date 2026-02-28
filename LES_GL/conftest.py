import allure
import pytest


from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # 新增导入
#浏览器预制fix
@pytest.fixture()
def browser():
    # 全局变量 driver
    global driver
    # 1. 替换为你解压后的 chromedriver.exe 路径
    driver_path = r"D:\Python\chromedriver.exe"  # 示例路径，根据实际修改
    # 2. 创建 Service 对象，指定驱动路径
    service = Service(executable_path=driver_path)
    # 3. 初始化 Chrome 浏览器
    driver = webdriver.Chrome(service=service)

    # 可选：设置隐式等待，提升稳定性
    driver.implicitly_wait(10)
    yield driver
    # 用例执行完后关闭浏览器
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


