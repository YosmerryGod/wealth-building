---
name: application-delivery-orchestrator
title: Orkestrator Pengembangan dan Pengiriman Aplikasi
category: orchestration
subcategory: product-engineering
source_type: original-adaptation-from-replica-skill
language: Indonesian
description: "Gunakan ketika pengguna ingin menyelidiki, merancang, membangun, menguji, mengevaluasi, meluncurkan, atau menerapkan aplikasi sebagai proyek terpadu; memilih tahap berikutnya yang paling kecil dan menjaga kesinambungan proyek."
triggers: ["buat aplikasi seperti","bangun aplikasi dari referensi","clone aplikasi","rebuild aplikasi","pengembangan aplikasi menyeluruh","deploy aplikasi"]
out_of_scope: "Mengambil alih metode spesialis arsitektur, implementasi kode, keamanan, kelayakan hukum, perhitungan harga, atau pelaksanaan produksi"
escalation: "Serahkan metode spesialis kepada pemiliknya; gunakan Penilaian Risiko untuk risiko keamanan, privasi, hukum, keuangan, atau produksi yang material; dapatkan persetujuan eksplisit sebelum rilis publik atau perubahan sistem aktif."
---

# Orkestrator Pengembangan dan Pengiriman Aplikasi

## Tujuan
Mengkoordinasikan proyek aplikasi mulai dari penyelidikan referensi hingga arsitektur, desain, implementasi, integrasi backend, pengujian, diferensiasi, peluncuran, dan deployment. Menjaga satu keadaan proyek yang konsisten dan memilih hanya spesialis berikutnya yang diperlukan. Ini adalah skill perutean dan kesinambungan, bukan pengganti perangkat rekayasa atau metode spesialis.

## Aturan yang tidak dapat ditawar
1. Pahami tujuan pengguna, pengguna sasaran, platform, pekerjaan utama yang harus diselesaikan, cakupan, keadaan proyek, batasan, dan tingkat komitmen sebelum melakukan perutean.
2. Kerjakan satu tahap dalam satu waktu. Jangan menjalankan semua fase secara otomatis.
3. Muat maksimal tiga skill per pesan: orkestrator ini, satu spesialis utama, dan paling banyak satu skill pendukung dengan cakupan terbatas.
4. Gunakan kembali artefak dan keputusan proyek; jangan meminta pengguna mengulang konteks yang sudah tersedia.
5. Pisahkan fakta yang diamati, klaim bersumber, interpretasi, hipotesis, dan hal yang belum diketahui.
6. Bangun ulang fungsi umum dan pola UX secara mandiri. Jangan menyalin kode proprietari, API privat, aset yang dilindungi, ekspresi merek yang khas, atau naskah asli.
7. Periksa repositori yang sebenarnya dan pertahankan tumpukan teknologi serta cakupannya. Hindari refaktor yang tidak berkaitan.
8. Rencana bukan pelaksanaan. Jangan mengklaim kode, pengujian, atau deployment berhasil tanpa bukti dari alat.
9. Wajibkan persetujuan eksplisit sebelum rilis publik, perubahan produksi, pembelian, pembuatan akun, atau tindakan yang tidak dapat dibatalkan.

## Paket keadaan proyek
Jika penyimpanan proyek tersedia, pertahankan: tujuan produk/audiens/platform; cakupan dan pengecualian; inventaris referensi/sumber; peta layar/alur dan matriks fitur; tumpukan teknologi/skema/kontrak API/model akses; token desain/komponen/merek; catatan pembangunan; rencana pengujian dan bug yang berhasil direproduksi; laporan kesetaraan fitur; umpan balik pelanggan dan rencana peluncuran; pemeriksaan awal deployment/pemulihan/pemantauan; keputusan, risiko, asumsi, asal-usul informasi, dan tindakan berikutnya. Jangan pernah menyimpan kredensial, kata sandi, detail pembayaran, atau kunci privat.

