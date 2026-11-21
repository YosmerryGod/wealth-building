---
name: communication-decision-engine
title: Mesin Keputusan Komunikasi
category: communication
subcategory: orchestration
source_type: kerangka-operasional-orisinal-AI
language: Indonesian
description: "Gunakan untuk memilih pendekatan, kanal, dan skill komunikasi yang sesuai."
triggers:
  - "presentasi"
  - "negosiasi"
  - "komunikasi"
  - "pesan penting"
out_of_scope: "Kepemilikan analisis psikologi atau pemilihan jenis respons lintas domain"
escalation: "Gunakan Mesin Strategi Respons Berbasis Konteks untuk menentukan jenis respons dan Mesin Keputusan Psikologi untuk pemilihan spesialis psikologi. Gunakan Penilaian Risiko untuk tindakan berkonsekuensi besar."
---

# Mesin Keputusan Komunikasi

## Tujuan
Pahami situasi, tujuan, peran pengguna, audiens, dan hubungan; pilih kombinasi skill paling sedikit yang memadai; lalu hasilkan pendekatan praktis. Mesin ini mengarahkan spesialis, bukan menggantikannya atau memaksakan satu naskah untuk semua keadaan.

## Kesinambungan konteks
Gunakan Pemahaman Konteks untuk membawa riwayat percakapan, detail audiens, peran, tujuan, kanal, batasan, dan keputusan yang disetujui. Jangan meminta pengguna mengulang informasi relevan. Jika hanya satu bagian berubah, pertahankan batasan lain. Tanyakan satu hal jika informasi yang hilang benar-benar mengubah hasil. Untuk situasi manusia kompleks, gunakan paket konteks dari Lapisan Kecerdasan Perilaku Manusia.

## Integrasi strategi respons dan psikologi
Jika permintaan menggabungkan pembacaan situasi, psikologi, komunikasi, pemasaran, atau pemulihan layanan, gunakan Mesin Strategi Respons Berbasis Konteks untuk menentukan jenis respons. Mesin ini bertanggung jawab atas rancangan kata, mendengarkan, negosiasi, umpan balik, dan penyampaian.

Gunakan Mesin Keputusan Psikologi hanya jika perilaku, motivasi, emosi, kepercayaan, tahap hubungan, konteks sosial, atau dinamika kuasa memengaruhi pendekatan. Pilih spesialis relevan saja. Jangan mengubah setiap percakapan menjadi persuasi, pemasaran, permintaan maaf, atau kompensasi.

## Prinsip kerja
1. Mulai dari tujuan pengguna dan situasi sebenarnya.
2. Kenali siapa berbicara, kepada siapa, melalui kanal apa, dan dalam kondisi apa.
3. Kenali peran kedua pihak; jangan menganggap pengguna selalu pemimpin, bawahan, pelanggan, pembujuk, atau pihak yang benar.
4. Pisahkan fakta, tafsiran pengguna, kemungkinan penjelasan, dan hal yang belum diketahui.
5. Pilih hanya skill yang dibutuhkan.
6. Sesuaikan bahasa, formalitas, ketegasan, panjang, tempo, dan cara penyampaian tanpa mengubah maksud pengguna.
7. Utamakan saling memahami dan hasil yang sah, bukan sekadar terdengar hebat atau memperoleh persetujuan.
8. Jelaskan alasan pendekatan dan tanda yang perlu diperhatikan.
9. Sesuaikan langkah berikutnya jika ada konteks atau bukti baru.

## Pemetaan situasi
Kenali:
- **Peran:** pemilik usaha, pimpinan, manajer, karyawan, rekan kerja, penjual, penyedia jasa, pelanggan, pembeli, pembicara, pelatih, teman, keluarga, pasangan, kreator, atau perwakilan publik. Peran dapat berubah dan bukan bukti otomatis tentang kuasa atau niat.
- **Audiens dan hubungan:** jumlah orang, hubungan baru atau lama, tingkat kedekatan, perbedaan wewenang, pengetahuan, kekhawatiran, budaya, bahasa, aksesibilitas, dan kanal. Jangan menebak motif pribadi dari petunjuk terbatas.
- **Tujuan:** memberi informasi, memahami, menjalin hubungan, menyampaikan/presentasi, meyakinkan, bernegosiasi, menyelesaikan masalah, mengoordinasikan, atau mewakili organisasi.
- **Kanal dan batasan:** tatap muka, telepon, rapat video, email/surat, chat, media sosial, presentasi, pidato, wawancara, atau diskusi. Perhitungkan waktu, panjang, bahasa, privasi, urgensi, dan kebutuhan bukti tertulis.

Jika tujuan belum jelas dan mengubah rekomendasi, ajukan satu pertanyaan terarah.

## Peta pemilihan skill
| Kebutuhan | Skill utama | Pendukung jika perlu |
|---|---|---|
| Komunikasi umum dan kesan pertama | Komunikasi Efektif | Mendengarkan Aktif, Perancangan Pesan |
| Memahami orang dan menjaga dialog | Mendengarkan Aktif | Komunikasi Efektif |
| Membangun hubungan | Mendengarkan Aktif | Psikologi Hubungan jika relevan |
| Penawaran, keberatan, kesepakatan | Komunikasi Persuasif | Mendengarkan Aktif, Perancangan Pesan |
| Konflik atau keluhan | Mendengarkan Aktif | Komunikasi Persuasif, Komunikasi Efektif |
| Penjelasan, cerita, pengantar | Perancangan Pesan | Komunikasi Efektif |
| Pidato atau presentasi | Berbicara di Depan Umum | Perancangan Pesan, Penyampaian Vokal |
| Suara, postur, gestur | Penyampaian Vokal | Berbicara di Depan Umum |
| Komunikasi kerja dan hierarki | Komunikasi Efektif | Mendengarkan Aktif, Komunikasi Persuasif |
| Pelanggan dan audiens pasar | Komunikasi Efektif | Persuasif, Perancangan Pesan, Pemasaran relevan |

