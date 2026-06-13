/* ============================================================
   AUTH.JS — Halaman Login
   ============================================================ */

(function () {
    'use strict';

    /* ── Toggle Tampilkan / Sembunyikan Password ─────────────── */
    const passInput  = document.getElementById('password');
    const btnToggle  = document.getElementById('btnTogglePass');

    if (passInput && btnToggle) {
        btnToggle.addEventListener('click', function () {
            const isHidden = passInput.type === 'password';
            passInput.type = isHidden ? 'text' : 'password';
            btnToggle.querySelector('i').className = isHidden
                ? 'bi bi-eye-slash'
                : 'bi bi-eye';
        });
    }

    /* ── Loading State saat Form Submit ──────────────────────── */
    const form    = document.getElementById('loginForm');
    const btnLogin = document.getElementById('btnLogin');

    if (form && btnLogin) {
        form.addEventListener('submit', function () {
            const username = document.getElementById('username').value.trim();
            const password = document.getElementById('password').value;

            if (!username || !password) return; /* biarkan server validasi */

            btnLogin.classList.add('loading');
        });
    }

    /* ── Auto focus input username ───────────────────────────── */
    const usernameInput = document.getElementById('username');
    if (usernameInput && !usernameInput.value) {
        usernameInput.focus();
    }

})();
