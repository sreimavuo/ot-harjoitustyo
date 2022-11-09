import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    # Konstruktorin testit
    def test_luodun_kassapaatteen_rahamaara_tasmaa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_luodun_kassapaatteen_myydyt_maukkaat_on_nolla(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_luodun_kassapaatteen_myydyt_edulliset_on_nolla(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    # Käteisostot kun raha riittää
    def test_syo_kateisella_maukkaasti_raha_riittaa_laskuri_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)

        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_syo_kateisella_maukkaasti_raha_riittaa_kassan_saldo_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_syo_kateisella_maukkaasti_raha_riittaa_vaihtoraha_oikein(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)

    def test_syo_kateisella_edullisesti_raha_riittaa_laskuri_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(500)

        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_syo_kateisella_edullisesti_raha_riittaa_kassan_saldo_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(500)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_syo_kateisella_edullisesti_raha_riittaa_vaihtoraha_oikein(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(500), 260)

    # Käteisostot kun raha ei riitä
    def test_syo_kateisella_maukkaasti_raha_ei_riita_laskuri_ei_kasva(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)

        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_syo_kateisella_maukkaasti_raha_ei_riita_kassan_saldo_ei_kasva(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_syo_kateisella_maukkaasti_raha_ei_riita_vaihtoraha_oikein(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(100), 100)

    def test_syo_kateisella_edullisesti_raha_ei_riita_laskuri_ei_kasva(self):
        self.kassapaate.syo_edullisesti_kateisella(100)

        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_syo_kateisella_edullisesti_raha_ei_riita_kassan_saldo_ei_kasva(self):
        self.kassapaate.syo_edullisesti_kateisella(100)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_syo_kateisella_edullisesti_raha_ei_riita_vaihtoraha_oikein(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(100), 100)

    # Korttiostot kun raha riittää
    def test_syo_kortilla_maukkaasti_raha_riittaa_kortin_saldo_vahenee(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.maksukortti.saldo, 600)

    def test_syo_kortilla_maukkaasti_raha_riittaa_paluuarvo_true(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)

    def test_syo_kortilla_maukkaasti_raha_riittaa_laskuri_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_syo_kortilla_maukkaasti_raha_riittaa_kassan_saldo_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_syo_kortilla_edullisesti_raha_riittaa_kortin_saldo_vahenee(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.maksukortti.saldo, 760)

    def test_syo_kortilla_edullisesti_raha_riittaa_paluuarvo_true(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)

    def test_syo_kortilla_edullisesti_raha_riittaa_laskuri_kasvaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_syo_kortilla_edullisesti_raha_riittaa_kassan_saldo_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    # Korttiostot kun raha ei riitä
    def test_syo_kortilla_maukkaasti_raha_ei_riita_kortin_saldo_ei_muutu(self):
        maksukortti = Maksukortti(100)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)

        self.assertEqual(maksukortti.saldo, 100)

    def test_syo_kortilla_maukkaasti_raha_ei_riita_laskuri_ei_kasva(self):
        maksukortti = Maksukortti(100)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)

        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_syo_kortilla_maukkaasti_raha_ei_riita_paluuarvo_false(self):
        maksukortti = Maksukortti(100)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(maksukortti), False)

    def test_syo_kortilla_edullisesti_raha_ei_riita_kortin_saldo_ei_muutu(self):
        maksukortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)

        self.assertEqual(maksukortti.saldo, 100)

    def test_syo_kortilla_edullisesti_raha_ei_riita_laskuri_ei_kasva(self):
        maksukortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)

        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_syo_kortilla_edullisesti_raha_ei_riita_paluuarvo_false(self):
        maksukortti = Maksukortti(100)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(maksukortti), False)

    # Rahan lataaminen kortille
    def test_rahan_lataaminen_kasvattaa_kortin_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)

        self.assertEqual(self.maksukortti.saldo, 2000)

    def test_rahan_lataaminen_kasvattaa_kassan_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 101000)

    def test_negatiivinen_lataaminen_ei_kasvata_kassan_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1000)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
