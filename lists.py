from user_list import User_list
import json

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

    def search_by_mail(self, email):
        l = []
        for userlist in self.lists:
            if self.is_add(email, userlist.list_name):
                l.append(userlist.list_name)
        return l

    def export_into_json(self, listname, filename):
        dictionary = {}
        for userlist in self.lists:
            if userlist.list_name == listname:
                for user in userlist.list_of_users:
                    dictionary[user.name] = user.email
        return dictionary


    def remove_from_list(self, listname, user):
        for userlist in self.lists:
            if userlist.list_name == listname:
                if self.is_add(user.email, listname):
                    userlist.list_of_users.remove(user)
                    return True
        return False

    #def update_user(self,listname, user):










