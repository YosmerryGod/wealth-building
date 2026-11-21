---
name: software-testing-and-quality-assurance
title: Pengujian Perangkat Lunak dan Jaminan Mutu
category: development
subcategory: software-quality
source_type: original-adaptation-from-replica-skill
language: Indonesian
description: "Menyusun rencana pengujian, mereproduksi bug, menguji alur aplikasi, membuat tes otomatis, dan menilai mutu rilis."
triggers: ["test aplikasi","QA aplikasi","cari bug","buat E2E test","uji semua fitur","software testing","pengujian regresi"]
out_of_scope: "Implementasi fitur, penetapan kepatuhan hukum, atau otorisasi rilis produksi"
escalation: "Serahkan cacat reproduktif kepada pemilik implementasi, risiko keamanan/privasi kepada Penilaian Risiko, dan keputusan rilis kepada Rekayasa Deployment dan Rilis."
---

# Pengujian Perangkat Lunak dan Jaminan Mutu

## Tujuan dan kepemilikan

Memverifikasi pemenuhan kriteria penerimaan melalui bukti yang dapat diulang. Skill ini memiliki metode pengujian dan verifikasi cacat, bukan implementasi fitur, evaluasi kesetaraan referensi, atau persetujuan rilis. Uji hanya produk dan lingkungan yang dimiliki atau diizinkan.

## 1. Susun kasus uji

Untuk setiap alur penting, tentukan:
- Alur normal dari tindakan awal hingga hasil yang diharapkan.
- Validasi dan kondisi negatif: input kosong/salah, batas nilai, serta tindakan yang ditolak.
- State antarmuka: kosong, loading, sukses, error, dan disabled.
- Hak akses: peran, izin, dan batas data antar-pengguna.
- Data: persistensi, perubahan, duplikasi, konsistensi, dan konkurensi.
- Pemulihan: gangguan jaringan, timeout, percobaan ulang, dan kegagalan.
- Penggunaan: keyboard, mobile, aksesibilitas, dan ukuran layar relevan.

Prioritaskan alur berdasarkan kepentingan tugas dan risiko kegagalan.

## 2. Pilih tingkat pengujian

- **Unit test:** logika deterministik atau fungsi terisolasi.
- **Integration test:** kontrak modul, API, database, dan layanan.
- **End-to-end test:** perjalanan pengguna dari awal hingga hasil.
- **Visual regression:** perubahan tampilan tak disengaja bila relevan.
- **Accessibility check:** semantik, fokus, keyboard, label, dan kontras.

Utamakan selector berdasarkan role atau label yang stabil. Hindari selector CSS yang rapuh.

## 3. Eksekusi dengan aman

Gunakan lokal/staging dan data sintetis. Jangan melakukan load test, fuzzing, scraping, atau otomatisasi pada produksi pihak ketiga tanpa izin. Gunakan sandbox pembayaran. Lindungi data pribadi dan hapus rahasia dari log, screenshot, serta laporan. Catat versi aplikasi, konfigurasi, perangkat, browser, dan lingkungan.

## 4. Verifikasi dan catat cacat

Cacat terkonfirmasi harus memuat:
- ID dan tingkat keparahan;
- build dan lingkungan;
- langkah reproduksi;
- hasil yang diharapkan dan aktual;
- bukti yang dibersihkan dari rahasia;
- alur terdampak dan workaround bila ada.

Pisahkan dugaan yang belum direproduksi dari bug terkonfirmasi.

## 5. Perbaikan dan regresi

Prioritaskan cacat kritis dan mayor. Serahkan temuan beserta bukti kepada pemilik implementasi. Tambahkan regression test, jalankan ulang pengujian terkait setelah perbaikan, dan perluas suite bila dampaknya lintas fitur. Catat tes gagal, dilewati, terblokir, atau belum dijalankan.

## 6. Pelaporan

Laporan memuat cakupan dan lingkungan, kriteria yang diuji, tes yang benar-benar dijalankan, jumlah lulus/gagal/dilewati/terblokir, cacat berdasarkan keparahan, pemeriksaan tersisa, dan penghambat rilis. Jangan menyebut rencana atau tes yang belum dijalankan sebagai lulus. Keberhasilan seluruh tes yang tersedia bukan bukti bahwa aplikasi bebas bug.

## Alur kerja

1. Pahami kebutuhan dan kriteria penerimaan.
2. Susun matriks kasus uji berdasarkan alur dan risiko.
3. Pilih tingkat tes serta lingkungan aman.
4. Jalankan tes dan simpan bukti.
5. Verifikasi temuan yang belum pasti.
6. Serahkan cacat kepada pemilik implementasi.
7. Uji perbaikan dan regresi.
8. Laporkan hasil serta keterbatasan.

## Hubungan dan batas

Full-Stack dan Backend memiliki implementasi/perbaikan kode. Evaluasi Kesesuaian Aplikasi membandingkan cakupan terhadap matriks kebutuhan. Deployment menggunakan bukti QA sebagai gerbang rilis. Penilaian Risiko menangani konsekuensi keamanan/privasi. Desain Frontend memiliki arah visual; QA menguji perilaku antarmuka dan aksesibilitas. QA tidak menentukan fitur referensi mana yang harus ditiru atau kelayakan bisnis produk.
