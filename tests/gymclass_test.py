import unittest
from models.gymclass import Gymclass

class TestGymclass(unittest.TestCase):

    def setUp(self):
        self.gymclass = Gymclass("Zumba", "12/03/21", "19:00", "Exercise and dance and have fun!")
        
    def test_gymclass_has_name(self):
        self.assertEqual("Zumba", self.gymclass.name)

    def test_gymclass_has_date(self):
        self.assertEqual("12/03/21", self.gymclass.date)

    def test_gymclass_has_time(self):
        self.assertEqual("19:00", self.gymclass.time)

    def test_gymclass_has_details(self):
        self.assertEqual("Exercise and dance and have fun!", self.gymclass.details)