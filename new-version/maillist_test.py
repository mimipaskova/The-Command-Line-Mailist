from maillist import MailList
import unittest
from collections import OrderedDict

class MailListTest(unittest.TestCase):
    def setUp(self):
        self.mail = MailList("Programming with Java")
        self.mail2 = MailList("Not Programming ")

    def test_get_listname(self):
        self.assertEqual("Programming with Java", self.mail.get_name())

    def test_set_name(self):
        self.mail.set_name("java")
        self.assertEqual(self.mail.get_name(),"java")

    def test_add_subscriber(self):
        self.mail.add_subscriber("Kristiyan Kisimov", "kristiyankisimov@yahoo")
        self.mail.add_subscriber("Ivan Ivanov", "ivanivanov@gmail.com")
        self.assertEqual(self.mail.count_of_subscribers(), 2)
        self.mail.add_subscriber("Dimo Dimov", "dimodimov@mail.com")
        self.assertEqual(self.mail.count_of_subscribers(), 3)

    def test_get_subscribers(self):
        self.mail.add_subscriber("Maria Paskova", "maria@maria")
        self.assertEqual(self.mail.get_subscibers(),{"Maria Paskova": "maria@maria"})
        self.mail.add_subscriber("gosho", "gosho@gosho")
        self.assertEqual(self.mail.get_subscibers(),{"Maria Paskova": "maria@maria", "gosho": "gosho@gosho" })

    def test_is_add(self):
        self.mail.add_subscriber("Kristiyan Kisimov", "kristiyankisimov@yahoo")
        self.mail.add_subscriber("Ivan Ivanov", "ivanivanov@gmail")
        self.assertEqual(True ,self.mail.is_add("kristiyankisimov@yahoo"))
        self.assertEqual(False, self.mail.is_add("asdf"))
        self.assertEqual(True, self.mail.is_add("ivanivanov@gmail"))

    def test_remove_subscriber(self):
        self.mail.add_subscriber("Kristiyan Kisimov", "kristiyankisimov@yahoo")
        self.mail.add_subscriber("Ivan Ivanov", "ivanivanov@gmail")
        self.mail.add_subscriber("Kristiyan", "kristiyankisimov")
        self.mail.add_subscriber("Ivan", "ivanov@gmail")

        self.mail.remove_subscriber("kristiyankisimov")
        self.assertEqual(False, self.mail.is_add("kristiyankisimov"))

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
