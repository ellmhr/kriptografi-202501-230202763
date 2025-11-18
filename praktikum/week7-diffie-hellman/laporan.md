# Laporan Praktikum Kriptografi
Minggu ke-: 7  
Topik: Diffie-Hellman Key Exchange  
Nama: Laeli Maharani  
NIM: 23020763  
Kelas: 5IKRB  

---

## 1. Tujuan
1. Melakukan simulasi protokol Diffie-hellman untuk pertukaran kunci publik.
2. Menjelaskan mekanisme pertukaran kunci rahasia menggunakan bilangan prima dan logaritma diskrit.
3. Menganalisis potensi serangan pada protokol Diffie-Hellman (termasuk serangan Man-in-the-Middle / MITM).

---

## 2. Dasar Teori
Diffie-Hellman Key Exchange adalah sebuah metode kriptografi yang memunginkan dua pihak bertukar kunci secara aman melalui jaringan yang tidka aman, tanpa harus mengirimkan kunci secara langsung. Konsep ini diperkenalkan oleh Whitfield Dfie dan Martin Hellman pada tahun 1976, dan menjadi dasar bagi banyak protokol keamanan modern. Inti dari metode ini adalah penggunaan matematika bilangan prima dan operasi eksponensial modular yang sullit dibalik tanpa informsi tertentu.

Dalam prosesnya, kedua pihak memilih bilangan publik berupa angka prima (p) dan generator (g). Masing-masing pihak kemudian membuat kunci rahasia privat dan menghitung nilai publik dengan operasi modular. Niai publik ini ditukar secara bebas melalui jarinagn. Setelah nlai publik diterima, masing-msing pihak melakukan perhitungan lanjutan untuk menghasilkan shared secret key yang identik, messkipun mereka tidak pernah mengirimkan kunci tersebut secara langsung.

Keamanan Diffie-Hellman bergantung pada kesulitan masalah Discrete Logarithm Problem (DLP), yaitu sulitnya mencari nilai eksponen dari hasil perhitungan modular. Karena sifat matematis ini, pihak ketiga tidak dapat menghitung kunci rahasia bersama meskipun mereka melihat data publik yang ditukar. Mekanisme ini embuat Diffie-Hellman menjadi salah satu fondasi penting dalam protokol seperti HTTPS, VPN, dan berbagai sistem keamanan modern.

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
Langkah 1 -- Simulasi Diffie-Hellman
```python
import random

# parameter umum (disepakati publik)
p = 23  # bilangan prima
g = 5   # generator

# private key masing-masing pihak
a = random.randint(1, p-1)  # secret Alice
b = random.randint(1, p-1)  # secret Bob

# public key
A = pow(g, a, p)
B = pow(g, b, p)

# exchange public key
shared_secret_A = pow(B, a, p)
shared_secret_B = pow(A, b, p)

print("Kunci bersama Alice :", shared_secret_A)
print("Kunci bersama Bob   :", shared_secret_B)
```

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
1. Mengapa Diffie-Hellman memungkinkan pertukaran kunc di saluran publik?
2. Apa kelemahan utama protokol Diffie-Hellman murni?
3. Bagaimanan cara mencegah serangan MITM pada protokol ini?

Jawab :
1. Diffie-Hellan memungkinkan pertukaran kunci di saluran publik karena kedua pihak hanya bertukar nilai publik yang aman untuk dilihat siapa saja. Nilai yang benar-benar bersifat rahasia tidak pernah dikirim, melainkan dihitung masing-masing pihak menggunakan angka privat yang disimpan sendiri.
Pengintai yang melihat komunikasi hanya mendapatkan data publik, tetapi tetap tidak bisa menebak kunci rahasia yang dihasilkan karena harus memecahkan Discrete Logrithm Problem, yaitu masalah matematika yang sangat sulit dan tidak efisien diselesaikan meskipun dengan komputer modern. Inilah yang membuat Diffie-Hellman aman meskipun berjalan di jaringan publik.

2. Kelemahan utama pada protokol Diffie-Hellman murni adalah rentan terhadap serangan Man-in-the-Middle. Dalam protokol aslinya, tidak ada mekanisme untuk memverifikasi indentitas pihak yang bertukar kunci, sehingga penyerang dapat menyamar sebagai masing-masing pihak dan membangun dua kunci rahasia berbeda tanpa terdeteksi.
Selain itu, Diffie-Hellman murni juga tidak menyediakan autentikasi dan tidak menjamin bahwa pihak yang diajak bertukar kunci benar-benar pihak yang dimaksud. Karena itu, DH biasanya dikobinasikan dengan tanda tangan digital atua sertifikat untuk meningkatkan keamanan.

3. Untuk mencegah serangan Man-in-the-Middle (MitM) pada protoko Diffie-Hellmn, langkah utamanya adalah menambahkan autentikasi. Berikut cara-cara umum dilakukan:
   - Mengguanakan tanda tangan digital (digital signature) setiap pihak menandatanani nilai publik DH mereka (misalnya g^a dan g^b) menggunakan kunci privat. pihak lain dapat memverifikasi tanda tangan tersebut dengan kunci publik. Dengan begitu, penyerang tidak bisa memaslkukan nilai DH karena tidak memiliki kunci privat.
   - Menggunakan sertifikat digital (PKI / SSl). Nillai publik DH dikirim bersama sertifikat digita yang dikeluarkan oleh Certificate Authory (CA). Dengan sertifikat ini, penerima dapat memastikan bahwa nilai kunci benar-benar berasal dari pihak yang saha, bukan dari penyerang.
   - Mengunakan protokol otentikasi (mislnya TLS) Protoko seperti HTTPS/TLS menggunakan Diffie-Hellman yang terintegrasi dengan autentikasi, sehingga pertukaran kunci dari penyadapan dan penyisipan nilai oleh penyerang.
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
