class Animal:
    def __init__(self, nama, makanan, hidup, berkembang_biak):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak

    def cetak(self):
        print(f"\nNama \t\t\t\t: ", self.nama,
              "\nmakanan \t\t\t: ", self.makanan, 
              "\nhidup \t\t\t\t: ", self.hidup,
              "\nberkembang biak \t\t: ", self.berkembang_biak
              )

object = Animal("Buaya", "Daging", "Amphibi", "Bertelur")
print (object.cetak())