class SystemWork:
    def __init__(self, baseurl, session):
        self.baseurl = baseurl
        self.session = session

    # 添加用户工单信息
    def post_addwoinfo(self, workContactTheme, workContactName, workContactEmail, workContactPhone, workContent):
        return self.session.post(url=self.baseurl+"/code/addUWOInfo",
                                 data={"workContactTheme": workContactTheme,
                                       "workContactName": workContactName,  # 30
                                       "workContactEmail": workContactEmail,
                                       "workContactPhone": workContactPhone,
                                       "workContent": workContent})  # 250

    # 管理员获取用户工单全部信息
    def get_userworkorders(self, pageNum):
        return self.session.get(url=self.baseurl+"/rdt/getUserWorkOrder",
                                params={"pageNum": pageNum})

    # 管理员获取用户工单 单条信息
    def get_userworkorder(self, userWorkOrderId):
        return self.session.get(url=self.baseurl+"/rdt/getUserWorkOrderInfo",
                                params={"userWorkOrderId": userWorkOrderId})
