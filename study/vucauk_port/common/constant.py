import os


base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_dir = os.path.join(base_dir, "data")
case_dir_admin = os.path.join(data_dir, "testdata_admin.xlsx")
case_dir_user = os.path.join(data_dir, "testdata_user.xlsx")
conf_dir = os.path.join(base_dir, "configer")
conffile_dir = os.path.join(conf_dir, "conf.conf")
# print(conffile_dir)
