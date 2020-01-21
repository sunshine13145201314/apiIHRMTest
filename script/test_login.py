# 导包
import unittest, logging
from api.login import LoginApi
from utils import assert_common
import requests


# 创建测试类
class TestLogin(unittest.TestCase):

    # 创建初始化函数
    @classmethod
    def setUpClass(cls) -> None:
        # 初始化LoginApi
        cls.login_api = LoginApi()

    # 登陆成功
    def test01_login_success(self):
        # 调用登陆接口
        response = self.login_api.login("13800000002", "123456", {"Content-Type": "application/json"})
        # 使用日志打印响应的数据
        logging.info("登陆成功的结果为:{}".format(response.json()))
        # 断言登陆返回的数据
        # # 断言响应状态码
        # self.assertEqual(200, response.status_code)
        # # 断言success
        # self.assertEqual(True, response.json().get('success'))
        # # 断言code
        # self.assertEqual(10000, response.json().get("code"))
        # # 断言message
        # self.assertIn("操作成功", response.json().get("message"))

        # 使用封装的通用断言函数进行断言
        assert_common(self, response, 200, True, 10000, "操作成功")

    # 无参
    def test02_none_params(self):
        # 发送无参的登陆请求
        response = requests.post("http://182.92.81.159/api/sys/login")
        # 打印结果
        logging.info("无参的登陆结果为：{}".format(response.json()))
        # 断言响应数据
        # 使用封装的通用断言函数进行断言
        assert_common(self, response, 200, False, 99999, "抱歉，系统繁忙，请稍后重试")

    # 手机号码为空
    def test03_mobile_is_empty(self):
        # 发送手机号码为空的接口请求
        response = self.login_api.login("", "error", {"Content-Type": "application/json"})
        # 打印结果
        logging.info("手机号码为空的结果为：{}".format(response.json()))
        # 断言响应数据
        assert_common(self, response, 200, False, 20001, "用户名或密码错误")

    # 密码为空
    def test04_password_is_empty(self):
        # 发送密码为空的接口请求
        response = self.login_api.login("13800000002", "", {"Content-Type": "application/json"})
        # 打印结果
        logging.info("密码为空的结果为：{}".format(response.json()))
        # 断言响应数据
        assert_common(self, response, 200, False, 20001, "用户名或密码错误")

    # 未注册手机号码登陆
    def test05_mobile_is_not_exists(self):
        # 发送未注册手机号码登陆的接口请求
        response = self.login_api.login("13900000002", "123456", {"Content-Type": "application/json"})
        # 打印结果
        logging.info("未注册手机号码登陆的结果为：{}".format(response.json()))
        # 断言响应数据
        assert_common(self, response, 200, False, 20001, "用户名或密码错误")

    # 密码错误
    def test06_password_is_error(self):
        # 发送密码错误登陆的接口请求
        response = self.login_api.login("13800000002", "error", {"Content-Type": "application/json"})
        # 打印结果
        logging.info("密码错误登陆的结果为：{}".format(response.json()))
        # 断言响应数据
        assert_common(self, response, 200, False, 20001, "用户名或密码错误")
