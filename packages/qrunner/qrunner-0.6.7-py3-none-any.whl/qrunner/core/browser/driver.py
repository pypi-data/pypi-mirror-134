import allure
import requests
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver import ChromeOptions
from selenium.webdriver import FirefoxOptions
from selenium.webdriver import EdgeOptions
from qrunner.utils.webdriver_manager_extend import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager
from qrunner.running.config import BrowserConfig
from qrunner.utils.log import logger
from qrunner.utils.data import get_time


def relaunch(func):
    """
    重启chromedriver的装饰器
    :param func: 待包裹的函数
    :return:
    """
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except requests.exceptions.ConnectionError as _:
            logger.warning("web driver error, relaunch now.")
            self.d = BrowserDriver(BrowserConfig.name)
    return wrapper


class Browser(object):
    """
    根据关键词初始化浏览器操作句柄，
    如'chrome、google chrome、gc'代表chrome浏览器，
    如'firefox、ff'代表火狐浏览器，
    如'internet explorer、ie、IE'代表ie浏览器，
    如'edge'代表edge浏览器，
    如'opera'代表opera浏览器，
    如'safari'代表safari浏览器
    """
    name = None

    def __new__(cls, name=None):
        cls.name = name

        if (cls.name is None) or (cls.name in ["chrome", "google chrome", "gc"]):
            return cls.chrome()
        elif cls.name in ['internet explorer', 'ie', 'IE']:
            return cls.ie()
        elif cls.name in ['firefox', 'ff']:
            return cls.firefox()
        elif cls.name == 'edge':
            return cls.edge()
        elif cls.name == 'opera':
            return cls.opera()
        elif cls.name == 'safari':
            return cls.safari()
        raise NameError(f"Not found {cls.name} browser")

    @staticmethod
    def chrome():
        if BrowserConfig.command_executor != "":
            return webdriver.Remote(command_executor=BrowserConfig.command_executor,
                                    desired_capabilities=DesiredCapabilities.CHROME.copy())

        if BrowserConfig.options is None:
            chrome_options = ChromeOptions()
        else:
            chrome_options = BrowserConfig.options
        if BrowserConfig.headless is True:
            chrome_options.add_argument('--headless')

        chrome_options.add_argument("--incognito")  # 隐身模式
        chrome_options.add_experimental_option("excludeSwitches",
                                               ['enable-automation'])  # 去除自动化控制提示
        # prefs = {'profile.managed_default_content_settings.images': 2}  # 不加载图片
        # prefs = {'profile.managed_default_content_settings.javascript': 2}  # 不加载js
        # chrome_options.add_experimental_option('prefs', prefs)
        chrome_options.page_load_strategy = 'normal'  # 设置页面加载策略

        driver = webdriver.Chrome(options=chrome_options,
                                  executable_path=ChromeDriverManager().install(),
                                  )
        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
                Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
                })"""
        })
        return driver

    @staticmethod
    def firefox():
        if BrowserConfig.command_executor != "":
            return webdriver.Remote(command_executor=BrowserConfig.command_executor,
                                    desired_capabilities=DesiredCapabilities.FIREFOX.copy())

        if BrowserConfig.options is not None:
            firefox_options = FirefoxOptions()
        else:
            firefox_options = BrowserConfig.options
        if BrowserConfig.headless is True:
            firefox_options.headless = True

        driver = webdriver.Firefox(options=firefox_options,
                                   executable_path=GeckoDriverManager().install())
        return driver

    @staticmethod
    def ie():
        if BrowserConfig.command_executor != "":
            return webdriver.Remote(command_executor=BrowserConfig.command_executor,
                                    desired_capabilities=DesiredCapabilities.INTERNETEXPLORER.copy())
        return webdriver.Ie(executable_path=IEDriverManager().install())

    @staticmethod
    def edge():
        if BrowserConfig.command_executor != "":
            return webdriver.Remote(command_executor=BrowserConfig.command_executor,
                                    desired_capabilities=DesiredCapabilities.EDGE.copy())

        if BrowserConfig.headless is True:
            edge_options = EdgeOptions()
            edge_options.headless = True
            return webdriver.Edge(executable_path=EdgeChromiumDriverManager(log_level=1).install(),
                                  options=edge_options)

        return webdriver.Edge(executable_path=EdgeChromiumDriverManager(log_level=1).install())

    @staticmethod
    def opera():
        if BrowserConfig.command_executor != "":
            return webdriver.Remote(command_executor=BrowserConfig.command_executor,
                                    desired_capabilities=DesiredCapabilities.OPERA.copy())
        return webdriver.Opera(executable_path=OperaDriverManager().install())

    @staticmethod
    def safari():
        if BrowserConfig.command_executor != "":
            return webdriver.Remote(command_executor=BrowserConfig.command_executor,
                                    desired_capabilities=DesiredCapabilities.SAFARI.copy())
        return webdriver.Safari(executable_path='/usr/bin/safaridriver')


class BrowserDriver(object):
    def __init__(self, browser_name=None):
        self.d = Browser(browser_name)
        self.d.set_page_load_timeout(30)
        if BrowserConfig.headless is True:
            self.d.set_window_size(1920, 1080)
        else:
            self.d.maximize_window()

    @relaunch
    def open_url(self, url):
        logger.info(f'访问: {url}')
        self.d.get(url)

    @relaunch
    def back(self):
        logger.info('返回上一页')
        self.d.back()

    @relaunch
    def upload_pic(self, filename):
        allure.attach.file(self.d.get_screenshot_as_png(),
                           attachment_type=allure.attachment_type.PNG,
                           name=f'{filename}-{get_time()}')

    @relaunch
    @property
    def page_content(self):
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
        current_windows = self.d.window_handles
        newest_window = [window for window in current_windows if window not in old_windows][0]
        self.d.switch_to.window(newest_window)

    @relaunch
    def switch_iframe(self, frame_id):
        logger.info(f'切换到frame {frame_id}')
        self.d.switch_to.frame(frame_id)

    @relaunch
    def execute_js(self, script, element):
        logger.info(f'执行js脚本: \n{script}')
        self.d.execute_script(script, element)

    @relaunch
    def click(self, element):
        logger.info(f'点击元素: {element}')
        self.d.execute_script('arguments[0].click();', element)

    @relaunch
    def quit(self):
        logger.info('退出浏览器')
        self.d.quit()

    @relaunch
    def close(self):
        logger.info('关闭当前页签')
        self.d.close()

    @relaunch
    def add_cookies(self, cookies: list):
        for cookie in cookies:
            self.d.add_cookie(cookie)

    @relaunch
    def refresh(self):
        self.d.refresh()










