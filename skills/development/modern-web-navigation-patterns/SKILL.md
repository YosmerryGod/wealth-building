---
name: modern-web-navigation-patterns
title: Pola Navigasi dan Interaksi Web Modern
category: development
source_type: user-provided-video-and-operational-framework
source: Video pengguna 67567.mp4 dan 67562.mp4
language: Indonesian
description: "Memilih dan merancang pola navigasi global website atau aplikasi berdasarkan struktur informasi, tugas, dan perangkat."
triggers: ["navbar","bottom tab","menu navigasi","command palette","radial sidebar","vertical typography","scroll progress"]
out_of_scope: "Desain visual menyeluruh, paginasi dalam koleksi, atau animasi feedback terperinci"
escalation: "Serahkan desain visual kepada Desain Frontend, paginasi kepada Pola Paginasi Tingkat Lanjut, dan feedback mikro kepada pemilik skill terkait."
---

# Pola Navigasi dan Interaksi Web Modern

## Tujuan dan batas

Memilih pola navigasi agar produk mudah dipahami, cepat digunakan, responsif, aksesibel, dan konsisten. Pola harus mengikuti arsitektur informasi, tugas pengguna, perangkat, dan kompleksitas; tidak ada satu gaya yang cocok untuk semua produk.

Skill ini memiliki navigasi antarbagian dan tujuan produk. Perpindahan halaman di dalam satu koleksi adalah milik Pola Paginasi dan Navigasi Data Tingkat Lanjut.

## Pola dari sumber video

### 1. Floating Pill Navigation
Kelompok tautan ringkas dalam wadah berbentuk pil, dapat mengambang atau berada di header.
- Cocok untuk landing page dengan sedikit tujuan utama.
- Batasi tujuan, bedakan item aktif, sediakan area sentuh cukup, dan jangan menutupi konten.
- Pada layar kecil, tentukan apakah navigasi membungkus, digulir, diringkas, atau diganti.
- Hindari jika tujuan banyak, hierarki dalam, atau elemen menghalangi tugas.

### 2. Bottom Tab Bar
Navigasi di bagian bawah untuk berpindah antarbagian utama.
- Cocok untuk aplikasi mobile dengan sedikit bagian yang sering dipakai.
- Gunakan hanya untuk tujuan tingkat atas; ikon dan label harus mudah dikenali.
- Perhitungkan safe area dan ruang konten agar bar tidak menutupi form atau tombol.
- Hindari terlalu banyak tab atau konflik dengan kontrol sistem.

### 3. Command Palette (Ctrl+K)
Antarmuka pencarian/perintah berbasis keyboard, umumnya Ctrl+K atau Cmd+K.
- Cocok untuk dashboard kompleks, alat admin, developer, dan produktivitas.
- Sediakan cara visual untuk membukanya; shortcut bukan satu-satunya akses.
- Kelompokkan halaman, tindakan, dan item terbaru. Dukung panah, Enter, Escape, fokus, loading, dan hasil kosong.
- Jangan tampilkan tindakan yang tidak diizinkan untuk pengguna.

### 4. Radial Sidebar
Tujuan sekunder disusun melingkar mengitari titik pusat.
- Cocok untuk portofolio kreatif atau pengalaman eksploratif dengan sedikit tujuan.
- Beri label jelas, urutan fokus logis, dan area sentuh yang tidak tumpang tindih.
- Sediakan menu konvensional untuk mobile, keyboard, dan teknologi bantu.
- Hindari untuk dashboard padat atau alur kerja yang menuntut pemindaian cepat.

### 5. Vertical Typography Navigation
Label navigasi disusun vertikal sebagai bagian komposisi tipografi.
- Cocok untuk editorial, portofolio, studio kreatif, dan landing page berarah seni.
- Pastikan label terbaca, urutan baca/fokus logis, dan state aktif/fokus terlihat.
- Gunakan pola horizontal atau konvensional pada breakpoint sempit bila perlu.
- Hindari bila label panjang atau gaya vertikal mengurangi keterbacaan.

