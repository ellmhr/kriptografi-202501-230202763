# Laporan Praktikum Kriptografi
Minggu ke-: 5  
Topik: Chiper Kasik (Caesar, Vigenere, Transposisi)  
Nama: Laeli Maharani  
NIM: 230202763  
Kelas: 5IKRB  

---

## 1. Tujuan
1. Menerapkan algoritma Caeshar Chiper untuk enkripsi dan dekripsi teks.
2. Menerapkan algoritma Vigenere Chiper dengan variasi kunci.
3. Mengimplementasikan algoritma transposisi sederhana
4. Menjelaskan kelemahan algoritma kriptografi klasik.

---

## 2. Dasar Teori
Chiper klasik adalah metode kriptografi awal yang digunakan untuk menyembunyikan pesan dengan cara sederhana, sebelum munculnya algoritma modern. Ada tiga jenis chiper kasik yang paling dikena, yaitu Caesar Chiper, Vigenere Chiper, dan Transposisi Chiper.
- Caesar Chiper bekerja dengan menggeser setiap huruf dalam teks asli sejumlah posisi tertentu dalam alfabet. Misalnya, dengan pergeseran 3, huruf A menjadi D, B menjadi E, dan seterusnya. Chiper ini mudah diimplementasikan namun sangat lemah karena hanya memiliki sedikit kemungkinan kunci (26 kemungkinan).
- Vigenere Chiper merupakan pengembangan dari Caesar Chiper yang menggunakan kunci berupa kata. Setiap huruf kunci menentukan pergeseran berbeda pada huruf pesan. Metode ini lebih kuat dibanding Caesar karena variasi pergeseran lebih banyak, meski tetap dapat dipecahkan dengan analisis frekuensi huruf jika kuncinya pendek.
- Transposisi Cipher tidak mengubah huruf, tetapi mengubah urutan posisi huruf dalam pesan berdasarkan pola tertentu (misalnya kolom atau baris). Chiper bergantung pada aturan pengurutan, bukan pada penggantian karakter.
  
Secara umum, ciper klasik berperan penting dalam sejarah kriptografi karena menjadi dasar bagi perkembangan sistem enkripsi modern, meskipun tingkat keamanannya sudah tidak memadai untuk penggunaan saat ini.

---

## 3. Alat dan Bahan
- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  

---

## 4. Langkah Percobaan
1. Membuat file `caesar.py` di folder `praktikum/week5-cipher-klasik/src/`.
2. Membuat file `vigenere.py` di folder `praktikum/week5-cipher-klasik/src/`.
3. Membuat file `transpose.py` di folder `praktikum/week5-cipher-klasik/src/`.
4. Membuat folder `screenshots` di folder `praktikum/week5-cipher-klasik/src/`.
5. Menyalin kode program dari panduan praktikum.
6. Menjalankan program dengan perintah sesuai nama file.

---

