# 导包
import logging, os
from logging import handlers

# 获取当前项目的目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# 定义全局变量HEADERS
HEADERS = {"Content-Type": "application/json"}
# 定义全局变量员工ID
EMP_ID = ""


# 创建日志器初始化的函数
def init_logging():
    # 1 创建日志器
    logger = logging.getLogger()
    # 2 设置日志等级
    logger.setLevel(logging.INFO)
    # 3 创建处理器
    # 创建控制台处理器
    sh = logging.StreamHandler()
    # 创建文件处理器
    log_path = BASE_DIR + '/log/ihrm.log'
    fh = logging.handlers.TimedRotatingFileHandler(log_path, when='D', interval=1, backupCount=3, encoding='utf-8')
    # 4 创建格式化器
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    # 5 将格式化器添加导处理器
    sh.setFormatter(logging.Formatter(fmt))
    fh.setFormatter(logging.Formatter(fmt))
    # 6 将处理器添加到日志器当中
    logger.addHandler(sh)
    logger.addHandler(fh)
