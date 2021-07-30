class Order:
    def __init__(self, baseurl, session):
        self.baseurl = baseurl
        self.session = session

    # 交易列表信息—管理员
    def get_orderinfo(self, pageNum):
        return self.session.get(url=self.baseurl+"/rdt/getOrderInfoDTO",
                                params={"pageNum": pageNum})

    # 管理员获取交易详细信息
    def get_paymentinfo(self, transactionId, orderId, orderStatus):
        return self.session.get(url=self.baseurl+"/rdt/getPaymentInfo",
                                params={"transactionId": transactionId, "orderId": orderId, "orderStatus": orderStatus})

    # 获取用户订单信息(买/卖方)
    def get_userorderinfo(self, matchOrderId, orderIdentity, pageNum):
        return self.session.get(url=self.baseurl+"/rdt/getUserOrderInfo",
                                params={"matchOrderId": matchOrderId,
                                        "orderIdentity": orderIdentity,
                                        "pageNum": pageNum})

    # 修改订单的交易状态----已交易
    def put_updatetransactionstatus(self, tranId, status, mangoPayPoundage, vat, vucaPoundage, stampDuty):
        return self.session.put(url=self.baseurl+"/rdt/updateTransactionStatus",
                                params={"tranId": tranId,
                                        "status": status,
                                        "mangoPayPoundage": mangoPayPoundage,
                                        "vat": vat,
                                        "vucaPoundage": vucaPoundage,
                                        "stampDuty": stampDuty})

    # 修改用户订单的状态---关闭订单
    def put_updateuserorderstate(self, state, userOrderId):
        return self.session.put(url=self.baseurl+"/rdt/updateUserOrderState",
                                params={"state": state, "userOrderId": userOrderId})

    # 管理员获取用户交易结余信息列表
    def get_accountbalanceinfolist(self, pageSize, pageNum):
        return self.session.get(url=self.baseurl+"/rdt/getAccountBalanceInfoList",
                                params={"pageSize": pageSize, "pageNum": pageNum})

    # 修改结余订单的状态
    def put_updateAccountBanlanceState(self, accountBalanceId, balanceType):
        return self.session.put(url=self.baseurl+"/rdt/updateAccountBalanceState",
                                params={"accountBalanceId": accountBalanceId,
                                        "balanceType": balanceType})

    # 管理员添加交易信息
    def post_addTransactionInfo(self, orderBuyerId, orderTransferId, orderSharesNumber, orderSharesPaid, enterpriseId,
                                transactionElectronicReceipt, transactionVoucher, stampDuty, vat, vucaPoundage,
                                mangoPayPoundage, amount):
        return self.session.post(url=self.baseurl+"/rdt/addTransactionInfo",
                                 data={"orderBuyerId": orderBuyerId,
                                       "orderTransferId": orderTransferId,
                                       "orderSharesNumber": orderSharesNumber,
                                       "orderSharesPaid": orderSharesPaid,
                                       "enterpriseId": enterpriseId,
                                       "transactionElectronicReceipt": transactionElectronicReceipt,
                                       "transactionVoucher": transactionVoucher,
                                       "stampDuty": stampDuty,
                                       "vat": vat,
                                       "vucaPoundage": vucaPoundage,
                                       "mangoPayPoundage": mangoPayPoundage,
                                       "amount": amount})
