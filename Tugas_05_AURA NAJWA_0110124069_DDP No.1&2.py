#list utama : kendaraan
kendaraan = ["vario", "motor", "200cc", "hitam", "roda 2"]

#mencetak isi dari list kendaraan
print(kendaraan)

#menambahkan value atau nilai di ujung list (pakai append())

#proses append 1(harga kendaraan)
kendaraan.append("20.000.000")

#proses append 2(tipe kendaraan)
kendaraan.append("matic")

#cetak nilai kendaraan setelah perubahan
print(kendaraan)

#sisipkan nilai untuk tipe kendaraan
kendaraan.insert (2, "yamaha")

#cetak hasil list akhirnya
print (kendaraan)



pilihan = int(input("""pilih nomor pilihan :
1. Menghitung Luas Persegi
2. Menghitung Luas Lingkaran
3. Menghitung Luas Segitiga
"""))

match pilihan:
    case 1:
        print("Menghitung Luas Persegi")
        s = int(input("Masukkan nilai sisi: "))
        luaspersegi = s * s
        print(f"Luas persegi dengan sisi {s} adalah {luaspersegi}")
    case 2:
        print("Menghitung Luas Lingkaran")
        pi = 3.14
        r = int(input("Masukkan nilai jari-jari"))
        luaslingkaran = pi * r**2
        print(f"Luas lingkaran dengan jari-jari {r} adalah {luaslingkaran}")
    case 3:
        print("Menghitung Luas Segitiga")
        alas = int(input("Masukkan nilai alas:"))
        tinggi =int(input("Masukkan nilai tinggi:")) 
        luassegitiga = 1/2 * alas * tinggi 
        print(f"Luas segitiga dengan alas {alas} dan tinggi {tinggi} adalah {luassegitiga}")
    case _:
        print("Input Tidak Valid")
                  



