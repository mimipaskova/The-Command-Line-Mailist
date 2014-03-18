import unittest
from user_list import User_list

class Test_user_list(unittest.TestCase):
    def setUp(self):
        self.new_user_list=User_list("new list 1")

    def test_new_user_list(self):

        self.assertEqual("new list 1",self.new_user_list.list_name)

if __name__ == '__main__':
    unittest.main()