---
name: review-desain-platform-apple
title: Review Desain Platform Apple dan Human Interface Guidelines
category: development
subcategory: platform-ux-and-design-review
source_type: official-guideline-based-operational-synthesis
sources:
  - Apple Human Interface Guidelines: https://developer.apple.com/design/human-interface-guidelines/
  - Apple Design Skill: https://github.com/dickwu/apple-design-skill
language: Indonesian
description: "Meninjau antarmuka untuk platform Apple berdasarkan konvensi platform dan Human Interface Guidelines."
triggers: ["iOS","iPhone app","HIG","apple design","desain macOS","SwiftUI"]
out_of_scope: "Desain visual universal atau kepemilikan implementasi"
escalation: "Serahkan arah visual umum dan implementasi kepada pemilik skill terkait; periksa panduan Apple resmi terkini untuk komponen spesifik."
---

# Review Desain Platform Apple dan Human Interface Guidelines

## Tujuan

Membantu merancang, meninjau, dan memperbaiki antarmuka Apple dengan menjaga konvensi platform, aksesibilitas, identitas produk, serta tugas pengguna.

Gunakan untuk review iOS, iPadOS, macOS, watchOS, visionOS; aplikasi SwiftUI/UIKit/AppKit atau lintas platform; serta navigasi, toolbar, tab bar, sheet, dialog, form, pengaturan, onboarding, notifikasi, dan widget.

Skill ini fokus pada review platform, bukan pengganti desain frontend umum, implementasi engineering, atau konsultasi panduan resmi untuk komponen tertentu.

## Prinsip desain

1. **Tujuan:** fungsi produk dan tugas saat ini harus jelas.
2. **Kendali:** pengguna memahami tindakan dan dapat membatalkannya bila memungkinkan.
3. **Tanggung jawab:** hormati privasi, keamanan, aksesibilitas, data, dan konsekuensi sistem.
4. **Keakraban:** gunakan pola platform yang dikenali bila membantu.
5. **Fleksibilitas:** dukung konteks, preferensi, input, ukuran layar, dan tingkat pengalaman berbeda.
6. **Kesederhanaan:** kurangi kompleksitas tanpa menyembunyikan pilihan penting.
7. **Kualitas craft:** perhatikan tipografi, hierarki, alignment, material, transisi, konten, dan implementasi.
8. **Kesenangan:** tambahkan karakter bila memperkuat produk, bukan mengganggu tugas.

Prinsip ini kerangka review, bukan pengganti aturan komponen spesifik. Bila panduan Apple terkini berbeda, ikuti panduan relevan dan jelaskan konteks.

## Lensa review

1. **Aksesibilitas:** skala teks, kontras, VoiceOver, keyboard/fokus, target interaksi, reduced motion, form, validasi, dan status. Jangan mengklaim lulus tanpa tes.
2. **Konvensi platform:** mobile/tablet mencakup hierarki navigasi, safe area, keyboard, sheet, alert, gestur, dan alternatif. Desktop mencakup window, menu, toolbar, sidebar, shortcut, hover, fokus, dan drag-drop. Tentukan dengan sengaja perilaku native vs konsisten pada lintas platform.
3. **Visual/craft:** peran warna, tipografi, density, spasi, ikon, material, motion, dan merek. Pastikan efek sesuai versi OS dan konteks.
4. **Interaksi:** loading, sukses/error/kosong/offline, feedback, modalitas, cancel/undo, aksi destruktif, input, validasi, dan fokus.
5. **Konten:** label akurat, instruksi ringkas, empty/error state jelas, istilah platform tepat, prompt izin menjelaskan manfaat, dan tidak meniru pesan sistem.

## Alur review

1. Tetapkan platform, versi OS bila diketahui, framework, perangkat, tujuan, audiens, dan tugas utama.
2. Periksa screenshot, file desain, render, atau source yang benar-benar tersedia; nyatakan cakupan bukti.
3. Buka halaman Apple HIG resmi yang relevan dengan komponen dan teknologi yang terlihat.
4. Audit lima lensa di atas; pisahkan mismatch platform dari preferensi visual/usability umum.
5. Prioritaskan: **Kritis** (menghalangi akses/tugas inti), **Tinggi** (mismatch besar), **Sedang** (membingungkan/tidak konsisten), **Polish** (penyempurnaan craft).
6. Berikan isu, dampak, panduan terkait, dan arah perbaikan sesuai framework.
7. Verifikasi render, ukuran, appearance, interaksi, dan aksesibilitas sejauh alat memungkinkan.
8. Pisahkan bukti observasi, interpretasi panduan, asumsi, dan tes yang belum dilakukan.

## Format laporan

Ringkasan; temuan kritis; perbaikan (bukti, dampak, panduan resmi, solusi); craft; keputusan yang perlu dipertahankan; verifikasi platform/viewport/state dan batas pemeriksaan.

## Sumber dan keterbatasan

Sumber utama: Apple Human Interface Guidelines, https://developer.apple.com/design/human-interface-guidelines/. Referensi sekunder: https://github.com/dickwu/apple-design-skill. Dokumen ini sintesis operasional, bukan salinan koleksi panduan Apple atau reproduksi penuh dokumentasi. Prinsip dan lensa review adalah kerangka ringkas; keputusan komponen harus dicek pada halaman Apple resmi terkini. Screenshot saja tidak dapat membuktikan perilaku runtime, accessibility tree, target sentuh, keyboard, atau kepatuhan App Store. Tes otomatis tidak menggantikan assistive technology dan perangkat nyata.
