# Laporan Praktikum Kriptografi
Minggu ke-: 12  
Topik: Aplikasi TLS & E-commerce 
Nama: Laeli Maharani  
NIM: 230202763  
Kelas: 5IKRB  

---

## 1. Tujuan
1. Menganalisis penggunaan kriptografi pada email dan SSL/TLS
2. Menjelaskan enkripsi dalam transaksi e-commerce.
3. Mengevaluasi isu etika & privasi dalam penggunaan kriptografi di kehidupan sehari-hari.

---

## 2. Dasar Teori
Transport Layer Security (TLS) adalah protokol keamanan yang digunakan untuk melindungi komunikasi data melalui jaringan publik seperti internet. TLS menyediakan tiga tujuan utama, yaitu kerahasiaa melaui enkripsi, integritas data melalui mekanisme hash dan Message Authentication Code (MAC), serta autentikasi menggunakan sertifikat digital berbasis Publik key infrastrukture. Protokol ini memastikan bahwa data yang dikirim tidak dapat dibaca atau dimodifikasi oleh pihak yang tidak berwenang.

Dalam konteks e-commerce, TLS berperan penting untuk mengamankan transaksi online seperti login pengguna, pertukaran data pribadi, dan pembayaran elektronik. TLS mencegah serangan seperti penyadapan, manipulasi data, dan MITM dengan cara mengenkripsi komunikasi antara browser pelanggan dan server toko online. Keamanan ini ditandai dengan menggunakan HTTPS dan icon gembok pada browser.

Dengan adanya TLS, pengguna dapat bertransaksi secara aman dan percaya bahwa identitas server telah diverifikasi oleh Certificate Authority. Hal ini meningkatkan kepercayaan konsumen, menjaga keamanan data sensitif, dan menjadi komponen wajib dalam sistem e-commerce modern.

---

## 3. Alat dan Bahan
- Python 3.x  
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
