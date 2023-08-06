import sys
from qrunner.running.config import Qrunner, BrowserConfig
from qrunner.utils.log import logger
from qrunner.utils.config import conf
from qrunner.core.android.driver import AndroidDriver
from qrunner.core.android.element import Element as AndroidElement
from qrunner.core.ios.driver import IosDriver
from qrunner.core.ios.element import Element as IosElement
from qrunner.core.browser.driver import BrowserDriver
from qrunner.core.browser.element import Element as WebElement


class TestCase:
    """
    测试用例基类，所有测试用例需要继承该类
    """
    def start_class(self):
        """
        Hook method for setup_class fixture
        :return:
        """
        pass

    def end_class(self):
        """
        Hook method for teardown_class fixture
        :return:
        """
        pass

    @classmethod
    def setup_class(cls):
        # 初始化driver
        logger.info('初始化driver')
        # 从配置文件中获取浏览器相关配置（为了支持并发执行）
        Qrunner.platform = conf.get_name('info', 'platform')
        if conf.get_name('info', 'headless') == 'true':
            BrowserConfig.headless = True
        BrowserConfig.name = conf.get_name('info', 'browser_name')

        if Qrunner.platform == 'android':
            if Qrunner.serial_no:
                cls.driver: AndroidDriver = AndroidDriver(Qrunner.serial_no)
            else:
                logger.info('serial_no为空')
                sys.exit()
        elif Qrunner.platform == 'ios':
            if Qrunner.serial_no:
                cls.driver: IosDriver = IosDriver(Qrunner.serial_no)
            else:
                logger.info('serial_no为空')
                sys.exit()
        elif Qrunner.platform == 'browser':
            cls.driver: BrowserDriver = BrowserDriver(BrowserConfig.name)
        else:
            logger.info(f'不支持的平台: {Qrunner.platform}')
            sys.exit()
        cls().start_class()

    @property
    def driver(self):
        driver = None
        if Qrunner.platform == 'android':
            driver: AndroidDriver = self.driver
        elif Qrunner.platform == 'ios':
            driver: IosDriver = self.driver
        elif Qrunner.platform == 'browser':
            driver: BrowserDriver = self.driver
        return driver

    @classmethod
    def teardown_class(cls):
        logger.info('teardown_class')
        logger.info(Qrunner.platform)
        if Qrunner.platform == 'browser':
            cls().driver.quit()
        cls().end_class()

    def start(self):
        """
        Hook method for setup_method fixture
        :return:
        """
        pass

    def end(self):
        """
        Hook method for teardown_method fixture
        :return:
        """
        pass

    def setup_method(self):
        if Qrunner.platform in ['android', 'ios']:
            self.driver.force_start_app()
        self.start()

    def teardown_method(self):
        self.end()
        if Qrunner.platform in ['android', 'ios']:
            self.driver.stop_app()

    def el(self, *args, **kwargs):
        """
        :param args: 暂时无用
        :param kwargs: 元素定位方式
        :return: 根据平台返回对应的元素
        """
        if Qrunner.platform == 'android':
            element: AndroidElement = AndroidElement(**kwargs)
        elif Qrunner.platform == 'ios':
            element: IosElement = IosElement(**kwargs)
        elif Qrunner.platform == 'browser':
            element: WebElement = WebElement(self.driver, **kwargs)
        else:
            logger.info(f'不支持的平台: {Qrunner.platform}，暂时只支持android、ios、browser')
            sys.exit()
        return element

    def open(self, url, cookies: list = None):
        """
        访问链接为url的页码
        :param url: 页面链接
        :param cookies: [
            {'name': 'xxx', 'value': 'xxxx'},
            {'name': 'xxx', 'value': 'xxxx'},
        ]
        :return:
        """
        self.driver.open_url(url)
        if cookies:
            self.driver.add_cookies(cookies)
            self.driver.refresh()

    def screenshot(self, file_name):
        """
        截图并存为文件
        :param file_name: 如test.png
        :return:
        """
        self.driver.screenshot(file_name)

    def allure_shot(self, file_name):
        """
        截图并上传至allure
        :param file_name: 如首页截图
        :return:
        """
        self.driver.upload_pic(file_name)







