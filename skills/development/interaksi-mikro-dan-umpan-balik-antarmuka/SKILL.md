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

1. **Animasi tombol:** perubahan kecil pada skala, posisi, warna, atau bayangan untuk mengakui interaksi. Definisikan default, hover, focus, pressed, disabled, loading; cegah submit berulang. Animasi bukan pengganti status penting.
2. **Hover kartu:** elevasi/border/latar ringan untuk kartu yang benar-benar interaktif. Sediakan fokus keyboard, area klik jelas, dan dukungan touch; jangan sembunyikan informasi penting saat hover.
3. **Skeleton loading:** placeholder sesuai struktur konten. Ganti dengan konten, empty, atau error; jangan tampil selamanya. Gunakan shimmer hanya bila berguna dan hormati reduced motion.
4. **Glow:** highlight selektif untuk fokus/pilihan. Jaga kontras; jangan jadikan glow satu-satunya indikator state atau gunakan efek berat/terus bergerak.

Video 67332.mp4 menunjukkan empat teknik visual tersebut. Kriteria pemilihan, aksesibilitas, implementasi, dan pengujian adalah panduan tambahan.

## Memilih feedback

| Kebutuhan | Feedback |
|---|---|
| Mengakui klik | Animasi tombol |
| Menandai kartu interaktif | Hover dan fokus |
| Menunjukkan loading | Skeleton |
| Menekankan fokus/pilihan | Glow ringan plus indikator lain |
| Konfirmasi aksi penting | Teks status/ikon/notifikasi |
| Menjelaskan kegagalan | Error dan petunjuk pemulihan |

Jangan menambah efek jika tidak memperbaiki feedback, pemahaman, hierarki, atau tugas.

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

Jangan menyembunyikan fungsi pada hover. Semua kontrol dapat dioperasikan dengan keyboard dan fokus terlihat. Jangan menyampaikan state hanya lewat warna/animasi. Hindari flashing dan gerak berulang; hormati reduced motion. Jaga target stabil, kontras cukup, dan status loading jelas.

Utamakan sistem animasi proyek atau CSS sederhana. Gunakan transform/opacity bila sesuai; hindari animasi layout, blur/shadow berat, dependensi tak perlu, layout shift, serta gerak yang menunda tugas. Uji mobile berdaya rendah.

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
