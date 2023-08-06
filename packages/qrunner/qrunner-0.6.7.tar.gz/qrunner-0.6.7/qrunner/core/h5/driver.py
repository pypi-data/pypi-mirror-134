import requests
from selenium import webdriver
from qrunner.running.config import Qrunner
from qrunner.utils.log import logger


# 重启chromedriver的装饰器
def relaunch(func):
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except requests.exceptions.ConnectionError as _:
            logger.warning("h5 driver error, relaunch now.")
            self.d = H5Driver.get_instance(Qrunner.serial_no)
    return wrapper


class H5Driver(object):
    _instance = {}

    def __new__(cls, serial_no=None):
        if not serial_no:
            serial_no = Qrunner.serial_no
        if serial_no not in cls._instance:
            cls._instance[serial_no] = super().__new__(cls)
        return cls._instance[serial_no]

    def __init__(self, serial_no=None, pkg_name=None):
        if not serial_no:
            serial_no = Qrunner.serial_no
        if not pkg_name:
            pkg_name = Qrunner.pkg_name

        logger.info(f'启动H5Driver for {serial_no}')
        options = webdriver.ChromeOptions()
        options.add_experimental_option('androidDeviceSerial', serial_no)
        options.add_experimental_option('androidPackage', pkg_name)
        options.add_experimental_option('androidUseRunningApp', True)
        options.add_experimental_option('androidProcess', pkg_name)
        self.d = webdriver.Chrome(options=options)
        self.d.set_page_load_timeout(10)

    @staticmethod
    def get_instance(cls, serial_no=None):
        if serial_no not in cls._instance:
            logger.info(f'{serial_no} Create h5 driver singleton')
            return H5Driver(serial_no)
        return H5Driver._instance[serial_no]

    @relaunch
    def back(self):
        logger.info('返回上一页')
        self.d.back()

    @relaunch
    def get_ui_tree(self):
        page_source = self.d.page_source
        logger.info(f'获取页面内容: \n{page_source}')
        return page_source

    @relaunch
    def get_windows(self):
        logger.info(f'获取当前打开的窗口列表')
        return self.d.window_handles

    @relaunch
    def switch_window(self, old_windows):
        logger.info('切换到最新的window')
        current_windows = self.get_windows()
        newest_window = [window for window in current_windows if window not in old_windows][0]
        self.d.switch_to.window(newest_window)

    @relaunch
    def execute_js(self, script, element):
        logger.info(f'执行js脚本: \n{script}')
        self.d.execute_script(script, element)





