class Ucus():
    havayolu = "THY"

    def __init__(self, kod, kalkıs, varis, sure, kapasite, yolcu):
        self.kod = kod
        self.kalkıs = kalkıs
        self.varis = varis
        self.sure = sure
        self.kapasite = kapasite
        self.yolcu = yolcu

    def anaons(self):
        return print(f"{self.kod} Numaralı ucak kalkıcak")

    def kalanKoltuk(self):
        self.kalankoltuklar = self.kapasite - self.yolcu
        print(f"Kalan Koltuk sayisi {self.kalankoltuklar}")
        return self.kalankoltuklar

    def koltukGuncelleme(self):
        return self.kapasite - self.yolcu

    def biltSatis(self, bilet=1):
        if self.kalankoltuklar >= bilet:
            self.yolcu += bilet
            self.kalanKoltuk()
            self.koltukGuncelleme()
        else:
            print(f"Kapasite doldu maksimum alınabilcek bilet sayisi : {self.kalankoltuklar}")

    def biletIptal(self, biletiptal=1):

        if self.yolcu >= biletiptal:
            self.yolcu -= biletiptal
            self.kalanKoltuk()
            self.koltukGuncelleme()
        else:
            print(
                f"Yolcu sayısından fazla bilet iptal edemezsiniz maksimum iptal edilebilecek bilet sayisi {self.yolcu}")


#           (ucakno, kalkis , varis, süre,kapasite, yolcus.)
ucus1 = Ucus("tk222", "ist", "ank", "2 saat", 250, 200)
ucus1.anaons()
ucus1.kalanKoltuk()
ucus1.biltSatis(35)
ucus1.biletIptal(20)
ucus1.biltSatis(10)