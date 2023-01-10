from django.test import TestCase
from .models import Table


class TestModels(TestCase):

    def test_create_table(self):
        """Create a table and test of the DB has 1 entry"""
        table = Table.objects.create(table_number=1, num_seats=2)
        tables = Table.objects.all()
        self.assertEqual(len(tables), 1)

    def test_delete_table(self):
        """Delete a table and test of the DB has 0 entries"""
        table = Table.objects.create(table_number=1, num_seats=2)
        tables = Table.objects.all()
        table.delete()
        self.assertEqual(len(tables), 0)