## 5. Source Code
Langkah 1 -- implementasi Caesar Chiper
```
def caesar_encrypt(plaintext, key):
    result = ""
    for char in plaintext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result

def caesar_decrypt(ciphertext, key):
    return caesar_encrypt(ciphertext, -key)

# Contoh uji
msg = "CLASSIC CIPHER"
key = 3
enc = caesar_encrypt(msg, key)
dec = caesar_decrypt(enc, key)
print("Plaintext :", msg)
print("Ciphertext:", enc)
print("Decrypted :", dec)
```
Hasil :
```
Plaintext : CLASSIC CIPHER
Ciphertext: FODVVLF FLSKHU
Decrypted : CLASSIC CIPHER
```
Langkah 2 -- Implementasi Vigerere Cipher
```
def vigenere_encrypt(plaintext, key):
    result = []
    key = key.lower()
    key_index = 0
    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 97
            base = 65 if char.isupper() else 97
            result.append(chr((ord(char) - base + shift) % 26 + base))
            key_index += 1
        else:
            result.append(char)
    return "".join(result)

def vigenere_decrypt(ciphertext, key):
    result = []
    key = key.lower()
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 97
            base = 65 if char.isupper() else 97
            result.append(chr((ord(char) - base - shift) % 26 + base))
            key_index += 1
        else:
            result.append(char)
    return "".join(result)

# Contoh uji
msg = "KRIPTOGRAFI"
key = "KEY"
enc = vigenere_encrypt(msg, key)
dec = vigenere_decrypt(enc, key)
print("Plaintext :", msg)
print("Ciphertext:", enc)
print("Decrypted :", dec)
```
Hasil :
```
Plaintext : KRIPTOGRAFI
Ciphertext: UVGZXMQVYPM
Decrypted : KRIPTOGRAFI
```
Langkah 3 -- Implementasi Transposisi Sederhana
```
def transpose_encrypt(plaintext, key=5):
    ciphertext = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(plaintext):
            ciphertext[col] += plaintext[pointer]
            pointer += key
    return ''.join(ciphertext)

def transpose_decrypt(ciphertext, key=5):
    num_of_cols = int(len(ciphertext) / key + 0.9999)
    num_of_rows = key
    num_of_shaded_boxes = (num_of_cols * num_of_rows) - len(ciphertext)
    plaintext = [''] * num_of_cols
    col = 0
    row = 0
    for symbol in ciphertext:
        plaintext[col] += symbol
        col += 1
        if (col == num_of_cols) or (col == num_of_cols - 1 and row >= num_of_rows - num_of_shaded_boxes):
            col = 0
            row += 1
    return ''.join(plaintext)

# Contoh uji
msg = "TRANSPOSITIONCIPHER"
enc = transpose_encrypt(msg, key=5)
dec = transpose_decrypt(enc, key=5)
print("Plaintext :", msg)
print("Ciphertext:", enc)
print("Decrypted :", dec)
```
Hasil :
```
Plaintext : TRANSPOSITIONCIPHER
Ciphertext: TPIPROOHASNENICRSTI
Decrypted : TRANSPOSITIONCIPHER
```
---

## 6. Hasil dan Pembahasan
Hasil eksekusi langkah (1) Implementasi Caesar Cipher:
![Hasil Eksekusi](screenshots/1-caesar.png)
Caesar Cipher adalah metode enkripsi klasik yang bekerja dengan cara menggeser setiap huruf dalam teks asli sebanyak nilai kunci tertentu. Jika pergeseran melewati huruf Z, maka akan kembali ke A (menggunakan operasi mod 26).

Pada kode di atas, fungsi caesar_encrypt membaca setiap huruf, mengubahnya ke kode ASCII, kemudian menghitung posisi barunya dengan rumus (ord(char) -shift + key) % 26 + shif. Fungsi caesar_decrypt melakukan hal yang sama namun dengan kunci negatif untuk mengembalikan teks ke bentuk semula.

Contoh perhitungan : huruf C dengan key = 3 menjadi F, karena C (posisi ke-2) digeser tiga langkah ke kanan (D, E, F). Dengan plaintext "CLASSIC CIPHER" dan key = 3, hasil enkripsi adalah "FODVVLF FLSKHU". Setelah didekripsi dengan kunci yang sama, teks kembali menjadi "CLASSIC CIPHER".

Kesimpulannya, Caesar Cipher menyandikan pesan dengan pergeseran huruf secara tetap, dan mudah dipecahkan jika kuncinya kecil atau pola gesernya diketahui.

Hasil eksekusi langkah (2) Implementasi Vigenere Cipher
![Hasil Ekesekusi](screenshots/2-vigenere.png)
Vigenere Cipher adalah metode enkripsi klasik yang menggunakan kata kunci (key) untuk menentukan jumlah pergeseran setiap huruf pada plaintext. Tidak seperti Caesar Cipher yang menggunakan satu angka kunci tetap, setiap huruf pada key menentukan pergeseran berbeda, sehingga hasil enkripsi lebih sulit ditebak.

