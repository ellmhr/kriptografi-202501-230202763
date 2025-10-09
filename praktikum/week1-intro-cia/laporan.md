# Laporan Praktikum Kriptografi 
Minggu ke-: 1
Topik: 01 Sejarah Kriptografi dan Prinsip CIA
Nama: Laeli Maharani
NIM: 230202763
Kelas: 5IKRB

---

# 1. Tujuan
- Menjelaskan sejarah dan evolusi kriptografi dari masa klasik hingga modern.  
- Menyebutkan prinsip Confidentiality, Integrity, Availability (CIA) dengan benar.  
- Menyimpulkan peran kriptografi dalam sistem keamanan informasi modern.  
- Menyiapkan repositori GitHub sebagai media kerja praktikum. 
---

# 2. Dasar Teori
Kriptografi klasik adalah metode penyandian informasi yang telah digunakan sejak zaman kuno. Dua contoh terkenal dari era ini adalah Caesar Cipher dan Vigenère Cipher. 
1. Caesar Cipher: Metode ini dinamai setelah Julius Caesar, yang menggunakan teknik ini untuk mengamankan pesan-pesannya. Dalam Caesar Chiper, setiap huruf dalam pesan digeser sebanyak n posisi di dalam alfabet. Misalnya, dengan n=3, huruf A akan menjadi D, B menjadi E, dan seterusnya. Meskipun sederhana, metode ini mudah diteba dan tidak aman untuk digunakan dalam konteks modern.
2. Vigenère Cipher: Menggunakan kunci yang lebih kompleks, Vigenère Cipher menggabungkan beberapa Caesar Cipher dengan kunci yang diulang. Setiap huruf dalam kunci menentukan berapa banyak posisi yang harus digeser untuk huruf yang bersangkutan. Meskipun lebih aman dibandingkan Caesar Cipher, metode ini masih rentan terhadap analisis frekuensi.

# Perkembangan Kriptografi Modern
Dengan berkembangnya teknologi dan kebutuhan akan keamanan yang lebih tinggi, kriptografi modern muncul dengan algoritma yang lebih canggih. Dua contoh utama adalah AES (Advanced Encryption Standard) dan RSA (Rivest-Shamir-Adleman).
1. AES: Merupakan algoritma simetris yang digunakan secara luas untuk enkripsi data. AES menggunakan kunci dengan panjang 128, 192, atau 256 bit dan dikenal karena keamanannya yang tinggi serta efisiensi dalam pemrosesan. AES telah diadopsi secara luas sebagai standar enkripsi oleh pemerintah dan organisasi di seluruh dunia.
2. RSA: Merupakan algoritma kriptografi kunci publik yang menggunakan dua bilangan prima besar untuk menghasilkan sepasang kunci (publik dan pribadi). RSA memungkinkan pengiriman pesan yang aman dan otentikasi digital, menjadikannya sangat penting dalam komunikasi aman dan transaksi online.
Contoh: definisi cipher klasik, konsep modular aritmetika, dll.  )

# Evolusi Menuju Kriptografi Kontemporer
Kriptografi kontemporer mengalami revolusi dengan munculnya teknologi baru seperti blockchain dan cryptocurrency.
1. Blockchain: Teknologi ini menggunakan prinsip kriptografi untuk menciptakan buku besar yang aman dan transparan. Setiap blok dalam rantai berisi informasi yang dienkripsi, dan setiap blok baru terkait dengan blok sebelumnya. Ini menjadikan blockchain sangat aman dan tahan terhadap manipulasi data.
2. Cryptocurrency: Mata uang digital seperti Bitcoin dan Ethereum menggunakan kriptografi untuk mengamankan transaksi dan mengontrol penciptaan unit baru. Cryptocurrency menawarkan cara baru untuk melakukan transaksi tanpa perantara, memberikan privasi dan keamanan yang lebih besar bagi pengguna.
---

## 3. Alat dan Bahan
- Visual Studio Code
- Chrome  
- Git dan akun GitHub  
- Terminal (CMD)

---

## 4. Langkah Percobaan
1. Melakukan fork repository kriptografi
2. Melakukan clone reository ke komputer lokal
3. Membuat folder praktikum/week1-intro-cia/ berisi laporan.md dan folder screenshots.
4. Menulis ringkasan materi singkat.
5. Menjawab quiz.

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
1. Tokoh yang sering dianggap sebagai bapak kriptografi modern adalah Whitfield Diffie. Bersama dengan Martin Hellman, Diffie memperkenalkan konsep kriptografi kunci publik pada tahun 1976. Inovasi ini memungkinkan dua pihak untuk berkomunikasi secara aman tanpa perlu bertukar kunci rahasia sebelumnya, yang merupakan langkah revolusioner dalam bidang keamanan informasi.
2. Beberapa algoritma kunci publik yang populer digunakan saat ini antara lain RSA (Rivest-Shamir-Adleman), DSA (Digital Signature Algorithm), dan ECC (Elliptic Curve Cryptography). RSA adalah salah satu yang paling banyak digunakan untuk enkripsi dan tanda tangan digital. DSA, yang dikembangkan khusus untuk tanda tangan digital, juga banyak digunakan dalam protokol keamanan. ECC semakin populer karena menawarkan tingkat keamanan yang tinggi dengan ukuran kunci yang lebih kecil, menjadikannya efisien dalam penggunaan sumber daya.
3. Perbedaan Utama antara Kriptografi Klasik dan Modern
Kriptografi klasik, seperti Caesar Cipher dan Vigenère Cipher, bergantung pada teknik penyandian yang relatif sederhana dan menggunakan satu kunci untuk enkripsi dan dekripsi (algoritma simetris). Metode ini sering kali rentan menangani kebutuhan keamanan yang kompleks di era digital. Sebaliknya, kriptografi modern menggunakan algoritma yang lebih canggih, seperti AES dsip matematis yang kompleks untuk memberikan tingkat keamanan yang jauh lebih tinggi. Kriptografi modern juga mengenalkan konsep kunci publik dan pribadi, memungkinkan komunikasi yang aman tanpa memerlukan pertukan kunci rahasia sebelumnya, menjadikannya lebih fleksibel dan aman.
---

## 8. Kesimpulan
kriptografi telah berkembang dari teknik klasik yang sederhana, seperti yang diperkenalkan oleh tokoh-tokoh seperti Julius Caesar, menjadi sistem modern yang kompleks berkat kontribusi inovatif dari individu seperti Whitfield Diffie. Algoritma kunci publik yang populer, termasuk RSA, DSA, dan ECC, menawarkan solusi keamanan yang lebih canggih dibandingkan metode tradisional yang rentan. Dengan pemisahan antara kunci publik dan pribadi, kriptografi modern memberikan fleksibilitas dan keamanan yang lebih tinggi, menjadikannya esensial dalam melindungi data di era digital saat ini.

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log

commit week1-intro-cia
Author: Laeli Maharani <laelimaharani09@gmail.com>
Date:   2025-10-07

    week1-intro-cia: Ringkasan sejarah kriptografi, prinsip CIA, jawaban quiz dan dokumentasi screenshoot.

