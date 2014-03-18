from lists import Lists
from user_list import User_list
import unittest
from user import User

class ListsTest(unittest.TestCase):
    def setUp(self):
        self.list = Lists()
        self.userlist = User_list("List1")
        self.userlist2 = User_list("List2")
        self.user = User("Kristiyan", "kristiyankisimov@yahoo.com")

    def test_list(self):
        self.assertEqual([], self.list.lists)

    def test_add(self):
        self.list.lists.append(self.userlist)
        self.assertEqual(self.list.add(self.user, self.userlist.list_name), True)
        self.assertEqual(self.list.add(self.user, self.userlist.list_name), False)

    def test_search_by_mail(self):
        self.list.lists.append(self.userlist)
        self.list.lists.append(self.userlist2)
        self.assertEqual(self.list.add(self.user, self.userlist.list_name), True)
        self.assertEqual(self.list.add(self.user, self.userlist2.list_name), True)
        self.assertEqual(self.list.search_by_mail(self.user.email), ["List1", "List2"])

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()