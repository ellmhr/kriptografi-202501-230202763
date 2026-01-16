# Laporan Praktikum Kriptografi
Minggu ke-: 13  
Topik: TinyChain - Proof or Work  
Nama: Laeli Maharani  
NIM: 230202763  
Kelas: 5IKRB  

---

## 1. Tujuan
1. Menjelaskan peran hash function dalam blockchain.
2. Melakukan simulasi sederhana Proof of Work (PoW).
3. Menganalisis keamanan cryptocurrency berbasis kriptografi.

---

## 2. Dasar Teori
Proof of Work (PoW) merupakan salah satu mekanisme konsensus dalam teknologi blockchain yang digunakan untuk memastikan keabsahan transaksi dan menjaga keamanan jariangan terdistribusi. Dalam PoW, setiap node (miner) harus menyelesaikan sebuah permasalahan kriptografi yang bersifat komputasi intensif sebelum dapat menambahkan blok baru ke dalam blockchain. Permasalahan ini umumnya berupa pencarian nilai nonce sehingga hasil fungsi hash (misalnya SHA-256) memenuhi tingkat kesulitan tertentu, seperti memiliki sejumlah angka nol di awal hash.

TinyChain adalah implementasi blockchain sederhana yang digunakan untuk tujuan pembelajaran. TiniChain memanfaatkan konsep Proof of Work untuk memperkenalkan cara kerja dasar blockchain, seperti pembentukan block, perhitungan hash, dan proses penambangan (minimg). Dengan PoW, TinyChain menunjukkan bagaimana usaha komputasi diperlukan untuk menghasilkan block yang valid, sehingga mencegah manipulasi data dan serangan seperti pemalsuan transaksi atau perubahan isi blok.

Melalui mekanisme PoW, TinyChain mampu menjaga integritas data dan kepercayaan antar node tanpa memerlukan orotitas terpusat. Jika ada pihak yang ingin mengubah data satu blok, maka ia harus mengulang proses PoW untuk blok tersebut dan seluruh blok setelahnyam yang secara komputas sangat mahal. Oleh karena itu, PoW pada TiniChain berberan penting dalam menunjukkan bagaimana blockchain dapat bersifat aman, transparan, dan tahan terhadap manipulasi.

---

## 3. Alat dan Bahan
- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
1. Membuat file `tinychain.py` di folder `praktikum/week13-tinychain/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python caesar_cipher.py`.)
4. Melakukan analisis hasil eksekusi program.
   
---

## 5. Source Code
Langkah 1 -- Membuat struktur BLok
```python
import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, data, timestamp=None):
        self.index = index
        self.timestamp = timestamp or time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(self.nonce)
        return hashlib.sha256(value.encode()).hexdigest()

    def mine_block(self, difficulty):
        while self.hash[:difficulty] != "0" * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print(f"Block mined: {self.hash}")
```
Langkah 2 -- Membuat Blockchain
```python
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4

    def create_genesis_block(self):
        return Block(0, "0", "Genesis Block")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

# Uji coba blockchain
my_chain = Blockchain()
print("Mining block 1...")
my_chain.add_block(Block(1, "", "Transaksi A → B: 10 Coin"))

print("Mining block 2...")
my_chain.add_block(Block(2, "", "Transaksi B → C: 5 Coin"))
```
Langkah 3 -- Analisis Proof of Work
- Perhatikan bahsa proses mining membutuhkan waktu (bergantung pada `difficulty`)
Beerdasarkan hasil eksekusi program, terlihat bahwa setiap blok harus melalui proses mining sebelum berhasil ditambahkan ke dalam blockchain. Proses mining dilakukan dengan mencari nilai `nonce` yang menghasilkan hash dengan awalan nol sebanyak nilai `difficulty` yang ditentukan. Pada program ini, tingkat kesulitan ditetapkan sebesar 4, sehingga hash yang valid harus diawali dengan empat karakter `0`, seperti yang terlihat pada hasil :
```
0000f5ac9fe4d62d...
0000ca088be99dc1...
```
- Analisis: semakin tinggi difficulty, semakin lama proses mining.
Proses pencarian hash yang memnuhi syarat tersebut dilakukan secara berulang (trial and error), sehingga membutuhkan waktu komputasi. Semakin tinggi nilai `difficulty`, semakin banyak percobaan yang harus dilakukan untuk menemukan hash yang valid. Hal ini menyebabkan waktu mining menjadi lebih lama dan membutuhkan sumber daya komputasi yang lebih besar.
- Diskusikan bagaimana hal ini menjamin keamanan blockchain.
Mekanisme ini menjamin keamanan blockchain karena membuat pemalsuan data menjadi sulit. Jika seseorang ingin merubah isi satu blok, maka nilai hash blok tersebut akan berubah dan tidak lagi memenuhi syarat difficulty. Akibatnya penyerang harus melakukan proses mining ulang tidak hanya pada blok tersebut, tetapi juga pada seluruh blok setelahnya. Dengan difficulty yang tinggi dan banyaknya blok, usaha ini menjadi sangat mahal secara komputasi dan waktu, sehingga blockchain tetap aman dari manupulasi data.
  
