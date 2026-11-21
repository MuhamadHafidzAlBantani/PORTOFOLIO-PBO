
class PenontonKonser:
    nama = ""
    kota = ""
    band = ""

    def perkenalan(self):
        print(f"{self.nama}: Halo, nama saya {self.nama}")

    def menyapa(self, nama):
        print(f"{self.nama}: Hai {nama}, nama saya {self.nama}")

    def asal_kota(self, nama):
        print(f"{self.nama}: Oke {nama}, saya orang {self.kota}")

    def membahas_band(self, nama, band_lawan):
        print(f"{self.nama}: Oh, {nama}, saya ke sini karena suka {self.band}")
        print(f"{self.nama}: Oke {nama}, kalau saya suka {band_lawan}")


# Data orang pertama

orang1 = PenontonKonser()
orang1.nama = input("Masukkan nama: ")
orang1.kota = input("Masukkan kota asal: ")
orang1.band = input("Masukkan band favorit: ")

print()

# Data orang kedua

orang2 = PenontonKonser()
orang2.nama = input("Masukkan nama: ")
orang2.kota = input("Masukkan kota asal: ")
orang2.band = input("Masukkan band favorit: ")

print("\n=== PERCAKAPAN DI KONSER ===")

orang1.perkenalan()
orang2.menyapa(orang1.nama)

print()

orang1.asal_kota(orang2.nama)
orang2.asal_kota(orang1.nama)

print()

orang1.membahas_band(orang2.nama, orang2.band)
