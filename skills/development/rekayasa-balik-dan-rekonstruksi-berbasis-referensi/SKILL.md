---
name: rekayasa-balik-dan-rekonstruksi-berbasis-referensi
title: Rekayasa Balik dan Rekonstruksi Berbasis Referensi
category: development
subcategory: product-investigation
source_type: original-ai-reasoning-framework
language: Indonesian
description: "Gunakan saat menganalisis produk digital berdasarkan bukti dan menyusun brief rekonstruksi atau adaptasi."
triggers: ["tiru tampilan","referensi website","bongkar situs"]
out_of_scope: "Klaim tentang bagian internal yang tidak diamati atau kepemilikan akhir produk"
escalation: "Serahkan klaim tentang bagian internal yang tidak diamati atau kepemilikan akhir produk kepada pemiliknya; gunakan Penilaian Risiko untuk konsekuensi penting dan minta persetujuan sebelum tindakan eksternal."
---

# Rekayasa Balik dan Rekonstruksi Berbasis Referensi

## Tujuan
Memahami cara kerja produk digital yang terlihat dan alasan pengalaman penggunanya disusun, lalu menggunakan temuan tersebut untuk merancang solusi berbeda yang memenuhi tujuan pengguna.

Pendekatan ini merupakan proses investigasi dan pembelajaran yang disiplin, bukan penyalinan tanpa analisis. Berlaku untuk situs, aplikasi web, aplikasi mobile/desktop, layanan digital, dan produk lain yang dapat diamati.

## 1. Tentukan objek dan tujuan investigasi

Klasifikasikan referensi:
- Situs atau aplikasi web aktif.
- Aplikasi mobile atau desktop.
- Screenshot, mockup, atau referensi desain statis.
- Rekaman layar atau perjalanan pengguna.
- Repositori kode atau dokumentasi publik.
- Paket aplikasi, binary, firmware, atau artefak distribusi.
- Perilaku API, pertukaran jaringan, atau integrasi.
- Produk bernama tanpa artefak langsung.

Tentukan tujuan: memahami pengalaman produk, merekonstruksi halaman, mempelajari fitur, memetakan navigasi/perjalanan, menemukan pola, membandingkan versi, menjelaskan perilaku implementasi, atau membuat adaptasi orisinal. Klarifikasi hanya jika perbedaan tujuan mengubah pekerjaan secara material. Jangan menganggap permintaan "seperti produk X" berarti tiruan piksel demi piksel.

## 2. Pilih metode bukti yang sesuai

| Bukti tersedia | Metode |
|---|---|
| Screenshot | Periksa hierarki, tata letak, tipografi, warna, jarak, gambar, dan kontrol yang terlihat; jangan menyimpulkan perilaku tersembunyi |
| Rekaman layar | Susun urutan, perubahan state, waktu, dan feedback yang terlihat |
| Situs aktif | Periksa halaman, navigasi, responsivitas, konten, tautan, dan interaksi yang dapat diakses |
| Source code publik | Baca arsitektur, komponen, style, route, aliran data, dan tes; pisahkan maksud kode dari perilaku deployment |
| Dokumentasi API atau traffic tertangkap | Petakan request, response, transisi state, dan kontrak integrasi sesuai bukti |
| Aplikasi terpasang/binary | Gunakan alat reverse engineering yang sesuai, tersedia, dan diizinkan |
| Tidak ada artefak langsung | Gunakan informasi publik terdokumentasi dan tandai analisis sebagai tidak langsung |

Browser biasanya tidak mengungkap seluruh arsitektur internal. Screenshot tidak membuktikan perilaku kontrol. Source code tidak membuktikan aplikasi deployment berperilaku sama. Untuk investigasi binary, paket, firmware, atau runtime yang lebih dalam, gunakan toolchain khusus seperti REA hanya jika benar-benar tersedia dan terhubung. Skill ini tidak memasang atau menyediakan REA.

Jangan mengaku telah membuka, menguji, mendekompilasi, atau menjalankan target jika alat terkait tidak benar-benar melakukannya.

## 3. Buat peta bukti

Pisahkan setiap temuan menjadi:
1. **Diamati:** terlihat langsung atau dikembalikan oleh artefak/tool yang diperiksa.
2. **Interpretasi didukung:** penjelasan masuk akal berdasarkan satu atau lebih pengamatan.
3. **Hipotesis:** penjelasan yang masih perlu diuji.
4. **Tidak diketahui:** informasi yang belum tersedia.

Catat asal temuan: URL dan halaman, screenshot, timestamp rekaman, berkas sumber, route, request, hasil tool, atau referensi lain.

