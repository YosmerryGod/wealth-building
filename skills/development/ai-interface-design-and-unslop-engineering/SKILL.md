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

1. **Berangkat dari produk:** arah desain berasal dari audiens, tugas, dan konten, bukan tren.
2. **Antarmuka tenang, fokus bermakna:** kontrol mendukung tugas; kekayaan visual dipakai untuk konten atau hasil yang penting.
3. **Hierarki sengaja:** skala, warna, spasi, tipografi, komposisi, dan gerak memperjelas prioritas.
4. **Identitas di atas template:** desain tidak boleh terasa dapat dipertukarkan hanya dengan mengganti logo dan judul.
5. **Pertahankan produk:** saat memperbaiki layar, jaga tujuan, fitur, konten, arsitektur informasi, dan urutan bagian kecuali pengguna meminta perubahan UX.

## Sinyal pola generik

Audit konteks aktual. Waspadai gradasi ungu-biru tanpa alasan, glow/neon/bayangan berwarna yang bersaing dengan konten, emoji sebagai ikon kontrol, badge generik tanpa fungsi, terlalu banyak uppercase dan bobot font, spasi/alignment acak, kartu seragam untuk konten berbeda, hero copy generik, metrik/testimoni palsu, animasi dekoratif berulang, serta layout dashboard/landing yang tidak sesuai konteks.

Ini sinyal audit, bukan larangan universal. Gradien, glow, emoji, kartu, animasi, atau layout tertentu dapat tepat bila didukung merek, konten, aksesibilitas, atau fungsi.

## Alur kerja

### Fase 1 — Inspeksi nyata
1. Temukan file dan komponen layar.
2. Identifikasi framework, routing, komponen, styling, token, font, breakpoint, dan tema.
3. Jalankan produk bila memungkinkan dan periksa render pada viewport target.
4. Ambil screenshot baseline jika tersedia.
5. Jika hanya URL, gunakan workflow browser yang diizinkan; jangan mengaku melihat source.
6. Jika hanya screenshot, nyatakan hasil sebagai rekonstruksi visual, bukan perubahan aplikasi nyata.
7. Catat fitur, konten, urutan bagian, responsivitas, dan state sebelum mengedit.

### Fase 2 — Audit
Catat temuan konkret beserta lokasinya: kejelasan produk, spasi, alignment, density, warna/kontras, ikon, copy/klaim, tipografi, komposisi, responsivitas, detail komponen, visual, motion, aksesibilitas, keyboard, touch, reduced motion, performa, dan konsistensi implementasi.

Untuk setiap temuan, tulis apa yang terlihat, lokasi, dampak, dan apakah perlu diubah. Perbedaan estetika bukan otomatis cacat.

### Fase 3 — Tetapkan cakupan
- **Redesign besar:** masalah luas merusak hierarki, konsistensi, atau identitas.
- **Polish terarah:** identitas sudah koheren; perbaiki isu spesifik.
- **Tidak ada masalah berarti:** nyatakan apa adanya; jangan mengubah layar hanya agar terlihat sibuk.

Jika arah atau cakupan ambigu, tunjukkan audit dan usulan sebelum mengedit. Lewati jeda bila pengguna jelas meminta implementasi langsung.

### Fase 4 — Definisikan arah
Tuliskan lima hal:
1. **Produk:** fungsi dan pengguna dalam satu kalimat.
2. **Karakter:** 2–3 sifat konkret.
3. **Dunia:** konteks, material, lingkungan, atau metafora produk.
4. **Momen:** satu atau dua area yang layak mendapat detail visual lebih kaya.
5. **Ciri khas:** detail yang mudah dikenali dan konsisten, bukan dekorasi di semua tempat.

Pertahankan identitas merek yang sah. Rebranding adalah cakupan terpisah yang memerlukan permintaan eksplisit.

### Fase 5 — Perbaikan berurutan

