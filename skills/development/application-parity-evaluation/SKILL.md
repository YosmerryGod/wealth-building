---
name: application-parity-evaluation
title: Evaluasi Kesesuaian Aplikasi
category: development
subcategory: product-validation
source_type: original-adaptation-from-replica-skill
language: Indonesian
description: "Gunakan saat membandingkan implementasi dengan produk referensi atau matriks penerimaan untuk menemukan fitur yang belum terpenuhi dan perbedaan perilaku yang bermakna."
triggers: ["bandingkan aplikasi","feature parity","apa yang kurang dari clone","cek kesesuaian aplikasi","pemeriksaan kesesuaian","bandingkan fitur"]
out_of_scope: "Klaim kesamaan piksel sempurna, pengganti QA, atau keputusan izin hukum untuk meniru produk"
escalation: "Gunakan QA untuk verifikasi cacat yang dapat direproduksi, Penemuan Peluang Bisnis untuk masalah dan diferensiasi pelanggan, serta Penilaian Risiko untuk isu kekayaan intelektual/hukum."
---

# Evaluasi Kesesuaian Aplikasi

## Tujuan dan kepemilikan

Mengukur apakah implementasi mampu menyelesaikan pekerjaan pengguna dan memenuhi kriteria penerimaan. Menemukan perbedaan yang bermakna, kekurangan persyaratan, serta peningkatan yang perlu diprioritaskan.

Kesesuaian berarti kecukupan fungsi dan pengalaman untuk tujuan yang disepakati. Bukan izin menyalin ekspresi yang dilindungi atau mengejar kesamaan piksel dengan produk lain.

## 1. Tetapkan dasar perbandingan

Sebelum membandingkan, pastikan:
- matriks fitur dan kriteria penerimaan yang berlaku;
- peran pengguna, bentuk data, state, ukuran viewport, dan versi yang setara;
- sumber referensi dan bagian yang benar-benar dapat diamati;
- bukti yang tidak tersedia atau tidak dapat dibandingkan.

Jangan menyimpulkan perilaku internal yang tidak terlihat. Catat perbedaan lingkungan atau versi yang dapat memengaruhi hasil.

## 2. Ukur cakupan fitur

Klasifikasikan setiap persyaratan sebagai:
- **Lengkap:** memenuhi kriteria yang disepakati.
- **Sebagian:** tersedia, tetapi ada bagian alur atau kondisi yang belum terpenuhi.
- **Belum ada:** tidak tersedia atau tidak dapat diselesaikan.
- **Dikecualikan:** sengaja tidak dibuat, disertai alasan.

Gunakan bobot prioritas proyek bila tersedia. Jika tidak ada, jelaskan metode penilaian yang dipakai. Tampilkan pembilang, penyebut, bobot, dan rumus. Jangan mengarang persentase atau menyamakan jumlah layar dengan cakupan fungsi.

Contoh rumus berbobot:
Cakupan = total bobot persyaratan lengkap dan parsial sesuai nilai parsial / total bobot seluruh persyaratan × 100%.
Nilai parsial harus didefinisikan sebelum dihitung, bukan dipilih agar skor terlihat tinggi.

## 3. Bandingkan pengalaman dan perilaku

Periksa pada state yang sebanding:
- hierarki dan struktur informasi;
- penyelesaian tugas dan jumlah langkah;
- validasi, error, dan pemulihan;
- persistensi data dan konsistensi;
- izin serta perbedaan peran;
- perilaku responsif pada ukuran layar relevan.

Jangan menjadikan warna, logo, naskah, gambar, atau identitas khas milik pihak lain sebagai target peniruan. Pola kegunaan umum dapat menjadi referensi, tetapi ekspresi produk baru harus tetap berbeda.

## 4. Bedakan kekurangan dari perbedaan yang disengaja

Kelompokkan temuan menjadi:
1. **Kesenjangan wajib:** kriteria yang disepakati belum terpenuhi.
2. **Fitur kesetaraan opsional:** ada pada referensi tetapi bukan kebutuhan produk saat ini.
3. **Peningkatan berbasis umpan balik:** usulan yang didukung masalah pengguna.
4. **Divergensi disengaja:** keputusan desain atau fungsi yang berbeda dengan alasan jelas.

Perbedaan tidak otomatis merupakan cacat. Cacat yang perlu direproduksi dan diverifikasi menjadi tanggung jawab QA.

## 5. Prioritaskan perbaikan

Urutkan berdasarkan:
- dampak terhadap pekerjaan utama pengguna;
- kekuatan bukti dan frekuensi kejadian;
- upaya implementasi;
- dependensi teknis;
- risiko dan konsekuensi;
- kesesuaian dengan arah produk.

Tandai dampak yang belum terbukti sebagai hipotesis. Jangan menyamarkan preferensi visual sebagai kebutuhan pengguna tanpa bukti.

## 6. Format hasil evaluasi

Laporan memuat:
- ruang lingkup dan dasar perbandingan;
- sumber serta cakupan bukti;
- matriks fitur dan statusnya;
- metode, rumus, dan hasil perhitungan;
- perbedaan perilaku dan pengalaman;
- divergensi yang disengaja;
- persyaratan yang belum terpenuhi;
- daftar perbaikan berurutan;
- tingkat keyakinan dan keterbatasan evaluasi.

## Alur kerja

1. Konfirmasi matriks kebutuhan dan versi yang dibandingkan.
2. Kumpulkan bukti yang sepadan.
3. Nilai setiap fitur dan state.
4. Hitung cakupan dengan metode yang dinyatakan.
5. Pisahkan kesenjangan, opsi, peningkatan, dan divergensi.
6. Prioritaskan perbaikan berdasarkan dampak dan bukti.
7. Serahkan bug reproduktif kepada QA dan pekerjaan yang disetujui kepada engineering.

## Hubungan dan batas skill

- **Rekayasa Balik dan Rekonstruksi Berbasis Referensi** memiliki investigasi dan bukti produk referensi.
- **Pengujian Perangkat Lunak dan Jaminan Mutu** memiliki reproduksi bug, kasus uji, dan bukti regresi.
- **Penemuan Peluang Bisnis** menilai masalah pelanggan dan bukti permintaan.
- **Rekayasa Aplikasi Full-Stack** mengimplementasikan kesenjangan yang telah disetujui.
- **Desain Frontend** memiliki arah visual dan spesifikasi antarmuka.

Evaluasi Kesesuaian Aplikasi memiliki penilaian cakupan dan perbedaan terhadap persyaratan. Ia tidak menggantikan QA, tidak mengklaim kesamaan sempurna, dan tidak memutuskan kelayakan hukum peniruan.
