from Animal import *

class Ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, design, racun):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.design = design
        self.racun = racun

    def cetak_ular(self):
        super().cetak()
        print("Design \t\t\t\t: ", self.design,
              "\nRacun \t\t\t\t: ", self.racun)
        
anaconda = Ular("Anaconda", "Kambing", "Amazon", "Bertelur", "Batik Solo", "Tidak Beracun")
anaconda.cetak_ular()

Cobra = Ular("Cobra", "Tikus", "Hutan", "Bertelur", "Abu-Abu", "Beracun")
Cobra.cetak_ular()