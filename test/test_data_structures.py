import unittest
from datastructures.hash_table import HashTable


class TestHashTable(unittest.TestCase):
    def test_insert(self):
        ht = HashTable(3)
        ht1 = HashTable()

        ht.insert(1, 2)
        ht1.insert("John Doe", 5)
        ht1.insert("Janey Doe", 6)
        self.assertEqual(ht.table, [[], [[1, 2]], []])
        self.assertIn([["John Doe", 5]], ht1.table)
        self.assertIn([["Janey Doe", 6]], ht1.table)
        ht1.insert("Janey Doe", 8)
        self.assertIn([["Janey Doe", 8]], ht1.table)
        self.assertNotIn([["Janey Doe", 6]], ht1.table)

