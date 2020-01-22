# 1 导包
import unittest, time, app
from script.test_login_params import TestLoginParams
from script.test_employee import TestEmployee
from tools.HTMLTestRunner import HTMLTestRunner

# 2 创建测试套件
suite = unittest.TestSuite()
# 3 将测试用例添加到测试套件
suite.addTest(unittest.makeSuite(TestLoginParams))
suite.addTest(unittest.makeSuite(TestEmployee))
# 4 定义测试报告的名称
# report_name = app.BASE_DIR + "/report/ihrm-{}.html".format(time.strftime('%Y%m%d %H%M%S'))
report_name = app.BASE_DIR + "/report/ihrm.html"
# 5 打开测试报告，初始化runner，执行测试用例，生成测试报告
with open(report_name, mode='wb') as f:
    # 初始化runner
    runner = HTMLTestRunner(f, verbosity=1, title="IHRM人力资源管理系统接口测试", description="V1.0.1")
    # 使用runner运行测试套件
    runner.run(suite)

print("Hello World")
