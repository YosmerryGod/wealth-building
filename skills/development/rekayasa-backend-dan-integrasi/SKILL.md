---
name: backend-engineering-and-integrations
title: Rekayasa Backend dan Integrasi
category: development
subcategory: backend-engineering
source_type: original-adaptation-from-replica-skill
language: Indonesian
description: "Gunakan untuk membangun autentikasi, otorisasi, basis data, migrasi, pembayaran, webhook, email, job, penyimpanan, dan integrasi API pihak ketiga."
triggers: ["buat backend","login register","integrasi API","database aplikasi","payment gateway","webhook","rekayasa backend"]
out_of_scope: "Desain visual frontend, arsitektur produk secara keseluruhan, sertifikasi hukum, atau persetujuan rilis"
escalation: "Gunakan Perencanaan Arsitektur Aplikasi untuk kontrak sistem, Penilaian Risiko untuk risiko keamanan/privasi/hukum, QA untuk verifikasi, dan Rekayasa Deployment dan Rilis untuk penerapan produksi."
---

# Rekayasa Backend dan Integrasi

## Tujuan
Membangun kapabilitas sisi server yang andal dengan kepemilikan data, otorisasi, pengelolaan rahasia, penanganan kegagalan, dan batas integrasi yang jelas.

## Metode
1. **Kontrak dan konteks:** baca arsitektur, skema, definisi route, kode aktual, serta dokumentasi penyedia yang telah disetujui. Identifikasi aktor, klasifikasi data, izin, perkiraan beban, dan pola kegagalan. Jangan menggunakan API privat atau tidak terdokumentasi milik produk referensi.
2. **Autentikasi dan otorisasi:** gunakan mekanisme terpelihara. Verifikasi identitas di server, amankan sesi, dan tegakkan izin pada setiap operasi baca/tulis. Uji isolasi antar pengguna dan tenant. Sediakan pemulihan akun, pencabutan akses, dan penghapusan secara aman jika relevan.
3. **Basis data dan siklus hidup:** gunakan migrasi berversi, constraint, dan indeks yang beralasan. Tetapkan transaksi, konsistensi, perilaku penghapusan, data awal sintetis, retensi, ekspor, penghapusan, pencadangan, dan pemulihan.
4. **Pembayaran dan webhook:** gunakan API resmi serta akun milik pengguna; mulai dari mode sandbox. Verifikasi tanda tangan, simpan ID peristiwa, buat handler idempoten, dan jadikan status penyedia sebagai acuan ketika sesuai. Jelaskan pembatalan dan pengembalian dana. Jangan meminta rahasia produksi melalui percakapan.
5. **Integrasi dan pekerjaan latar:** dokumentasikan penyedia, versi API, cakupan izin minimum, batas permintaan, kuota, kebutuhan peninjauan, timeout, retry, fallback, dan observabilitas. Gunakan salinan transaksional yang konsisten serta job idempoten.
6. **Baseline keamanan:** simpan rahasia dalam environment/secret manager; validasi masukan di server; otorisasi setiap operasi; batasi penyalahgunaan; lindungi tanda tangan dan replay; batasi unggahan; jangan letakkan data sensitif pada URL/log; audit dependensi; minimalkan data serta jelaskan retensi dan pemrosesannya.
7. **Kegagalan dan pemulihan:** definisikan perilaku saat penyedia tidak tersedia, koneksi terputus, permintaan berulang, proses parsial, dan data tidak konsisten. Hindari retry tanpa batas atau operasi ganda.

Checklist bukan bukti bahwa aplikasi aman. Sistem berisiko tinggi membutuhkan peninjauan tenaga ahli dan pengujian yang sesuai.

## Keluaran
Migrasi, implementasi server, nama variabel environment tanpa nilainya, catatan integrasi, pemeriksaan keamanan, hasil tes/celah, serta risiko operasional. Jangan membuat akun, membeli layanan, atau mengaktifkan mode pembayaran langsung atas nama pengguna.

## Batas tanggung jawab
- Perencanaan Arsitektur Aplikasi memiliki kontrak sistem dan keputusan arsitektur.
- Skill ini memiliki implementasi server, keamanan autentikasi/otorisasi, pengelolaan data, serta integrasi.
- Rekayasa Aplikasi Full-Stack menghubungkan kapabilitas backend ke alur produk.
- Penilaian Risiko memiliki pemeriksaan konsekuensi.
- QA memiliki verifikasi independen.
- Rekayasa Deployment dan Rilis memiliki penerapan produksi.
