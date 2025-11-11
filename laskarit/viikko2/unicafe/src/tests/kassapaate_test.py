import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()

    def test_kassapaatteen_alkusaldo_on_oikea(self):
        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1000.0)

    def test_myytyjen_lounaiden_maara_alussa_nolla(self):
        self.assertEqual(self.kassa.edulliset, 0)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_edullinen_kateisosto_antaa_oikean_vaihtorahan(self):
        vaihtoraha = self.kassa.syo_edullisesti_kateisella(300)
        self.assertEqual(vaihtoraha, 60)

    def test_edullinen_kateisosto_kasvattaa_kassan_saldoa(self):
        self.kassa.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1002.40)

    def test_edullinen_kateisosto_kasvattaa_myytyjen_maaraa(self):
        self.kassa.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassa.edulliset, 1)

    def test_maukas_kateisosto_antaa_oikean_vaihtorahan(self):
        vaihtoraha = self.kassa.syo_maukkaasti_kateisella(500)
        self.assertEqual(vaihtoraha, 100)

    def test_maukas_kateisosto_kasvattaa_kassan_saldoa(self):
        self.kassa.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1004.00)

    def test_maukas_kateisosto_kasvattaa_myytyjen_maaraa(self):
        self.kassa.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassa.maukkaat, 1)

    def test_edullinen_kateisosto_ei_riittava_maksu_palauttaa_kaiken(self):
        vaihtoraha = self.kassa.syo_edullisesti_kateisella(200)
        self.assertEqual(vaihtoraha, 200)

    def test_edullinen_kateisosto_ei_riittava_maksu_ei_kasvata_kassaa(self):
        self.kassa.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1000.0)

    def test_edullinen_kateisosto_ei_riittava_maksu_ei_kasvata_myytyja(self):
        self.kassa.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassa.edulliset, 0)

    def test_maukas_kateisosto_ei_riittava_maksu_palauttaa_kaiken(self):
        vaihtoraha = self.kassa.syo_maukkaasti_kateisella(300)
        self.assertEqual(vaihtoraha, 300)

    def test_maukas_kateisosto_ei_riittava_maksu_ei_kasvata_kassaa(self):
        self.kassa.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1000.0)

    def test_maukas_kateisosto_ei_riittava_maksu_ei_kasvata_myytyja(self):
        self.kassa.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_edullinen_korttiosto_veloittaa_kortilta(self):
        kortti = Maksukortti(1000)
        self.kassa.syo_edullisesti_kortilla(kortti)
        self.assertEqual(kortti.saldo_euroina(), 7.6)

    def test_edullinen_korttiosto_palauttaa_true(self):
        kortti = Maksukortti(1000)
        tulos = self.kassa.syo_edullisesti_kortilla(kortti)
        self.assertTrue(tulos)

    def test_edullinen_korttiosto_kasvattaa_myytyjen_maaraa(self):
        kortti = Maksukortti(1000)
        self.kassa.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassa.edulliset, 1)

    def test_maukas_korttiosto_veloittaa_kortilta(self):
        kortti = Maksukortti(1000)
        self.kassa.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(kortti.saldo_euroina(), 6.0)

    def test_maukas_korttiosto_palauttaa_true(self):
        kortti = Maksukortti(1000)
        tulos = self.kassa.syo_maukkaasti_kortilla(kortti)
        self.assertTrue(tulos)

    def test_maukas_korttiosto_kasvattaa_myytyjen_maaraa(self):
        kortti = Maksukortti(1000)
        self.kassa.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassa.maukkaat, 1)

    def test_edullinen_korttiosto_ei_riittava_saldo_ei_muuta_korttia(self):
        kortti = Maksukortti(100)
        self.kassa.syo_edullisesti_kortilla(kortti)
        self.assertEqual(kortti.saldo_euroina(), 1.0)

    def test_edullinen_korttiosto_ei_riittava_saldo_palauttaa_false(self):
        kortti = Maksukortti(100)
        tulos = self.kassa.syo_edullisesti_kortilla(kortti)
        self.assertFalse(tulos)

    def test_edullinen_korttiosto_ei_riittava_saldo_ei_kasvata_myytyja(self):
        kortti = Maksukortti(100)
        self.kassa.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassa.edulliset, 0)

    def test_maukas_korttiosto_ei_riittava_saldo_ei_muuta_korttia(self):
        kortti = Maksukortti(300)
        self.kassa.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(kortti.saldo_euroina(), 3.0)

    def test_maukas_korttiosto_ei_riittava_saldo_palauttaa_false(self):
        kortti = Maksukortti(300)
        tulos = self.kassa.syo_maukkaasti_kortilla(kortti)
        self.assertFalse(tulos)

    def test_maukas_korttiosto_ei_riittava_saldo_ei_kasvata_myytyja(self):
        kortti = Maksukortti(300)
        self.kassa.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_korttiosto_ei_muuta_kassan_rahamaaraa_edullinen(self):
        kortti = Maksukortti(1000)
        self.kassa.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1000.0)

    def test_korttiosto_ei_muuta_kassan_rahamaaraa_maukas(self):
        kortti = Maksukortti(1000)
        self.kassa.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1000.0)

    def test_rahan_lataus_kasvattaa_kortin_saldoa(self):
        kortti = Maksukortti(0)
        self.kassa.lataa_rahaa_kortille(kortti, 500)
        self.assertEqual(kortti.saldo_euroina(), 5.0)

    def test_rahan_lataus_kasvattaa_kassan_saldoa(self):
        kortti = Maksukortti(0)
        self.kassa.lataa_rahaa_kortille(kortti, 500)
        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1005.0)

    def test_negatiivisen_summan_lataaminen_ei_muuta_kortin_saldoa(self):
        kortti = Maksukortti(1000)
        self.kassa.lataa_rahaa_kortille(kortti, -500)
        self.assertEqual(kortti.saldo_euroina(), 10.0)

    def test_negatiivisen_summan_lataaminen_ei_muuta_kassan_saldoa(self):
        kortti = Maksukortti(1000)
        self.kassa.lataa_rahaa_kortille(kortti, -500)
        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1000.0)

    def test_negatiivisen_summan_lataaminen_palauttaa_none(self):
        kortti = Maksukortti(1000)
        tulos = self.kassa.lataa_rahaa_kortille(kortti, -500)
        self.assertIsNone(tulos)