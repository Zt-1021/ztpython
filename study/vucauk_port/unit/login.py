import requests


class Login:
    def __init__(self, baseurl, session):
        self.baseurl = baseurl
        self.session = session

    def get_image(self):
        return self.session.get(url=self.baseurl+"/code/image")

    def get_entrance(self, userapplyemail):
        return self.session.get(url=self.baseurl + "/code/getloginEntrance", params={"userapplyEmail": userapplyemail})

    def get_userstatus(self, username):
        return self.session.get(url=self.baseurl + "/code/getUserStatus", params={"username": username})

    def post_form(self, username, password, imagecode):
        return self.session.post(url=self.baseurl+"/authentication/form",
                                 data={"username": username, "password": password, "imageCode": imagecode})

    def get_judgingIdentity(self, email):
        return self.session.get(url=self.baseurl+"/code/judgingIdentity", params={"email": email})

    def get_signout(self):
        return self.session.get(url=self.baseurl + "/signOut")



