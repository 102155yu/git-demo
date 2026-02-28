"""
    封装：函数、类（方法）
"""
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

#定义工具类（进行关键字驱动）

class WebKeys:
    # 构造方法，用来接收driver对象
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,5)
        # 编代码用，写完删掉
        # self.driver = webdriver.Chrome()

    #打开浏览器

    def open(self,url):
        self.driver.get(url)
        self.wait.until(ec.url_contains(url))

    #元素定位
    def locator(self,name,value):
        """元素定位➕显示等待"""
        locator = (name , value)
        self.wait.until(ec.visibility_of_element_located(locator))
        el = self.driver.find_element(name , value)
        #将定位的元素标记出来
        self.locator_station(el)
        return el

    #显示定位的地方，方便确认定位位置
    def locator_station(self, ele):
        self.driver.execute_script(
            "arguments[0].setAttribute('style',arguments[1]);",
            ele,
            "border: 2px solid red"  # 边框，red红色
        )

    #日期控件

    # wait.until(ec.visibility_of_element_located(locator)).send_keys("2022‐09‐30")