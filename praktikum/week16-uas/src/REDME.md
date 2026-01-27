# 🎓 EduToken - Platform Pembelajaran Kriptografi Berbasis Blockchain

Platform pembelajaran interaktif yang mengintegrasikan konsep kriptografi dengan teknologi blockchain. Pengguna mendapatkan reward token digital (EDT) setelah menyelesaikan kuis pembelajaran.

## ✨ Fitur Utama

- 🔐 **Pembelajaran Kriptografi** - Materi terstruktur tentang kriptografi, hashing, dan blockchain
- 🎯 **Kuis Interaktif** - Pertanyaan dengan timer untuk menguji pemahaman
- 💎 **Reward System** - Dapatkan EDT token sebagai reward
- ⛓️ **Blockchain Integration** - Terhubung dengan Sepolia Testnet
- 💸 **Transfer Token** - Kirim EDT ke wallet lain
- 📊 **Riwayat Transaksi** - Tracking semua transaksi Anda
- 🦊 **MetaMask Integration** - Koneksi langsung dengan wallet

## 🛠️ Teknologi yang Digunakan

**Backend:**
- Python 3.8+
- Flask - Web framework
- Flask-CORS - Cross-Origin Resource Sharing

**Frontend:**
- HTML5, CSS3, JavaScript
- Bootstrap 5 - UI framework
- Ethers.js 5.7.2 - Blockchain interaction

**Blockchain:**
- Solidity 0.8.20 - Smart contract
- Hardhat - Development environment
- OpenZeppelin Contracts - Security standards
- Sepolia Testnet - Testing network

## 📁 Struktur Project

```
KRIPTO_PROJECT/
├── contracts/
│   └── EduToken.sol          # Smart contract
├── scripts/
│   └── deploy.js             # Deployment script
├── content/
│   ├── materi1.txt           # Materi kriptografi
│   ├── materi2.txt           # Materi hashing
│   └── materi3.txt           # Materi token
├── data/
│   └── transactions.json     # Database transaksi
├── templates/
│   ├── dashboard.html        # Halaman utama
│   ├── info_token.html       # Info & transfer
│   ├── login.html            # Login page
│   ├── materi.html           # Pembelajaran & kuis
│   └── profil.html           # User profile
├── static/                   # Assets statis
├── .env                      # Environment variables
├── app.py                    # Flask application
├── hardhat.config.js         # Hardhat config
├── package.json              # Node dependencies
└── README.md                 # Dokumentasi
```

## 🚀 Instalasi & Setup

### 1. Prerequisites