---

## 6. Hasil dan Pembahasan
Hasil eksekusi program TinyChain : 
![Hasil Eksekusi](screenshots/hasil_tinychain.png)
Pada saat program dijalankan, sistem memulai proses dengan membuat sebuah genesis blok sebagai blok pertama dalam blockchain. Setelah itu, program melakukan proses mining untuk Block 1 yang berisi data transaksi "Transaksi A -> B: 10 Coin". Proses mining berjalan hingga ditemukan nilai hash yang memenuhi tingkat kesulitan (difficulty) yang ditentukan, yaitu hash dengan empat angka nol di dibagian awal. Setelah hash yang valid ditemukan, block berhasil ditambang dan ditambahkan ke dalam blockchain.

Selanjutnya, program melakukan proses mining untuk Block 2 yang berisi data transaksi "Transaksi B -> C: 5 Coin", Proses yang sama kembali dilakukan, di mana sistem menyesuaikan nilai `nonce` hingga menghasilkan hash sesuai dengan tingkat kesulitan. Setelah hash yang valid diperoleh, program menampilkan hasil mining dan blok kedua berhasil ditambahkan ke blockchain. Hasil eksekusi menunjukkan bahwa setiap blok memiliki hash yang unik dan memnuhi syarat PoW sebelum disimpan dalam rantai blockchain.

---

## 7. Jawaban Pertanyaan
1. Mengapa fungsi hash sangat penting dalam blockchain?
Fungsi hash sangat penting dalam blockchain karena berperan sebagai penjaga integritas data. Setiap blok ci blockchain memiliki nilai hash yang dihasilkan dari seluruh isi blok tersebut, termasuk data transaksi dan hash blok sebelumnya. Jika ada satu bit data saja yang diubah, maka nilai hash akan berubah seccara drastis. Hal ini membuat manupulasi data dapat langusng terdeteksi. Selain itu, fungsi hash besifat satu arah (one-way), sehingga data asli tidak dapat dikembalikan dari nilai hash, yang mendukung aspek keamanan dan keandalan blockchain.

2. Bagaimana Proof of Work mencegah double spending?
Proof of Work mencegah double spending dengan mewajibkan setiap transaksi untuk divalidasi dan dimasukkan ke dalam blok yang telah melewati proses komputasi berat. Ketika sebuah transaksi sudah tercatat dalam blockchain dan blok tersebut telah dikonfirmasi oleh jaringan, maka transaksi tersebut tidak dapat digunakan kembali. Untuk memaslkusan transaksi atau menggandakan pengeluaran, penyerang hasrus menghitung ulang PoW pada blcok tersebut dan seluruh blok setelahnya, yang secara komputas sangat mahal dan hanpir tidak mungkin dilakukan jika jaringan mayoritas bersifat jujur.

3. Apa kelemahan dari Proof of Work dalam hal efisiensi energi?
Kelemahan utama PoW adalah konsumsi energi yang sangat tinggi. Proses penambangan membutuhkan bahnya daya komputasi untuk mencoba berbagai nilai nonce sehingga menemukan hash yagn valid. Sebagian besar usaha komputasi ini tidak menghasilkan nilai guna lain selain validasi blok, sehingga dianggap boros energi. Dalam skala besar seperti Bitcoin, hal ini berdampak pada biaya operasional tinggi dan isu lingkungan, sehingga mendorong pengembangan mekanisme konsensus alternatif yang lebih hemat energi. 


---

## 8. Kesimpulan
Berdasarkan hasil praktikum, dapat simimpulkan bahwa mekanisme Proof of Work bekerja dengan cara mencari nilai hash yang memenui tingkat kesulitasn tertentu sebelum sebuah blok dapat ditambahkan ke dalam blockchain. Proses mining ditunjukan pada program berhasil menghasilkan hash valid melalui penyesuaian nilai nonce. Hal ini membuktikan bahwa PoW berperan penting dalam menjagga keabsahan dan keamanan data pada sistem blockchain.

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log

```
commit week13_tinychain_pow
Author: Laeli Maharani <laelimaharani09@gmail.com>
Date:   2025-01-16

    week13-tinychain-pow: implementasi tinychain dan laporan )
```
