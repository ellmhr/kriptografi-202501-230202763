# Laporan Praktikum Kriptografi
Minggu ke-: 9 
Topik: Digital Signature (RSA/DSA)  
Nama: laeli Maharani  
NIM: 230202763  
Kelas: 5IKRB  

---

## 1. Tujuan
1. Mengimplemntasikan tanda tangan digital menggunakan algoritma RSA/DSA.
2. Memverifikasi keaslian tanda tangan digital.
3. Menjelsakan manfaat tanda tangan digital dalam otentikasi pesan dan itegritas data.

---

## 2. Dasar Teori
Digital SIgnature atau tanda tangan digital adalah mekanisme kriptografi yang digunakan untuk memastikan keaslian, integritas dan non-repudiation dari sebuah pesan atau dokumen elektronik. Berbeda dari enkripsi yang bertujuan merahasiakan data, tanda tangan digital fokus pada pembuktian bahwa suatu pesan benar-benar dikirim oleh pihak yang saha dan tidak mengalami perubahan selama proses transmisi. Mekanisme ini selalu menggunakan fungsi hash untuk menghasilkan representasi unik dari pesan sebelum ditandatangani.

Pada RSA Digital SIgnature, prosesnya dilakukan dengan "membalik" mekanisme enkripsi RSA. Pengirim membuat signature dengan cara mengenkripsi hash pesan menggunakan privarte key, lalu penerima memverifikasinya menggunakan private key, lalu penerima memverifikasinya menggunakan public key. Jika hasil verifikasi sesuai dengan hash pesan, maka penerima dapat memastikan bahwa pesan tersebut asli dan tidak dimodifikasi. Keamanan RSA Signature terletak pada kesulitan memfaktorkan bilangan besar, sehingga dapat sangat sulit dipalsukan tanpa private key.

Sedangkan DSA (Digital Signature Algorithm) bekerja berdasarkan Discrete Logarithm Problem dan menghasilkan tanda tangan berupa pasangan nilai (r,s) yang dihitung menggunakan private key dan nilai acak k. Penerima kemudian memverifikasi signature menggunakan public key dan formula DSA. Baik RSA maupun DSA memberikan jaminan kuat terhadap integritas dan autentikasi pesan, menjadikan digital signature sebagai fondasi penting dalam keamanan modern, seperti pada SSL/TLS, e-commerce, dan distribusi perangkat lunak.

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
