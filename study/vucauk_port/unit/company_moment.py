class CompanyMoment:
    def __init__(self, baseurl, session):
        self.baseurl = baseurl
        self.session = session

    # 添加公司动态
    def post_addcompanymoment(self, enterpriseid, eventscontent, eventstitle):
        return self.session.post(url=self.baseurl+"/rdt/addCompanyMomentInfo", data={"enterpriseId": enterpriseid,
                                                                                 "eventsContent": eventscontent,
                                                                                 "eventsTitle": eventstitle})

    # 修改公司动态
    def post_updatecompanymomentinfo(self, companyMomentInfoId, eventscontent, eventstitle):
        return self.session.post(url=self.baseurl + "/rdt/updateCompanyMomentInfo",
                                 data={"companyMomentInfoId": companyMomentInfoId,
                                       "eventsContent": eventscontent,
                                       "eventsTitle": eventstitle})

    # 获取公司动态全部
    def get_getemomentinfoall(self, enterpriseid, pagenum):
        return self.session.get(url=self.baseurl + "/code/getEMomentInfoAll", parmas={"enterpriseId": enterpriseid,
                                                                                  "pageNum": pagenum})

    # 获取公司单条动态详细信息
    def get_getCompanyMomentInfo(self, companymomentid):
        return self.session.get(url=self.baseurl+"/code/getCompanyMomentInfo",
                            parmas={"companyMomentId": companymomentid})

    # 删除公司动态信息
    def delete(self, companymomentinfoids):
        return self.session.delete(url=self.baseurl + "/rdt/deleteCompanyMomentInfo",
                                   params={"companyMomentInfoIds": companymomentinfoids})

