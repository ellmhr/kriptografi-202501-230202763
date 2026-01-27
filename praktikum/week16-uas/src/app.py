from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_cors import CORS
import json
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = "edutoken_kriptografi_2026_sepolia"
CORS(app)

# File untuk menyimpan data transaksi
TRANSACTIONS_FILE = "data/transactions.json"

# Pastikan folder data ada
os.makedirs("data", exist_ok=True)
if not os.path.exists(TRANSACTIONS_FILE):
    with open(TRANSACTIONS_FILE, 'w') as f:
        json.dump([], f)

# ============== HELPER FUNCTIONS ==============

def save_transaction(tx_data):
    """Simpan transaksi ke file JSON"""
    try:
        with open(TRANSACTIONS_FILE, 'r') as f:
            transactions = json.load(f)
    except:
        transactions = []
    
    transactions.append(tx_data)
    
    with open(TRANSACTIONS_FILE, 'w') as f:
        json.dump(transactions, f, indent=2)

def get_user_transactions(username):
    """Ambil riwayat transaksi user"""
    try:
        with open(TRANSACTIONS_FILE, 'r') as f:
            transactions = json.load(f)
        return [tx for tx in transactions if tx.get('username') == username]
    except:
        return []

# ============== ROUTES ==============

@app.route("/")
def index():
    """Redirect ke login"""
    if "user" in session:
        return redirect(url_for("dashboard"))
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    """Halaman login"""
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()
        
        if not username:
            return render_template("login.html", error="Username tidak boleh kosong!")
        
        # Simpan username ke session
        session["user"] = username
        session["login_time"] = datetime.now().isoformat()
        
        return redirect(url_for("dashboard"))
    
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    """Halaman dashboard"""
    if "user" not in session:
        return redirect(url_for("login"))
    
    return render_template("dashboard.html", user=session["user"])

@app.route("/materi")
def materi():
    """Halaman materi pembelajaran & kuis"""
    if "user" not in session:
        return redirect(url_for("login"))
    
    return render_template("materi.html")

@app.route("/info_token")
def info_token():
    """Halaman info token & transfer"""
    if "user" not in session:
        return redirect(url_for("login"))
    
    return render_template("info_token.html")

@app.route("/profil")
def profil():
    """Halaman profil user"""
    if "user" not in session:
        return redirect(url_for("login"))
    
    # Hitung statistik user
    transactions = get_user_transactions(session["user"])
    total_earned = sum(tx.get("amount", 0) for tx in transactions if tx.get("type") == "claim")
    total_sent = sum(tx.get("amount", 0) for tx in transactions if tx.get("type") == "transfer")
    
    stats = {
        "total_earned": total_earned,
        "total_sent": total_sent,
        "transaction_count": len(transactions)
    }
    
    return render_template("profil.html", user=session["user"], stats=stats)

@app.route("/logout")
def logout():
    """Logout user"""
    session.clear()
    return redirect(url_for("login"))

# ============== API ENDPOINTS ==============

@app.route("/api/save_transaction", methods=["POST"])
def api_save_transaction():
    """API untuk menyimpan transaksi dari frontend"""
    if "user" not in session:
        return jsonify({"error": "Unauthorized"}), 401
    
    data = request.json
    tx_data = {
        "username": session["user"],
        "type": data.get("type"),  # "claim" atau "transfer"
        "amount": data.get("amount"),
        "tx_hash": data.get("tx_hash"),
        "to_address": data.get("to_address", ""),
        "timestamp": datetime.now().isoformat()
    }
    
    save_transaction(tx_data)
    
    return jsonify({"success": True, "message": "Transaction saved"})

@app.route("/api/transactions")
def api_transactions():
    """API untuk mengambil riwayat transaksi user"""
    if "user" not in session:
        return jsonify({"error": "Unauthorized"}), 401
    
    transactions = get_user_transactions(session["user"])
    return jsonify({"transactions": transactions})

@app.route("/api/stats")
def api_stats():
    """API untuk statistik user"""
    if "user" not in session:
        return jsonify({"error": "Unauthorized"}), 401
    
    transactions = get_user_transactions(session["user"])
    
    stats = {
        "total_claims": len([tx for tx in transactions if tx.get("type") == "claim"]),
        "total_transfers": len([tx for tx in transactions if tx.get("type") == "transfer"]),
        "total_earned": sum(tx.get("amount", 0) for tx in transactions if tx.get("type") == "claim"),
        "total_sent": sum(tx.get("amount", 0) for tx in transactions if tx.get("type") == "transfer")
    }
    
    return jsonify(stats)

# ============== ERROR HANDLERS ==============

@app.errorhandler(404)
def not_found(e):
    return redirect(url_for("dashboard"))

@app.errorhandler(500)
def server_error(e):
    return "Terjadi kesalahan server. Silakan coba lagi.", 500

# ============== RUN APPLICATION ==============

if __name__ == "__main__":
    print("\n" + "="*60)
    print("🎓 EDUTOKEN - PLATFORM PEMBELAJARAN KRIPTOGRAFI")
    print("="*60)
    print("🌐 Server berjalan di: http://127.0.0.1:5000")
    print("🔐 Tekan CTRL+C untuk menghentikan server")
    print("="*60 + "\n")
    
    app.run(debug=True, host='127.0.0.1', port=5000)