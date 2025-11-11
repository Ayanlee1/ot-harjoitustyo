import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    #def test_luotu_kortti_on_olemassa(self):
        #self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(500)
        self.assertEqual(self.maksukortti.saldo_euroina(), 15.0)

    def test_ota_rahaa_vahentaa_saldoa_jos_tarpeeksi(self):
        self.maksukortti.ota_rahaa(500)
        self.assertEqual(self.maksukortti.saldo_euroina(), 5.0)

    def test_ota_rahaa_ei_muuta_saldoa_jos_ei_tarpeeksi(self):
        self.maksukortti.ota_rahaa(1500)
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_ota_rahaa_palauttaa_true_jos_tarpeeksi(self):
        tulos = self.maksukortti.ota_rahaa(500)
        self.assertEqual(tulos, True)

    def test_ota_rahaa_palauttaa_false_jos_ei_tarpeeksi(self):
        tulos = self.maksukortti.ota_rahaa(1500)
        self.assertEqual(tulos, False)