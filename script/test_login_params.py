# 导包
import unittest, logging
from api.login import LoginApi
from utils import assert_common,read_login_data
import requests
from parameterized.parameterized import parameterized

# 创建测试类
class TestLoginParams(unittest.TestCase):

    # 创建初始化函数
    @classmethod
    def setUpClass(cls) -> None:
        # 初始化LoginApi
        cls.login_api = LoginApi()

    # 登陆
    @parameterized.expand(read_login_data)
    def test01_login(self, mobile, password, http_code, success, code, message):
        # 调用登陆接口
        response = self.login_api.login(mobile, password, {"Content-Type": "application/json"})
        # 使用日志打印响应的数据
        logging.info("登陆的结果为:{}".format(response.json()))

        # 使用封装的通用断言函数进行断言
        assert_common(self, response, http_code, success, code, message)
