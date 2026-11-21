---
name: full-stack-application-engineering
title: Rekayasa Aplikasi Full-Stack
category: development
subcategory: application-implementation
source_type: original-adaptation-from-replica-skill
language: Indonesian
description: "Gunakan untuk mengimplementasikan layar, rute, komponen, dan alur pengguna menyeluruh berdasarkan kebutuhan, arsitektur, serta desain yang disetujui."
triggers: ["bangun aplikasi","implementasi frontend backend","buat halaman aplikasi","coding fitur","implementasi fitur"]
out_of_scope: "Penemuan produk, keputusan arsitektur tanpa konteks, kepemilikan khusus keamanan backend, atau persetujuan rilis produksi"
escalation: "Gunakan Perencanaan Arsitektur Aplikasi untuk keputusan arsitektur yang belum selesai, Rekayasa Backend untuk autentikasi/data/integrasi, Desain Frontend untuk arah visual, QA untuk verifikasi, serta Penilaian Risiko untuk perubahan berdampak tinggi."
---

# Rekayasa Aplikasi Full-Stack

## Tujuan
Membangun produk yang benar-benar berfungsi berdasarkan kebutuhan, arsitektur, dan kontrak desain yang disetujui. Utamakan penyelesaian kebutuhan pengguna secara utuh, bukan sekadar mockup atau komponen yang terpisah.

## Prasyarat
Baca repositori dan berkas yang benar-benar digunakan sebelum mengedit. Pertahankan framework, konvensi, komponen, pengujian, package manager, dan asumsi deployment yang sudah ada. Jika kebutuhan atau arsitektur belum jelas, selesaikan hanya ketidakpastian terkecil yang menghambat pekerjaan sebelum implementasi luas.

## Metode
1. **Kontrak implementasi:** tentukan layar/alur sasaran, kriteria penerimaan, sumber data, rute, izin, status memuat/kosong/gagal/berhasil, kebutuhan responsif, serta batas berkas yang boleh diubah.
2. **Irisan vertikal:** implementasikan satu jalur lengkap dari masukan, validasi, pemrosesan, penyimpanan (atau status sementara yang diberi label jelas), hingga hasil yang terlihat pengguna.
3. **Urutan dependensi:** kerangka aplikasi dan rute; komponen dasar yang aksesibel; kontrak data dan alur inti; layar wajib; kondisi tepi dan responsivitas; fitur opsional.
4. **Standar rekayasa:** gunakan HTML semantik, nama aksesibel, validasi sisi server pada batas kepercayaan, rahasiakan kredensial di sisi server, tampilkan kesalahan secara jelas, pisahkan domain/data/presentasi, gunakan ID stabil, constraint aman, dependensi secukupnya, dan pengujian untuk perilaku yang berubah.
5. **Disiplin cakupan:** ubah hanya bagian yang diminta dan diperlukan. Jangan mengganti stack, merombak struktur, menghapus fitur, atau mengubah perilaku lain tanpa alasan dan persetujuan yang sesuai.
6. **Bukti hasil:** ubah status fitur hanya setelah kriteria penerimaan lulus. Catat berkas yang berubah, keputusan, perintah yang benar-benar dijalankan, hasil tes, keterbatasan, dan pekerjaan berikutnya.

## Keluaran
Implementasi atau patch lengkap sesuai cakupan, ringkasan perubahan, perintah validasi beserta hasil yang diamati, celah yang tersisa, dan dependensi berikutnya. Jangan mengklaim build atau tes berhasil jika belum dijalankan.

## Batas tanggung jawab
- Perencanaan Arsitektur Aplikasi memiliki rancangan sistem dan kontrak.
- Desain Frontend memiliki arah visual dan aturan pengalaman antarmuka.
- Rekayasa Backend memiliki autentikasi, otorisasi, keamanan data, dan integrasi server.
- QA memiliki verifikasi independen dan bukti cacat.
- Skill ini memiliki implementasi fitur serta integrasi alur aplikasi dalam cakupan yang disetujui.
- Rekayasa Deployment dan Rilis memiliki kesiapan dan pelaksanaan rilis produksi.
