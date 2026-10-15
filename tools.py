import json
import logging
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from logging import handlers
from config import (PATH,DRIVER_PATH)

# 浏览器驱动类
class DriverTools:

    driver = None

    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            ser = Service(executable_path=DRIVER_PATH)
            # 启动时禁用密码泄露检测
            options = webdriver.ChromeOptions()
            options.add_experimental_option("prefs", {
                "profile.password_manager_leak_detection": False
            })

            cls.driver = webdriver.Chrome(service=ser, options=options)
            # 浏览器最大化
            cls.driver.maximize_window()
            cls.driver.implicitly_wait(10)

        return cls.driver

    @classmethod
    def quit_driver(cls):

        if cls.driver:
            time.sleep(2)
            cls.driver.quit()
            cls.driver = None


# 读取json文件并转换成格式为 [(),(), ...] 的列表
def read_json(file_name):
    data = []
    file_path = PATH + "/data/" + file_name
    with open(file_path, mode="r", encoding="utf-8") as f:
        tmp = json.load(f)
        for i in tmp:
            a = tuple(i.values())
            data.append(a)
        return data


class GetLog:
    __log = None

    @classmethod
    def get_log(cls):
        if cls.__log is None:
            cls.__log = logging.getLogger()
            cls.__log.setLevel(logging.INFO)

            filename = PATH + "/log/" + "web.log"
            tf = logging.handlers.TimedRotatingFileHandler(
                filename=filename, # 日志文件名
                when="midnight", # 日志归档时间
                interval=1, # 每天归档一次
                backupCount=3, # 保留3天日志
                encoding="utf-8" # 日志编码格式
            )

            # 获取格式器
            fmt = "%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
            fm = logging.Formatter(fmt)
            # 将格式器添加到处理器
            tf.setFormatter(fm)
            # 将处理器添加到日志器
            cls.__log.addHandler(tf)

        return cls.__log


if __name__ == "__main__":
    print(read_json("login_data.json"))