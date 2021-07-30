class CompanyExit:
    def __init__(self, baseurl, session):
        self.baseurl = baseurl
        self.session = session

    # 管理员根据条件筛选公司信息
    def get_searchEnterprise(self, pageNum, conditions):  # 页码， 条件（公司名字/公司报价名字）
        params = {"pageNum": pageNum, "conditions": conditions}
        return self.session.get(url=self.baseurl+"/rdt/getConditionsEnterpriseInfo",
                                params=params)

    # 添加公司---保存公司基本信息basicinfo---添加和修改共用一个
    def post_saveenterpriseinfo(self, en, ect, et, dbcn, dce, eg, dcr, ee, do, erc, ds, ets, dfr, epv, st, ei, era):
        return self.session.post(url=self.baseurl+"/rdt/saveEnterpriseInfo",
                                 data={"enterpriseName": en,   # 企业名称
                                       "enterpriseCapitalType": ect,   # 资本类型：0:Capital holdings;1:VIE
                                       "enterpriseType": et,  # 企业类型
                                       "detailBusinessCertificateNumber": dbcn,  # 注册证书号码
                                       "detailCommercialEnterprise": dce,  # 商业部门
                                       "enterpriseGicscode": eg,  # GICS行业代码
                                       "detailCorporateRepresentative": dcr,  # 法人代表
                                       "enterpriseEstablishdate": ee,  # 成立日期
                                       "detailOfficeaddress": do,  # 办公地址
                                       "enterpriseRegisteredcapital": erc,  # 注册资本
                                       "detailStuffamount": ds,  # 员工数量
                                       "enterpriseTotalShares": ets,  # 总股份
                                       "detailFinancingRound": dfr,  # 融资轮次
                                       "enterpriseParValue": epv,  # 票面价格
                                       "systemType": st,  # 系统类型(0:展示型，1：交易型)
                                       "enterpriseId": ei,  # 公司id(新增时传0)
                                       "enterpriseRegisteredaddress": era})  # 注册地址

    # 添加公司---保存公司详细信息
    def post_addEnterpriseDetailInfo(self, eqn, enin, dpn, de, ei, dtm):
        return self.session.post(url=self.baseurl + "/rdt/addEnterpriseDetailInfo",
                                 data={"enterpriseQuotename": eqn,  # 报价名称
                                       "enterpriseIntroduce": enin,  # 公司简介
                                       "detailPhonenumber": dpn,  # 联系电话
                                       "detailEmail": de,  # 联系邮箱
                                       # "detailOfficialwebsite": dow,  # 官方网站--选填
                                       # "detailBusinesswebsite": dbw,  # 商务网站--选填
                                       "enterpriseId": ei,  # 公司id
                                       "detailTrademark": dtm})  # 商标URL

    #  修改公司详细信息
    def put_updateenterprisedetailinfo(self, eqn, enin, dpn, de, ei, dtm):
        return self.session.put(url=self.baseurl + "/rdt/updateEnterpriseDetailInfo",
                                data={"enterpriseQuotename": eqn,  # 报价名称
                                      "enterpriseIntroduce": enin,  # 公司简介
                                      "detailPhonenumber": dpn,  # 联系电话
                                      "detailEmail": de,  # 联系邮箱
                                      # "detailOfficialwebsite": dow,  # 官方网站--选填
                                      # "detailBusinesswebsite": dbw,  # 商务网站--选填
                                      "enterpriseId": ei,  # 公司id
                                      "detailTrademark": dtm})  # 商标URL

    # 获取公司基本信息
    def get_edetailinfo(self, enterpriseid):
        return self.session.get(url=self.baseurl+"/code/getEDetailInfo",
                                params={"enterpriseId": enterpriseid})

    # 获取估值记录列表信息
    def get_valuationrecordinfolist(self, pageNum, pageSize, enterpriseId):
        return self.session.get(url=self.baseurl+"/code/getValuationRecordInfoList",
                                params={"pageNum": pageNum,
                                        "pageSize": pageSize,
                                        "enterpriseId": enterpriseId})

    # 保存估值记录信息
    def post_savevaluationrecordinfo(self, enterpriseId, valuationTime, valuationResult, valuationResultsDate, valuationRecordId, valuationEvaluator):
        return self.session.post(url=self.baseurl+"/rdt/saveValuationRecordInfo",
                                 data={"enterpriseId": enterpriseId,   # 99999最大，但是不会判断公司id存不存在
                                       "valuationTime": valuationTime,  # 估值时间  未做限制
                                       "valuationResult": valuationResult,
                                       "valuationResultsDate": valuationResultsDate,  # 财报日期
                                       "valuationRecordId": valuationRecordId,  # 估值信息id,0-添加,其他-修改
                                       "valuationEvaluator": valuationEvaluator})  # 评估者 modgo

    # 删除估值记录信息
    def put_deletevaluationrecordinfo(self, valuationRecordId):
        return self.session.put(url=self.baseurl+"/rdt/deleteValuationRecordInfo",
                                params={"valuationRecordId": valuationRecordId})

    # 获取估值记录详情信息
    def get_getValuationRecordInfo(self, valuationRecordId):
        return self.session.get(url=self.baseurl + "/code/getValuationRecordInfo",
                                params={"valuationRecordId": valuationRecordId})

    # 保存知识产权信息接口
    def post_saveIntellectualPropertyRightsInfo(self, iPN, iPT, iPST, iPET, eI, iPId):
        return self.session.post(url=self.baseurl + "/rdt/saveIntellectualPropertyRightsInfo",
                                 data={"intellectualPropertyName": iPN,  # 专利名称
                                       "intellectualPropertyType": iPT,  # 专利类型（0-5）
                                       "intellectualPropertyStartTime": iPST,  # 专利开始时间
                                       "intellectualPropertyEndTime": iPET,  # 专利结束时间
                                       "enterpriseId": eI,  # 公司id
                                       "intellectualPropertyId": iPId})  # 专利id

    # 删除知识产权信息
    def put_deleteIntellectualPropertyRightsInfo(self, intellectualPropertyId):
        return self.session.put(url=self.baseurl + "/rdt/deleteIntellectualPropertyRightsInfo",
                                params={"intellectualPropertyId": intellectualPropertyId})

    # 获取知识产权信息列表
    def get_IntellectualPropertyRightsInfos(self, pageNum, pageSize, enterpriseId):
        return self.session.get(url=self.baseurl + "/code/getIntellectualPropertyRightsInfos",
                                params={"pageNum": pageNum,
                                        "pageSize": pageSize,
                                        "enterpriseId": enterpriseId})

    # 获取知识产权详细信息
    def get_IntellectualPropertyRightsInfo(self, intellectualPropertyId):
        return self.session.get(url=self.baseurl + "/code/getIntellectualPropertyRightsInfo",
                                params={"intellectualPropertyId": intellectualPropertyId})

    # 获取公司未分配股份
    def get_EnterpriseAllotmentShares(self, enterpriseid):
        return self.session.get(url=self.baseurl+"/code/getEnterpriseAllotmentShares",
                                params={"enterpriseId": enterpriseid})

    # 分配股本获取用户列表信息
    def get_DistributingUserInfo(self, pageNum, enterpriseId, sharesNumber):
        return self.session.get(url=self.baseurl+"/rdt/getDistributingUserInfo",
                                params={"pageNum": pageNum, "enterpriseId": enterpriseId, "sharesNumber": sharesNumber})

    # 公司给用户分配/定增公司股份信息
    def post_saveTargetedCapitalIncrease(self, enterpriseId, tciUserIdList, tciUserStockList):
        return self.session.post(url=self.baseurl+"/rdt/saveTargetedCapitalIncrease",
                                 data={"enterpriseId": enterpriseId,
                                       "tciUserIdList": tciUserIdList,
                                       "tciUserStockList": tciUserStockList})

    # 管理员对公司增发记录
    def post_saveAdminRigthsRecord(self, enterpriseId, tciPrice, tciShares):
        return self.session.post(url=self.baseurl+"/rdt/saveAdminRigthsRecord",
                                 data={"enterpriseId": enterpriseId,
                                       "tciPrice": tciPrice,
                                       "tciShares": tciShares})

