class User_list():
    def __init__(self, list_name):
        self.list_name = list_name
        self.list_of_users = []

    def merge(self, llist):
        new_list = []
        for user in self.list_of_users:
            new_list.append(user)
        for user in llist:
            new_list.append(user)
        return new_list