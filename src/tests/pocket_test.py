import unittest
from entities.item import Item
from entities.pocket import Pocket

class TestItem(unittest.TestCase):
    def setUp(self):
        self.pocket1 = Pocket("Vasen Sivutasku")

    def test_pocket_creation_is_succesful_str_matches(self):
        self.assertEqual(self.pocket1.name, "Vasen Sivutasku")

    def test_add_item_to_pocket_is_succesful(self):
        self.item1 = Item("Kompassi", "Suunto M3")
        self.pocket1.add_item(self.item1)

        self.assertEqual(str(self.pocket1.list_items()[0]), "Kompassi, Suunto M3")