"""
    一.Base类 封装元素 定位方法/操作元素的方法（点击，输入）
"""
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self, driver):
        self.driver = driver

    # 查找单个元素的方法
    def find_ele(self, loc, timeout=5, poll=1):
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*loc))

    # 查找一组元素的方法
    def find_eles(self, loc, timeout=5, poll=1):
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(*loc))

    # 点击元素的操作
    def click_ele(self, loc, timeout=5, poll=1):
        WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*loc)).click()

    # 输入操作
    def send_ele(self, loc, text, timeout=5, poll=1):
        WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*loc)).send_keys(text)
