from hashlib import sha256
class Credential:
    def __init__(self):
        self.__hash = None

    @property
    def password(self):
        return self.__hash

    @password.setter
    def password(self, key):
        if len(key) > 0:
            self.__hash = sha256(key.encode("utf-8")).hexdigest()
        else:
            raise ValueError("Invalid Password")


    def validate(self, key):
        pass

