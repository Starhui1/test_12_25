"""获取android的driver"""
from appium import webdriver


def get_android_driver(pag, act):
    capabilities = {
        "platformName": "Android",  # 手机系统
        "platformVersion": "5.1",   # 手机版本
        "deviceName": "模拟器",      # 手机名称
        "appPackage": pag,          # 包名
        "appActivity": act}         # 启动名
    return webdriver.Remote('http://127.0.0.1:4723/wd/hub',
                     desired_capabilities=capabilities)
