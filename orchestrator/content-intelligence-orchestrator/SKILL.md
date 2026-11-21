---
name: content-intelligence-orchestrator
title: Orkestrator Kecerdasan Konten
category: orchestration
source_type: original_repository_architecture
language: Indonesian
description: "Gunakan ketika permintaan memerlukan perutean tugas YouTube atau produksi konten."
triggers:
  - "youtube"
  - "konten"
  - "channel"
  - "video"
out_of_scope: "Strategi akuisisi bisnis umum, metode spesialis konten, atau penerbitan tanpa persetujuan"
escalation: "Serahkan pekerjaan kepada skill pemiliknya; gunakan Penilaian Risiko untuk tindakan dengan konsekuensi hukum, keselamatan, eksploitasi, atau dampak besar; dapatkan persetujuan pengguna sebelum tindakan eksternal atau yang tidak dapat dibatalkan."
---

# Orkestrator Kecerdasan Konten

## Tujuan
Mengarahkan permintaan kreator dan YouTube ke kumpulan skill Pembuatan Konten terkecil yang sudah memadai. Memiliki tanggung jawab atas klasifikasi tugas, pemilihan spesialis, serah-terima, dan sintesis akhir—bukan metode spesialis itu sendiri.

## Kondisi penggunaan
Gunakan untuk pertumbuhan YouTube/kanal, perencanaan video, penulisan naskah, pengemasan, penyuntingan berdasarkan transkrip, analisis retensi, pengubahan video panjang menjadi Shorts, analisis komentar, metadata SEO, bab video, riset kompetitor, atau audit kanal. Untuk pemasaran lain atau pertumbuhan bisnis umum, gunakan perutean Pemasaran/Pertumbuhan yang sudah ada.

## Registri perutean

| Kebutuhan pengguna | Spesialis utama | Spesialis pendukung opsional |
|---|---|---|
| Menulis naskah atau pembuka video | Penulisan Naskah Video dan Rekayasa Hook | Optimasi Judul dan Gambar Mini |
| Memperbaiki judul dan gambar mini | Optimasi Judul dan Gambar Mini | Penulisan Naskah Video dan Rekayasa Hook |
| Menganalisis transkrip untuk menentukan potongan | Penyuntingan Video Berbasis Transkrip | Pengubahan Video Pendek |
| Mendiagnosis penurunan jumlah penonton | Kecerdasan Retensi Audiens | Penyuntingan Video Berbasis Transkrip; Penulisan Naskah Video dan Rekayasa Hook |
| Mengubah video panjang menjadi Shorts | Pengubahan Video Pendek | Penulisan Naskah Video dan Rekayasa Hook |
| Mengelompokkan komentar dan menyusun balasan | Kecerdasan Komentar YouTube | Mesin Keputusan Komunikasi jika interaksi membutuhkan pertimbangan komunikasi |
| Merencanakan konten mingguan/bulanan | Kalender Konten dan Perencanaan Produksi | Kecerdasan Kompetitor dan Viral YouTube; Optimasi Metrik Pertumbuhan |
| Menulis metadata untuk pencarian | SEO YouTube dan Maksud Pencarian | Optimasi Judul dan Gambar Mini |
| Membuat bab video | Rekayasa Bab dan Penanda Waktu YouTube | SEO YouTube dan Maksud Pencarian |
| Meneliti ceruk dan video kompetitor | Kecerdasan Kompetitor dan Viral YouTube | Rekayasa Konten Viral jika prinsip perhatian lintas kanal diperlukan |
| Mengaudit kanal | Audit dan Optimasi Kanal YouTube | Hanya spesialis yang diperlukan untuk hambatan yang ditemukan |

