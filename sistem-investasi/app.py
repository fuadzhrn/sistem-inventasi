from flask import Flask, render_template, redirect, url_for, request, session
from werkzeug.security import check_password_hash
from functools import wraps
from config import Config
from db import get_db_connection

app = Flask(__name__)
app.secret_key = Config.SECRET_KEY


# ============================================================
# DECORATORS — Proteksi Route
# ============================================================

def login_required(f):
    """Redirect ke /login jika belum login."""
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'id_user' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated


def admin_required(f):
    """Hanya admin yang boleh akses. User biasa diarahkan ke dashboard user."""
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'id_user' not in session:
            return redirect(url_for('login'))
        if session.get('role') != 'admin':
            return redirect(url_for('user_dashboard'))
        return f(*args, **kwargs)
    return decorated


def user_required(f):
    """Hanya nasabah (user) yang boleh akses. Admin diarahkan ke dashboard admin."""
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'id_user' not in session:
            return redirect(url_for('login'))
        if session.get('role') != 'user':
            return redirect(url_for('admin_dashboard'))
        return f(*args, **kwargs)
    return decorated


# ============================================================
# AUTH ROUTES
# ============================================================

@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    # Sudah login → langsung arahkan ke dashboard yang sesuai
    if 'id_user' in session:
        if session.get('role') == 'admin':
            return redirect(url_for('admin_dashboard'))
        return redirect(url_for('user_dashboard'))

    error = None

    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')

        if not username or not password:
            error = 'Username dan password wajib diisi.'
        else:
            conn = None
            try:
                conn   = get_db_connection()
                cursor = conn.cursor()
                cursor.execute(
                    'SELECT * FROM users WHERE username = %s LIMIT 1',
                    (username,)
                )
                user = cursor.fetchone()
            finally:
                if conn:
                    conn.close()

            if not user:
                error = 'Username tidak ditemukan.'
            elif user['status'] != 'aktif':
                error = 'Akun Anda tidak aktif. Hubungi administrator.'
            elif not check_password_hash(user['password'], password):
                error = 'Password salah.'
            else:
                session.clear()
                session['id_user']    = user['id_user']
                session['username']   = user['username']
                session['role']       = user['role']
                session['id_nasabah'] = user['id_nasabah']

                if user['role'] == 'admin':
                    return redirect(url_for('admin_dashboard'))
                return redirect(url_for('user_dashboard'))

    return render_template('auth/login.html', error=error)


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


# ============================================================
# USER ROUTES — Dilindungi @user_required
# ============================================================

@app.route('/user/dashboard')
@user_required
def user_dashboard():
    return render_template('user/dashboard.html')


@app.route('/user/profil')
@user_required
def user_profil():
    return render_template('user/profil.html')


@app.route('/user/produk')
@user_required
def user_produk():
    return render_template('user/produk.html')


@app.route('/user/transaksi')
@user_required
def user_transaksi():
    return render_template('user/transaksi.html')


@app.route('/user/portofolio')
@user_required
def user_portofolio():
    return render_template('user/portofolio.html')


# ============================================================
# ADMIN ROUTES — Dilindungi @admin_required
# ============================================================

@app.route('/admin')
@admin_required
def admin_index():
    return redirect(url_for('admin_dashboard'))


@app.route('/admin/dashboard')
@admin_required
def admin_dashboard():
    return render_template('admin/dashboard.html')


# ── Nasabah ───────────────────────────────────────────────────
@app.route('/admin/nasabah')
@admin_required
def admin_nasabah_index():
    return render_template('admin/nasabah/index.html')


@app.route('/admin/nasabah/tambah')
@admin_required
def admin_nasabah_tambah():
    return render_template('admin/nasabah/tambah.html')


@app.route('/admin/nasabah/edit')
@admin_required
def admin_nasabah_edit():
    return render_template('admin/nasabah/edit.html')


# ── Users ─────────────────────────────────────────────────────
@app.route('/admin/users')
@admin_required
def admin_users_index():
    return render_template('admin/users/index.html')


@app.route('/admin/users/tambah')
@admin_required
def admin_users_tambah():
    return render_template('admin/users/tambah.html')


@app.route('/admin/users/edit')
@admin_required
def admin_users_edit():
    return render_template('admin/users/edit.html')


# ── Produk ────────────────────────────────────────────────────
@app.route('/admin/produk')
@admin_required
def admin_produk_index():
    return render_template('admin/produk/index.html')


@app.route('/admin/produk/tambah')
@admin_required
def admin_produk_tambah():
    return render_template('admin/produk/tambah.html')


@app.route('/admin/produk/edit')
@admin_required
def admin_produk_edit():
    return render_template('admin/produk/edit.html')


# ── Transaksi ─────────────────────────────────────────────────
@app.route('/admin/transaksi')
@admin_required
def admin_transaksi_index():
    return render_template('admin/transaksi/index.html')


@app.route('/admin/transaksi/tambah')
@admin_required
def admin_transaksi_tambah():
    return render_template('admin/transaksi/tambah.html')


@app.route('/admin/transaksi/edit')
@admin_required
def admin_transaksi_edit():
    return render_template('admin/transaksi/edit.html')


# ── Portofolio ────────────────────────────────────────────────
@app.route('/admin/portofolio')
@admin_required
def admin_portofolio_index():
    return render_template('admin/portofolio/index.html')


# ── Laporan ───────────────────────────────────────────────────
@app.route('/admin/laporan')
@admin_required
def admin_laporan_index():
    return render_template('admin/laporan/index.html')


# ============================================================
# RUN
# ============================================================

if __name__ == '__main__':
    app.run(debug=True)
