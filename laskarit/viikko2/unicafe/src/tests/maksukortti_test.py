import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_alkusaldo_on_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_lataaminen_kasvattaa_saldoa(self):
        self.maksukortti.lataa_rahaa(1000)
        
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 20.00 euroa")

    def test_ottaminen_toimii_kun_saldoa_on(self):
        self.maksukortti.ota_rahaa(500)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 5.00 euroa")

    def test_saldo_ei_muutu_jos_otto_liian_iso(self):
        self.maksukortti.ota_rahaa(10000)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_ottaminen_palauttaa_true_kun_saldo_riittaa(self):
        self.assertEqual(self.maksukortti.ota_rahaa(500), True)
    
    def test_ottaminen_palauttaa_false_kun_saldo_ei_riita(self):
        self.assertEqual(self.maksukortti.ota_rahaa(5000), False)
    