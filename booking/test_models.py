from django.test import TestCase
from .models import Table, Booking, User
import datetime


class TestModels(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_user = User.objects.create(username='test-user')

    def test_create_user(self):
        """Test if the user exists"""
        self.assertTrue(self.test_user)

    def test_create_table(self):
        """Create a table and test if the DB has 1 entry"""
        table = Table.objects.create(table_number=1, num_seats=2)
        tables = Table.objects.all()
        self.assertEqual(len(tables), 1)

    def test_delete_table(self):
        """Delete a table and test if the DB has 0 entries"""
        table = Table.objects.create(table_number=1, num_seats=2)
        tables = Table.objects.all()
        table.delete()
        self.assertEqual(len(tables), 0)

    def test_create_booking(self):
        """Create a booking and test if the DB has 1 entry"""
        table = Table.objects.create(table_number=1, num_seats=2)
        booking = Booking.objects.create(table=table, booked_by=self.test_user, booking_time=datetime.time(10, 00, 00))
        bookings = Booking.objects.all()
        self.assertEqual(len(bookings), 1)

    def test_delete_booking(self):
        """Delete a booking and test if the DB has 0 entries"""
        table = Table.objects.create(table_number=1, num_seats=2)
        booking = Booking.objects.create(table=table, booked_by=self.test_user, booking_time=datetime.time(10, 00, 00))
        bookings = Booking.objects.all()
        booking.delete()
        self.assertEqual(len(bookings), 0)

    @classmethod
    def tearDownClass(cls):
        ...