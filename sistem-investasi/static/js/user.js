/* ============================================================
   USER.JS — Sistem Manajemen Nasabah, Transaksi & Portofolio
   ============================================================ */

(function () {
    'use strict';

    const sidebar        = document.getElementById('sidebar');
    const overlay        = document.getElementById('sidebarOverlay');
    const btnToggle      = document.getElementById('btnToggleSidebar');

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

    function toggleSidebar() {
        sidebar.classList.contains('open') ? closeSidebar() : openSidebar();
    }

    if (btnToggle) btnToggle.addEventListener('click', toggleSidebar);
    if (overlay)   overlay.addEventListener('click', closeSidebar);

    /* Close sidebar on Escape key */
    document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape' && sidebar.classList.contains('open')) closeSidebar();
    });

    /* Close sidebar when resizing to desktop */
    window.addEventListener('resize', function () {
        if (window.innerWidth > 768) closeSidebar();
    });

    /* ── Active Menu Highlighting ────────────────────────────── */
    function setActiveMenu() {
        const currentPath = window.location.pathname;
        const navLinks = document.querySelectorAll('.nav-link[data-path]');

        navLinks.forEach(function (link) {
            const linkPath = link.getAttribute('data-path');
            if (linkPath && currentPath.startsWith(linkPath)) {
                link.classList.add('active');
            } else {
                link.classList.remove('active');
            }
        });
    }

    setActiveMenu();

    /* ── Format Currency ─────────────────────────────────────── */
    function formatRupiah(angka) {
        return 'Rp' + Number(angka).toLocaleString('id-ID');
    }

    /* ── Auto format semua elemen .format-rupiah ─────────────── */
    document.querySelectorAll('.format-rupiah').forEach(function (el) {
        const raw = el.getAttribute('data-value');
        if (raw) el.textContent = formatRupiah(raw);
    });

    /* ── Table Row Hover Enhance ─────────────────────────────── */
    document.querySelectorAll('tbody tr').forEach(function (row) {
        row.addEventListener('mouseenter', function () {
            row.style.cursor = 'default';
        });
    });

})();
