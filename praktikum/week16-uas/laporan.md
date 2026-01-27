# Laporan Praktikum Kriptografi
Minggu ke-: 16  
Topik: UAS KRIPTOGRAFI  
Nama: Laeli Maharani  
NIM: 230202763  
Kelas: 5IKRB  

---

## 1. Tujuan
Tujuan dikembangkannya projek EduToken :
1. Membangun aplikasi edukasi berbasis blockchain yang menyajikan konsep kriptografi secara praktis melalui platfrom pembelajaran berbasis web yang interaktif.
2. Menggabungkan materi ajak dan kuis dengan mekanisme reward berupa token digital untuk meningkatkan keterlibatan pengguna.
3. Memanfaatkan smart contract ERC-20 di jaringan Ethereum Sepolia melalui integrasi MetaMask sebagai basis teknologi utama.
4. Memperagakan protokol keamanan digital, termasuk proses hashing, autentikasi, serta jaminan integritas data dalam setiap transaksi yang dilakukan.


---

## 2. Dasar Teori
Teknologi blockchain hadir sebagai sistem basis data terdistribusi yang menawarkan transparansi, keamanan, dan desentralisasi yang unggul. Di sektor pendidikan, teknologi ini memiliki potensi besar sebagai instrumen pendukung pembelajaran, terutama melalui mekanisme reward berbasis token digital. Pendekatan ini bertujuan untuk menciptakan ekosistem belajar yang lebih dinamis guna meningkatkan motivasi serta partisipasi aktif mahasiswa dalam mengikuti materi perkuliahan.

Di sisi lain, kriptografi merupakan pilar fundamental menjamin keamanan data dan validitas transaksi di dalam blockchain. Prinsip-prinsip seperti hashing, enkripsi, dan tanda tangan digiral menjadi dasar utama yang menjaga integritas sistem tersebut. Namun, pemahaman terhadap kriptografi sering kali menjadi tantangan bagi mahasiswa karena sifatnya yang abstrak dan jarang disajikan dalam bentuk aplikasi praktis yang mudah dipahami.

Sebagai solusi atas tantangan tersebut, platform EduToken dikembangkan untuk mengintegrasikan konsep kriptografi langsung dengan teknologi blockchain Ethereum. Melalui pemanfaatan smart contract ERC-20 yang dibangun dengan bahasa Solidity pada jaringan Sepolia Tesnet, mahasiswa dapat memperoleh pengalaman nyata dalam mengelola transaksi dan protokol keamanan. Sistem ini memungkinkan mahasiswa belajar secara eksperimental melalui pemberian token sebagai imbalan kuis tanpa memerlukan biaya transaksi yang sebenarnya.
---

## 3. Alat dan Bahan
- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Remix IDE
- Akum MetaMask
- Onrender
- Frontend menggunaakn HTML, CSS, JavaScript
- Smart contract menggunakan solidity
- Netword menggunakan Ethereum Sepolia

---

## 4. Langkah Percobaan
1. Login ke website EduToken
![Hasil Eksekusi](screenshots/login.png)
- Login ke website EduToken dengan masuk melalui : https://edutoken-crypto.onrender.com/
- User diminta login dengan memasukkan username dan password.

---
2. Tampilan Dashboard EduToken
![Hasil Eksekusi](screenshots/dashboard.png)
- Setelah user berhasil login akan diarahkan ke menu dashboard Edutoken yang didalamnya menampilkan informasi Saldo Wallet pada EduToken.
- Pada bagian navigasi sidebar, tersedia bebreapa menu utama, yaitu materi dan kuis pembelajaran, informasi token, profile pengguna, dan logout.
   
---
3. Tampilan Menu Materi dan Kuis
![Hasil Eksekusi](screenshots/materi_kuis.png)
- Pada menu materi dan kuis, sistem menyediakan beberapa materi pembelajaran singkat yang terbagi menjadi materi1, materi2, dan materi3. 
- Setelah mempelajari materi yang tersedia, user dapat melanjutkan ke tahap evaluasi dengan menekan tombol mulai kuiz untuk mengerjakan kuis pembelajaran yang telah disediakan oleh sistem.

---
4. Tampilan mengerjakan kuis
![Hasil Eksekusi](screenshots/kuis.png)
- Pada tahap pengerjaan kuis, sistem menampilkan halaman soal yang terdiri dari total 5 pertanyaan.
- Setiap soal memiliki bobot reward sebesar dua token apabila dijawab dengan benar. Dengan demikian, apabila pengguna berhasil menjawab seluruh soal dengan benar, maka pengguna akan memperoleh total 10 token sebagai hasil evaluasi pembelajaran.

---
5. Tampilan Klaim Token
![Hasil Eksekusi](screenshots/klaim_token.png)
- Setelah pengguna menyelesaikan seluruh soal kuis, sistem menampilkan halaman evaluasi yang menunjukkan reward pembelajaran yang diperoleh.
- Pengguna dapat menekan tombol klaim ke wallet untuk memproses pengiriman token EDU ke dompet digital milik pengguna melalui mekanisme transaksi blockchain.

---
6. Tampilan Konfirmasi Klaim
![Hasil Eksekusi](screenshots/konfirmasi_klaim.png)
- Setelah pengguna menekan tombol klaim ke wallet, sistem  secara otomatis akan terhubung dengan dompet digital MetaMask milik pengguna.
- Metamask menampilkan notifikasi konfirmasi transaksi yang berisi detail pengiriman token EDU.
- Pengguna diminta menekan tombol confirm sebagai persetujuan transaksi.
- Setelah konfirmasi diberikan, proses klaim token berhasil dilakukan dan token EDU dikirm ke wallet pengguna melalui jaringan blockchain.

---
7. Tampilan Notifikasi Berhasil Klaim Token
![Hasil Eksekusi](screenshots/klaim_berhasil.png)
- Seelah dikonfirmai sistem akan memberikan notifikasi bahwa token berhasil diklaim dan klik "oke".

---
8. Tampilan Menu Info Token dan Transfer
![Hasil Eksekusi](screenshots/transfer_token.png)


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
