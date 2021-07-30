class UserExit:
    def __init__(self, baseurl, session):
        self.baseurl = baseurl
        self.session = session


    # 获取随机生成的账号
    def get_getNumberInfo(self):
        return self.session.get(url=self.baseurl+"/rdt/getNumberInfo")

    # 管理员管理员添加用户信息
    def post_saveUserInfo(self, uid, userName, userGender, userCellphone, user163Email, userBirthday, userType, city,
                          area, userNationality, userBankAccount, userDomicile, countryOfResidence, userPostalcode,
                          userAccountNumber, userPassport, userResidenceProof, password, userTaxResidency, swiftCode):
        return self.session.post(url=self.baseurl+"/rdt/saveUserInfo",
                                 data={"uid": uid,
                                       "userName": userName,
                                       "userGender": userGender,
                                       "userCellphone": userCellphone,
                                       "user163Email": user163Email,
                                       "userBirthday": userBirthday,
                                       "userType": userType,
                                       "userNationality": userNationality,
                                       "userBankAccount": userBankAccount,
                                       "userDomicile": userDomicile,
                                       "userPassport": userPassport,
                                       "countryOfResidence": countryOfResidence,
                                       "city": city,
                                       "area": area,
                                       "userAccountNumber": userAccountNumber,
                                       "userPostalcode": userPostalcode,
                                       "password": password,
                                       "userTaxResidency": userTaxResidency,
                                       "swiftCode": swiftCode,
                                       "userResidenceProof": userResidenceProof})

# 管理员修改用户信息
    def post_updateUserInfo(self, uid, userName, userGender, userCellphone, user163Email, userBirthday, userType, city,
                          area, userNationality, userBankAccount, userDomicile, countryOfResidence, userPostalcode,
                          userAccountNumber, userPassport, userResidenceProof, userTaxResidency, swiftCode):
        return self.session.post(url=self.baseurl+"/rdt/updateUserInfo",
                                 data={"uid": uid,
                                       "userName": userName,
                                       "userGender": userGender,
                                       "userCellphone": userCellphone,
                                       "user163Email": user163Email,
                                       "userBirthday": userBirthday,
                                       "userType": userType,
                                       "userNationality": userNationality,
                                       "userBankAccount": userBankAccount,
                                       "userDomicile": userDomicile,
                                       "userPassport": userPassport,
                                       "countryOfResidence": countryOfResidence,
                                       "city": city,
                                       "area": area,
                                       "userAccountNumber": userAccountNumber,
                                       "userPostalcode": userPostalcode,
                                       "userTaxResidency": userTaxResidency,
                                       "swiftCode": swiftCode,
                                       "userResidenceProof": userResidenceProof})

    # 管理员获取系统用户信息列表
    def get_userinfolist(self, pageNum):
        return self.session.get(url=self.baseurl+"/rdt/getUserInfoList",
                                params={"pageNum": pageNum})

    # 获取单条用户信息
    def get_userinfo(self, userId):
        return self.session.get(url=self.baseurl+"/code/getUserInfo",
                                params={"userId": userId})

    # 管理员获取指定用户拥有的所有公司股数
    def get_usertransationinfo(self, userId):
        return self.session.get(url=self.baseurl+"/rdt/getUserTransactionInfo",
                                params={"userId": userId})

    # 管理员根据用户名字获取列表信息--搜索
    def get_usernameinfolist(self, userName, pageNum):
        return self.session.get(url=self.baseurl+"/rdt/getUserNameInfoList",
                                params={"userName": userName, "pageNum": pageNum})

    # 管理员修改用户状态
    def put_updateuserstatus(self, username, status):
        return self.session.put(url=self.baseurl+"/rdt/updateUserStatus",
                                params={"username": username, "status": status})  # 0-正常登录，1-禁止登录，2-禁止交易，3-未激活
