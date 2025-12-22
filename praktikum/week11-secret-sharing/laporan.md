# Laporan Praktikum Kriptografi
Minggu ke-: 11  
Topik: Secret Sharing (Shamir's Secret Sharing)  
Nama: Laeli Maharani 
NIM: 2302020763  
Kelas: 5IKRB 

---

## 1. Tujuan
1. Menjelaskan konsep Shamir Secret Sharing (SSS).
2. Melakukan simulasi pembagian rahasia ke beberapa pihak menggunakan skema SSS.
3. Menganalisis keamanan skema distribusi rahasia.

---

## 2. Dasar Teori
Shamir's Secret Sharing adalah skema kriptografi yang digunakan untuk membagi sebuah rahasia menjadi beberapa bagian (share) sehingga rahasia tersebut tidak dapat diketahui dari satu bagian saja. Rahasia hanya dapat direkontruksi kembali jika jumlah minimum bagian tertentu (treshold) telah digabungkan. Metode ini dirancang untuk meningkatkan keamanan penyimpanan dan distribusi informasi sensitif.

Skema ini bekerja berdasarkan polinomial matematika di atas aritmetika modular. Sebuah rahasia disisipkan sebagai konstanta dalam polinomial berderajat k-1, lalu beberapa titik pada polinomial tersebut dibagikan sebagai share. Selama kurang dari k share dikumpulkan, nilai rahasia tetap tidak dapat ditebak secara matematis.

Shamir's Secret Sharing banyak digunakan pada sistem keamanan modern, seperti manajemen kunci kriptografi, backup kunci privat, dan kontrol akses terdistribusi, karena mampu mencegah satu pihak tunggal memiliki akses penuh terhadap rahasia penting.

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
Langkah 1 -- Implementasi Shamir's Secret Sharing

```python
from secretsharing import SecretSharer

# Rahasia yang ingin dibagi
secret = "KriptografiUPB2025"

# Bagi menjadi 5 shares, ambang batas 3 (minimal 3 shares untuk rekonstruksi)
shares = SecretSharer.split_secret(secret, 3, 5)
print("Shares:", shares)

# Rekonstruksi rahasia dari 3 shares
recovered = SecretSharer.recover_secret(shares[:3])
print("Recovered secret:", recovered)
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
1. Keuntungan utama Shamir's Sharing dibanding membagikan salinan kunci langsung.
   - Tidak ada satu pihak pun yang menyimpan kumci utuh, sehingga lebih aman.
   - Jika satu share bocor atau hilang, rahasia tetap tidak terbuka.
   - Menghindari single poin of failure, karena kunci tidak bergantung pada satu orang atau satu kondisi.

2. Peran treshold (k) dalam keamanan secret sharing
   - Treshold k menentukan jumlah minimum share yang dibutuhkan untuk membuka rahasia.
   - Jika share yang terkumpul kurang dari k, rahasia tidak dapat direkonstruksi.
   - Semakin besar nilai k, semakin tinggi tingkat keamanannya, tetapi semakin sulit proses pemulihan rahasia.

3. Contoh skenario nyata penggunaan Shamir Seccret Sharing
   - Penyimpanan kunci privat cryptocurrency: kunci dibadi ke beberapa pengelola, dan hanya bisa digunakan jika minimal k orang setuju.
   - Sistem manajemen akses perusahaan: kunci utama server hanya dapat dipulihkan jika beberapa administrator bekerja sama.
   - Backup data penting: rahasia dibagi ke beberapa lokai untuk mencegah kehilangan total.

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