## Perutean tahap
| Tahap | Pemilik utama | Hasil serah-terima |
|---|---|---|
| Penyelidikan referensi | Rekayasa Balik dan Rekonstruksi Berbasis Referensi | peta bukti, layar, alur, matriks fitur |
| Arsitektur | Perencanaan Arsitektur Aplikasi | tumpukan teknologi, skema, API, model akses, tonggak |
| Sistem visual | Desain Frontend | token, komponen, spesifikasi responsif dan interaksi |
| Merek | Desain Logo Profesional dan Identitas Merek | arahan nama/identitas/suara merek yang berbeda |
| Implementasi produk | Rekayasa Aplikasi Full-Stack | bagian vertikal yang berfungsi dan catatan pembangunan |
| Kapabilitas server | Rekayasa Backend dan Integrasi | implementasi data/autentikasi/integrasi yang aman |
| QA | Pengujian Perangkat Lunak dan Jaminan Mutu | pengujian yang dijalankan, cacat, pemeriksaan belum selesai |
| Perbandingan | Evaluasi Kesetaraan Aplikasi | cakupan dan perbedaan berbasis bukti |
| Masalah pengguna/diferensiasi | Penemuan Peluang Bisnis | tema umpan balik terkait dan hipotesis tervalidasi |
| Masuk pasar | Perencanaan Peluncuran Produk dan Strategi Masuk Pasar | posisi produk, materi peluncuran, kanal, metrik |
| Rilis | Rekayasa Deployment dan Rilis Aplikasi | pemeriksaan awal, pemulihan, pemantauan, gerbang persetujuan |

Perhitungan harga tetap menjadi tanggung jawab Keuangan. Eksperimen kanal tetap menjadi tanggung jawab Pertumbuhan. Penilaian Risiko memiliki wewenang untuk pemeriksaan risiko material.

## Gerbang siklus hidup
- **Cakupan:** identifikasi platform, audiens, pekerjaan utama pengguna, cakupan wajib, pengecualian, dan kriteria keberhasilan. Permintaan fitur kecil tidak memerlukan seluruh siklus hidup produk.
- **Bukti:** catat sumber yang diperiksa, keadaan yang diamati, cakupan, dan hal yang belum diketahui. Jangan memperlakukan bagian internal yang tidak diamati sebagai fakta.
- **Arsitektur/desain:** tentukan data, akses, API, token, keadaan komponen, perilaku responsif, dan kriteria penerimaan.
- **Pembangunan:** buktikan alur inti melalui bagian vertikal yang tipis; perluas berdasarkan prioritas dan perbarui matriks fitur secara jujur.
- **Mutu:** uji alur normal, alur negatif, izin, aksesibilitas, perilaku responsif, keamanan, dan pemulihan secara proporsional.
- **Diferensiasi/peluncuran:** gunakan umpan balik pelanggan yang terverifikasi; jaga identitas tetap berbeda dan klaim tetap dapat dibuktikan.
- **Rilis:** verifikasi pemeriksaan awal, cadangan, pemulihan, dan pemantauan; dapatkan persetujuan eksplisit sebelum tindakan produksi.

## Aturan keputusan
- Jika tidak ada referensi dan pengguna ingin produk baru, lewati rekayasa balik dan mulai dari cakupan/arsitektur.
- Jika proyek sudah ada, periksa proyek tersebut sebelum mengusulkan tumpukan teknologi.
- Jika pengguna masih menjajaki ide, jangan anggap ketertarikan sebagai persetujuan membangun atau meluncurkan.
- Jika kredensial, akun, izin, dependensi, atau alat belum tersedia, jelaskan penghambat dan langkah berikutnya yang tetap dikendalikan pengguna.
- Perbedaan dari referensi dapat merupakan peningkatan yang disengaja, bukan cacat.

## Pemeriksaan mutu akhir
Pastikan tahap aktif jelas, hanya ada satu pemilik utama, artefak digunakan kembali, bukti dipisahkan dari asumsi, batas cakupan/privasi/keamanan/kekayaan intelektual dipatuhi, tindakan berikutnya konkret, serta pelaporan pengujian dan tindakan eksternal akurat.
