# Laporan Praktikum Kriptografi
Minggu ke-: 14  
Topik: Analisis Serangan Kriptografi  
Nama: Laeli Maharani  
NIM: 230202763  
Kelas: 5IKRB  

---

## 1. Tujuan
1. Mengidentifikasi jenis serangan pada sistem informasi nyata.
2. Mengevaluasi kelemahan algoritma kriptografi yang digunakan.
3. Memberikan rekomendasi algoritma kriptografi yang sesuai untuk perbaikan keamanan.

---

## 2. Dasar Teori
Analisis serangan kriptografi adalah proses mempelajari cara penyerang mencoba melemahkan atau memecahkan sistem kriptografi. Tujuannya untuk menilai seberapa aman algoritma dalam melindungi data. Analisis ini membantu menemukan kelemahan sebelum sistem digunakan secara luas.

Jenis serangan kriptografi dibedakan berdasarkan informasi yang dimiliki penyerang, seperti chipertext-only attack dan known-palintext attack. Ada juga serangan brute force yang mencoba semua kemungkinan kunci. Selain itu, serangan modern dapat memanfaatkan kelemahan implementasi sistem.

Analisis serangan kriptografi penting untuk memastkan keamanan informasi digital. Hasil analisis digunakan untuk memilih algoritma dan ukuran kunci yang kuat. Dengan demikian, sistem kriptogradi dapat melindungi data secara lebih aman dan andal.

---

## 3. Alat dan Bahan
- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan

1. Identifikasi serangan dengan memilih salah satu kasus myata serangan kriptografi.
2. Evaluasi kelemahan dengan menganalisis kelemahan algoritma yang digunakan. 
3. Rekomendasi Solusi dengan mengusulkan algoritma yang lebih aman.
4. Melakukan percobaan brute force sederhana. 

---

## 5. Source Code

---

## 6. Hasil dan Pembahasan
Langkah 1 -- Identifikasi Serangan 
Kasus nyata : 
Contoh serangan kriptografi yang pernah terjadi adalah serangan Man-in-the-Middle (MITM) pada komunikasi SSL/TLS akibat Certificate Authority (CA) palsu. Salah satu kasus terkenal adalah insiden DigiNotar (2011), di mana sertifikat palsu diterbitkqan untuk domain terkenal.

Vektor serangan 
- Penyerang berhasil mendapatkan atau membuat sertifikat digital palsu.
- Sertifikat tersebut digunakan untuk menyamar sebagai website asli.
- Pengguna yang terhubung ke jaringan tidak aman (misalnya Wi-Fi buplik) diarahkan ke server palsu tanpa disadari).

Penyebab kelemahan :
- Kepercayaan penuh terhadap CA yang ternyata dikompromikan.
- Browser masih menganggap sertifikat tersebut valid.
- Pengguna tidak menyadari adanya pemalsuan identitas server.

Langkah 2 -- Evaluasi Kelemahan
Analisis Algoritma
- Algoritma Kriptografi (RSA, AES) sebenarnya masih kuat.
- Masalah utama bukan pada algoritma, tetapi pada kepercayaan (trust mode)PKI.
- Jika CA bocor maka seluruh sistem kepercayaan TLS ikut terancam.

Sumber Kelemahan 
- Implementasi dan manajemen CA yang tidak aman.
- Tidak adanya mekanisme deteksi cepat terhadap sertifikat palsu.
- Pengguna mengabaikan peringatan keamanan browser.

Langkah 3 -- Rekomendasi Solusi
Solusi yang disarankan
- Menggunakan Certificate Transparency (CT) untuk memantau sertifikat yang diterbitkan.
- Menerapkan HTTP Strict Transport Security (HSTS).
- Menggunakan OCSP Stapling untuk verifikasi status sertifikat.
- Edukasi pengguna agar tidak mengabaikan peringatan sertifikat.

Alasan Pemilihan Solusi
- Certificate Transparency memungkinkan deteksi sertifikat ilegal.
- HST mencegah downgrade ke HTTP.
- OSCP memastikan sertifikat tidak dicabut.

Dampak terhadap keamanan 
- Risiko MITM dapat ditekan secara signifikan.
- Identitas server lebih terjamin.
- Kepercayaan pengguna terhadap komunikasi TLS meningkat.

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
