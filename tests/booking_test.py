import unittest

from models.booking import Booking
from models.member import Member
from models.gymclass import Gymclass

class TestBooking(unittest.TestCase):

    def setUp(self):
        member = Member("Dani")
        gymclass = Gymclass("Zumba", "12/03/21", "19:00", "Exercise and dance and have fun!")
        self.booking = Booking(member, gymclass)

    def test_booking_has_member(self):
        self.assertEqual("Dani", self.booking.member.name)

    def test_booking_has_gymclass(self):
        self.assertEqual("Zumba", self.booking.gymclass.name)