Nilai cakupan bukti:
- Halaman, layar, state, dan alur apa yang diperiksa?
- Ukuran viewport atau perangkat apa yang dicakup?
- Interaksi mana yang benar-benar diuji?
- Apa yang memerlukan login, pembayaran, lokasi, akun nyata, atau izin yang tidak tersedia?
- Apa yang belum dapat diperiksa dan apakah ada beberapa penjelasan yang mungkin?

Sampel beberapa halaman bukan bukti seluruh produk. Hasil kosong dari pencarian terbatas bukan bukti bahwa fitur tidak ada.

## 4. Investigasi sesuai lapisan yang relevan

Jangan memaksakan semua lapisan pada setiap tugas.

- **Produk dan bisnis:** nilai yang ditawarkan, calon pengguna, masalah utama, posisi/pembeda, tindakan sukses, serta batasan bisnis yang terlihat. Pisahkan klaim eksplisit dari strategi yang disimpulkan.
- **Arsitektur informasi:** hierarki bagian/halaman, model navigasi, pengelompokan konten, pencarian/filter/pengurutan, hubungan halaman, titik masuk dan keluar.
- **Visual:** komposisi/grid, lebar konten, tipografi, peran warna dan kontras, ritme jarak, media, border, permukaan, ikon, bentuk komponen, dan perubahan responsif.
- **Interaksi dan state:** state awal, aksi, hasil, feedback/animasi, loading, kosong, error, sukses, disabled, persistensi, keyboard, sentuhan, dan aksesibilitas. Tandai state yang belum diuji sebagai belum diketahui.
- **Perjalanan pengguna:** telusuri tugas penting dari masuk hingga selesai. Catat maksud, langkah, titik keputusan, hambatan, feedback, dan kondisi penyelesaian.
- **Konten dan konversi:** headline, proposisi nilai, CTA, sinyal kepercayaan, harga/penawaran, FAQ, penanganan keberatan, checkout, dan retensi. Penjelasan konversi tetap hipotesis kecuali didukung analitik atau eksperimen.
- **Teknis:** bila kode, DevTools, dokumentasi API, atau runtime tersedia, periksa route, komponen, sumber data, state, request, autentikasi/otorisasi, persistensi, integrasi, performa, dan aksesibilitas. Jangan menebak framework, database, backend, atau hosting hanya dari tampilan.

## 5. Ubah temuan menjadi pola yang dapat digunakan

Klasifikasikan tiap temuan:
- **Pertahankan prinsip:** solusi umum terhadap masalah pengguna.
- **Adaptasi:** pola berguna yang perlu disesuaikan.
- **Ganti:** pilihan yang bertentangan dengan produk, pelanggan, merek, atau operasi baru.
- **Abaikan:** detail yang tidak relevan.
- **Investigasi lanjut:** ketidakpastian yang dapat mengubah desain atau implementasi.

Untuk pola penting, jelaskan masalah yang diselesaikan, cara referensi menyelesaikannya, bukti pendukung, kecocokan konteks baru, adaptasi, kompromi, dan pertanyaan tersisa. Pertahankan logika produk yang berguna, bukan ekspresi visualnya secara membabi buta.

## 6. Sesuaikan dengan produk baru

Sebelum mengusulkan solusi, pahami produk/penawaran baru, pelanggan, tugas utama, konversi, konten, aturan bisnis, identitas merek, aset, prioritas perangkat/kanal, dan batasan operasi seperti stok, pembayaran, pengiriman, atau area layanan.

Buat peta translasi: pola referensi → tujuan awal → adaptasi konteks baru. Contohnya, gambar produk editorial dapat diterjemahkan menjadi foto produk autentik dengan ukuran/porsi yang jelas; kategori katalog menjadi kategori yang sesuai cara pelanggan mencari; detail produk menjelaskan varian dan harga; checkout disesuaikan dengan alur transaksi baru. Contoh bukan aturan wajib.

## 7. Susun brief rekonstruksi yang dapat ditindaklanjuti

Pilih bagian yang relevan:
1. Ringkasan referensi dan alasan relevansinya.
2. Bukti, cakupan pemeriksaan, interpretasi, dan hal yang belum diketahui.
3. Peta situs, halaman, atau fitur.
4. Alur pengguna dan state penting.
5. Pola yang dipertahankan, diadaptasi, diganti, diabaikan, atau perlu diselidiki.
6. Arah produk baru: audiens, tujuan, konten, merek, dan konversi.
7. Pengalaman yang diusulkan: struktur halaman, komponen, perilaku, dan prioritas responsif.
8. Catatan implementasi bila diminta.
9. Checklist validasi.

Untuk permintaan kecil, buat versi ringkas. Jangan membuat laporan panjang jika pengguna hanya ingin memahami satu halaman atau fitur.

## 8. Validasi adaptasi

