from user_list import User_list

class Lists():
    def __init__(self):
        self.lists = []

    def add(self, user, listname):
        for userlist in self.lists:
            if userlist.list_name == listname:
                if not self.is_add(user.email, listname):
                    userlist.list_of_users.append(user)
                    return True
        return False

    def is_add(self, email, listname):
        for userlist in self.lists:
            if userlist.list_name == listname:
                for user in userlist.list_of_users:
                    if user.email == email:
                        return True
        return False