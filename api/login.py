# 导包
import requests

# 封装登陆接口测试类
class LoginApi:

    def __init__(self):
        # 定义登陆接口的URL
        self.login_url = "http://182.92.81.159/api/sys/login"

    # 登陆接口
    def login(self, mobile, password, headers):
        # 定义要发送的请求json数据
        jsonData = {"mobile":mobile, "password":password}
        # 发送登陆接口请求
        return requests.post(self.login_url, json=jsonData, headers=headers)
