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

Diadaptasi dari **Unslop** oleh Damir Sokolovsky (https://github.com/heydamir/unslop), lisensi CC BY 4.0. Ini adaptasi independen, bukan rilis resmi upstream.

## Tujuan

Membantu merancang, mengaudit, memperbaiki, dan mengimplementasikan antarmuka digital yang memiliki arah visual sesuai produk, bukan template generik AI. Berlaku untuk landing page, SaaS, dashboard, admin, mobile web, dan commerce.

Prinsip utama: hilangkan kebiasaan visual generik tanpa menghilangkan identitas, konten berguna, atau fungsi produk. Antarmuka bersih belum tentu khas. Desain harus mengomunikasikan fungsi, pengguna, dan karakter produk.

## Prinsip desain

Arah berasal dari produk, audiens, tugas, dan konten; bukan tren. Kontrol mendukung tugas, visual kaya menonjolkan konten bermakna, dan seluruh elemen memperjelas hierarki. Desain harus memiliki karakter produk. Saat memperbaiki layar, pertahankan tujuan, fitur, konten, dan arsitektur informasi kecuali perubahan diminta.

## Alur kerja

### Fase 1 — Inspeksi nyata
Temukan komponen, framework, routing, token, font, breakpoint, dan tema. Jalankan aplikasi dan ambil baseline bila tersedia. Jika hanya URL/screenshot, nyatakan batas bukti. Catat fitur, konten, urutan, responsivitas, dan state sebelum edit.

### Fase 2 — Audit
Catat lokasi dan bukti terkait kejelasan produk, spasi, warna/kontras, ikon, copy/klaim, tipografi, komposisi, responsivitas, komponen, visual, motion, aksesibilitas, input, performa, dan konsistensi. Jelaskan dampak dan apakah perlu diubah; beda estetika bukan otomatis cacat.

### Fase 3 — Tetapkan cakupan
Pilih **redesign besar** bila masalah luas merusak hierarki/identitas, **polish terarah** bila sistem sudah koheren, atau **tidak ada masalah berarti** bila tak ada isu substantif. Jangan mengubah layar hanya demi aktivitas. Bila arah ambigu, minta persetujuan sebelum edit; lewati bila pengguna jelas meminta implementasi langsung.

### Fase 4 — Definisikan arah
Tetapkan produk/fungsi, 2–3 sifat karakter, dunia/metafora produk, satu-dua momen visual penting, dan satu ciri khas konsisten. Pertahankan identitas merek yang sah; rebranding adalah cakupan terpisah.

### Fase 5 — Perbaikan berurutan

1. **Spasi:** gunakan skala konsisten; periksa tabel, sidebar, dan mobile.
2. **Warna:** tetapkan peran surface/teks/aksen/status; cek kontras tiap tema.
3. **Ikon:** gunakan keluarga konsisten dan nama aksesibel; emoji hanya bila bagian identitas/konten.
4. **Copy:** judul spesifik; hapus klaim/metrik/testimoni tanpa bukti; tandai data contoh.
5. **Tipografi:** tetapkan skala dan cek wrapping, line-height, angka, bahasa.
6. **Layout:** jaga arsitektur informasi dan urutan mobile; hindari kartu seragam bila tidak sesuai.
7. **Komponen/data:** rancang state aktif, disabled, loading, sukses, error, kosong, dan usang.
8. **Visual:** gunakan aset yang menjelaskan produk; jangan mengarang kemampuan/bukti.
9. **Gerak:** dukung state/relasi; hormati reduced motion dan hindari gerak menghambat.

### Fase 6 — QA visual dan fungsi

Render dan bandingkan dengan baseline. Periksa temuan satu per satu, desktop/tablet/mobile, keyboard, fokus, target sentuh, kontras, reduced motion, alur terdampak, console, aset rusak, overflow, layout shift, dan loading bila alat tersedia. Pastikan fitur/rute/konten lama tetap bekerja.

### Fase 7 — Laporan

Ringkas arah visual, temuan, perubahan, fitur yang dipertahankan, pemeriksaan responsif/aksesibilitas/interaksi, isu tersisa, asumsi, dan apakah hasil diterapkan di proyek atau hanya direkonstruksi. Jangan mengklaim tes yang tidak dilakukan.

## Kerangka keputusan

Apakah pilihan memperjelas tugas, memperkuat hierarki, sesuai audiens/merek, meningkatkan kegunaan/aksesibilitas, memberi informasi, konsisten dengan sistem, dan sepadan dengan biaya performa/pemeliharaan?

## Hubungan dan batas

Pola Navigasi Web Modern memiliki navigasi; Micro-Interactions memiliki feedback; Desain Frontend memiliki arah visual; Apple HIG memiliki kepatuhan platform. Skill ini mengkritik pola generik dan tidak mengambil alih spesialis tersebut.

## Batas sumber

Upstream Unslop membahas arah berbasis produk, audit, alur perbaikan, visual QA, serta spasi/warna/ikon/copy/tipografi/layout/detail/visual/motion. Adaptasi ini menambah pelestarian produk, responsivitas, aksesibilitas, QA fungsi, dan pelaporan. Referensi upstream yang tidak tersedia tidak direproduksi; lihat upstream untuk versi lengkap.
