import requests
from configer.conf_class import Conf
from common import constant


class Request:
    def __init__(self):
        self.session = requests.sessions.session()
        # envior01 = envior.upper()
        # if envior01 == "TEST":
        #     self.baseurl = Conf(constant.conffile_dir).getvalue("Http", "testurl")
        # elif envior01 == "PROD":
        #     self.baseurl = Conf(constant.conffile_dir).getvalue("Http", "produrl")

        value = Conf(constant.global_dir).getboolean("global", "switch")
        if value:
            self.baseurl = Conf(constant.testconf_dir).get("Api", "url")
        else:
            self.baseurl = Conf(constant.prodconf_dir).get("Api", "url")

    def request(self, method, url, data=None):
        method01 = method.upper()
        url01 = self.baseurl + url

        if method01 == "GET":
            return self.session.request(method01, url01, params=data)
        elif method01 == "POST":
            return self.session.request(method01, url01, data=data)
        elif method01 == "PUT":
            return self.session.request(method01, url01, params=data)
        elif method01 == "DELETE":
            return self.session.request(method01, url01, params=data)


if __name__ == "__main__":
    request = Request()
    # data = {"pageNum": 0}
    # data02 = {"username":"zhangteng@fuyoubank.com","password":"da_123","imageCode":"0"}
    # response = request.request('get', '/code/getEInfoList', data)
    # print(response.text)
    # request.request("get", "/code/image")
    # response = request.request("post", "/authentication/form", data02)
    # request.request("get", "/signOut")
    # print(response.text)
    data = {"companyMomentInfoIds": 119}
    response = request.request("delete", "/rdt/deleteCompanyMomentInfo", data)
    print(response.text)
