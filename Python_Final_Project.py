print("\n==============================================================\n")
print("            PROGRAM DIAGNOSA PENYAKIT BATUK DAN PILEK            ")
print("\n==============================================================\n")

tgl = input(str("Tanggal Pemeriksaan (DD-MM-YYYY) : "))
nama = input(str("Nama Pasien                      : "))
jk = input(str("Jenis Kelamin (P/L)              : "))

print("\nSilahkan jawab pertanyaan di bawah ini! (Yes = y / No = n)")
p1 = input(str("\n1. Apakah Anda merasa pusing? (y/n)               : ")).lower()
p2 = input(str("2. Apakah Anda merasa sakit tenggorokan? (y/n)    : ")).lower()
p3 = input(str("3. Apakah hidung Anda terasa tersumbat? (y/n)     : ")).lower()
p4 = input(str("4. Apakah tenggorokan Anda terasa gatal? (y/n)    : ")).lower()
p5 = input(str("5. Apakah Anda bersin-bersin terus menerus? (y/n) : ")).lower()
p6 = input(str("6. Apakah Anda sulit menelan saat makan? (y/n)    : ")).lower()

pilek_score = 0
batuk_score = 0

if p1 == "y": 
    pilek_score += 1
if p2 == "y": 
    batuk_score += 1
if p3 == "y": 
    pilek_score += 1
if p4 == "y": 
    batuk_score += 1
if p5 == "y": 
    pilek_score += 1
if p6 == "y": 
    batuk_score += 1

if pilek_score > batuk_score:
    hasil = "Pilek"
elif batuk_score > pilek_score:
    hasil = "Batuk"
elif pilek_score == batuk_score and pilek_score != 0:
    hasil = "Batuk dan Pilek"
else:
    hasil = "Penyakit tidak terdeteksi"

if hasil == "Batuk":
    solusi = ["- Hindari makanan dan minuman yang tidak higienis", 
              "- Istirahat yang cukup", 
              "- Memperbanyak minum air putih hangat",
              "- Hindari minuman yang dingin"]
    obat = ["- Combi", 
            "- Siladex", 
            "- Woods"]
elif hasil == "Pilek":
    solusi = ["- Istirahat yang cukup", 
              "- Minum teh hangat atau air jahe", 
              "- Konsumsi makanan yang hangat",
              "- Memperbanyak minum air putih"]
    obat = ["- Ultraflu", 
            "- Neozep", 
            "- Intunal-F"]
elif hasil == "Batuk dan Pilek":
    solusi = ["- Hindari makanan dan minuman yang tidak higienis",
              "- Istirahat yang cukup",
              "- Memperbanyak minum air putih hangat",
              "- Hindari makanan berminyak dan dingin",
              "- Konsumsi vitamin C"]
    obat = ["- Mixagrip Flu & Batuk",
            "- OBH Combi",
            "- Sanmol Flu & Batuk"]
else:
    solusi = ["Gejala tidak cukup untuk menentukan solusi"]
    obat = ["Gejala tidak bisa mendeteksi obat"]

print("\n==============================================================\n")
print("            PROGRAM DIAGNOSA PENYAKIT BATUK DAN PILEK            ")
print("\n==============================================================\n")

print("Tanggal Pemeriksaan : ", tgl)
print("Nama Pasien         : ", nama)
print("Jenis Kelamin       : ", jk)
print("Hasil Diagnosa      : ", hasil)

print("\nSolusi :")
for s in solusi:
    print(s)

print("\nObat :")
for o in obat:
    print(o)

print("\n==============================================================\n")
print("                     SEMOGA LEKAS SEMBUH YA                   \n")