Pastikan sudah terinstall:
- [Python 3.8+](https://www.python.org/downloads/)
- [Node.js 16+](https://nodejs.org/)
- [MetaMask Browser Extension](https://metamask.io/)

### 2. Clone Repository

```bash
git clone <repository-url>
cd KRIPTO_PROJECT
```

### 3. Setup Python Backend

```bash
# Buat virtual environment (opsional)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# atau
venv\Scripts\activate     # Windows

# Install dependencies
pip install flask flask-cors
```

### 4. Setup Blockchain Development

```bash
# Install Node.js dependencies
npm install

# Install Hardhat dan libraries
npm install --save-dev hardhat @nomicfoundation/hardhat-toolbox
npm install @openzeppelin/contracts dotenv ethers@5.7.2
```

### 5. Konfigurasi MetaMask

1. Install MetaMask di browser Anda
2. Buat wallet baru atau import existing
3. Tambahkan Sepolia Network:
   - Network Name: `Sepolia Test Network`
   - RPC URL: `https://rpc.sepolia.org`
   - Chain ID: `11155111`
   - Currency Symbol: `ETH`
   - Explorer: `https://sepolia.etherscan.io`

### 6. Dapatkan Sepolia ETH (Testnet)

Kunjungi salah satu faucet:
- https://sepoliafaucet.com
- https://www.infura.io/faucet/sepolia
- https://sepolia-faucet.pk910.de

Masukkan alamat wallet Anda dan dapatkan ETH gratis untuk testing.

### 7. Setup Environment Variables

Buat file `.env` di root project:

```env
SEPOLIA_RPC_URL=https://rpc.sepolia.org
PRIVATE_KEY=your_metamask_private_key_without_0x
```

**⚠️ PENTING:** Jangan bagikan private key Anda!

**Cara mendapatkan Private Key:**
1. Buka MetaMask
2. Klik 3 titik → Account Details
3. Export Private Key
4. Masukkan password
5. Copy private key (tanpa "0x")

### 8. Deploy Smart Contract

```bash
# Compile contract
npx hardhat compile

# Deploy ke Sepolia
npx hardhat run scripts/deploy.js --network sepolia
```

**Simpan contract address yang muncul!** Contoh output:
```
✅ EduToken deployed successfully!
📝 Contract address: 0x1234567890abcdef...
```

### 9. Update Contract Address

Ganti `CONTRACT_ADDRESS` di 3 file berikut dengan address hasil deployment:

1. **templates/materi.html** (line ~570)
```javascript
const CONTRACT_ADDRESS = "0xYOUR_CONTRACT_ADDRESS_HERE";
```

2. **templates/info_token.html** (line ~370)
```javascript
const CONTRACT_ADDRESS = "0xYOUR_CONTRACT_ADDRESS_HERE";
```

3. **edutoken/index.html** (jika ada)

### 10. Jalankan Aplikasi

```bash
python app.py
```

Server akan berjalan di: **http://127.0.0.1:5000**

## 📖 Cara Menggunakan

### Login
1. Buka http://127.0.0.1:5000
2. Masukkan username (bebas)
3. Masukkan password (bebas)
4. Klik "Masuk & Belajar"

### Belajar & Klaim Token
1. Klik menu "Materi & Kuis"
2. Connect MetaMask saat diminta
3. Baca materi yang tersedia
4. Klik "MULAI KUIS"
5. Jawab 5 pertanyaan (20 detik per soal)
6. Klik "KLAIM KE METAMASK"
7. Konfirmasi transaksi di MetaMask
8. Tunggu ~15-30 detik untuk konfirmasi

**Reward:**
- Jawaban benar = 2 EDT/soal
- Maksimal 10 EDT per kuis
- Unlock Materi 2: butuh 10 EDT
- Unlock Materi 3: butuh 20 EDT

### Transfer Token
1. Klik menu "Info Token"
2. Lihat saldo EDT Anda
3. Masukkan alamat wallet tujuan
4. Masukkan jumlah EDT
5. Klik "KIRIM SEKARANG"
6. Konfirmasi di MetaMask

### Cek Profil
1. Klik menu "Profil"
2. Lihat statistik Anda:
   - Kuis selesai
   - Total transfer
   - Token earned
   - Token sent

## 🔍 Troubleshooting

### Error: "MetaMask tidak terdeteksi"
**Solusi:**
- Install MetaMask extension
- Refresh halaman
- Pastikan MetaMask aktif

### Error: "Insufficient funds"
**Solusi:**
- Dapatkan Sepolia ETH dari faucet
- Pastikan ada cukup ETH untuk gas fee
- Tunggu beberapa menit jika baru request faucet

### Error: "Network mismatch"
**Solusi:**
- Buka MetaMask
- Klik logo network di pojok atas
- Pilih "Sepolia Test Network"

### Error: "Claim cooldown active"
**Solusi:**
- Tunggu 5 menit setelah klaim terakhir
- Ini fitur anti-spam

### Contract tidak ditemukan
**Solusi:**
- Pastikan contract sudah dideploy
- Cek contract address di Etherscan
- Pastikan address di HTML sudah benar

### Transaksi pending lama
**Solusi:**
- Tunggu ~30-60 detik
- Jika > 5 menit, cek di Sepolia Etherscan
- Network mungkin sedang sibuk

## 📊 Smart Contract Details

**Contract:** EduToken
**Symbol:** EDT
**Decimals:** 18
**Network:** Sepolia Testnet
**Standard:** ERC-20

**Fungsi Utama:**
- `balanceOf(address)` - Cek saldo
- `transfer(address, amount)` - Transfer token
- `claimReward(address, amount)` - Klaim reward (owner only)

**Security Features:**
- Cooldown 5 menit antar claim
- Owner-only claim function
- OpenZeppelin battle-tested contracts

## 🎯 Konsep Pembelajaran

### Materi 1: Kriptografi
- Definisi kriptografi
- Tujuan: Confidentiality, Integrity, Authentication
- Penerapan: HTTPS, Login, Blockchain

### Materi 2: Hashing
- Fungsi hash one-way
- SHA-256 algorithm
- Penggunaan: Password, Data integrity

### Materi 3: Token & Blockchain
- Token digital concept
- Blockchain basics
- Smart contracts
- Transaction integrity

## 🔐 Keamanan

**Yang HARUS dilakukan:**
✅ Simpan private key dengan aman
✅ Jangan share private key ke siapapun
✅ Gunakan testnet untuk belajar
✅ Backup seed phrase MetaMask

**Yang JANGAN dilakukan:**
❌ Commit `.env` ke Git
❌ Share private key
❌ Deploy ke mainnet tanpa audit
❌ Gunakan wallet utama untuk testing

## 🚧 Development Roadmap

- [x] Smart contract deployment
- [x] Basic UI/UX
- [x] MetaMask integration
- [x] Quiz system
- [x] Reward mechanism
- [x] Transfer functionality
- [ ] NFT certificates
- [ ] Leaderboard
- [ ] Multi-language support
- [ ] Mobile responsive optimization
- [ ] Mainnet deployment

## 📝 License

MIT License - Bebas digunakan untuk pembelajaran.

## 👥 Kontributor

Dikembangkan untuk tugas mata kuliah Kriptografi.

## 📞 Support

Jika mengalami kesulitan:
1. Cek dokumentasi ini
2. Cek console browser (F12)
3. Cek Sepolia Etherscan untuk transaksi
4. Hubungi tim support

## 🎉 Selamat Belajar!

Nikmati pembelajaran kriptografi yang interaktif dan menyenangkan dengan EduToken! 🚀

---
*Built with ❤️ for Blockchain Education*