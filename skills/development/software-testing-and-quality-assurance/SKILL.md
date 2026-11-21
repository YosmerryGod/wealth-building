---
name: software-testing-and-quality-assurance
title: Pengujian Perangkat Lunak dan Jaminan Mutu
category: development
subcategory: software-quality
source_type: original-adaptation-from-replica-skill
language: Indonesian
description: "Gunakan saat menyusun rencana pengujian, mereproduksi bug, menguji alur aplikasi, membuat pengujian otomatis, atau menilai mutu rilis."
triggers: ["test aplikasi","QA aplikasi","cari bug","buat E2E test","uji semua fitur","software testing","pengujian regresi"]
out_of_scope: "Implementasi fitur produk, penetapan kepatuhan hukum, atau otorisasi rilis produksi"
escalation: "Kembalikan cacat yang dapat direproduksi kepada pemilik implementasi; serahkan risiko keamanan/privasi kepada Penilaian Risiko dan keputusan rilis kepada Rekayasa Deployment dan Rilis."
---

# Pengujian Perangkat Lunak dan Jaminan Mutu

## Tujuan dan kepemilikan

Memverifikasi bahwa aplikasi memenuhi kriteria penerimaan melalui bukti yang dapat diulang. Skill ini memiliki metode pengujian dan verifikasi cacat; bukan pemilik implementasi fitur, penilaian kesetaraan dengan produk referensi, atau persetujuan rilis produksi.

Uji produk pengguna pada lingkungan yang dimiliki atau secara eksplisit diizinkan. Jangan menguji sistem produksi pihak ketiga tanpa otorisasi.

## 1. Turunkan kasus uji dari kriteria penerimaan

Untuk setiap alur penting, tentukan:
- **Alur normal:** tindakan pengguna dari awal sampai hasil yang diharapkan.
- **Validasi dan kondisi negatif:** input kosong, format salah, batas nilai, dan tindakan yang ditolak.
- **State antarmuka:** kosong, loading, sukses, error, dan disabled.
- **Hak akses:** peran, izin, batas antar-pengguna, dan akses langsung ke sumber daya.
- **Data:** persistensi, perubahan, duplikasi pengiriman, konsistensi, dan konkurensi.
- **Pemulihan:** gangguan jaringan, timeout, percobaan ulang, dan pemulihan setelah kegagalan.
- **Penggunaan:** keyboard, perangkat mobile, aksesibilitas, dan ukuran layar yang relevan.

Prioritaskan alur yang paling penting bagi pekerjaan pengguna dan risiko kegagalannya.

## 2. Pilih tingkat pengujian

- **Unit test:** logika deterministik atau fungsi terisolasi.
- **Integration test:** kontrak antarmodul, API, database, dan layanan.
- **End-to-end test:** perjalanan pengguna dari awal hingga hasil pada aplikasi.
- **Visual regression:** perubahan tampilan yang tidak disengaja, bila relevan.
- **Accessibility check:** semantik, fokus, keyboard, label, dan kontras.

Gunakan selector berdasarkan role, label, atau teks yang stabil. Hindari selector CSS rapuh yang bergantung pada struktur internal.

## 3. Jalankan pengujian dengan aman

- Utamakan lingkungan lokal atau staging dan data sintetis.
- Jangan melakukan load test, fuzzing, scraping, atau otomatisasi pada layanan produksi pihak ketiga tanpa izin.
- Gunakan mode sandbox untuk pembayaran dan integrasi yang dapat menimbulkan transaksi.
- Lindungi data pribadi dan hapus rahasia dari log, screenshot, serta laporan.
- Catat versi aplikasi, konfigurasi penting, perangkat, browser, dan lingkungan pengujian.

## 4. Catat bukti cacat

Cacat terkonfirmasi harus memiliki:
- ID dan tingkat keparahan;
- build serta lingkungan yang diuji;
- langkah reproduksi yang tepat;
- hasil yang diharapkan dan hasil aktual;
- bukti yang sudah dibersihkan dari rahasia;
- alur atau pengguna yang terdampak;
- workaround bila tersedia.

Pisahkan dugaan yang belum berhasil direproduksi ke daftar investigasi. Jangan menyebut dugaan sebagai bug terkonfirmasi.

## 5. Perbaikan dan regresi

1. Urutkan cacat kritis dan mayor terlebih dahulu.
2. Serahkan temuan kepada pemilik implementasi dengan bukti reproduksi.
3. Tambahkan regression test untuk mencegah cacat yang sama muncul kembali.
4. Jalankan ulang pengujian terkait setelah perbaikan.
5. Jalankan suite yang lebih luas bila perubahan berpotensi berdampak lintas fitur.
6. Catat pengujian yang gagal, dilewati, diblokir, atau belum dijalankan.

## 6. Penilaian mutu dan pelaporan

Laporan harus memuat:
- cakupan dan lingkungan pengujian;
- kriteria penerimaan yang diuji;
- daftar pengujian yang benar-benar dijalankan;
- jumlah lulus, gagal, dilewati, dan terblokir;
- cacat terkonfirmasi berdasarkan keparahan;
- pemeriksaan yang belum selesai;
- penghambat rilis yang ditemukan.

Jangan melaporkan rencana atau pengujian yang belum dijalankan sebagai lulus. Jangan menyimpulkan aplikasi bebas bug hanya karena semua kasus yang tersedia berhasil.

## Alur kerja

1. Pahami kebutuhan dan kriteria penerimaan.
2. Susun matriks kasus uji berdasarkan alur dan risiko.
3. Pilih tingkat pengujian serta lingkungan yang aman.
4. Jalankan pengujian dan simpan bukti.
5. Verifikasi ulang temuan yang belum pasti.
6. Serahkan cacat kepada pemilik implementasi.
7. Uji perbaikan dan regresi.
8. Laporkan hasil, batas cakupan, serta risiko yang tersisa.

## Hubungan dan batas skill

- **Rekayasa Aplikasi Full-Stack** dan **Rekayasa Backend dan Integrasi** memiliki implementasi dan perbaikan kode.
- **Evaluasi Kesesuaian Aplikasi** membandingkan cakupan fitur dan perbedaan terhadap matriks kebutuhan atau referensi.
- **Rekayasa Deployment dan Rilis Aplikasi** menggunakan bukti QA sebagai salah satu gerbang rilis.
- **Penilaian Risiko** menangani konsekuensi keamanan dan privasi yang material.
- **Desain Frontend** memiliki arah visual; QA memverifikasi perilaku antarmuka dan aksesibilitas yang dapat diuji.

QA memastikan perilaku terhadap kriteria penerimaan. QA tidak menentukan apakah semua fitur referensi harus ditiru atau apakah produk layak secara bisnis.
