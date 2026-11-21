---
name: frontend-design
title: Desain Frontend
category: development
subcategory: product-design
source_type: original-adaptation-from-anthropic-frontend-design
language: Indonesian
description: "Gunakan saat merancang arah visual dan pengalaman antarmuka website atau aplikasi berdasarkan kebutuhan produk."
triggers: ["desain web","landing page","tampilan app","frontend","desain antarmuka"]
out_of_scope: "Kepatuhan platform khusus, rekonstruksi referensi, dan implementasi fitur aplikasi secara menyeluruh"
escalation: "Serahkan investigasi referensi, implementasi, QA, serta kepatuhan platform kepada pemilik skill terkait; gunakan Penilaian Risiko untuk risiko material."
---

# Desain Frontend

## Tujuan dan kepemilikan

Menentukan arah visual dan rancangan antarmuka yang khas, relevan dengan produk, mudah digunakan, responsif, dan dapat diterapkan. Skill ini menjadi pemilik keputusan desain visual dan spesifikasi frontend, bukan pemilik implementasi seluruh fitur, arsitektur backend, atau pengujian rilis.

Gunakan untuk membuat website/aplikasi baru atau merombak bahasa visual antarmuka yang sudah ada. Gabungkan dengan skill engineering, navigasi, audit UI, dan micro-interaction hanya jika cakupannya diperlukan.

## 1. Pahami produk sebelum memilih gaya

Identifikasi:
- **Produk dan domain:** apa yang dibuat dan istilah atau pola yang memang relevan.
- **Pengguna:** siapa yang memakai, tingkat pemahaman, dan kebutuhan utamanya.
- **Pekerjaan utama:** tugas yang harus paling mudah diselesaikan.
- **Lingkungan:** desktop, mobile, tablet, kiosk, atau lintas perangkat.
- **Batasan:** aset merek, stack, konten, aturan bisnis, aksesibilitas, dan preferensi yang sudah disetujui.

Jika konteks penting belum tersedia, ajukan satu interpretasi konkret untuk dikonfirmasi sebelum mengunci arah desain. Gunakan konteks produk yang diketahui sebagai petunjuk, bukan alasan untuk mengarang fakta.

Jangan menyamakan desain aplikasi komunikasi, POS, terminal trading, dan situs restoran hanya karena semuanya antarmuka web.

## 2. Tetapkan arah visual yang khas

Buat rencana desain ringkas sebelum implementasi.

### Warna
Tentukan palet inti 4–6 warna beserta kode hex dan perannya: latar, permukaan, teks utama, teks sekunder, aksen, serta status bila diperlukan. Periksa kontras. Jangan memilih warna hanya karena sedang tren.

### Tipografi
Pilih satu atau dua keluarga font dengan peran jelas. Tetapkan skala ukuran, bobot, lebar, dan jarak. Hindari otomatis memakai font umum atau memberi aksen pada satu kata di setiap judul.

### Tata letak
Jelaskan komposisi, perataan, hierarki, dan alasan pemilihannya. Gunakan sketsa sederhana bila membantu. Biarkan alur tugas dan hubungan informasi menentukan struktur.

### Ciri pembeda
Tentukan satu gagasan visual yang mudah diingat beserta prinsip pendukungnya. Gunakan penekanan secara terarah; satu fokus kuat biasanya lebih efektif daripada banyak dekorasi yang saling bersaing.

## 3. Jadikan struktur visual bermakna

- Border dan outline menunjukkan kelompok atau batas yang nyata.
- Divider memisahkan konteks atau bagian yang berkaitan.
- Label menjelaskan status, kategori, kepemilikan, atau tindakan.
- Nomor menunjukkan urutan atau proses yang benar-benar ada.
- Spasi memperjelas hierarki dan hubungan.
- Ikon memperkuat tindakan atau konsep yang dikenali.

Jangan menambahkan elemen untuk sekadar mengisi ruang. Hindari label kecil berulang, angka dekoratif, metadata tanpa fungsi, dan ornamen template generik.

## 4. Rancang kesan pertama sesuai fungsi

Untuk halaman web, tentukan hal pertama yang perlu dipahami pengguna. Pembuka dapat berupa judul, gambar produk, demo langsung, interaksi, tugas utama, atau pendekatan lain yang paling mewakili nilai produk.

Jangan otomatis memakai judul besar di tengah, aksen gradasi, atau statistik berukuran besar. Untuk aplikasi kerja, utamakan tugas utama dan konteks kerja; jangan memaksakan hero pemasaran.

## 5. Gunakan gerak dan interaksi dengan tujuan

Batasi animasi yang berjalan tanpa tindakan pengguna. Satu rangkaian entrance/reveal yang terarah biasanya lebih baik daripada animasi acak pada setiap bagian.

Animasi akibat tindakan pengguna berguna bila menjelaskan perubahan, misalnya panel terbuka, detail diperluas, penyimpanan berhasil, atau perpindahan konteks. Jangan menghalangi konten atau memperlambat tugas rutin.

