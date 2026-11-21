---
name: frontend-design
title: Desain Frontend
category: development
subcategory: product-design
source_type: original-adaptation-from-anthropic-frontend-design
language: Indonesian
description: "Menentukan arah visual dan rancangan antarmuka website atau aplikasi berdasarkan kebutuhan produk."
triggers: ["desain web","landing page","tampilan app","frontend","desain antarmuka"]
out_of_scope: "Rekonstruksi referensi, kepatuhan platform khusus, dan implementasi fitur menyeluruh"
escalation: "Serahkan investigasi referensi, implementasi, QA, dan kepatuhan platform kepada pemilik skill terkait."
---

# Desain Frontend

## Tujuan dan kepemilikan

Menentukan arah visual serta spesifikasi antarmuka yang khas, relevan dengan produk, mudah digunakan, responsif, dan dapat diterapkan. Skill ini memiliki keputusan desain visual, bukan implementasi seluruh fitur, arsitektur backend, atau pengujian rilis.

## 1. Pahami produk

Sebelum memilih gaya, identifikasi:
- Produk, domain, dan konteks penggunaan.
- Pengguna, tingkat pemahaman, serta kebutuhan utama.
- Pekerjaan terpenting yang harus diselesaikan.
- Lingkungan: desktop, mobile, tablet, atau lintas perangkat.
- Batasan: aset merek, stack, konten, aturan bisnis, aksesibilitas, dan preferensi yang disetujui.

Jika konteks penting belum tersedia, ajukan satu interpretasi konkret untuk dikonfirmasi. Gunakan konteks yang diketahui sebagai petunjuk, bukan alasan mengarang fakta. Jangan menyamakan desain POS, aplikasi komunikasi, terminal trading, dan situs restoran.

## 2. Tetapkan arah visual

Buat rencana desain ringkas:
- **Warna:** palet 4–6 warna dengan kode hex dan peran jelas untuk latar, permukaan, teks, aksen, serta status. Periksa kontras; jangan memilih warna hanya karena tren.
- **Tipografi:** satu atau dua keluarga font, skala ukuran, bobot, lebar, dan jarak yang konsisten. Hindari pilihan generik otomatis.
- **Tata letak:** jelaskan komposisi, perataan, hierarki, dan alasannya. Biarkan alur tugas menentukan struktur.
- **Ciri pembeda:** tentukan satu gagasan visual yang terkait dengan produk. Satu fokus kuat lebih efektif daripada dekorasi yang saling bersaing.

## 3. Jadikan struktur bermakna

Border menunjukkan kelompok; divider memisahkan konteks; label menjelaskan status atau tindakan; nomor menunjukkan urutan nyata; spasi memperjelas hierarki; ikon memperkuat konsep yang dikenali. Jangan menambah elemen untuk mengisi ruang. Hindari metadata tanpa fungsi, angka dekoratif, dan ornamen template.

## 4. Rancang kesan pertama

Pilih pembuka yang paling mewakili nilai produk: judul, gambar, demo, interaksi, atau tugas utama. Jangan otomatis memakai judul besar di tengah, gradasi, atau statistik besar. Untuk aplikasi kerja, utamakan tugas dan konteks kerja, bukan hero pemasaran.

## 5. Gerak dan konten antarmuka

Batasi animasi otomatis. Gerak akibat tindakan pengguna berguna bila menjelaskan perubahan, seperti panel terbuka atau penyimpanan berhasil. Jangan menghalangi konten atau memperlambat tugas. Gunakan [Micro-Interactions & UI Feedback Design](../micro-interactions-and-ui-feedback/SKILL.md) untuk pola feedback dan [Modern Web Navigation & Interaction Patterns](../modern-web-navigation-patterns/SKILL.md) untuk navigasi.

Tulis dari sudut pandang pengguna dengan nama tindakan konsisten, kalimat aktif, dan teks ringkas. Error harus menjelaskan kejadian serta cara memperbaiki. Empty state memberi petunjuk tindakan berikutnya.

## 6. Validasi rencana sebelum coding

Periksa:
1. Apakah desain tetap sama jika domain produk diganti?
2. Apakah ciri visual utama benar-benar terkait dengan produk?
3. Apakah hierarki mendukung tugas utama?
4. Apakah setiap label, garis, angka, dan dekorasi membawa informasi?
5. Adakah elemen yang hanya mengikuti kebiasaan desain generik AI?

Revisi pilihan generik sebelum implementasi.

## 7. Spesifikasi dan implementasi

Ikuti framework, komponen, dan arsitektur yang ada. Pisahkan token desain dari kode komponen. Tetapkan peran warna, skala tipografi/spasi, breakpoint, aturan layout, varian komponen, dan state interaksi. Gunakan HTML semantik serta pola aksesibel. Hindari dependensi dan efek dekoratif tanpa manfaat.

## 8. Kritik hasil

Periksa render/screenshot aktual bila tersedia. Nilai kekhasan produk, hierarki, tipografi, spasi, kejelasan konten, fungsi, responsivitas mobile, fokus keyboard, kontras, reduced motion, dan state loading/kosong/error/sukses/disabled. Hapus elemen tanpa fungsi; catat hal yang belum diuji dan jangan mengklaim review selesai tanpa bukti.

## Alur kerja

Pahami produk dan batasan → rencanakan arah visual → bandingkan bila perlu → revisi pilihan generik → serahkan spesifikasi → inspeksi hasil dan perbaiki isu utama.

## Hubungan dan batas

Rekayasa Balik memiliki bukti referensi; AI Interface Design mengaudit pola generik; Apple HIG Review memeriksa konvensi Apple; Micro-Interactions memiliki feedback; Modern Web Navigation memiliki navigasi; Professional Logo memiliki identitas merek; Full-Stack mengimplementasikan fitur; QA memverifikasi fungsi/regresi. Desain Frontend memiliki arah visual dan spesifikasi antarmuka.

## Sumber

Diadaptasi dan ditulis ulang dari **Frontend Design** oleh Anthropic: https://github.com/anthropics/skills/tree/main/skills/frontend-design. Sumber berlisensi Apache License 2.0; atribusi dan lisensi dipertahankan dalam direktori ini. Panduan tambahan merupakan sintesis khusus repositori.
