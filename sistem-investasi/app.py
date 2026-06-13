from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# ── Root & Login ──────────────────────────────────────────────
@app.route('/')
def index():
    return redirect(url_for('user_dashboard'))

@app.route('/login')
def login():
    return redirect(url_for('user_dashboard'))

@app.route('/logout')
def logout():
    return redirect(url_for('user_dashboard'))

# ── User Pages ────────────────────────────────────────────────
@app.route('/user/dashboard')
def user_dashboard():
    return render_template('user/dashboard.html')

@app.route('/user/profil')
def user_profil():
    return render_template('user/profil.html')

@app.route('/user/produk')
def user_produk():
    return render_template('user/produk.html')

@app.route('/user/transaksi')
def user_transaksi():
    return render_template('user/transaksi.html')

@app.route('/user/portofolio')
def user_portofolio():
    return render_template('user/portofolio.html')

# ── Run ───────────────────────────────────────────────────────
if __name__ == '__main__':
    app.run(debug=True)
