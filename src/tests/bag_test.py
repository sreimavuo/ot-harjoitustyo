import unittest
from entities.bag import Bag

class TestItem(unittest.TestCase):
    def setUp(self):
        self.bag1 = Bag("Reppu", "Eberlestock Switchblade")

    def test_bag_creation_is_succesful_str_matches(self):
        self.assertEqual(str(self.bag1), "Reppu, Eberlestock Switchblade")
