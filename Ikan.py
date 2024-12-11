from Animal import *

class Ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis, bunyi):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis = jenis
        self.bunyi = bunyi

    def cetak_ikan(self):
        super().cetak()
        print("Jenis \t\t\t\t: ", self.jenis,
              "\nBunyi \t\t\t\t: ", self.bunyi)
        
MasKoki = Ikan("Mas Koki", "Pelet", "Lautan", "Bertelur", "Warna Mas", "Blububb blububb")
MasKoki.cetak_ikan()

Cere = Ikan("Cere", "Lumut sawah", "Sawah", "Bertelur", "Kecil-Kecil", "Biipp bippp")
Cere.cetak_ikan()