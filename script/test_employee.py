# 导包
import unittest, logging
from api.login import LoginApi
from api.employee import EmployeeApi
import app
from utils import assert_common,read_add_emp,read_query_emp,read_modify_emp,read_delete_emp
import pymysql
from parameterized.parameterized import parameterized

# 创建测试类
class TestEmployee(unittest.TestCase):

    # 初始化配置函数
    @classmethod
    def setUpClass(cls) -> None:
        # 初始化登陆
        cls.login_api = LoginApi()
        # 初始化员工
        cls.employee_api = EmployeeApi()

    # 添加员工
    @parameterized.expand(read_add_emp)
    def test01_add_emp(self, username, mobile, http_code, success, code, message):
        # 调用登陆接口
        response = self.login_api.login("13800000002", "123456", app.HEADERS)
        # 打印登陆的结果
        logging.info("员工模块的登陆结果为：{}".format(response.json()))
        # 把登陆信息中的令牌拼接成以Bearer xxx-xxx的字符串然后，保存到全局变量HEADERS
        app.HEADERS['Authorization'] = "Bearer " + response.json().get('data')
        # 打印保存的令牌HEADERS
        logging.info("保存的令牌HEADERS为：{}".format(app.HEADERS))

        # 调用添加员工接口
        response = self.employee_api.add_emp(username, mobile, app.HEADERS)
        # 打印添加员工接口的结果
        logging.info("添加员工接口的结果为：{}".format(response.json()))
        # 断言添加员工接口
        assert_common(self, response, http_code, success, code, message)

        # 保存员工id到全局变量（app.EMP_ID)
        app.EMP_ID = response.json().get('data').get('id')
        # 输出员工ID
        logging.info("保存的员工ID为：{}".format(app.EMP_ID))

    # 查询员工
    @parameterized.expand(read_query_emp)
    def test02_query_emp(self, http_code, success, code, message):
        # 调用封装的查询员工接口
        response = self.employee_api.query_emp(app.EMP_ID, app.HEADERS)
        # 打印结果
        logging.info("查询员工接口的结果为：{}".format(response.json()))
        # 断言
        assert_common(self, response, http_code, success, code, message)

    # 修改员工
    @parameterized.expand(read_modify_emp)
    def test03_modify_emp(self, username, http_code, success, code, message):
        # 调用封装的修改员工接口
        response = self.employee_api.modify_emp(app.EMP_ID, app.HEADERS, username)
        # 打印结果
        logging.info("修改员工的结果为：{}".format(response.json()))

        # 查询数据库信息
        # 获取连接
        conn = pymysql.connect('182.92.81.159', 'readuser', 'iHRM_user_2019', 'ihrm')
        # 获取游标
        cursor = conn.cursor()
        # 执行SQL语句
        cursor.execute("select username from bs_user where id={};".format(app.EMP_ID))
        # 打印执行结果
        result = cursor.fetchone()
        logging.info("数据库查询结果为：{}".format(result))
        # 断言比较修改的用户名和查询出来的用户名
        self.assertEqual(username, result[0])
        # 关闭游标
        cursor.close()
        # 关闭连接
        conn.close()

        # 断言
        assert_common(self, response, http_code, success, code, message)

    # 删除员工
    @parameterized.expand(read_delete_emp)
    def test04_delete_emp(self, http_code, success, code, message):
        # 调用封装的删除员工接口
        response = self.employee_api.delete_emp(app.EMP_ID, app.HEADERS)
        # 打印结果
        logging.info("删除员工接口的结果为：{}".format(response.json()))
        # 断言
        assert_common(self, response, http_code, success, code, message)
