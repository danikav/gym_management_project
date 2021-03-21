import unittest
from models.member import Member

class TestMember(unittest.TestCase):

    def setUp(self):
        self.member = Member("Dani")

    def test_member_has_name(self):
        self.assertEqual("Dani", self.member.name)