from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# ── Root & Auth ───────────────────────────────────────────────
@app.route('/')
def index():
    return redirect(url_for('user_dashboard'))

@app.route('/login')
def login():
    return redirect(url_for('user_dashboard'))

@app.route('/logout')
def logout():
    return redirect(url_for('admin_dashboard'))

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

# ── Admin: Dashboard ──────────────────────────────────────────
@app.route('/admin')
def admin_index():
    return redirect(url_for('admin_dashboard'))

@app.route('/admin/dashboard')
def admin_dashboard():
    return render_template('admin/dashboard.html')

# ── Admin: Nasabah ────────────────────────────────────────────
@app.route('/admin/nasabah')
def admin_nasabah_index():
    return render_template('admin/nasabah/index.html')

@app.route('/admin/nasabah/tambah')
def admin_nasabah_tambah():
    return render_template('admin/nasabah/tambah.html')

@app.route('/admin/nasabah/edit')
def admin_nasabah_edit():
    return render_template('admin/nasabah/edit.html')

# ── Admin: Users ──────────────────────────────────────────────
@app.route('/admin/users')
def admin_users_index():
    return render_template('admin/users/index.html')

@app.route('/admin/users/tambah')
def admin_users_tambah():
    return render_template('admin/users/tambah.html')

@app.route('/admin/users/edit')
def admin_users_edit():
    return render_template('admin/users/edit.html')

# ── Admin: Produk ─────────────────────────────────────────────
@app.route('/admin/produk')
def admin_produk_index():
    return render_template('admin/produk/index.html')

@app.route('/admin/produk/tambah')
def admin_produk_tambah():
    return render_template('admin/produk/tambah.html')

@app.route('/admin/produk/edit')
def admin_produk_edit():
    return render_template('admin/produk/edit.html')

# ── Admin: Transaksi ──────────────────────────────────────────
@app.route('/admin/transaksi')
def admin_transaksi_index():
    return render_template('admin/transaksi/index.html')

@app.route('/admin/transaksi/tambah')
def admin_transaksi_tambah():
    return render_template('admin/transaksi/tambah.html')

@app.route('/admin/transaksi/edit')
def admin_transaksi_edit():
    return render_template('admin/transaksi/edit.html')

# ── Admin: Portofolio ─────────────────────────────────────────
@app.route('/admin/portofolio')
def admin_portofolio_index():
    return render_template('admin/portofolio/index.html')

# ── Admin: Laporan ────────────────────────────────────────────
@app.route('/admin/laporan')
def admin_laporan_index():
    return render_template('admin/laporan/index.html')

# ── Run ───────────────────────────────────────────────────────
if __name__ == '__main__':
    app.run(debug=True)
