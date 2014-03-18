import unittest
from user import User
from user_list import User_list

class Test_user_list(unittest.TestCase):
    def setUp(self):
        self.new_user_list=User_list("new list 1")
        for i in range(5):
            user = User("user" + str(i), "user" + str(i) + "@mail.bg")
            self.new_user_list.list_of_users.append(user)
        self.new_user_list2=User_list("new list 2")
        for i in range(5):
            user = User("usr" + str(i), "user" + str(i) + "@mail.bg")
            self.new_user_list2.list_of_users.append(user)


    def test_new_user_list(self):
        self.assertEqual("new list 1",self.new_user_list.list_name)

    def test_merge(self):
        self.assertEqual(self.new_user_list.merge(self.new_user_list2.list_of_users), self.new_user_list.list_of_users + self.new_user_list2.list_of_users)

if __name__ == '__main__':
    unittest.main()