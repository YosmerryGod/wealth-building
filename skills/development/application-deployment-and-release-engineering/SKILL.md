---
name: application-deployment-and-release-engineering
title: Rekayasa Deployment dan Rilis Aplikasi
category: development
subcategory: release-engineering
source_type: original-adaptation-from-replica-skill
language: Indonesian
description: "Gunakan saat menyiapkan aplikasi untuk staging atau produksi, mengatur hosting dan domain, memeriksa kesiapan rilis, atau merencanakan rollback dan pemantauan."
triggers: ["deploy aplikasi","terbitkan aplikasi","rilis ke produksi","hubungkan domain","rilis aplikasi","rekayasa rilis"]
out_of_scope: "Membeli domain, membuat akun, memasukkan kredensial, mengubah mode pembayaran langsung, atau menyetujui rilis atas nama pengguna"
escalation: "Perubahan produksi memerlukan persetujuan eksplisit; gunakan Penilaian Risiko untuk risiko hukum, privasi, keamanan, atau keuangan dan jadikan bukti QA sebagai gerbang rilis."
---

# Rekayasa Deployment dan Rilis Aplikasi

## Tujuan
Menyiapkan rilis yang terverifikasi melalui build yang dapat diulang, konfigurasi lingkungan yang aman, kemampuan pemulihan versi, dan pemantauan setelah rilis.

## Metode

1. **Pemeriksaan awal:** verifikasi pengujian dan build wajib, cacat kritis, migrasi yang telah ditinjau, dokumentasi variabel lingkungan, penyimpanan rahasia, backup/pemulihan, privasi/ketentuan/penghapusan data, domain/HTTPS/email/OAuth/webhook, pencatatan log/pelacakan error/uptime, serta identitas dan klaim produk yang jujur. Tandai setiap item lulus, gagal, belum diuji, atau tidak berlaku. Item yang belum diperiksa bukan berarti lulus.
2. **Staging:** deploy ke preview atau staging terlebih dahulu. Uji alur utama, autentikasi, izin akses, pembayaran sandbox, email, dan integrasi.
3. **Rencana produksi:** dokumentasikan penyedia hosting, metode deployment, migrasi, variabel lingkungan, DNS, callback webhook/OAuth, backup, potensi downtime, dan pemicu rollback. Gunakan dokumentasi penyedia terkini; jangan menebak target DNS.
4. **Persetujuan:** sampaikan hasil pemeriksaan, risiko, dampak, dan rencana rollback. Jangan menerbitkan aplikasi, mengganti kredensial live, mengubah DNS, membeli layanan, atau melakukan perubahan produksi yang sulit dibatalkan tanpa persetujuan eksplisit pengguna.
5. **Verifikasi dan pemantauan:** setelah rilis yang disetujui, periksa URL publik dan alur penting, pantau error/latensi, pastikan alert aktif, lalu catat ID rilis, waktu, hasil, dan pemantauan minggu pertama.

## Keluaran
Checklist rilis berbasis bukti, perintah dan hasil yang tepat, rencana deployment, langkah rollback, tindakan yang harus dilakukan pengguna, serta rencana pemantauan. Jangan mengklaim deployment berhasil tanpa konfirmasi dari lingkungan target.

## Batas kepemilikan
- QA memiliki bukti pengujian.
- Backend memiliki keamanan sisi server dan integrasi.
- Penilaian Risiko menilai konsekuensi penting.
- Orkestrator Pengembangan dan Pengiriman Aplikasi menjaga kesinambungan proyek serta gerbang persetujuan.
