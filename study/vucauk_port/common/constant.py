import os


# 测试用例文件读取路径
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_dir = os.path.join(base_dir, "data")
case_dir_admin = os.path.join(data_dir, "testdata_admin.xlsx")
case_dir_user = os.path.join(data_dir, "testdata_user.xlsx")

# 配置文件读取路径
conf_dir = os.path.join(base_dir, "configer")
global_dir = os.path.join(conf_dir, "global.conf")
testconf_dir = os.path.join(conf_dir, "test.conf")
prodconf_dir = os.path.join(conf_dir, "prod.conf")