### 6. Scroll Progress Navigation
Indikator posisi pada halaman panjang dengan penanda bagian yang dapat dipilih.
- Cocok untuk storytelling, studi kasus, editorial, dan landing page multi-bagian.
- Hubungkan tiap penanda ke bagian bernama; tampilkan bagian aktif dan dukung klik langsung.
- Perhitungkan header sticky, deep link, history, konten dinamis, dan posisi mobile.
- Hindari untuk halaman pendek atau tanpa struktur bagian yang bermakna.

## Memilih pola

Nilai jenis produk, jumlah/kedalaman tujuan, tugas yang sering dilakukan, perangkat/input, pengalaman pengguna, aksesibilitas, ruang konten, serta biaya kompleksitas.

| Konteks | Pola awal | Catatan |
|---|---|---|
| Website pemasaran sederhana | Header atau Floating Pill | Tujuan sedikit dan jelas |
| Aplikasi mobile | Bottom Tab Bar | Hanya bagian utama |
| Dashboard kompleks | Navigasi terlihat + Command Palette | Palette hanya jalan pintas |
| Website konten | Header/sidebar berbasis hierarki | Susun kategori dahulu |
| Portofolio kreatif | Radial atau Vertical Typography | Label dan fallback jelas |
| Cerita panjang | Scroll Progress | Gunakan bagian nyata |

Ini titik awal, bukan aturan kaku. Kombinasikan pola hanya bila masing-masing punya fungsi berbeda.

## Alur implementasi

1. Periksa framework, router, layout, token, breakpoint, dan navigasi yang ada.
2. Petakan tujuan tingkat atas, halaman turunan, dan tindakan; pisahkan navigasi dari aksi seperti simpan/kirim.
3. Pilih pola paling sederhana yang mendukung tugas.
4. Tentukan perilaku desktop, tablet, dan mobile.
5. Rancang state aktif, hover, fokus, disabled, terbuka, tertutup, loading, dan kosong sesuai kebutuhan.
6. Gunakan landmark navigasi, tautan untuk tujuan, tombol untuk aksi, nama aksesibel, dan fokus terlihat.
7. Pertahankan komponen, router, dan gaya proyek.
8. Uji route, back/forward, refresh rute turunan, keyboard, touch, safe area, breakpoint, serta akurasi anchor.
9. Pastikan tujuan mudah ditemukan tanpa gestur tersembunyi.

## Pemeriksaan mutu

- Tujuan utama mudah ditemukan dan state aktif jelas.
- Keyboard, touch, fokus, label, dan nama aksesibel berfungsi.
- Navigasi tidak menutupi konten atau area sistem.
- Perilaku responsif dirancang, bukan sekadar mengecilkan layout.
- Deep link dan browser navigation bekerja.
- Radial/vertical memiliki fallback.
- Scroll progress mengikuti bagian aktual.
- Kompleksitas tambahan memberi manfaat nyata.

## Aturan implementasi AI

Periksa codebase sebelum mengubah navigasi. Ubah cakupan yang diminta saja. Jangan menganggap pola modern otomatis lebih mudah digunakan, jangan mengganti navigasi terlihat dengan palette, jangan memakai ikon tanpa nama aksesibel, dan jangan menyembunyikan aksi penting pada hover. Bila pilihan berdampak besar belum jelas, ajukan satu pertanyaan terarah.

## Hubungan skill

Desain Frontend memiliki arah visual; AI Interface Design mengaudit kekhasan dan pola generik; Pola Paginasi menangani halaman dalam koleksi; Full-Stack mengimplementasikan komponen dan rute; aksesibilitas memberi audit lebih mendalam. Skill ini tidak menggantikan rekayasa frontend atau riset UX.

## Batas bukti sumber

Video 67567.mp4 menunjukkan Floating Pill, Bottom Tab Bar, dan Command Palette. Video 67562.mp4 menunjukkan Radial Sidebar, Vertical Typography, dan Scroll Progress. Video tidak menyediakan kode, riset usability, pengukuran performa, atau bukti keunggulan universal. Kriteria seleksi, aksesibilitas, fallback, implementasi, dan pengujian adalah panduan operasional tambahan.
