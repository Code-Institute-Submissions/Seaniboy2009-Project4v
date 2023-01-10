from django.test import TestCase
from .models import Table, Booking, User
from .views import BookingPage
import datetime


class TestModels(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_user = User.objects.create(username='test-user2')

    def test_create_user(self):
        """Test if the user exists"""
        self.assertTrue(self.test_user)

    def test_check_booking_exists(self):
        """Create a booking"""
        table = Table.objects.create(table_number=1, num_seats=2)
        booking = Booking.objects.create(table=table, booked_by=self.test_user, booking_time=datetime.time(10, 00, 00))
        bookings = Booking.objects.all()
        check_avalible_tables()
        self.assertEqual(len(bookings), 1)

    @classmethod
    def tearDownClass(cls):
        ...