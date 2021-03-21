import unittest
from models.gymclass import Gymclass

class TestGymclass(unittest.TestCase):

    def setUp(self):
        self.gymclass = Gymclass("Zumba", "12/03/21", "19:00", "Exercise and dance and have fun!")
        
    def test_gymclass_has_name(self):
        self.assertEqual("Zumba", self.gymclass.name)