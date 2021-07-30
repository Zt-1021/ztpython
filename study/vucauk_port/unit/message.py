class Message:
    def __init__(self, baseurl, session):
        self.baseurl = baseurl
        self.session = session

    # 消息提示
    def get_getNotice(self, flag):
        return self.session.get(url=self.baseurl+"/rdt/getNotice",
                                params={"flag": flag})

    # 消息状态变更
    def put_changeMessageState(self, sid, time):
        return self.session.put(url=self.baseurl+"/rdt/changeMessageState",
                                params={"sid": sid,
                                        "time": time})
