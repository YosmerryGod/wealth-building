---
name: ai-interface-design-and-unslop-engineering
title: Desain Antarmuka AI dan Rekayasa Anti-Generik
category: development
source_type: adapted-open-source-skill-and-operational-framework
source: Unslop oleh Damir Sokolovsky, CC BY 4.0; kerangka tambahan oleh Wealth Building
language: Indonesian
description: "Mengaudit dan memperbaiki antarmuka agar spesifik terhadap produk, bukan template AI generik."
triggers: ["UI terlihat generik","audit tampilan","unslop","rapikan desain AI"]
out_of_scope: "Kepatuhan platform khusus atau implementasi interaksi spesialis"
escalation: "Serahkan arah visual menyeluruh kepada Desain Frontend, review Apple kepada Apple HIG, dan interaksi spesifik kepada pemiliknya."
---

# Desain Antarmuka AI dan Rekayasa Anti-Generik

## Atribusi dan lisensi

Diadaptasi dari **Unslop** oleh Damir Sokolovsky, https://github.com/heydamir/unslop, berlisensi Creative Commons Attribution 4.0 International (CC BY 4.0). Ini adaptasi independen untuk Wealth Building, bukan rilis resmi upstream. Repository upstream tetap menjadi sumber utama untuk implementasi dan referensi lengkap.

## Tujuan

Membantu merancang, mengaudit, memperbaiki, dan mengimplementasikan antarmuka digital yang memiliki arah visual sesuai produk, bukan template generik AI. Berlaku untuk landing page, SaaS, dashboard, admin, mobile web, dan commerce.

Prinsip utama: hilangkan kebiasaan visual generik tanpa menghilangkan identitas, konten berguna, atau fungsi produk. Antarmuka bersih belum tentu khas. Desain harus mengomunikasikan fungsi, pengguna, dan karakter produk.

## Prinsip desain

- Arah berasal dari produk, audiens, tugas, dan konten, bukan tren.
- Kontrol dan permukaan mendukung tugas; visual kaya dipakai untuk konten/hasil bermakna.
- Warna, skala, spasi, tipografi, komposisi, dan gerak memperjelas hierarki.
- Desain harus punya karakter produk, bukan template yang dapat dipertukarkan.
- Saat memperbaiki layar, pertahankan tujuan, fitur, konten, arsitektur informasi, dan urutan kecuali perubahan diminta.

## Alur kerja

### Fase 1 — Inspeksi nyata
Temukan file/komponen; identifikasi framework, routing, sistem komponen, token, font, breakpoint, dan tema. Jalankan aplikasi dan ambil baseline bila memungkinkan. Jika hanya URL atau screenshot tersedia, nyatakan batas bukti; jangan mengaku memeriksa source. Catat fitur, konten, urutan, responsivitas, dan state sebelum edit.

### Fase 2 — Audit
Catat lokasi dan bukti terkait kejelasan produk, spasi, warna/kontras, ikon, copy/klaim, tipografi, komposisi, responsivitas, komponen, visual, motion, aksesibilitas, input, performa, dan konsistensi. Jelaskan dampak dan apakah perlu diubah; beda estetika bukan otomatis cacat.

### Fase 3 — Tetapkan cakupan
Pilih **redesign besar** bila masalah luas merusak hierarki/identitas, **polish terarah** bila sistem sudah koheren, atau **tidak ada masalah berarti** bila tak ada isu substantif. Jangan mengubah layar hanya demi aktivitas. Bila arah ambigu, minta persetujuan sebelum edit; lewati bila pengguna jelas meminta implementasi langsung.

### Fase 4 — Definisikan arah
Tetapkan produk/fungsi, 2–3 sifat karakter, dunia/metafora produk, satu-dua momen visual penting, dan satu ciri khas konsisten. Pertahankan identitas merek yang sah; rebranding adalah cakupan terpisah.

### Fase 5 — Perbaikan berurutan

Perbaiki dalam pass yang konsisten:
1. **Spasi/alignment:** gunakan skala yang konsisten; 4px hanya titik awal. Periksa tabel, sidebar, dan mobile.
2. **Warna:** tetapkan peran background, surface, border, teks, aksen, dan status; cek kontras semua tema/state.
3. **Ikon:** gunakan keluarga konsisten; kontrol ikon punya nama aksesibel. Emoji hanya dipertahankan bila bagian identitas/konten.
4. **Copy:** judul spesifik; hapus klaim, metrik, dan testimoni tanpa bukti. Tandai data contoh.
5. **Tipografi:** tetapkan skala; cek line-height, wrapping, angka, dan bahasa.
6. **Layout:** jaga arsitektur informasi; pilih komposisi sesuai tugas dan urutan mobile logis.
7. **Komponen/data:** konsistenkan detail; rancang state aktif, disabled, loading, sukses, error, kosong, dan usang.
8. **Visual:** gunakan aset/diagram/chart yang menjelaskan produk; jangan mengarang kemampuan atau bukti. Gambar generatif hanya untuk kebutuhan yang jelas.
9. **Gerak:** gunakan untuk state/relasi; hormati reduced motion dan hindari loop/flash yang menghambat.

### Fase 6 — QA visual dan fungsi

Render dan bandingkan dengan baseline. Periksa temuan satu per satu, desktop/tablet/mobile, keyboard, fokus, target sentuh, kontras, reduced motion, alur terdampak, console, aset rusak, overflow, layout shift, dan loading bila alat tersedia. Pastikan fitur/rute/konten lama tetap bekerja.

### Fase 7 — Laporan

Ringkas arah visual, temuan, perubahan per fase, fitur yang dipertahankan, pemeriksaan responsif/aksesibilitas/interaksi, isu tersisa, asumsi, dan apakah hasil diterapkan pada proyek nyata atau hanya direkonstruksi dari screenshot. Jangan mengklaim tes yang tidak dilakukan.

## Kerangka keputusan

Apakah pilihan memperjelas tugas, memperkuat hierarki, sesuai audiens/merek, meningkatkan kegunaan/aksesibilitas, memberi informasi, konsisten dengan sistem, dan sepadan dengan biaya performa/pemeliharaan?

## Hubungan dan batas

Pola Navigasi Web Modern memiliki navigasi; Micro-Interactions memiliki feedback; Desain Frontend memiliki arah visual; Apple HIG memiliki kepatuhan platform. Skill ini mengkritik pola generik dan tidak mengambil alih spesialis tersebut.

## Batas sumber

Upstream Unslop membahas arah berbasis produk, audit layar, alur perbaikan, visual QA, dan panduan spasi/warna/ikon/copy/tipografi/layout/detail/visual/motion. Adaptasi ini menyusun ulang menjadi sembilan pass dan menambah pelestarian produk, keputusan desain, responsivitas, aksesibilitas, QA fungsi, dan pelaporan. Referensi upstream terpisah yang tidak tersedia pada path yang diperiksa tidak direproduksi; lihat upstream untuk versi lengkap.

