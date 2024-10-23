# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (❌self, ❌cls)

class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user_and_password(self, user, password):
        # setter
        self.user = user
        self.password = password

    @classmethod
    def set_auto_user(cls, user, password):
        connection = cls()
        connection.set_user_and_password(user, password)
        return connection
        

c1 = Connection()
c1.set_user_and_password('Gui', 223311)
print(c1.user, c1.password)

c2 = Connection.set_auto_user('Giovana', 12345)
print(c2.user, c2.password)