# ============================================================
# config.py — Konfigurasi Aplikasi Flask & Database
# ============================================================

import os

class Config:
    # Secret key untuk session Flask
    # Ganti dengan string acak yang panjang di production
    SECRET_KEY = os.environ.get('SECRET_KEY', 'investasi-secret-key-2026-ganti-di-production')

    # Konfigurasi database MySQL (Laragon)
    DB_HOST     = 'localhost'
    DB_USER     = 'root'
    DB_PASSWORD = ''           # Kosong untuk Laragon default
    DB_NAME     = 'db_investasi'
    DB_PORT     = 3306
    DB_CHARSET  = 'utf8mb4'
