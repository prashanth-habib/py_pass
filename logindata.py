import hashlib
class UserInfo:

    _username = "admin"
    _password = "2c660ff4862df593db99df10377c1672846ab1978063d1099af478dd16790878"

    @property
    def user_name(self):
        return self._username

    @user_name.setter
    def user_name(self, new_user):
        self._username = new_user

    @property
    def user_password(self):
        return self._password

    @user_password.setter
    def user_password(self, new_password):
        print(f"Password was changed to {new_password} from {self._password}")
        self._password = hashlib.sha256(new_password.encode('utf-8')).hexdigest()

    def auth_creds(self, name, passwd):
        if name == self._username and self._password == hashlib.sha256(passwd.encode('utf-8')).hexdigest():
            return f"Welcome {self._username}!"
        else:
            return "Login failed!"
