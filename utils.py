import app
import json


# 封装通用断言函数
def assert_common(self, response, http_code, success, code, message):
    # 断言响应状态码
    self.assertEqual(http_code, response.status_code)
    # 断言success
    self.assertEqual(success, response.json().get('success'))
    # 断言code
    self.assertEqual(code, response.json().get("code"))
    # 断言message
    self.assertIn(message, response.json().get("message"))


# 读取登陆数据
def read_login_data():
    # 定义数据文件的路径
    login_data_path = app.BASE_DIR + "/data/login_data.json"
    # 打开登陆数据文件
    with open(login_data_path, mode='r', encoding='utf-8') as f:
        # 将文件加载成json格式
        jsonData = json.load(f)
        # 定义一个空列表，用于把获取到的数据转换成元组列表
        result_list = []
        for data in jsonData:
            # 读取数据
            mobile = data.get('mobile')
            password = data.get('password')
            http_code = data.get('http_code')
            success = data.get('success')
            code = data.get('code')
            message = data.get('message')
            result_list.append((mobile, password, http_code, success, code, message))

    print("登陆的数据为：", result_list)

    return result_list


# 读取添加员工数据
def read_add_emp():
    # 设置数据文件路径
    emp_data_path = app.BASE_DIR + "/data/employee_data.json"
    # 打开文件
    with open(emp_data_path, mode='r', encoding='utf-8') as f:
        # 加载文件成json格式
        jsonData = json.load(f)
        # 读取add_emp的数据
        add_emp_data = jsonData.get("add_emp")
        # 定义空列表，用于存放元组列表数据
        result_list = []
        # 读取数据
        username = add_emp_data.get('username')
        mobile = add_emp_data.get('mobile')
        http_code = add_emp_data.get('http_code')
        success = add_emp_data.get('success')
        code = add_emp_data.get('code')
        message = add_emp_data.get('message')
        # 将数据添加到resuilt_list当中，并组合成元组列表数据
        result_list.append((username, mobile, http_code, success, code, message))

    print("读取的添加员工的数据为：", result_list)
    return result_list


# 读取查询员工数据
def read_query_emp():
    # 设置数据文件路径
    emp_data_path = app.BASE_DIR + "/data/employee_data.json"
    # 打开文件
    with open(emp_data_path, mode='r', encoding='utf-8') as f:
        # 加载文件成json格式
        jsonData = json.load(f)
        # 加载查询员工的数据
        query_emp_data = jsonData.get('query_emp')
        # 定义空列表，用于存放元组列表数据
        result_list = []
        # 读取数据
        http_code = query_emp_data.get('http_code')
        success = query_emp_data.get('success')
        code = query_emp_data.get('code')
        message = query_emp_data.get('message')
        # 将数据添加到resuilt_list当中，并组合成元组列表数据
        result_list.append((http_code, success, code, message))

    print("读取的查询员工的数据为：", result_list)
    return result_list


# 读取修改员工数据
def read_modify_emp():
    # 设置数据文件路径
    emp_data_path = app.BASE_DIR + "/data/employee_data.json"
    # 打开文件
    with open(emp_data_path, mode='r', encoding='utf-8') as f:
        # 加载文件成json格式
        jsonData = json.load(f)
        # 加载修改员工的数据
        modify_emp_data = jsonData.get('modify_emp')
        # 定义空列表，用于存放元组列表数据
        result_list = []
        # 读取数据
        username = modify_emp_data.get('username')
        http_code = modify_emp_data.get('http_code')
        success = modify_emp_data.get('success')
        code = modify_emp_data.get('code')
        message = modify_emp_data.get('message')
        # 将数据添加到resuilt_list当中，并组合成元组列表数据
        result_list.append((username, http_code, success, code, message))

    print("读取的修改员工的数据为：", result_list)
    return result_list


# 读取删除员工数据
def read_delete_emp():
    # 设置数据文件路径
    emp_data_path = app.BASE_DIR + "/data/employee_data.json"
    # 打开文件
    with open(emp_data_path, mode='r', encoding='utf-8') as f:
        # 加载文件成json格式
        jsonData = json.load(f)
        # 加载查询员工的数据
        delete_emp_data = jsonData.get('delete_emp')
        # 定义空列表，用于存放元组列表数据
        result_list = []
        # 读取数据
        http_code = delete_emp_data.get('http_code')
        success = delete_emp_data.get('success')
        code = delete_emp_data.get('code')
        message = delete_emp_data.get('message')
        # 将数据添加到resuilt_list当中，并组合成元组列表数据
        result_list.append((http_code, success, code, message))

    print("读取的删除员工的数据为：", result_list)
    return result_list


if __name__ == '__main__':
    # read_login_data()
    # read_add_emp()
    # read_query_emp()
    # read_modify_emp()
    read_delete_emp()
