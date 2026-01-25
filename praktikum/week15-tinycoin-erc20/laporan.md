# Laporan Praktikum Kriptografi
Minggu ke-: 15  
Topik: TinyCoin ERC20  
Nama: laeli Maharani  
NIM: 2300202763  
Kelas: 5IKRB  

---

## 1. Tujuan
1. Mengembangkan proyek sederhana berbasis algoritma kriptografi.
2. Mendokumentasikan proses implementasi proyek ke dalam repository Git.
3. Menyusun laporan teknis hasil proyek akhir.

---

## 2. Dasar Teori
TinyCOin ERC20 adalah contoh implementasi token digital berbasis standar ERC-20 yang berjalan di atas blockchain Ethereum. ERC-20 merupakan standar teknis yang mendefinisikan seperangkat fungsi dan aturan dasar agar sebuah token dapat dikenali, ditransfer, dan digunakan secara konsisten oleh wallet, smart contract, dan aplikasi terdesentralisasi (DApp). FUngsi utama dalam ERC-20 meliputi totalSupply, balance0f, transferm approve, dan transferFrom.

Dalam konteks TinyCoin, token ERC-20 digunakan untuk mensimulasikan aset digital yang dapat dipindahkan antar pengguna tanpa perantara. Setiap transaksi diatat secara transparan di blockchain, sehingga menjamin integritas data, keandalan, dan non-repudiation. Smart contract ERC-20 juga memungkinkan otomatisasi aturan, seperti pembatasan suplai token atau mekanisme persetujuan sebelum transfer.

Secara teori, penggunaan standar ERC-20 pada TinyCoin memudahkan interperobabilitas dan pengembangan sistem berbasis blockchain. Karena mengikuti standar yang sama, TInyCoin dapat dengan mudah diintegrasikan ke berbagai wallet, exchange, dan aplikasi DeFi, sekaligus menjadi media pembelajaran untuk memahami konsep tokenisasi, smart contract, dan ekonomi digital berbasis blockchain.

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
Kontrak ERC-20
```python
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract TinyCoin is ERC20 {
    constructor(uint256 initialSupply) ERC20("TinyCoin", "TNC") {
        _mint(msg.sender, initialSupply);
    }
}

```

---

## 6. Hasil dan Pembahasan


Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan
1. Apa fungsi utama ERC-20 dalam ekosistem blockchain?
Fungsi utama ERC-20 adalah sebagai standar token di blockchain Ethereum agar semua token memiliki aturan dan fungsi yang sama. Dengan adanya standar ini, token dapat:
- Digunakan dan dikenali oleh wallet, exchange, dan DApp tanpa penyesuaian khusus.
- Mempermudah pertukaran token karena format dan cara kerjanya seragam.
- Mendukung pengembagnan ekosistem DeFi, NFT marketplace (sebagai alat bayar), dan sistem ekonomi digital lainnya.
- ERC-20 membuat token kompatibel, interoperable, dan mudah diintegrasikan dalam ekosistem blockchain Ethereum.

2. Bagaimana mekanisme transfer token bekerja dalam kontrak ERC-20?
Mekanisme transfer token ERC-20 bekerja melalui fungsi utama berikut:
- `transfer(to, amount)` Digunakan untuk megnirim token langsung dari pemilik ke alamat lain. Saldo pengirim berkurang dan saldo penerima bertambah.
- `approve(spender, amount)` Pemilik token memberi izin kepada pihak lain (misalnya smart contract) untuk menggunakan tokennya sampai jumlah tertentu.
- `transferForm(form, to, amount)` Digunakan oleh pihak yang sudah diberi izin untuk memindahkan token atas nama pemilik.
Setiap transfer akan :
- Dicek apakah saldo mencukupi.
- Dicatati di blockchain secara permanen.
- Memicu event `Transfer` agar dapat dilacak oleh sistem lain.

3. Apa risiko utama dalam implementasi smart contract dan bagaimana cara mitigasinya?
Risiko utama dalam smart contract ERC-20 antara lain:
- Bug atau kesalahan logika kode. Contoh kesalahan perhitungan saldo atau akses tanpa izin.
- Kerentanan keamanan, Seperti reentrancy attack, integer overflow/underflow, atau salah penggunaan `approve`.
- Kontrak tidak bisa diubah (immutable), jika sudah ter-deploy dan ada bug, perbaikannya sangat sulit.
Cara mitigasi risiko:
- Melakukan audit kode sebelum deployment.
- Menggunakan library terpercaya seperti OpenZeppelin.
- Menerapkan testing menyeluruh (unit test dan simulasi test).
- Membatasi fitur sensitif dan menggunakan best practice Solidity.

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
