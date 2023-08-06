# 公共配置
class Qrunner:
    driver = None  # 驱动
    platform = None  # 平台
    serial_no = None  # 设备id
    pkg_name = None  # 应用包名
    alert_list = []  # 需要处理的弹窗属性，安卓支持xx，ios支持xx


# pc端相关配置
class BrowserConfig:
    name = None  # 浏览器类型，暂时只支持chrome
    headless = False  # 无头模式
    command_executor = ""  # 浏览器驱动路径
    options = None  # 浏览器驱动选项