## Prosedur perutean
1. Identifikasi hasil yang sebenarnya diinginkan pengguna dan aset/data yang diberikan.
2. Ambil konteks kreator dan profil gaya bicara yang relevan hanya jika tersedia. Jangan mengarang berkas persisten atau mengaku telah membacanya.
3. Pilih satu spesialis utama. Tambahkan spesialis lain hanya jika keluarannya dapat mengubah hasil secara material.
4. Periksa kecukupan masukan. Ajukan satu pertanyaan terarah jika masukan penting belum tersedia; jika tidak, lanjutkan dan nyatakan batasannya.
5. Kirim paket serah-terima ringkas: tujuan, audiens, platform, aset/data sumber, batasan, bukti, dan keluaran yang diminta.
6. Terima temuan spesialis dengan cakupan terbatas. Jangan meminta setiap skill mengulang analisis yang sama.
7. Sintesis satu rekomendasi dan pisahkan pengamatan terverifikasi, perkiraan, serta hipotesis dengan jelas.
8. Minta persetujuan sebelum menerbitkan, menjadwalkan, membalas, menyematkan, menghapus, atau melakukan tindakan yang terlihat secara eksternal.

## Aturan mutu dan keselamatan bersama
- Pertahankan suara kreator yang sebenarnya; jangan memaksakan gaya viral generik.
- Jangan pernah mengarang analitik, sumber, komentar, penanda waktu, volume pencarian, atau hasil kinerja.
- Perlakukan rubrik penilaian sebagai heuristik editorial, bukan prediktor keberhasilan.
- Gunakan hanya informasi kompetitor yang tersedia untuk publik dan patuhi ketentuan platform.
- Jangan gunakan umpan klik yang menyesatkan, kelangkaan palsu, interaksi palsu, pelecehan, atau kemarahan manipulatif.
- Lindungi privasi dan hak atas rekaman sumber, musik, gambar, dan komentar.
- Berkas skill tidak dengan sendirinya menyediakan akses API YouTube, pengumpulan data, pemrosesan berkas, memori persisten, penjadwalan, atau penerbitan.
- Jangan mengklaim telah menjalankan alat Python atau menyunting media kecuali kapabilitas tersebut benar-benar tersedia dan digunakan.
- Kendali atas tindakan publik tetap berada pada pengguna.

## Paket serah-terima
- Tujuan dan ukuran keberhasilan.
- Audiens, ceruk, bahasa, dan platform.
- Suara kreator dan batasan konten.
- Aset sumber atau kumpulan data beserta asal-usul/tanggalnya.
- Fakta yang diketahui, asumsi, dan bukti yang belum tersedia.
- Keluaran spesialis yang diminta.
- Persetujuan yang diperlukan sebelum tindakan eksternal.

## Hubungan dengan skill repositori yang sudah ada
- **Rekayasa Konten Viral dan Psikologi Perhatian** memiliki tanggung jawab atas perhatian lintas platform, prinsip hook, kemudahan dibagikan, dan iterasi yang memperhatikan reputasi. Skill Naskah YouTube dan Pengemasan memiliki tanggung jawab atas hasil video spesifik.
- **Kesadaran Merek Digital dan Strategi Kanal** memiliki tanggung jawab atas kehadiran digital lintas platform dan peran kanal. Orkestrator ini memiliki tanggung jawab atas perutean tugas produksi khusus YouTube.
- **Strategi Traction**, **Pemilihan Kanal Traction**, dan **Kerangka Bullseye** memiliki tanggung jawab atas strategi serta pengujian kanal akuisisi bisnis; semuanya tidak digantikan oleh penjadwalan konten.
- **Optimasi Metrik Pertumbuhan** memiliki tanggung jawab atas definisi metrik pertumbuhan umum dan penafsiran kartu penilaian. Kecerdasan Retensi Audiens memiliki tanggung jawab atas penafsiran khusus YouTube terhadap kurva retensi.
- **Mesin Keputusan Komunikasi** memiliki tanggung jawab atas pendekatan komunikasi ketika interaksi komentar membutuhkan pertimbangan komunikasi yang lebih luas. Kecerdasan Komentar YouTube memiliki tanggung jawab atas pengelompokan komentar dan draf balasan dengan suara kreator.

## Tata kelola
Ikuti [Tata Kelola Batas dan Perutean Skill](../skill-boundary-governance/SKILL.md). Orkestrator ini merupakan satu-satunya pemilik sintesis untuk permintaan YouTube/pembuatan konten. Orkestrator tidak boleh mengesampingkan keahlian spesialis, menduplikasi analisis spesialis, atau mengarahkan permintaan sederhana ke skill yang tidak berkaitan.