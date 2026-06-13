/* ============================================================
   ADMIN.JS — Sistem Manajemen Nasabah, Transaksi & Portofolio
   ============================================================ */

(function () {
    'use strict';

    const sidebar   = document.getElementById('sidebar');
    const overlay   = document.getElementById('sidebarOverlay');
    const btnToggle = document.getElementById('btnToggleSidebar');

    /* ── Sidebar Toggle ──────────────────────────────────────── */
    function openSidebar() {
        sidebar.classList.add('open');
        overlay.classList.add('show');
        document.body.style.overflow = 'hidden';
    }

    function closeSidebar() {
        sidebar.classList.remove('open');
        overlay.classList.remove('show');
        document.body.style.overflow = '';
    }

    if (btnToggle) btnToggle.addEventListener('click', function () {
        sidebar.classList.contains('open') ? closeSidebar() : openSidebar();
    });

    if (overlay) overlay.addEventListener('click', closeSidebar);

    document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape' && sidebar && sidebar.classList.contains('open')) closeSidebar();
    });

    window.addEventListener('resize', function () {
        if (window.innerWidth > 768) closeSidebar();
    });

    /* ── Active Menu Highlighting ────────────────────────────── */
    function setActiveMenu() {
        const currentPath = window.location.pathname;
        const navLinks = document.querySelectorAll('.nav-link[data-path]');

        navLinks.forEach(function (link) {
            const linkPath = link.getAttribute('data-path');
            if (!linkPath) return;

            /* Exact match untuk dashboard, startsWith untuk sub-halaman */
            const isActive = linkPath === '/admin/dashboard'
                ? currentPath === linkPath
                : currentPath.startsWith(linkPath);

            link.classList.toggle('active', isActive);
        });
    }

    setActiveMenu();

    /* ── Konfirmasi Hapus ────────────────────────────────────── */
    document.querySelectorAll('.btn-hapus').forEach(function (btn) {
        btn.addEventListener('click', function (e) {
            e.preventDefault();
            const nama = btn.getAttribute('data-nama') || 'data ini';
            const ok = confirm('Apakah Anda yakin ingin menghapus ' + nama + '?\n\nTindakan ini tidak dapat dibatalkan.');
            if (ok) {
                /* Placeholder — akan dihubungkan ke route Flask saat backend siap */
                alert('Data berhasil dihapus. (simulasi)');
            }
        });
    });

    /* ── Auto Calculate Total Transaksi ──────────────────────── */
    const inputJumlah = document.getElementById('jumlah_unit');
    const inputHarga  = document.getElementById('harga_unit');
    const inputTotal  = document.getElementById('total_transaksi');

    function hitungTotal() {
        if (!inputJumlah || !inputHarga || !inputTotal) return;
        const jumlah = parseFloat(inputJumlah.value) || 0;
        const harga  = parseFloat(inputHarga.value.replace(/[^0-9]/g, '')) || 0;
        const total  = jumlah * harga;
        inputTotal.value = total > 0 ? total.toLocaleString('id-ID') : '';
    }

    if (inputJumlah) inputJumlah.addEventListener('input', hitungTotal);
    if (inputHarga)  inputHarga.addEventListener('input', hitungTotal);

    /* ── Format Currency Input (harga_unit) ──────────────────── */
    if (inputHarga) {
        inputHarga.addEventListener('blur', function () {
            const raw = parseFloat(inputHarga.value.replace(/[^0-9]/g, ''));
            if (!isNaN(raw) && raw > 0) {
                inputHarga.value = raw.toLocaleString('id-ID');
            }
        });
        inputHarga.addEventListener('focus', function () {
            inputHarga.value = inputHarga.value.replace(/[^0-9]/g, '');
        });
    }

})();
