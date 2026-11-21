---
name: application-architecture-planning
title: Perencanaan Arsitektur Aplikasi
category: development
subcategory: software-architecture
source_type: original-adaptation-from-replica-skill
language: Indonesian
description: "Gunakan untuk merancang tumpukan teknologi, batas sistem, skema basis data, kontrak API, model akses, integrasi, dan urutan pembangunan aplikasi."
triggers: ["arsitektur aplikasi","stack aplikasi","rancang database","skema database","desain API","arsitektur sistem"]
out_of_scope: "Desain visual, implementasi fitur terperinci, pengujian penetrasi, atau deployment produksi"
escalation: "Serahkan arah visual kepada Desain Frontend, implementasi produk kepada Rekayasa Aplikasi Full-Stack, kapabilitas server kepada Rekayasa Backend, risiko material kepada Penilaian Risiko, dan rilis kepada Rekayasa Deployment dan Rilis."
---

# Perencanaan Arsitektur Aplikasi

## Tujuan
Mengubah kebutuhan produk yang telah disetujui dan bukti proyek menjadi rancangan teknis yang dapat dibangun, dioperasikan, diamankan, dan dikembangkan tanpa kompleksitas yang tidak perlu.

## Masukan
Gunakan peta hasil rekonstruksi, matriks fitur, repositori aktual, tumpukan teknologi, kemampuan tim, batas biaya/hosting, klasifikasi data, dan kebutuhan integrasi. Periksa manifest, rute, akses data, migrasi, serta konfigurasi deployment sebelum mengusulkan perubahan. Pertahankan teknologi yang sudah bekerja kecuali ada alasan teknis yang terdokumentasi.

## Metode
1. **Batas sistem:** petakan aktor, peran, tenant, alur kerja, batas kepercayaan, serta kebutuhan ketersediaan, latensi, aksesibilitas, privasi, retensi, cadangan, pemulihan, dan biaya.
2. **Pemilihan stack:** bandingkan kesesuaian dengan kebutuhan, pengalaman tim, kematangan ekosistem, dukungan keamanan, hosting, biaya operasi, dan kemudahan berpindah. Pilih arsitektur terkelola paling sederhana yang memadai. Jangan memakai microservices atau infrastruktur tambahan tanpa kebutuhan nyata.
3. **Model data:** tentukan entitas, atribut, pemilik data, relasi, siklus hidup, retensi, kunci, aturan penghapusan, constraint, indeks, zona waktu, presisi mata uang, isolasi tenant, migrasi, data awal, serta cadangan.
4. **Kontrak API:** dokumentasikan metode/event, tujuan, autentikasi dan otorisasi, validasi masukan, keluaran dan format kesalahan, idempotensi, batas permintaan, serta alur pemilik untuk route, webhook, dan job. Gunakan API publik resmi.
5. **Risiko operasional:** periksa konkurensi, percobaan ulang, zona waktu, kuota, batas berkas, pencarian, real-time/offline, email, multi-tenant, penghapusan, observabilitas, backup, dan pemulihan sesuai kebutuhan.
6. **Urutan pembangunan:** mulai dari satu alur vertikal tipis, lalu fitur wajib, dependensi, integrasi, dan fitur opsional. Setiap tahap harus memiliki kriteria penerimaan.

## Keluaran
Dokumen arsitektur berisi cakupan, alasan pemilihan stack, batas layanan, skema/ERD, kontrak API/webhook/job, model autentikasi dan akses, risiko privasi/backup/observabilitas, tahapan pembangunan, asumsi, dan keputusan yang belum selesai.

Jangan mengubah proyek saat pengguna hanya meminta rancangan.

## Batas tanggung jawab
- Rekayasa Balik dan Rekonstruksi Berbasis Referensi memiliki bukti referensi dan pemetaan fitur.
- Skill ini memiliki keputusan arsitektur dan kontrak sistem.
- Desain Frontend memiliki sistem visual.
- Rekayasa Aplikasi Full-Stack memiliki implementasi dan integrasi alur produk.
- Rekayasa Backend memiliki implementasi layanan server, keamanan data, dan integrasi.
- Penilaian Risiko memeriksa konsekuensi berisiko tinggi.
- Rekayasa Deployment dan Rilis memiliki kesiapan serta pelaksanaan rilis.
