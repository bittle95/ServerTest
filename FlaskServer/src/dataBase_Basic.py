
class DataBase:
    def __init__(self):
        self.userID = ""
        self.userPW = ""

    def ToString(self):
        return self.userID + "@" + self.userPW