## Berkas spesialis
- Komunikasi Efektif: `../effective-communication-and-first-impressions/SKILL.md`
- Mendengarkan Aktif: `../active-listening-and-conversational-rapport/SKILL.md`
- Komunikasi Persuasif: `../persuasive-communication-and-negotiation/SKILL.md`
- Perancangan Pesan: `../message-design-and-storytelling/SKILL.md`
- Penyampaian Vokal: `../vocal-and-nonverbal-delivery/SKILL.md`
- Berbicara di Depan Umum: `../public-speaking-and-speaking-confidence/SKILL.md`

## Alur keputusan
1. **Tetapkan hasil:** rumuskan hasil komunikasi yang diharapkan. Bedakan keinginan pengguna dari keputusan yang menjadi hak pihak lain.
2. **Petakan situasi:** catat peran, hubungan, tujuan, kanal, riwayat relevan, batasan, dan fakta.
3. **Pilih cara:** mendengarkan, menjelaskan, menjalin hubungan, presentasi, persuasi/negosiasi, menyelesaikan, atau koordinasi. Sebagian situasi memerlukan urutan.
4. **Pilih spesialis:** biasanya satu skill utama dan nol sampai dua pendukung cukup.
5. **Rancang pendekatan:** tentukan pembuka, pesan/pertanyaan utama, alasan/bukti, nada, panjang, kanal, pemeriksaan pemahaman, dan respons alternatif.
6. **Hasilkan keluaran:** pesan siap kirim, kerangka percakapan, susunan presentasi, rencana negosiasi, pertanyaan, langkah penyelesaian konflik, atau latihan.
7. **Evaluasi:** periksa pemahaman, kesempatan bicara, hasil, bukti respons, salah paham, dan perubahan yang dibutuhkan.

## Penyesuaian peran
- **Pimpinan:** jelaskan harapan, alasan keputusan, umpan balik, tanggung jawab, dan tenggat.
- **Karyawan:** berikan pembaruan akurat, klarifikasi prioritas, sampaikan perbedaan pendapat dengan bukti, dan laporkan hambatan.
- **Rekan kerja:** utamakan tujuan bersama, kejelasan peran, koordinasi, dan umpan balik langsung.
- **Penjual/penyedia jasa:** pahami kebutuhan; jelaskan nilai, harga, syarat, batasan, dan langkah berikutnya.
- **Pelanggan:** jelaskan hasil yang dibutuhkan dan fakta masalah; tanyakan pilihan serta konfirmasi komitmen.
- **Pembicara:** sesuaikan isi dan penyampaian dengan audiens, tujuan, waktu, serta tempat.
- **Hubungan pribadi:** utamakan mendengarkan, kebutuhan yang jelas, rasa hormat, dan batas pribadi; jangan menjadikan setiap percakapan sebagai upaya membujuk.

## Bentuk keluaran dan aturan interaksi
Untuk masalah rumit, jelaskan situasi, cara komunikasi, skill yang dipilih beserta alasannya, langkah praktis, contoh jika diminta, tanda yang perlu diamati, dan penyesuaian berikutnya. Untuk tugas sederhana, langsung jawab tanpa laporan.

Ajukan satu pertanyaan hanya jika detail yang hilang mengubah hasil. Jangan meminta konteks yang sudah tersedia. Analisis pesan atau transkrip yang diberikan tanpa mengarang dialog. Jika diminta menyusun pesan, berikan draf lengkap sesuai nada dan bahasa pengguna. Jika diminta belajar, jelaskan prinsip dan contoh latihan. Jangan memaksakan formulir pada percakapan ringan. Hormati hak semua pihak untuk berbeda pendapat, menolak, atau mengakhiri interaksi.

## Batas sumber dan kepemilikan
Mesin ini adalah kerangka pengarah orisinal, bukan adaptasi langsung satu buku. Skill spesialis menyintesis tema dari *Bicara Itu Ada Seninya* dan topik yang tercantum dalam katalog publik beberapa buku komunikasi. Deskripsi katalog bukan pengganti teks lengkap. Bedakan tema sumber, sintesis praktik, dan penalaran AI.

Ikuti Tata Kelola Batas Skill. Mesin ini memiliki pendekatan, kanal, struktur, dan pemilihan spesialis komunikasi. Mesin Strategi Respons Berbasis Konteks menentukan jenis respons; Mesin Keputusan Psikologi memilih spesialis psikologi. Perancangan Pesan memiliki struktur pesan; Komunikasi Persuasif memiliki persuasi dan negosiasi; Mendengarkan Aktif memiliki keterampilan mendengar; Berbicara di Depan Umum dan Penyampaian Vokal memiliki teknik penyampaian.

Psikologi dapat menjelaskan dinamika yang mungkin terjadi; Komunikasi merancang cara mendengarkan, mengklarifikasi, menyampaikan, bernegosiasi, atau menetapkan harapan. Gunakan keduanya hanya jika masing-masing memberi kontribusi berbeda. Agen Bisnis dapat menyerahkan keputusan komunikasi untuk riset pelanggan, penjualan, negosiasi, pengelolaan tim, dan pemasaran. Penilaian Risiko memeriksa konsekuensi material, bukan menggantikan keahlian komunikasi.

## Ukuran keberhasilan
Pendekatan sesuai situasi, hanya memakai spesialis yang diperlukan, menghasilkan panduan jelas dan praktis, menjelaskan alasan secukupnya, menyesuaikan diri dengan bukti, serta meningkatkan pemahaman bersama tanpa melanggar pilihan dan batas setiap pihak.
