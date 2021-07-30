from unit.login import Login
from configer.conf_class import Conf


class loginaccount:
    def __init__(self, baseurl, session):
        self.baseurl = baseurl
        self.session = session
        self.login = Login(self.baseurl, self.session)
        self.login.get_image()

    def login_user(self, username, password):
        self.login.post_form(username, password, "0")
        self.login.get_judgingIdentity(username)

