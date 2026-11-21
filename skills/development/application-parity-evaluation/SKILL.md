---
name: application-parity-evaluation
title: Evaluasi Kesesuaian Aplikasi
category: development
subcategory: product-validation
source_type: original-adaptation-from-replica-skill
language: Indonesian
description: "Membandingkan implementasi dengan produk referensi atau matriks penerimaan untuk menemukan fitur yang belum terpenuhi dan perbedaan bermakna."
triggers: ["bandingkan aplikasi","feature parity","apa yang kurang dari clone","cek kesesuaian aplikasi","pemeriksaan kesesuaian","bandingkan fitur"]
out_of_scope: "Klaim kesamaan piksel sempurna, pengganti QA, atau keputusan izin hukum untuk meniru produk"
escalation: "Gunakan QA untuk verifikasi cacat, Penemuan Peluang Bisnis untuk masalah pelanggan, dan Penilaian Risiko untuk isu kekayaan intelektual/hukum."
---

# Evaluasi Kesesuaian Aplikasi

## Tujuan dan kepemilikan

Mengukur apakah implementasi menyelesaikan pekerjaan pengguna dan memenuhi kriteria penerimaan. Skill ini menilai cakupan fitur, perbedaan pengalaman, dan prioritas perbaikan. Kesesuaian berarti kecukupan fungsi, bukan izin menyalin ekspresi yang dilindungi atau mengejar kesamaan piksel.

## 1. Tetapkan dasar perbandingan

Pastikan matriks fitur/kriteria penerimaan, peran pengguna, bentuk data, state, ukuran viewport, dan versi yang sebanding. Catat sumber referensi, bagian yang benar-benar diamati, serta bukti yang tidak tersedia. Jangan menyimpulkan perilaku internal yang tidak terlihat.

## 2. Ukur cakupan

Klasifikasikan setiap persyaratan:
- **Lengkap:** memenuhi kriteria.
- **Sebagian:** tersedia, tetapi ada bagian alur atau kondisi yang belum terpenuhi.
- **Belum ada:** tidak tersedia atau tidak dapat diselesaikan.
- **Dikecualikan:** sengaja tidak dibuat dengan alasan yang dicatat.

Gunakan bobot prioritas proyek bila ada. Jika tidak, nyatakan metode yang dipakai. Tampilkan pembilang, penyebut, bobot, dan rumus; jangan mengarang persentase atau menyamakan jumlah layar dengan cakupan fungsi.

Rumus berbobot: cakupan = total bobot persyaratan lengkap dan nilai parsial yang disepakati / total bobot seluruh persyaratan × 100%. Tetapkan nilai parsial sebelum menghitung.

## 3. Bandingkan perilaku

Pada state yang sebanding, periksa hierarki informasi, penyelesaian tugas/langkah, validasi, error dan pemulihan, persistensi data, konsistensi, izin, serta responsivitas. Jangan menjadikan warna, logo, naskah, gambar, atau identitas khas pihak lain sebagai target peniruan. Gunakan pola kegunaan umum tanpa menyalin ekspresi produk.

## 4. Pisahkan kesenjangan dan perbedaan

Kelompokkan temuan:
1. **Kesenjangan wajib:** kriteria yang disepakati belum terpenuhi.
2. **Fitur opsional:** ada pada referensi tetapi bukan kebutuhan saat ini.
3. **Peningkatan dari umpan balik:** didukung masalah pengguna.
4. **Divergensi disengaja:** perbedaan desain/fungsi dengan alasan jelas.

Perbedaan tidak otomatis cacat. Bug yang harus direproduksi dan diverifikasi menjadi tanggung jawab QA.

## 5. Prioritaskan

Urutkan berdasarkan dampak pada tugas utama, kekuatan bukti/frekuensi, upaya, dependensi, risiko, dan kesesuaian arah produk. Tandai dampak yang belum terbukti sebagai hipotesis. Jangan menyebut preferensi visual sebagai kebutuhan pengguna tanpa bukti.

## 6. Laporan

Sertakan ruang lingkup dan dasar perbandingan, sumber/cakupan bukti, matriks status fitur, metode dan rumus skor, perbedaan perilaku, divergensi disengaja, persyaratan yang belum terpenuhi, prioritas perbaikan, keyakinan, serta keterbatasan.

## Alur kerja

1. Konfirmasi matriks kebutuhan dan versi.
2. Kumpulkan bukti yang sepadan.
3. Nilai fitur dan state.
4. Hitung cakupan dengan metode yang dinyatakan.
5. Pisahkan kesenjangan, opsi, peningkatan, dan divergensi.
6. Prioritaskan berdasarkan dampak dan bukti.
7. Serahkan bug reproduktif kepada QA dan pekerjaan yang disetujui kepada engineering.

## Hubungan dan batas

Rekayasa Balik memiliki investigasi referensi; Pengujian Perangkat Lunak memiliki reproduksi bug dan regresi; Penemuan Peluang Bisnis menilai masalah dan permintaan pelanggan; Full-Stack mengimplementasikan kesenjangan yang disetujui; Desain Frontend memiliki arah visual. Evaluasi Kesesuaian memiliki penilaian cakupan dan perbedaan, bukan QA, implementasi, atau penilaian hukum.
