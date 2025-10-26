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
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat file `caesar_cipher.py` di folder `praktikum/week2-cryptosystem/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python caesar_cipher.py`.)

---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
# contoh potongan kode
def encrypt(text, key):
    return ...
```
)

---

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/output.png)
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
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit abc12345
Author: Nama Mahasiswa <email>
Date:   2025-09-20

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
