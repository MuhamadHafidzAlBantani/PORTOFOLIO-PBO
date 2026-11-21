# Resume Materi Python OOP

## 1. Class dan Object

Dalam Python, class adalah cetakan atau rancangan untuk membuat object. Class bisa dibayangkan seperti cetakan yang digunakan untuk membuat beberapa benda dengan bentuk dan struktur yang sama.

Sedangkan object adalah hasil yang dibuat dari class tersebut. Setiap object memiliki struktur data dan fungsi yang sama, tetapi isi datanya bisa berbeda.

Contohnya, pada program percakapan penonton konser, terdapat class `PenontonKonser` yang digunakan sebagai rancangan untuk membuat dua object, yaitu `orang1` dan `orang2`. Keduanya memiliki atribut dan method yang sama, tetapi data nama, kota, dan band favoritnya dapat berbeda.

## 2. Attributes

Attribute adalah variabel yang digunakan untuk menyimpan data di dalam class atau object.

Pada program `PenontonKonser`, terdapat tiga atribut, yaitu:
- `nama` untuk menyimpan nama penonton.
- `kota` untuk menyimpan kota asal penonton.
- `band` untuk menyimpan band favorit penonton.

Nilai atribut tersebut dapat berbeda pada setiap object. Misalnya, `orang1` dan `orang2` memiliki nama, kota asal, serta band favorit masing-masing.

## 3. Class Attribute

Class attribute adalah atribut yang ditulis di dalam class dan dapat digunakan bersama oleh object-object yang dibuat dari class tersebut.

Pada program `PenontonKonser`, atribut `nama`, `kota`, dan `band` ditulis di dalam class sebagai nilai awal berupa string kosong. Ketika data dimasukkan melalui object, nilai atribut dapat diisi sesuai dengan masing-masing penonton.

## 4. Methods

Method adalah fungsi yang ditulis di dalam class. Method digunakan untuk menjelaskan tindakan atau aktivitas yang dapat dilakukan oleh object.

Pada program `PenontonKonser`, terdapat beberapa method:
- `perkenalan()` untuk memperkenalkan diri.
- `menyapa()` untuk menyapa penonton lain.
- `asal_kota()` untuk membahas kota asal.
- `membahas_band()` untuk membahas band favorit masing-masing penonton.

Method tersebut membuat setiap object dapat melakukan aktivitas dalam simulasi percakapan di konser.

## 5. Parameter self

`self` adalah parameter khusus yang digunakan di dalam method untuk merujuk pada object yang sedang menjalankan method tersebut.

Pada program `PenontonKonser`, penggunaan `self.nama`, `self.kota`, dan `self.band` berfungsi untuk mengambil data milik object yang sedang menjalankan method.

Contohnya, ketika `orang1.perkenalan()` dipanggil, `self.nama` akan mengambil nama yang dimiliki oleh object `orang1`.

## 6. Method dengan Parameters

Method dapat menerima parameter tambahan selain `self`. Parameter tersebut digunakan untuk menerima data dari luar object ketika method dipanggil.

Pada program `PenontonKonser`, contohnya:
- `menyapa(self, nama)`
- `asal_kota(self, nama)`
- `membahas_band(self, nama, band_lawan)`

Parameter tersebut digunakan untuk menerima nama penonton lain dan informasi band favoritnya sehingga kedua object dapat melakukan percakapan.

## 7. Naming Conventions

Naming conventions adalah aturan penulisan nama dalam program agar kode lebih mudah dibaca dan dipahami.

Dalam program `PenontonKonser`, penerapannya adalah:

- **Nama class:** menggunakan PascalCase, contohnya `PenontonKonser`.
- **Nama method:** menggunakan snake_case, contohnya `perkenalan()`, `asal_kota()`, dan `membahas_band()`.
- **Nama attribute:** menggunakan snake_case, contohnya `nama`, `kota`, dan `band`.

## Kesimpulan

Melalui program `PenontonKonser`, dapat dipahami bahwa konsep dasar Python OOP membantu menyusun program menggunakan class dan object. Class digunakan sebagai rancangan, sedangkan object merupakan hasil dari rancangan tersebut.

Program ini juga menerapkan penggunaan attribute untuk menyimpan data, method untuk menjalankan aktivitas, `self` untuk mengakses data milik object, serta parameter untuk menerima informasi tambahan. Dengan konsep tersebut, program percakapan dua penonton konser dapat dibuat lebih terstruktur dan mudah dipahami.
