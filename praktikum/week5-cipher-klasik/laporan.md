# Laporan Praktikum Kriptografi
Minggu ke-: 5  
Topik: Chiper Kasik (Caesar, Vigenere, Transposisi)  
Nama: Laeli Maharani  
NIM: 230202763  
Kelas: 5IKRB  

---

## 1. Tujuan
1. Menerapkan algoritma Caeshar Chiper untuk enkripsi dan dekripsi teks.
2. Menerapkan algoritma Vigenere Chiper dengan variasi kunci.
3. Mengimplementasikan algoritma transposisi sederhana
4. Menjelaskan kelemahan algoritma kriptografi klasik.

---

## 2. Dasar Teori
Chiper klasik adalah metode kriptografi awal yang digunakan untuk menyembunyikan pesan dengan cara sederhana, sebelum munculnya algoritma modern. Ada tiga jenis chiper kasik yang paling dikena, yaitu Caesar Chiper, Vigenere Chiper, dan Transposisi Chiper.
- Caesar Chiper bekerja dengan menggeser setiap huruf dalam teks asli sejumlah posisi tertentu dalam alfabet. Misalnya, dengan pergeseran 3, huruf A menjadi D, B menjadi E, dan seterusnya. Chiper ini mudah diimplementasikan namun sangat lemah karena hanya memiliki sedikit kemungkinan kunci (26 kemungkinan).
- Vigenere Chiper merupakan pengembangan dari Caesar Chiper yang menggunakan kunci berupa kata. Setiap huruf kunci menentukan pergeseran berbeda pada huruf pesan. Metode ini lebih kuat dibanding Caesar karena variasi pergeseran lebih banyak, meski tetap dapat dipecahkan dengan analisis frekuensi huruf jika kuncinya pendek.
- Transposisi Cipher tidak mengubah huruf, tetapi mengubah urutan posisi huruf dalam pesan berdasarkan pola tertentu (misalnya kolom atau baris). Chiper bergantung pada aturan pengurutan, bukan pada penggantian karakter.
Secara umum, ciper klasik berperan penting dalam sejarah kriptografi karena menjadi dasar bagi perkembangan sistem enkripsi modern, meskipun tingkat keamanannya sudah tidak memadai untuk penggunaan saat ini.

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
