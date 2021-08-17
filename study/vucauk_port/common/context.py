import re
from configer.conf_class import Conf
from common import constant


class Context:  # 上下文 数据的准备与记录
    admin_user = Conf(constant).get()

