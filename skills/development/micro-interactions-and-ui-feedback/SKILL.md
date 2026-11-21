---
name: micro-interactions-and-ui-feedback
title: Interaksi Mikro dan Desain Umpan Balik UI
category: development
source_type: user-provided-video-and-operational-framework
source: Video pengguna 67332.mp4
language: Indonesian
description: "Merancang respons kecil, state interaksi, animasi, loading, dan feedback antarmuka yang membantu pengguna."
triggers: ["animasi tombol","hover","skeleton","micro-interaction","feedback UI"]
out_of_scope: "Arsitektur navigasi atau identitas visual keseluruhan"
escalation: "Serahkan navigasi global kepada pemiliknya dan arah visual kepada Desain Frontend; gunakan Penilaian Risiko untuk risiko material."
---

# Interaksi Mikro dan Desain Umpan Balik UI

## Tujuan

Merancang respons kecil terhadap tindakan pengguna, peristiwa sistem, atau perubahan state agar produk terasa jelas dan responsif. Interaksi mikro dapat menunjukkan elemen interaktif, mengakui tindakan, memberi progres, menjelaskan perubahan, atau mengarahkan perhatian. Jangan menganimasikan semua elemen; setiap efek harus meningkatkan feedback, pemahaman, orientasi, atau responsivitas tanpa mengganggu tugas.

Video 67332.mp4 menunjukkan empat teknik visual: animasi tombol, hover kartu, skeleton loading, dan glow. Kriteria pemilihan, aksesibilitas, implementasi, serta pengujian di bawah adalah panduan tambahan, bukan klaim dari video.

## Teknik

### 1. Animasi tombol
Perubahan kecil pada skala, posisi, warna, bayangan, atau highlight untuk mengakui hover/tekan.
- Definisikan state default, hover, focus-visible, pressed, disabled, dan loading sesuai kebutuhan.
- Gunakan transisi singkat dan terkendali; pertahankan kontras.
- Cegah pengiriman berulang saat proses berlangsung.
- Animasi bukan pengganti status untuk aksi penting seperti simpan, pembayaran, atau hapus.

### 2. Efek hover kartu
Elevasi, bayangan, border, latar, atau gerak kecil untuk menunjukkan kartu interaktif.
- Gunakan hanya jika kartu memiliki aksi.
- Sediakan fokus keyboard yang terlihat dan area klik/destinasi yang jelas.
- Informasi penting tidak boleh hanya muncul saat hover.
- Pastikan tetap jelas di perangkat sentuh.
- Bila kartu punya beberapa aksi, gunakan tautan/tombol terpisah.

### 3. Skeleton loading
Placeholder sementara yang meniru bentuk konten saat data dimuat.
- Sesuaikan ukuran dan susunan dengan konten yang diharapkan.
- Ganti dengan konten nyata, empty state, atau error setelah proses selesai.
- Gunakan shimmer hanya bila membantu; hormati reduced motion.
- Sediakan status aksesibel bila waktu tunggu bermakna.
- Jangan biarkan skeleton tampil selamanya ketika request gagal.

### 4. Glow
Highlight lembut di sekitar elemen untuk menekankan fokus, pilihan, atau aksi utama.
- Gunakan secara selektif dan sebagai penguat state yang sudah jelas.
- Jaga kontras; jangan jadikan glow satu-satunya indikator fokus, validasi, atau status.
- Hindari glow besar/terus bergerak dan efek bayangan berlapis yang berat.

## Memilih feedback

| Kebutuhan | Feedback | Syarat |
|---|---|---|
| Mengakui klik/tekan | Animasi tombol | Aksi tetap jelas |
| Menunjukkan kartu bisa dibuka | Hover dan fokus | Keyboard dan touch didukung |
| Menunjukkan konten sedang dimuat | Skeleton | Berakhir pada konten, kosong, atau error |
| Menekankan fokus/pilihan | Glow ringan | Ada indikator state lain |
| Mengonfirmasi aksi penting | Teks status, ikon, notifikasi | Jangan hanya mengandalkan animasi |
| Menjelaskan aksi gagal | Validasi/error | Jelaskan pemulihan bila perlu |

Jika efek tidak memperbaiki feedback, pemahaman, hierarki, atau penyelesaian tugas, jangan gunakan.

## Model state

Pilih state yang relevan: default, hover, focus-visible, active/pressed, selected, disabled, loading, success, dan error. Tidak semua komponen membutuhkan semuanya. Makna visual harus konsisten di seluruh produk.

## Alur implementasi

1. Periksa framework, komponen, token, konvensi styling, dan perilaku saat ini.
2. Pahami tindakan/peristiwa dan feedback yang dibutuhkan.
3. Pilih respons terkecil yang berguna.
4. Tentukan awal, akhir, sukses, gagal, pembatalan, dan timeout.
5. Rancang untuk pointer, keyboard, touch, dan teknologi bantu.
6. Hormati reduced motion.
7. Jaga kontras, fokus, semantik, status, dan target sentuh.
8. Utamakan transform/opacity bila sesuai; hindari animasi layout mahal.
9. Gunakan komponen dan token yang ada; jangan menambah dependensi tanpa alasan.
10. Uji state relevan dan pastikan feedback cukup terlihat tanpa mengalihkan perhatian.

## Aksesibilitas dan performa

Jangan menyembunyikan fungsi penting pada hover. Semua elemen interaktif harus dapat diakses keyboard dengan fokus jelas. Jangan menyampaikan sukses, gagal, pilihan, atau validasi hanya lewat warna/animasi. Hindari flashing, pulsing cepat, dan gerak berulang yang mengganggu. Jaga target stabil, status loading dapat dipahami, serta kontras cukup.

Utamakan sistem animasi proyek atau CSS sederhana. Gunakan transform/opacity bila tepat; hindari animasi dimensi layout, blur besar, dan banyak shadow bergerak. Jangan menambah library untuk transisi sederhana. Gerak tidak boleh menunda tindakan, menyebabkan layout shift, atau menutupi konten. Uji perangkat mobile berdaya rendah.

## Checklist

- Setiap efek punya tujuan pengguna.
- Tombol memiliki feedback state yang sesuai.
- Kartu interaktif jelas dan berfungsi tanpa hover.
- Skeleton sesuai konten dan hilang setelah loading.
- Kegagalan loading menampilkan error/retry.
- Glow memperkuat, bukan menggantikan informasi state.
- Fokus terlihat, reduced motion dihormati, kontras cukup.
- Gerak tidak menghambat tugas atau performa.
- Implementasi mengikuti sistem proyek.

## Hubungan skill

AI Interface Design memberi audit visual menyeluruh; Pola Navigasi Web Modern memiliki navigasi global; Desain Frontend memiliki arah visual; Full-Stack mengimplementasikan state; QA menguji perilaku. Skill ini fokus pada feedback dan respons state komponen, bukan navigasi atau identitas visual.
