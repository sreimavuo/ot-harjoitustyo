import unittest
from entities.item import Item

class TestItem(unittest.TestCase):
    def setUp(self):
        self.item1 = Item("Kompassi", "Suunto M3")

    def test_item_creation_is_succesful_str_matches(self):
        self.assertEqual(str(self.item1), "Kompassi, Suunto M3")
