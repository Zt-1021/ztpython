class Register:
    def __init__(self, baseurl, session):
        self.baseurl = baseurl
        self.session = session

    # 管理员分页获取用户申请信息列表
    def get_userapplicationinfos(self, pageNum, pageSize):
        return self.session.get(url=self.baseurl+"/rdt/getUserApplicationInfos",
                                params={"pageNum": pageNum, "pageSize": pageSize})

    # 获取用户申请信息详情
    def get_userapplicationinfo(self, userId):
        return self.session.get(url=self.baseurl+"/rdt/getUserApplicationInfo",
                                params={"userId": userId})

    # 保存用户申请账号信息(第一步)
    def post_saveUserApplicationInfo(self, userapplyName, userapplyEmail, password, userapplyCellphone, userGender):
        return self.session.post(url=self.baseurl+"/code/saveUserApplicationInfo",
                                 data={"userapplyName": userapplyName,
                                       "userapplyEmail": userapplyEmail,
                                       "password": password,
                                       "userapplyCellphone": userapplyCellphone,
                                       "userGender": userGender})

    # 保存用户注册发送邮件(第一步)
    def post_sendRegisterMail(self, userId, url):
        return self.session.post(url=self.baseurl+"/code/sendRegisterMail",
                                 data={"userId": userId,
                                       "url": url})

    # 保存用户选择投资者分类信息(第二步)
    def post_saveInvestorTypeInfo(self, userId, investorType):
        return self.session.post(url=self.baseurl+"/rdt/saveInvestorTypeInfo",
                                 data={"userId": userId,
                                       "investorType": investorType})

    # 保存客户尽职调查信息(第三步)
    def post_saveCustomerDueDiligenceInfo(self, userId, userapplyBrithdate, userapplyAddress, userapplyTaxResidency,
                                          userapplyPassport, userapplyJoinCause, userapplyExpectedTradingFrequency,
                                          userapplyCapitalSource, userNationality, userPostalcode, userResidenceProof,
                                          countryOfResidence):
        return self.session.post(url=self.baseurl+"/rdt/saveCustomerDueDiligenceInfo",
                                 data={"userId": userId,
                                       "userapplyBrithdate": userapplyBrithdate,
                                       "userapplyAddress": userapplyAddress,
                                       "userapplyTaxResidency": userapplyTaxResidency,
                                       "userapplyPassport": userapplyPassport,
                                       "userapplyJoinCause": userapplyJoinCause,
                                       "userapplyExpectedTradingFrequency": userapplyExpectedTradingFrequency,
                                       "userapplyCapitalSource": userapplyCapitalSource,
                                       "userNationality": userNationality,
                                       "userPostalcode": userPostalcode,
                                       "userResidenceProof": userResidenceProof,
                                       "countryOfResidence": countryOfResidence,})

    # 保存用户风险警告信息(第四步)
    def post_saveRiskWarningInfo(self, userId):
        return self.session.post(url=self.baseurl+"/rdt/saveRiskWarningInfo",
                                 data={"userId": userId})

    # 保存用户申请投资知识测验信息(第五步)
    def post_saveInvestmentTestInfo(self, userId, tsetQids, tsetAnswers):
        return self.session.post(url=self.baseurl+"/rdt/saveInvestmentTestInfo",
                                 data={"userId": userId,
                                       "tsetQids": tsetQids,
                                       "tsetAnswers": tsetAnswers})

    # 获取用户申请投资知识测验记录数量(第五步)
    def get_QuantitativeTestCount(self, userId):
        return self.session.get(url=self.baseurl+"/rdt/getQuantitativeTestCount",
                                data={"userId": userId})

    # 保存用户申请定量测试信息(第六步)
    def post_saveQuantitativeTestInfo(self, userId, quantitativeTest):
        return self.session.post(url=self.baseurl+"/rdt/saveQuantitativeTestInfo",
                                 data={"userId": userId,
                                       "quantitativeTest": quantitativeTest})

    # 保存用户同意专业投资者通知信息(第七步)
    def post_saveInvestorNotification(self, userId):
        return self.session.post(url=self.baseurl+"/rdt/saveInvestorNotification",
                                 data={"userId": userId})

    # 管理员同意用户申请并添加银行卡号
    def post_saveUserAccountInfo(self, userId, userBankAccount):
        return self.session.post(url=self.baseurl+"/rdt/saveUserAccountInfo",
                                 data={"userId": userId,
                                       "userBankAccount": userBankAccount})

    # 修改申请用户登录入口
    def put_updateLoginEntrance(self, userapplyEmail, loginEntrance):
        return self.session.put(url=self.baseurl+"/code/updateLoginEntrance",
                                params={"userapplyEmail": userapplyEmail,
                                        "loginEntrance": loginEntrance})

