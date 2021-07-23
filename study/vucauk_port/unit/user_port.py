class UserPort:
    def __init__(self, baseurl, session):
        self.baseurl = baseurl
        self.session = session

    # 获取用户未支付订单
    def get_UserUnpaidOrder(self):
        return self.session.get(url=self.baseurl+"/rdt/getUserUnpaidOrder")

    # 用户交易结余
    def get_accountbalance(self):
        return self.session.get(url=self.baseurl+"/rdt/getAccountBalance")

    # 待支付的订单详情
    def get_orderdetail(self, transactionNumber):
        return self.session.get(url=self.baseurl+"/rdt/getOrderDetailsDto",
                                params={"transactionNumber": transactionNumber})

    # 保存支付订单
    def post_saveacconuntbalabceinfo(self, transactionNumber, decimal):
        return self.session.post(url=self.baseurl+"/rdt/saveAccountBalanceInfo",
                                 data={"transactionNumber": transactionNumber,
                                       "decimal": decimal})

    # 获取用户的公司信息
    def get_userenterprisedata(self):
        return self.session.get(url=self.baseurl+"/rdt/getUserEnterpriseData")

    # 获取公司列表
    def get_getEnterpriseData(self, pageNum):
        return self.session.get(url=self.baseurl+"/rdt/getEnterpriseData",
                                params={"pageNum": pageNum})

    # 添加公司
    def post_saveUserEnterpriseReleation(self, enterpriseId):
        return self.session.post(url=self.baseurl+"/rdt/saveUserEnterpriseReleation",
                                 data={"enterpriseId": enterpriseId})

    # 获取公司的股权证书
    def get_sharecertificateinfo(self, enterpriseId):
        return self.session.get(url=self.baseurl+"/rdt/getShareCertificateInfos",
                                params={"enterpriseId": enterpriseId})

    # 下载股权证书
    def get_downloadShareCertificate(self, shareId):
        return self.session.get(url=self.baseurl+"/rdt/downloadShareCertificate",
                                params={"shareId": shareId})

    # 发起交易订单
    def post_saveUserTransactionOrder(self, enterpriseId, userorderIdentity, userorderSharesNumber, intuserorderSharesPaid,
                                      userId, certificateId):
        return self.session.post(url=self.baseurl+"/rdt/saveUserTransactionOrder",
                                 data={"enterpriseId": enterpriseId,
                                       "userorderIdentity": userorderIdentity,
                                       "userorderSharesNumber": userorderSharesNumber,
                                       "intuserorderSharesPaid": intuserorderSharesPaid,
                                       "userId": userId,
                                       "certificateId": certificateId})

    # 获取订单详情
    def get_getUserOrderInfoDTO(self, userOrderId):
        return self.session.get(url=self.baseurl+"/rdt/getUserOrderInfoDTO",
                                params={"userOrderId": userOrderId})

    # 修改订单详情
    def put_updateUserOrderState(self, state, userOrderId):
        return self.session.put(url=self.baseurl+"/rdt/updateUserOrderState",
                                params={"state": state, "userOrderId": userOrderId})

    # 获取用户详情
    def get_UserInfo(self, userId):
        return self.session.get(url=self.baseurl+"/code/getUserInfo",
                                params={"userId": userId})
