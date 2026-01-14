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
1. Analisis SSL/TLS pada Web (Contoh:Shopee)
Berdasarkan hasil pengamatan pada website https://shopee.co.id menggunakan browser Google Chrome, website Shopee telah menggunakan protokol HTTPS yang ditandai dengan ikon gembok pada addres bar. Hal ini menunjukkan bahwa komunikasi antara pengguna dan server telah diamankan menggunakan SSL/TLS.
Informasi sertifikat digital yang diperoleh adalah sebagai berikut:
- Issuer(Certificate Authority): DigiCert Inc
CA ini berpertan sebagai pihak terpercaya yang memverifikasi identitas server Shopee.
- Masa berlaku sertifikat: Sertifikat periode valid tertentu (misalnya beberap bulan) dan akan diperbarui secara berkala.
- Algoritma kriptografi:
    - Public key : RSA 2048-bit atau ECDSA
    - Enkripsi data : AES (misalnnya AES-128 atau AES-256)
    - Hash : SHA-256
perbandingan HTTPS dan HTTP:
- Website dengan HTTPS menyediakan enkripsi, autentikasi server, dan perlindungan terhadap penyadapan data.
- Website tanpa HTTPS tidak mengenkripsi data sehingga informasi login dan transaksi mudah disadap (rentan terhadap serangan Man-in-the-Middle).

# Langkah 2 -- Studi Kasus E-Commerce (Shopee)

Pada website e-commercce seperti Shopee, enkripsi TLS digunakan untuk menlindungi data sensitif pengguna, terutama saat:
- Login (username dan password)
- Transaksi pembayaran
- Pengiriman data pribadi (alamat, nomor telepon)
TLS bekerja dengan mengamankan koneksi menggunakan enkripsi simetris (AES) setelah proses pertukaran kunci aman menggunakan kriptografi asimetris (RSA/ECDHE). Dengan demikian, data yang dikirmkan tidak dapat dibaca oleh pihak ketifa meskipun berhasil disadap.

JIka TLS tidak digunakan, maka risiko keamanan yang dapat terjadi antara lain:
- Man-in-the-Middle (MITM): Penyerang dapat menyadap atau mengubah data transaksi.
- Pencurian kredensial: username dan password dapat diambil.
- Pemalsuan website : pengguna bisa diarahkan ke situs palsu tanpa disadari.

# Langkah 3 --Analisis Etika & Privasi

Dalam penggunaan email terenkripsi seperti PGP atau S/MIME, terdapat isu privasi penting, yaitu bahwa isi pesan hanya dapat dibaca oleh pengirim dan penerima yang memiliki kunci yang sesuai. Hal ini melindungi kerahasiaan komunikasi pribadi dan profesional.

Dari sisi etika, muncul dilema seperti :
- Apakah perusahaan boleh mendekripsi email karyawan untuk keperluan audit? Hal ini dapat dibenarkan jika ada kebijakan tertulis dan persetujuan karyawan.
- Bagaimana peran pemerintah dalam pengawasan komunikasi terenkripsi? Pemerintah perlu menyeimbangkan antara keamanan nasional dan hak privasi individu agar tidak melanggar kebebasan berkomunikasi.



---

## 5. Source Code


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

1.  Apa perbedaan utama antara HTTP dan HTTPS?
Perbedaan utama antara HTTP dan HTTPS terletak pada aspek keamanannya. HTTP mengirimkan data tanpa enkripsi, sehingga informasi seperti username, password, dan data transaksi dapat dengan mudah disadap oleh pihak ketiga.
Sebaiknya, HTTPS (HTTP Secure) menggunakan SSL/TLS untuk mengenkripsi komunikasi antara klien dan server. Dengan HTTPS, data yang dikirimkan menjadi lebih aman, terlindungi dari penyadapan, serta menjamin keaslian server yang diakses pengguna.

2 Mengapa sertifikat digital menjadi penting dalam komunikasi TLS?

Sertifikat digital berfungsi sebagai bukti identitas server dalam komuniasi TLS. Sertifikat ini diterbitkan oleh Certificate Authority (CA) yang terpercaya dan berisi informasi tentang pemiliki website serta kunci publiknya.
Dengan adanya sertifikat digital:
- Pengguna dapat memastikan bahwa mereka terhubung ke server yang benar.
- Risiko serangan Man-in-the-Middle dapat dikurangi.
- Proses pertukaran kuni enkripsi dapat dilakukan secara aman.
Tanpa sertifikat digital, tidak ada jaminan bahwa server yang diakses adalah server asli.

Bagaimana kriptografi mendukung privasi dalam komunikasi digital, tetapi sekaligus menimbulkan tantangan hukum dan etika?

Kriptogradi mendukung privasi dengan cara mengenkripsi data, sehingga hanya pihak yang berwenang yang dapat membaca isi komunikasi. Hal ini melindungi informasi pribadi, rahasia bisnis, dan komunikasi sensitif dari penyadapan atau penyalahgunaan.
Namun, kriptografi juga menimbulkan tantangan hukum dan etikal, karena:
- Penegak hukum dapat kesulitan mengakses data terenkripsi dalam kasus kejahatan.
- Muncul dilema antara hak privasi individu dan kepentingan keamanan negara.
- Potensi penyalahgunaan enkripsi oleh pihak yang berniat jahat.
Oleh karena itu, diperlukan kebijakan dan regulasi yang seimbang agar kriptogradi dapat melindungi tanpa mengabaikan aspek hukum dan etika.


---

## 8. Kesimpulan
Berdasarkan praktikum analisi SSL/TLS pada website e-commerce Shopee, dapat disimulkan bahwa penggunaan protokol HTTPS dan TLS berperan penting dalam menjaga keamanan data antara pengguna dan server, karena sertifikat digital memungkinkan verifikasi identitas server dan enkripsi melindungi informasi sensitif seperti data login dan transaksi dari penyadapan atau serangan Man-in-the-Middle, sehingga integritas, kerahasiaan, dan kepercayaan pengguna dalam transaksi online dapat terjaga dengan baik.

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
