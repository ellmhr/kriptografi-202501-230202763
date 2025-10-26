# Laporan Praktikum Kriptografi
Minggu ke-: 4  
Topik: Entropy & Unicity Distance (Evaluasi Kekuatan Kunci dan Brute Force)
Nama: Laeli Maharani
NIM: 230202763
Kelas: 5IKRB
---

## 1. Tujuan
1. Menyelesaikan perhitungan sederhana terkait entropi kunci.  
2. Menggunakan teorema Euler pada contoh perhitungan modular & invers.  
3. Menghitung **unicity distance** untuk ciphertext tertentu.  
4. Menganalisis kekuatan kunci berdasarkan entropi dan unicity distance.  
5. Mengevaluasi potensi serangan brute force pada kriptosistem sederhana.  
---

## 2. Dasar Teori
Dalam kriptografi, entropy menggambarkan tingkat ketidakpastian atau keacakan suatu sistem kunci. Semakin tinggi nilai entropi, semakin sulit bagi pihak yang tidak berwenang untuk menebak kunci secara benar. Entropy biasanya diukur dalam satuan bit, dan menunjukkan berapa banyak kemungkinan kombinasi kunci yang bisa digunakan dalam suatu algoritma. Misalnya, kunci sepanjang 128 bit memiliki 2^128 kemungkinan kombinasi, yang menjadikannya sangat sulit dipecahkan dengan brute force.

Unicity distance adalah ukuran yang menunjukkan jumlah data terenkripsi (ciphertext) minimum yang diperlukan agar serangan kriptanalisis dapat menentukan satu kunci yang benar secara unik. Jika ciphertext yang tersedia lebih kecil dari unicity distance, maka masih terdapat banyak kemungkinan kunci yang dapat menghasilkan pesan yang masuk akal. Dengan kata lain, semakin besar nilai unicity distance, semakin kuat sistem kriptografi terhadap serangan analisis.

Dalam konteks brute force attack, penyerang mencoba semua kemungkinan kunci hingga menemukan yang cocok untuk mendeskripsikan pesan. Kekuatan sistem kriptografi bergantung pada kombinasi tingginya entropy dan besarnya unicity distance, yang membuat pencarian kunci dengan brute force menjadi sangat tidak efisien dan memakan waktu lama. Oleh karena itu, kedua konsep ini penting dalam menilai tingkat keamanan suatu algoritma kriptografi modern.
---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan

1. Membuat file `entropy-unicity.py` di folder `praktikum/week4-entropy-unicity/src/`.
2. Membuat folder `screenshots` di folder `praktikum/week4-entropy-unicity/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah sesuai nama file.

---

## 5. Source Code
1. Langkah (1) Perhitungan Entropy
```
import math

def entropy(keyspace_size):
    return math.log2(keyspace_size)

print("Entropy ruang kunci 26 =", entropy(26), "bit")
print("Entropy ruang kunci 2^128 =", entropy(2**128), "bit")
```
Hasil :
```
Entropy ruang kunci 26 = 4.700439718141093 bit
Entropy ruang kunci 2^128 = 128.0 bit
```

2. Langkah (2) Menghitung Unicity Distance
```
def unicity_distance(HK, R=0.75, A=26):
    return HK / (R * math.log2(A))

HK = entropy(26)
print("Unicity Distance untuk Caesar Cipher =", unicity_distance(HK))
```
Hasil :
```
Unicity Distance untuk Caesar Cipher = 1.3333333333333333
```

3. Langkah (3) Analsis Brute Force
```
def brute_force_time(keyspace_size, attempts_per_second=1e6):
    seconds = keyspace_size / attempts_per_second
    days = seconds / (3600*24)
    return days

print("Waktu brute force Caesar Cipher (26 kunci) =", brute_force_time(26), "hari")
print("Waktu brute force AES-128 =", brute_force_time(2**128), "hari")
```
Hasil :
```
Waktu brute force Caesar Cipher (26 kunci) = 3.0092592592592593e-10 hari
Waktu brute force AES-128 = 3.938453320844195e+27 hari
```

Source Code keseluruhan :
```
import math

def entropy(keyspace_size):
    return math.log2(keyspace_size)

print("Entropy ruang kunci 26 =", entropy(26), "bit")
print("Entropy ruang kunci 2^128 =", entropy(2**128), "bit")

def unicity_distance(HK, R=0.75, A=26):
    return HK / (R * math.log2(A))

HK = entropy(26)
print("Unicity Distance untuk Caesar Cipher =", unicity_distance(HK))

def brute_force_time(keyspace_size, attempts_per_second=1e6):
    seconds = keyspace_size / attempts_per_second
    days = seconds / (3600*24)
    return days

print("Waktu brute force Caesar Cipher (26 kunci) =", brute_force_time(26), "hari")
print("Waktu brute force AES-128 =", brute_force_time(2**128), "hari")
```
Hasil :
```
Entropy ruang kunci 26 = 4.700439718141093 bit
Entropy ruang kunci 26 = 4.700439718141093 bit
Entropy ruang kunci 2^128 = 128.0 bit
Entropy ruang kunci 2^128 = 128.0 bit
Unicity Distance untuk Caesar Cipher = 1.3333333333333333
Waktu brute force Caesar Cipher (26 kunci) = 3.0092592592592593e-10 hari
Waktu brute force AES-128 = 3.938453320844195e+27 hari
```

---

## 6. Hasil dan Pembahasan
# Hasil eksekusi langkah (1) (perhitungan entropy)
![Hasil Eksekusi](screenshots/L1-perhitungan-entropy.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: …  
- Pertanyaan 2: …  
)
---

## 8. Kesimpulan
(Tuliskan kesimpulan singkat (2–3 kalimat) berdasarkan percobaan.  )

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log
```
commit week4-entropy-unicity
Author: Laeli Maharani <laelimaharani09@gmail.com>
Date:   2025-07-10

    week4-entropy-unicity: (Evaluasi Kekuatan Kunci dan Brute Force dan laporan).
```