Pada kode di atas, setiap huruf pada key diubah menjadi nilai pergeseran dengan rumus shift =ord(key[i]) - 97, di mana a=0, b=1, dan seterusnya. Huruf pada plaintext kemudian digeser sesuai nilai shift tersebut menggunakan operasi (ord(char) - base + shift) % 26 + base. Proses dekripsi dilakukan dengan menggeser ke arah sebaliknya (mengurangi shift).

Contoh :
Plaintext: KRIPTOGRAFI
Key : KEY (K=10, E=4, Y=24)
Setiap huruf plaintext digeser bedsarkan huruf kunci secara berulang:
K(+10) → U
R(+4) → V
I(+24) → G
dan seterusnya, menghasilkan ciphertext UVGZXMQVVPM. Ketika didekripsi dengan kunci yang sama, hasilnya kembali ke KRIPTOGRAFI.
Kesimpulannya, Vigenere Cipher menyadikan pesan dengan pola pergeseran yang berubah-ubah mengikuti kunci, membuatnya lebih kuat dari Caesar Cipher, namun masih dapat dipecahkan jika panjang kuni diketahui melalui analisis frekuensi.

Hasil eksekusi langkah (3) Implementasi Transposisi Sederhana
![Hasil Eksekusi](screenshots/3-transposisi.png)
Transposisi Cipher adalah metode penyandian yang tidak mengubah huruf asli, tetapi mengubah urutan (posisi) huruf dalam pesan Artinya, huruf-huruf tetap sama, hanya diacak berdasarkan pola tertentu.

Pada kode di atas, proses enkripsi dilakukan dengan menulis teks secara berkolom, kemudian membaca huruf-hurufnya per kolom dari atas ke bawah.

Penjelasan enkripsi
Fungsi transpose_encrypt() bekerja dengan :
- Membuat sejumlah kolom sesuai dengan nilai key (misalnya 5).
- Huruf plaintext ditulis berurutan ke bawah tiap kolom, lalu hasilnya dibaca dari kolom pertama ke terakhir.
- Hasil akhirnya adalah susunan huruf yang berpindah posisi.

Contoh  
```
Plaintext : T R A N S P O S I T I O N C I P H E R
Key = 5
```
Teks ditulis dalam tabel 5 kolom :
```
T R A N S  
P O S I T  
I O N C I  
P H E R
```
Kemudian dibaca kolom demi kolom menghasikan:
Ciphertext = TPIPROOHASNENICRSTI 

Penjelasan dekripsi 
fungsi transpose_decrypt melakukan proses kebalikan yaitu :
- Menentukan jumlah baris dan kolom
- Mengembalikan urutan huruf ke posisi semula berdasarkan pola pembacaan kolom.
- Hasil akhirnya kembali menjadi plaintext semula.

Transposisi cipher menyandikan pesan dengan mengubah urutan huruf berdasarkan jumlah kolom (key), Huruf-hurufnya tidak berubah, hanya posisinya yang diacak. Karena itu, cipher ini mudah dipahami, tetapi msih bisa dipecahkan dengan analisis pada posisi huruf.

---

