# 导包
import requests

# 创建员工模块的接口类
class EmployeeApi:

    def __init__(self):
        # 设置员工模块的url
        self.emp_url = "http://182.92.81.159/api/sys/user"

    # 添加员工
    def add_emp(self, username, mobile, headers):
        # 拼接json数据
        jsonData = {
            "username": username,
            "mobile": mobile,
            "workNumber": "9527",
            "timeOfEntry": "1970-01-01",
            "formOfEmployment": "1",
            "departmentId": "10086",
            "departmentName": "测试部",
            "correctionTime": "1970-03-01T09:00:00.000Z"
        }
        # 发送添加员工的接口请求
        return requests.post(self.emp_url, json=jsonData, headers=headers)

    # 查询员工
    def query_emp(self, emp_id, headers):
        # 拼接查询员工的url
        query_url = self.emp_url + "/" + emp_id
        # 发送查询员工接口请求
        return requests.get(query_url, headers=headers)

    # 修改员工
    def modify_emp(self, emp_id, headers, username):
        # 拼接修改员工的url
        modify_url = self.emp_url + "/" + emp_id
        # 拼接修改员工的json数据
        jsonData = {"username": username}
        # 发送修改员工接口请求
        return requests.put(modify_url, json=jsonData, headers=headers)

    # 删除员工
    def delete_emp(self, emp_id, headers):
        # 拼接删除员工的url
        delete_url = self.emp_url + "/" + emp_id
        # 发送删除员工的接口请求
        return requests.delete(delete_url, headers=headers)
