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

1. **Floating Pill Navigation:** tautan utama dalam wadah pil; cocok untuk website dengan sedikit tujuan. Bedakan state aktif, jaga area sentuh, dan pastikan tidak menutupi konten. Pada mobile, tentukan wrap, scroll, collapse, atau pengganti.
2. **Bottom Tab Bar:** navigasi bawah untuk bagian utama aplikasi mobile. Batasi tab, gunakan label/ikon jelas, hormati safe area, dan jangan menutupi konten atau aksi.
3. **Command Palette (Ctrl+K/Cmd+K):** pencarian tujuan/aksi berbasis keyboard untuk dashboard kompleks. Sediakan pemicu visual, kelompok hasil, dukung panah/Enter/Escape, fokus, loading/kosong, dan izin pengguna.
4. **Radial Sidebar:** tujuan melingkar untuk portofolio/landing kreatif dengan pilihan sedikit. Beri label, urutan fokus, target sentuh, serta fallback konvensional. Hindari dashboard padat.
5. **Vertical Typography:** label vertikal untuk editorial/portofolio. Jaga keterbacaan, urutan baca/fokus, dan fallback horizontal di layar sempit.
6. **Scroll Progress:** penanda bagian pada halaman panjang. Hubungkan ke section nyata, tampilkan posisi aktif, dukung anchor, header sticky, deep link, dan alternatif mobile.

Video tidak menyediakan kode, riset usability, atau pengukuran performa. Panduan seleksi dan implementasi adalah sintesis operasional.

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

Pastikan tujuan mudah ditemukan, state aktif jelas, keyboard/touch/fokus/label aksesibel berfungsi, layout tidak menutupi konten atau area sistem, breakpoint dirancang, deep link/back-forward bekerja, radial/vertical memiliki fallback, dan scroll progress mengikuti section aktual.

## Hubungan skill

Desain Frontend memiliki arah visual; AI Interface Design mengaudit pola generik; Paginasi Tingkat Lanjut memiliki navigasi halaman dalam koleksi; Full-Stack mengimplementasikan; QA memverifikasi. Skill ini fokus pada navigasi global.