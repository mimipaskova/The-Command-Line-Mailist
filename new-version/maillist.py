class MailList():
    def __init__(self, name):
        self.__name = name
        self.__subscribers = {}

    def add_subscriber(self, name, email):
        self.__subscribers[name] = email

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def get_subscribers(self):
        return self.__subscribers

    def count_of_subscribers(self):
        return len(self.__subscribers)

    def list_of_subscribers(self):
        subscribers_list = []
        for key in self.__subscribers:
            subscribers_list.append((key, self.__subscribers[key]))
        return subscribers_list

    def is_add(self, email):
        for key in self.__subscribers:
            if self.__subscribers[key] == email:
                return True
        return False

    def remove_subscriber(self, email):
        new_subscribers = {}
        for key in self.__subscribers:
            if self.__subscribers[key] != email:
                new_subscribers[key] = self.__subscribers[key]
        self.__subscribers = new_subscribers

    def merge_lists(self, other):
        new_subscribers = {}
        for key in self.__subscribers:
            if not key in other:
                new_subscribers[key] = self.__subscribers[key]
        for key in other:
            new_subscribers[key] = other[key]
        return new_subscribers

    def update_subscriber(self, name, new_name, new_email):
        new_subscribers = {}
        for key in self.__subscribers:
            if key == name:
                new_subscribers[new_name] = new_email
            else:
                new_subscribers[key] = self.__subscribers[key]
        self.__subscribers = new_subscribers