1. **Spasi dan alignment:** gunakan skala konsisten; grid 4px hanya titik awal. Periksa tabel padat, sidebar, navigasi ringkas, dan mobile.
2. **Warna:** tetapkan peran background, surface, border, teks, aksen, dan status. Batasi aksen; periksa kontras semua tema/state. Warna grafik harus mewakili data.
3. **Ikon:** gunakan keluarga konsisten. Ganti emoji kontrol generik bila ikon lebih jelas; pertahankan simbol yang memang bagian identitas/konten. Beri nama aksesibel pada kontrol ikon.
4. **Copy:** buat judul spesifik; hapus klaim, jumlah pelanggan, testimoni, dan metrik yang tidak didukung. Tandai data contoh sebagai ilustrasi.
5. **Tipografi:** tetapkan skala display, heading, body, label, metadata; cek line-height, wrapping, angka, dan bahasa. Gunakan angka tabular bila membantu.
6. **Layout:** jaga arsitektur informasi kecuali diminta berubah. Pilih komposisi sesuai tugas; jangan memaksa dashboard padat menjadi kolom sempit atau semua konten menjadi kartu. Pastikan urutan mobile logis.
7. **Komponen dan data:** konsistenkan radius, border, shadow, dan elevasi. Rancang state aktif, selected, disabled, loading, sukses, error, serta data kosong/usang. Pilih visualisasi yang menjawab kebutuhan.
8. **Visual produk:** utamakan aset nyata, diagram, chart, objek render, atau ilustrasi yang menjelaskan produk. Jangan mengarang fitur atau bukti pelanggan. Gunakan gambar generatif hanya bila diminta atau ada kebutuhan visual jelas.
9. **Gerak:** gunakan untuk sebab-akibat, state, hierarki, atau ruang. Hormati reduced motion; hindari loop, flashing, dan gerak yang menghambat.

### Fase 6 — QA visual dan fungsi

Render dan bandingkan dengan baseline. Periksa temuan satu per satu, desktop/tablet/mobile, keyboard, fokus, target sentuh, kontras, reduced motion, alur terdampak, console, aset rusak, overflow, layout shift, dan loading bila alat tersedia. Pastikan fitur/rute/konten lama tetap bekerja.

### Fase 7 — Laporan

Ringkas arah visual, temuan, perubahan per fase, fitur yang dipertahankan, pemeriksaan responsif/aksesibilitas/interaksi, isu tersisa, asumsi, dan apakah hasil diterapkan pada proyek nyata atau hanya direkonstruksi dari screenshot. Jangan mengklaim tes yang tidak dilakukan.

## Kerangka keputusan

Tanyakan: apakah pilihan memperjelas produk/tugas, memperkuat hierarki, sesuai audiens/merek/konten, meningkatkan kegunaan dan aksesibilitas, memberi informasi bukan dekorasi, konsisten dengan sistem, serta sepadan dengan biaya implementasi/performa/pemeliharaan?

## Hubungan dan batas

Pola Navigasi Web Modern memiliki struktur navigasi; Micro-Interactions memiliki feedback komponen; Desain Frontend memiliki arah visual dan komposisi; Apple HIG memiliki kepatuhan platform. Skill ini memiliki kritik antarmuka AI dan penghilangan pola generik, bukan spesifikasi visual penuh atau implementasi interaksi.

## Batas sumber

Upstream Unslop membahas arah berbasis produk, audit layar, alur perbaikan, visual QA, dan panduan spasi/warna/ikon/copy/tipografi/layout/detail/visual/motion. Adaptasi ini menyusun ulang menjadi sembilan pass dan menambah pelestarian produk, keputusan desain, responsivitas, aksesibilitas, QA fungsi, dan pelaporan. Referensi upstream terpisah yang tidak tersedia pada path yang diperiksa tidak direproduksi; lihat upstream untuk versi lengkap.

## Klasifikasi

- Domain: Development / UI/UX
- Sumber: Unslop oleh Damir Sokolovsky, CC BY 4.0
- Penggunaan: audit UI, arah visual, redesign, polish, sistem responsif, dan QA visual
- Status: adaptasi dengan atribusi dan kerangka operasional tambahan.
