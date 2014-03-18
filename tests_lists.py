from lists import Lists
from user_list import User_list
import unittest
from user import User

class ListsTest(unittest.TestCase):
    def setUp(self):
        self.list = Lists()
        self.userlist = User_list("List1")
        self.user = User("Kristiyan", "kristiyankisimov@yahoo.com")

    def test_list(self):
        self.assertEqual([], self.list.lists)

    def test_add(self):
        self.list.lists.append(self.userlist)
        self.assertEqual(self.list.add(self.user, self.userlist.list_name), True)
        self.assertEqual(self.list.add(self.user, self.userlist.list_name), False)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()