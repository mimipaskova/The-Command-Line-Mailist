import unittest
from mail import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User("Kristiyan", "kristiyankisimov@yahoo.com")

    def test_user_name(self):
        self.assertEqual(self.user.name, "Kristiyan")

    def test_user_email(self):
        self.assertEqual(self.user.email, "kristiyankisimov@yahoo.com")

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()