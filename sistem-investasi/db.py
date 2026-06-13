# ============================================================
# db.py — Koneksi Database MySQL menggunakan PyMySQL
# ============================================================

import pymysql
import pymysql.cursors
from config import Config


def get_db_connection():
    """
    Membuka dan mengembalikan koneksi ke database MySQL.
    Gunakan DictCursor agar hasil query bisa diakses dengan nama kolom.
    Selalu tutup koneksi setelah selesai digunakan.
    """
    conn = pymysql.connect(
        host     = Config.DB_HOST,
        user     = Config.DB_USER,
        password = Config.DB_PASSWORD,
        database = Config.DB_NAME,
        port     = Config.DB_PORT,
        charset  = Config.DB_CHARSET,
        cursorclass = pymysql.cursors.DictCursor
    )
    return conn
