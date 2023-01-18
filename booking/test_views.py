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
        self.assertEqual(len(bookings), 1)

    def test_get_home_page(self):
        """Get home page url"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_get_menu_page(self):
        """Get menu page url"""
        response = self.client.get('/menu/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu.html')

    def test_get_booking_page(self):
        """Get booking page url"""
        response = self.client.get('/booking/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book.html')

    def test_get_login_page(self):
        """Get login page url"""
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/login.html')

    def test_get_create_account_page(self):
        """Get create account page url"""
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/signup.html')

    def test_get_management_page(self):
        """Get management url"""
        response = self.client.get('/management/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'management.html')

    @classmethod
    def tearDownClass(cls):
        ...
