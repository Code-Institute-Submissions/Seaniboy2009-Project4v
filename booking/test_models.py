from django.test import TestCase
from .models import Table


class TestModels(TestCase):

    def test_done_defaults_to_false(self):
        table = Table.objects.create(table_number=1, num_seats=2)
        self.assertFalse(table.has_booking)