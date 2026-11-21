---
name: 3d-media-storefront-experience
title: Pengalaman Etalase Media 3D
category: development
subcategory: 3d-media-experience
source_type: original-adaptation-from-halcyon-video
language: Indonesian
description: "Gunakan saat merancang katalog media 3D dan pengalaman etalase spasial untuk menjelajah, memeriksa, dan membuka atau membeli konten."
triggers: ["toko 3d","katalog 3d"]
out_of_scope: "Desain frontend umum atau pemeriksaan hak media"
escalation: "Serahkan desain frontend umum dan pemeriksaan hak media kepada skill pemiliknya; gunakan Penilaian Risiko untuk konsekuensi penting dan minta persetujuan sebelum tindakan eksternal."
---

# Pengalaman Etalase Media 3D

## Tujuan
Mengubah katalog digital konvensional menjadi pengalaman ritel spasial. Pengguna dapat menjelajahi lorong, memeriksa item, menemukan kategori, lalu menuju tindakan melihat atau membeli yang jelas.

## Model pengalaman
- **Identitas toko:** arsitektur, era, warna, papan nama, pencahayaan, dan detail lingkungan.
- **Departemen:** kelompokkan koleksi ke lorong dan zona genre yang mudah dikenali.
- **Penjelajahan rak:** tampilkan sampul item, judul, metadata, dan konteks kategori dengan jelas.
- **Pemeriksaan item:** sediakan tampilan lebih dekat dan detail berguna tanpa membuat pengguna kehilangan posisi.
- **Titik tindakan:** hubungkan penjelajahan ke langkah nyata, misalnya membuka layanan streaming, menjalankan gim, atau mengakses produk.
- **Kehidupan lingkungan:** karakter, lalu lintas, dan animasi lingkungan bersifat opsional. Elemen ini tidak boleh menghalangi navigasi.

## Alur kerja

1. Identifikasi sumber katalog, audiens, jumlah koleksi, dan tindakan utama pengguna.
2. Rancang tata letak toko berdasarkan arsitektur informasi, bukan sekadar efek visual.
3. Tentukan metadata item, pencarian, filter, pengurutan, dan navigasi kategori.
4. Pilih kontrol yang sesuai untuk keyboard, gamepad, remote TV, layar sentuh, dan mouse.
5. Hubungkan ke sumber media atau katalog yang diizinkan; tangani item yang tidak tersedia secara wajar.
6. Optimalkan pemuatan aset, level of detail, draw call, ukuran tekstur, dan rendering pada perangkat berdaya rendah.
7. Sediakan mode daftar atau grid konvensional bagi pengguna yang mengutamakan kecepatan atau aksesibilitas.
8. Uji navigasi, pemilihan item, pencarian, performa, serta kegagalan layanan eksternal.

## Produk dan integrasi
- Toko 3D adalah lapisan presentasi, bukan solusi hosting atau lisensi media.
- Patuhi API, autentikasi, dan ketentuan layanan yang terhubung.
- Bedakan metadata katalog dari konten yang benar-benar dapat diputar dan hak akses langganan.
- Jangan memberi kesan bahwa etalase memiliki atau menyediakan konten yang sebenarnya berasal dari layanan lain.
- Pertimbangkan privasi dan keamanan saat membuka pustaka media yang di-host sendiri kepada pengunjung.

## Sumber dan atribusi
Terinspirasi oleh konsep pengalaman pengguna dan integrasi [halcyon-video/halcyon-video](https://github.com/halcyon-video/halcyon-video), berlisensi GPL-3.0. Skill ini merupakan deskripsi orisinal, bukan salinan kode Halcyon. Distribusi perangkat lunak yang dimodifikasi atau digabungkan dengan perangkat lunak GPL-3.0 harus mematuhi kewajiban GPL-3.0. Artwork media dan aset katalog pihak ketiga dapat memiliki hak terpisah.
