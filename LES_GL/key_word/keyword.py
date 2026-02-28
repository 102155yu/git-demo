"""
    封装：函数、类（方法）
"""
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import os
import threading

#定义工具类（进行关键字驱动）
class WebKeys:
    # 构造方法，用来接收driver对象
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,5)
        # 计数器文件锁（解决多线程冲突）
        self.counter_lock = threading.Lock()
        # 计数器文件路径（放在keyword同级目录，避免路径问题）
        self.counter_file = os.path.join(os.path.dirname(__file__), "counter.txt")

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

    # ---------- 新增计数器核心方法 ----------
    def read_counter(self):
        """读取计数器值，文件不存在则返回0"""
        with self.counter_lock:
            if not os.path.exists(self.counter_file):
                return 0
            try:
                with open(self.counter_file, 'r', encoding='utf-8') as f:
                    # 防止文件为空或非数字
                    content = f.read().strip()
                    return int(content) if content.isdigit() else 0
            except (PermissionError, ValueError) as e:
                print(f"读取计数器失败：{e}，默认返回0")
                return 0

    def write_counter(self, value):
        """写入计数器值到文件"""
        with self.counter_lock:
            try:
                with open(self.counter_file, 'w', encoding='utf-8') as f:
                    f.write(str(value))
            except PermissionError as e:
                print(f"写入计数器失败：{e}")
                raise  # 抛出异常让用例感知错误

    def increment_counter(self):
        """计数器自增1并返回新值"""
        current = self.read_counter()
        new_value = current + 1
        self.write_counter(new_value)
        return new_value

    #日期控件（保留原有注释，后续可补充）
    # wait.until(ec.visibility_of_element_located(locator)).send_keys("2022‐09‐30")