Untuk pola feedback terperinci, gunakan [Micro-Interactions & UI Feedback Design](../micro-interactions-and-ui-feedback/SKILL.md). Untuk navigasi, gunakan [Modern Web Navigation & Interaction Patterns](../modern-web-navigation-patterns/SKILL.md).

## 6. Tulis konten antarmuka sebagai bagian desain

- Tulis dari sudut pandang pengguna akhir.
- Gunakan nama yang sederhana dan spesifik, bukan istilah internal implementasi.
- Utamakan kalimat aktif dan ringkas.
- Pastikan setiap teks memiliki satu fungsi.
- Jaga konsistensi nama tindakan dan konfirmasi.
- Jelaskan error: apa yang terjadi dan cara memperbaikinya.
- Jadikan empty state sebagai petunjuk tindakan berikutnya.
- Sesuaikan nada dengan produk tanpa mengorbankan kejelasan.

## 7. Uji rencana terhadap kebutuhan

Sebelum coding, periksa:
1. Apakah palet, tipografi, tata letak, dan komponen ini akan sama jika produknya diganti dengan domain lain?
2. Apakah ciri visual utama benar-benar terkait dengan produk?
3. Apakah hierarki mendukung tugas utama?
4. Apakah label, border, angka, dan dekorasi menyampaikan informasi?
5. Adakah elemen yang hanya muncul karena kebiasaan desain generik AI?

Perbaiki pilihan generik dan catat alasan perubahannya. Mulai implementasi setelah arah desain memiliki dasar yang jelas.

## 8. Siapkan spesifikasi yang dapat dibangun

- Ikuti framework, konvensi komponen, dan arsitektur proyek yang ada.
- Gunakan komponen ulang untuk konsistensi, bukan memaksa semua bagian menjadi kartu seragam.
- Pisahkan token desain dari kode komponen.
- Tetapkan peran token warna, skala tipografi dan spasi, breakpoint, aturan layout, varian komponen, serta state interaksi.
- Gunakan HTML semantik dan pola interaksi yang aksesibel.
- Pertahankan fungsi serta konten produk yang nyata.
- Hindari dependensi dan efek dekoratif yang menambah kompleksitas tanpa manfaat.

## 9. Kritik hasil implementasi

Jika lingkungan mendukung screenshot, periksa hasil render aktual, bukan hanya source code. Nilai:
- kekhasan produk dan arah visual;
- hierarki, tipografi, perataan, spasi, dan kejelasan konten;
- konsistensi tanpa pengulangan monoton;
- penyelesaian tugas dan state fungsional;
- responsivitas hingga mobile;
- fokus keyboard dan kemudahan penggunaan keyboard;
- kontras serta keterbacaan;
- preferensi reduced motion;
- state loading, kosong, error, sukses, dan disabled.

Hapus setidaknya satu elemen visual yang tidak membantu pemahaman, identitas, atau penyelesaian tugas. Catat isu yang belum diperiksa; jangan mengklaim QA selesai bila antarmuka belum dirender atau diuji.

## 10. Alur kerja

1. **Temukan konteks:** produk, pengguna, tugas utama, lingkungan, dan batasan.
2. **Rencanakan:** palet, tipografi, tata letak, hierarki, dan ciri pembeda.
3. **Bandingkan:** buat alternatif bila arah belum jelas.
4. **Tinjau:** tantang pilihan generik dan revisi.
5. **Serahkan untuk implementasi:** berikan spesifikasi yang disetujui kepada engineering.
6. **Inspeksi:** periksa screenshot atau antarmuka aktual.
7. **Kritik:** nilai kegunaan, responsivitas, aksesibilitas, dan state.
8. **Perbaiki:** prioritaskan masalah berdampak tinggi.

## Hubungan dan batas skill

- **Rekayasa Balik dan Rekonstruksi Berbasis Referensi:** mengumpulkan bukti dari produk referensi sebelum desain baru ditentukan.
- **AI Interface Design & Unslop Engineering:** mengaudit kekhasan produk dan pola UI generik.
- **Apple Platform Design & HIG Review:** meninjau konvensi platform Apple.
- **Micro-Interactions & UI Feedback Design:** merancang state feedback dan gerak.
- **Modern Web Navigation & Interaction Patterns:** merancang navigasi global.
- **Professional Logo & Brand Identity:** membuat identitas merek; Desain Frontend menerapkannya pada antarmuka.
- **Rekayasa Aplikasi Full-Stack:** mengimplementasikan fitur berdasarkan spesifikasi yang disetujui.
- **Software Testing & Quality Assurance:** memverifikasi fungsi dan regresi.

Desain Frontend memiliki keputusan arah visual dan spesifikasi antarmuka. Ia tidak mengambil alih investigasi referensi, arsitektur sistem, implementasi fitur, QA, atau keputusan rilis.

## Sumber dan adaptasi

Sintesis operasional ini diadaptasi dan ditulis ulang dari skill **Frontend Design** milik Anthropic: https://github.com/anthropics/skills/tree/main/skills/frontend-design. Sumber berlisensi Apache License 2.0; atribusi dan lisensi dipertahankan dalam direktori ini. Panduan implementasi, review, dan routing tambahan merupakan sintesis khusus repositori.
