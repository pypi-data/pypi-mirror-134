import sys
import pytest
from qrunner.running.config import Qrunner, BrowserConfig
from qrunner.utils.log import logger
from qrunner.utils.config import conf
from qrunner.core.android.driver import AndroidDriver
from qrunner.core.ios.driver import IosDriver
from qrunner.core.browser.driver import BrowserDriver
from selenium.webdriver.remote.webdriver import WebDriver as SeleniumWebDriver


class TestMain(object):
    """
    Support for app and web
    """
    def __init__(self,
                 platform=None,
                 serial_no=None,
                 pkg_name=None,
                 browser_name='chrome',
                 headless=False,
                 case_path=None,
                 rerun='0',
                 alert_list=None,
                 concurrent=False
                 ):
        """
        :param platform: 平台，如browser、android、ios
        :param serial_no: 设备id，如UJK0220521066836、00008020-00086434116A002E
        :param pkg_name: 应用包名，如com.qizhidao.clientapp、com.qizhidao.company
        :param browser_name: 浏览器类型，如chrome、其他暂不支持
        :param headless: 前后台运行，如前台运行False、后台运行True
        :param case_path: 用例路径
        :param rerun: 失败重试次数
        :param alert_list: 需要处理的alert弹窗
        :param concurrent: 是否需要并发执行，只支持platform为browser的情况
        """

        if alert_list is None:
            alert_list = []
        self.platform = platform
        self.serial_no = serial_no
        self.pkg_name = pkg_name
        self.browser_name = browser_name
        self.headless = headless
        self.case_path = case_path
        if isinstance(rerun, int):
            self.rerun = str(rerun)
        self.rerun = rerun
        self.alert_list = alert_list
        self.concurrent = concurrent

        # 将数据写入全局变量
        Qrunner.platform = self.platform
        Qrunner.serial_no = self.serial_no
        Qrunner.pkg_name = self.pkg_name
        Qrunner.alert_list = self.alert_list
        BrowserConfig.name = self.browser_name

        # 将platform写入配置文件（为了支持并发执行）
        conf.set_name('info', 'platform', self.platform)
        if self.headless:
            conf.set_name('info', 'headless', 'true')
        else:
            conf.set_name('info', 'headless', 'false')
        conf.set_name('info', 'browser_name', self.browser_name)

        # 执行用例
        logger.info('执行用例')
        logger.info(f'平台: {Qrunner.platform}')
        cmd_list = [
            '-sv',
            '--reruns', self.rerun,
            '--alluredir', 'allure-results', '--clean-alluredir',
            '--html=report.html', '--self-contained-html'
        ]
        if self.case_path:
            cmd_list.insert(0, self.case_path)
        if self.concurrent:
            if self.platform == 'browser':
                cmd_list.insert(1, '-n')
                cmd_list.insert(2, 'auto')
                cmd_list.insert(3, '--dist=loadscope')
            else:
                logger.info(f'{self.platform}平台不支持并发执行')
                sys.exit()
        logger.info(cmd_list)
        pytest.main(cmd_list)


main = TestMain


if __name__ == '__main__':
    main()