Periksa apakah solusi:
- Menyelesaikan masalah pengguna yang sama dengan cara yang sesuai konteks baru.
- Mempertahankan pola referensi yang berguna dan membuang konvensi yang tidak relevan.
- Memiliki alur dan state penting yang lengkap.
- Memiliki perilaku responsif, aksesibilitas, dan performa yang layak.
- Memiliki identitas visual/konten yang berbeda, bukan sekadar ganti kulit.
- Mendukung klaim tentang referensi dan implementasi dengan bukti.

Jika implementasi aktif tersedia, periksa hasil render dan uji alur penting. Brief atau tinjauan source code saja tidak cukup untuk menyatakan validasi selesai.

## 9. Kekayaan intelektual dan diferensiasi

Rekayasa balik dapat mempelajari produk yang dapat diamati serta gagasan, metode, alur kerja, dan pola fungsional umum. Hasilnya harus diekspresikan secara mandiri sesuai konteks pengguna.

Bedakan gagasan fungsional dari ekspresi yang dilindungi seperti merek, logo, teks, foto, ilustrasi, aset eksklusif, dan source code. Jangan menyajikan identitas atau aset perusahaan lain sebagai milik pengguna. Untuk permintaan tiruan dekat, jelaskan prinsip pengalaman yang dapat diadaptasi dan buat arah visual/konten yang berbeda.

## 10. Alur praktis
1. Bingkai referensi, produk tujuan, sasaran pengguna, dan cakupan.
2. Pilih bukti: browser, gambar, rekaman, source, API, atau tool khusus yang tersedia.
3. Periksa lapisan produk, visual, interaksi, perjalanan, dan teknis yang relevan.
4. Catat pengamatan, interpretasi, hipotesis, dan hal yang belum diketahui.
5. Petakan struktur, state, dan perjalanan utama.
6. Ekstrak pola yang layak dipertahankan.
7. Terjemahkan pola ke audiens, bisnis, merek, dan batasan baru.
8. Susun brief desain atau implementasi.
9. Bangun dan validasi menggunakan skill desain/rekayasa yang relevan jika implementasi diminta.
10. Laporkan apa yang diperiksa, yang belum diperiksa, dan tingkat keyakinan.

## 11. Hubungan dengan skill lain
- **Desain Frontend:** menetapkan arah visual produk baru; skill ini menyelidiki referensi dan menerjemahkan polanya.
- **Desain Antarmuka AI dan Rekayasa Anti-Generik:** mengaudit kekhasan dan mutu UI hasil adaptasi.
- **Pola Navigasi dan Interaksi Web Modern:** memilih struktur navigasi produk baru.
- **Interaksi Mikro dan Desain Umpan Balik UI:** merinci feedback dan transisi state.
- **Desain Logo Profesional dan Identitas Merek:** membuat identitas berbeda dari merek referensi.
- **Business Agent Orchestrator:** mengoordinasikan penemuan bisnis, riset pelanggan/pesaing, persiapan merek, dan eksekusi yang disetujui.
- **Pemahaman Konteks:** menafsirkan maksud "seperti ini", mempertahankan batasan sebelumnya, dan menghindari pertanyaan berulang.
- **REA:** toolchain terpisah untuk investigasi native, managed, paket, browser, dan runtime yang didukung; gunakan hanya jika MCP/CLI serta mesin yang diperlukan benar-benar tersedia.

## Serah-terima rekonstruksi aplikasi
Untuk produk multi-layar, berikan ID layar stabil, route/titik masuk, alur utama dan edge case, inventaris komponen, entitas data berbasis bukti beserta tingkat keyakinan, prioritas/pengecualian fitur, daftar sumber, cakupan pemeriksaan, dan risiko yang belum terselesaikan. Pisahkan capture referensi dari aset produksi. Jangan menandai field hasil inferensi atau state yang belum diuji sebagai hasil observasi.

## Batas kemampuan
Skill ini mendefinisikan alur investigasi dan penalaran. Skill ini tidak dengan sendirinya membuka situs, mengoperasikan browser, menangkap traffic, mendekompilasi binary, menjalankan aplikasi, memasang REA, atau menyimpan bukti secara persisten. Kemampuan tersebut bergantung pada tool dan akses yang tersedia.

## Serah-terima siklus aplikasi
- **Perencanaan Arsitektur Aplikasi:** mengubah paket rekonstruksi berbasis bukti menjadi stack, skema, kontrak API, model akses, dan urutan pembangunan.
- **Desain Frontend:** membuat sistem visual dan spesifikasi komponen baru dari prinsip yang telah diadaptasi.
- **Orkestrator Pengembangan dan Pengiriman Aplikasi:** menjaga tahap proyek, keputusan, dan serah-terima berikutnya yang paling kecil.
- **Evaluasi Kesesuaian Aplikasi:** memeriksa cakupan fitur dan perbedaan yang disengaja; bukan pengganti pengumpulan bukti.
