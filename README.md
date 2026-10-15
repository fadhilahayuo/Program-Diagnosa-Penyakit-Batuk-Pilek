# Program Diagnosa Penyakit Batuk dan Pilek

Program Python berbasis terminal untuk mendiagnosis **batuk**, **pilek**, atau **keduanya** berdasarkan gejala pasien. Pengguna mengisi data pasien dan menjawab enam pertanyaan gejala dengan `y` (yes) atau `n` (no). Program menghitung skor, menentukan diagnosa, lalu mencetak hasil lengkap beserta solusi dan obat yang disarankan.

Proyek ini adalah **Final Project mata kuliah Dasar Pemrograman** (Semester 1, Program Studi Informatika, Universitas Bina Sarana Informatika), dikerjakan oleh Kelompok 7.

> **Penting:** program ini dibuat untuk latihan belajar pemrograman. Hasilnya **bukan diagnosa medis** dan tidak menggantikan pemeriksaan oleh dokter atau tenaga kesehatan.

## Fitur

- Input data pasien: tanggal pemeriksaan, nama, dan jenis kelamin
- Enam pertanyaan gejala dengan jawaban `y` / `n` (huruf besar maupun kecil diterima)
- Perhitungan skor terpisah untuk pilek dan batuk
- Empat kemungkinan hasil: **Pilek**, **Batuk**, **Batuk dan Pilek**, atau **Penyakit tidak terdeteksi**
- Output rapi seperti hasil pemeriksaan: data pasien, hasil diagnosa, daftar solusi, dan daftar obat

## Cara Kerja

Tiap gejala yang dijawab `y` menambah 1 poin ke salah satu skor:

| No | Pertanyaan | Menambah skor |
|----|------------|---------------|
| 1 | Apakah Anda merasa pusing? | Pilek |
| 2 | Apakah Anda merasa sakit tenggorokan? | Batuk |
| 3 | Apakah hidung Anda terasa tersumbat? | Pilek |
| 4 | Apakah tenggorokan Anda terasa gatal? | Batuk |
| 5 | Apakah Anda bersin-bersin terus menerus? | Pilek |
| 6 | Apakah Anda sulit menelan saat makan? | Batuk |

Skor kemudian dibandingkan:

| Kondisi | Hasil diagnosa |
|---------|----------------|
| skor pilek > skor batuk | Pilek |
| skor batuk > skor pilek | Batuk |
| skor sama dan bukan 0 | Batuk dan Pilek |
| kedua skor 0 | Penyakit tidak terdeteksi |

Jawaban selain `y` dianggap sebagai `n`.

## Konsep Pemrograman yang Dipakai

- Input dan output: `input()`, `print()`
- Tipe data: string, integer, list
- Variabel dan operator penugasan (`=`, `+=`)
- Operator perbandingan (`>`, `==`, `!=`) dan operator logika (`and`)
- Percabangan `if`, `elif`, `else`
- Perulangan `for` untuk mencetak isi list solusi dan obat

## Cara Menjalankan

1. Pastikan Python 3 sudah terpasang. Cek dengan `python --version`.
2. Unduh file `Python_Final_Project.py` dari repository ini.
3. Buka terminal di folder file tersebut, lalu jalankan:

```bash
python Python_Final_Project.py
```

Di beberapa sistem (Linux atau macOS) perintahnya `python3 Python_Final_Project.py`.

## Contoh Penggunaan

Jawaban pengguna ditulis setelah tanda titik dua. Pada contoh ini gejala 1, 3, dan 5 dijawab `y`, sehingga skor pilek 3 dan skor batuk 0.

```text
==============================================================

            PROGRAM DIAGNOSA PENYAKIT BATUK DAN PILEK

==============================================================

Tanggal Pemeriksaan (DD-MM-YYYY) : 15-10-2026
Nama Pasien                      : Contoh Pasien
Jenis Kelamin (P/L)              : P

Silahkan jawab pertanyaan di bawah ini! (Yes = y / No = n)

1. Apakah Anda merasa pusing? (y/n)               : y
2. Apakah Anda merasa sakit tenggorokan? (y/n)    : n
3. Apakah hidung Anda terasa tersumbat? (y/n)     : y
4. Apakah tenggorokan Anda terasa gatal? (y/n)    : n
5. Apakah Anda bersin-bersin terus menerus? (y/n) : y
6. Apakah Anda sulit menelan saat makan? (y/n)    : n
```

Output yang dicetak:

```text
==============================================================

            PROGRAM DIAGNOSA PENYAKIT BATUK DAN PILEK

==============================================================

Tanggal Pemeriksaan :  15-10-2026
Nama Pasien         :  Contoh Pasien
Jenis Kelamin       :  P
Hasil Diagnosa      :  Pilek

Solusi :
- Istirahat yang cukup
- Minum teh hangat atau air jahe
- Konsumsi makanan yang hangat
- Memperbanyak minum air putih

Obat :
- Ultraflu
- Neozep
- Intunal-F

==============================================================

                     SEMOGA LEKAS SEMBUH YA
```

## Tim Pengembang (Kelompok 7)

Dosen pengampu: Eni Pudjiarti, S.Kom, M.Kom

| Nama | Kontribusi |
|------|------------|
| Fadhilah Ayu Oktaviani | Menyusun makalah; kode bagian proses (inisialisasi skor, perhitungan skor, penentuan hasil diagnosa) |
| Talitha Rafa Febiani | Menyusun makalah; kode bagian output |
| Griggah Zadit Taqwa | Menyusun presentasi; kode bagian proses (penentuan solusi dan obat) |
| Dimas Saputra | Menyusun presentasi |

## Keterbatasan dan Pengembangan Lanjutan

- Jawaban selain `y` tidak divalidasi, jadi salah ketik dianggap `n`.
- Data tanggal dan jenis kelamin belum divalidasi formatnya.
- Gejala dan bobotnya sederhana (tiap gejala bernilai 1) dan tidak berdasarkan standar medis.
- Ide pengembangan: validasi input, perulangan agar bisa memeriksa beberapa pasien, bobot gejala yang berbeda, dan menyimpan hasil ke file.