## 7. Jawaban Pertanyaan
1. Kelemahan utama algoritma Caesar Chiper dan Vigenere Chiper
   
  Kelemahan utama Caesar Chiper terletak pada jumlah kuncinya yang sangat terbatas, yaitu hanya 26 kemungkinan (untuk alfabet latin). Hal ini membuatnya sangat rentan terhadap serangan brute force, karena penyerang dapat mencoba semua kemungkinan pergeseran dengan cepat. selain itu, Caesar Chiper tidak mengubah pola frekuensi huruf, sehingga analisis frekuensi dapat dengan mudah mengenali huruf-huruf umum seperti "E", "T". atau "A" dalam bahasa Inggris, dan mengembalikan teks aslinya.

  Sementara itu, Vigenere Cipher awalnya dianggap lebih kuat karena menggunakan kunci berulang yang membuat pergeseran tiap huruf berbeda. Namum, kelemahannya muncul jika panjang kunci terlalu pendek atau pola kunci berulang, sebab pola tersebut dapat dideteksi menggunakan analisis Kasiski atau ui Friedman untuk menentukan panjang kunci. Setelah panjang kunci diketahui, cipher ini dapat dipecahkan dengan metde analisis frekuensi pada setiap bagian teks. Dengan demikian, meskipun lebih kompleks daripada Caesar Cipher, Vigenere Cipher tetap tidak aman terhadap serangan kriptanalisis modern.

2. Alasan Cipher Klasik mudah diserang dengan analisis frekuensi

  Cipher klasik mudah diserang dengan analisis frekuensi karena setiap huruf pada teks asli (plaintext) diubah menjadi huruf lain secara tetap dan berulang sesuai aturan tertentu. Pola ini menyebabkan kemunculan huruf dalam ciphertext tetap mirip dengan pola bahasa aslinya.

  Misalnya, dalam bahasa Indonesia atau Inggris, huruf seperti "E" atau "A" muncul lebih sering dibandingakan huruf lain. Jika cipher tidak mengubah pola tersebut (seperti pada Caesar Cipher atau Vigenere Cipher dengan kunci pendek), maka penyerang dapat mencocokkan pola kemungkinan huruf terenkripsi dengan distribusi huruf bahasa alami untuk menebak huruf aslinya.

  Dengan kata lain, cipher klasik tidak cukup acak dan tidak menyembunyikan struktur statistik bahasa, sehingga sangat mudah dipecahkan menggunakan analisis frekuensi, bahkantanpa mengetahui kunci secara langsung.
  
3. Bandingkan kelebihan dan kelemahan cipher subsitusi vs transposisi
  - Ciper Substitusi
    - Kelebihan:
      - Konsepnya sederhana dan mudah diimplementasikan.
      - Dapat memberikan hasil enkripsi depat karena hanya mengganti huruf dengan huruf lain..
    - Kelemahan :
      - Pola frekuensi huruf tetap terlihat, sehingga mudah diserang dengan analisis frekuensi.
      - Tidak cukup kuat untuk digunakan dalam kriptografi modern.
 - Cipher Transposisi
    - Kelebihan :
      - Menyembunyikan pola teks asli dengan cara mengubah posisi huruf, bukan mengganti hurufnya.
      - Lebih sulit dianalisis dengan analisis frekuensi dibanding substitusi.
    - Kelemahan :
      - Struktur huruf tetap sama (huruf yang digunakan tidak berubahS). sehingga masih bisa dipecahkan dengan analisis pola atau serangan brute force.
      - Kurang aman jika digunakan sendriri tanpa dikombinasikan dengan metode lain.

## 8. Kesimpulan
Cipher klasik seperti Caesar, VIgenere, dan Transposisi merupakan dasar penting dalam perkembangan kriptografi modern. Cipher ini bekerja dengan prinsip sederhana -- mengganti atau menukar posisi huruf -- untuk menyembunyikan pesan. Namun, karena pola huruf dan struktur bahasa masih terlihat, cipher klasik mudah dipecahkan dengan alaisis frekuensi atau brute force. Meskipun tidak lagi digunakan untuk keamanan modern, cipher klasik tetap penting sebagai pondasi pemahaman konsep enkripsi dan keamanan dta dalam kriptografi.

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log
```
commit week5-cipher-klasik
Author: Laeli Maharani <laelimaharani09@gmail.com>
Date:   2025-11-01

    week5-cipher-klasik: implementasi Caesar Cipher, Vigenere Cipher, Transposisi dan laporan )
```
