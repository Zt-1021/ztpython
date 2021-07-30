import requests
from study.mogugu.configer.conf_class import Conf


class Login:
    def __init__(self):
        self.domain_name = Conf("D:\ztpython\study\mogugu\configer\conf.conf").getvalue("DomainName", "test")

    def get_getopenid(self, code):
        response = requests.get(url=self.domain_name + "/wxservice/getOpenId", params={"code": code})
        return response

    def get_mobilephone(self, code):
        data = self.get_getopenid(code).json()
        print(data)
        response = requests.post(url=self.domain_name + "/wxservice/mobilePhone", params=data)
        print(response.json())


if __name__ == '__main__':
    Login().get_getopenid("031fQaGa1rWxeA0ZUvFa1Rypvr3fQaGi")
