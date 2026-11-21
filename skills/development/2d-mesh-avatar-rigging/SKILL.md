---
name: 2d-mesh-avatar-rigging
title: Rigging Avatar Mesh 2D
category: development
subcategory: 2d-avatar-animation
source_type: original-adaptation-from-mesh-avatar-studio
language: Indonesian
description: "Gunakan saat menyiapkan ilustrasi menjadi avatar 2D ber-mesh yang dapat dianimasikan dan diperiksa mutunya."
triggers: ["avatar 2d","rigging","vtuber"]
out_of_scope: "Ilustrasi merek umum atau arsitektur frontend"
escalation: "Serahkan ilustrasi merek umum atau arsitektur frontend kepada skill pemiliknya; gunakan Penilaian Risiko untuk konsekuensi penting dan minta persetujuan sebelum tindakan eksternal atau yang sulit dibatalkan."
---

# Rigging Avatar Mesh 2D

## Tujuan
Membantu agen coding menyiapkan ilustrasi sebagai avatar 2D animasi, lalu menyerahkan proyek ke editor lokal untuk penyempurnaan dan ekspor.

## Persyaratan input
- Utamakan ilustrasi menghadap depan dengan tampilan kepala dan bahu serta fitur wajah yang jelas.
- PNG transparan mempermudah pemisahan bagian.
- Sudut tiga perempat, wajah tertutup, rambut bertumpuk, tangan di depan wajah, dan aksesori kompleks meningkatkan kesulitan rekonstruksi.
- Pertahankan gambar sumber secara lokal kecuali pengguna secara eksplisit menyetujui pengiriman ke layanan gambar eksternal.

## Alur kerja

1. Periksa dimensi gambar, transparansi, pose, keterlihatan wajah, dan tantangan segmentasi.
2. Buat struktur proyek yang memisahkan gambar sumber dan berkas kerja hasil pemrosesan.
3. Petakan landmark wajah dan tubuh; kalibrasi ketepatan pembacaan koordinat sebelum rigging rinci.
4. Tentukan bagian yang dapat diedit serta titik kontrol untuk wajah, mata, mulut, rambut, sanggul, aksesori, dan bagian tubuh opsional.
5. Pisahkan ilustrasi menjadi layer dengan mempertahankan bagian yang saling menutupi dan urutan kedalamannya.
6. Bangun rig mesh dengan area deformasi dan parameter gerak yang sesuai.
7. Pratinjau pose tetap: menoleh, memiringkan kepala, berkedip, bernapas saat diam, mengayunkan rambut, dan menggerakkan mulut.
8. Perbaiki distorsi dan bangun ulang layer bila kontur atau mask sumber berubah.
9. Tambahkan variasi gambar seperti mata tertutup, bentuk mulut vokal, dan ekspresi jika benar-benar meningkatkan animasi.
10. Ekspor paket avatar portabel serta dokumentasikan asal gambar dan ketentuan penggunaan aset.

## Pemeriksaan mutu
- Fitur wajah tetap sejajar saat kepala bergerak.
- Rambut dan aksesori tidak terlepas atau berubah bentuk secara tidak wajar.
- Kedipan menutup dan membuka kembali tanpa getaran.
- Bentuk bibir untuk sinkronisasi ucapan tetap terbaca.
- Gerakan idle halus dan tidak mengganggu.
- Avatar bekerja pada player, lingkungan streaming, atau aplikasi tujuan.

## Pertimbangan teknis
- Cocokkan kebutuhan Node.js, Python, pemrosesan gambar, dan rendering browser dengan dokumentasi proyek terkini.
- Jalankan perintah diagnostik proyek sebelum proses generasi.
- Gunakan kalibrasi visual dan pemeriksaan pose tetap; jangan mengandalkan perkiraan koordinat tanpa verifikasi.
- Susun layer, mask, data rig, dan gambar sumber agar terorganisasi serta dapat direproduksi.
- Pemrosesan kamera dan mikrofon harus transparan; jelaskan data yang tetap lokal dan yang dikirim keluar.

## Sumber dan atribusi
Sintesis pengetahuan orisinal berdasarkan alur kerja [shinshin86/mesh-avatar-studio](https://github.com/shinshin86/mesh-avatar-studio), berlisensi MIT. Karakter contoh Miko secara eksplisit tidak termasuk lisensi MIT repositori tersebut dan memiliki ketentuan penggunaan tersendiri. Jangan menggunakan ulang atau mendistribusikan karakter itu seolah aset MIT umum.
