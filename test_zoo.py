import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()
    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(5), 50)      
    # Add your additional test cases here.
    def test_invalid_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(-1), "invalid")
    def test__teen_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(6), 50)
    def test_student_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(15), 100)
    def test_people_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(40), 150)
    def test_elderly_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(61), 100)
if __name__ == '__main__':
    unittest.main()