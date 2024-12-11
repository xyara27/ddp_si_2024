from Animal import *

class Burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis, bunyi):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis = jenis
        self.bunyi = bunyi

    def cetak_burung(self):
        super().cetak()
        print("Jenis \t\t\t\t: ", self.jenis,
              "\nBunyi \t\t\t\t: ", self.bunyi)
        
perkutut = Burung("Perkutut", "Biji-Bijian", "Makassar", "Bertelur", "Warna Putih", "Cuiitt cuiitt")
perkutut.cetak_burung()

elang = Burung("elang", "ikan", "Pegunungan", "Bertelur", "Besar", "Kwaakkk kwaakk")
elang.cetak_burung()