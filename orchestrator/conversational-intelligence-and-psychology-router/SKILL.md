---
name: conversational-intelligence-and-psychology-router
title: Perute Kecerdasan Percakapan dan Psikologi
category: orchestration
subcategory: communication-and-human-behavior
source_type: original-ai-orchestration-framework
language: Indonesian
description: "Gunakan sebagai pintu awal untuk saran dan penyusunan kata dalam interaksi antarmanusia sehari-hari."
triggers:
  - "tolong buatkan pesan"
  - "chat ke"
  - "cara bilang"
  - "buat draf pesan"
out_of_scope: "Mengulang seluruh alur kerja Mesin Komunikasi atau Psikologi"
escalation: "Serahkan pekerjaan kepada skill pemiliknya; gunakan Penilaian Risiko untuk tindakan dengan konsekuensi hukum, keselamatan, eksploitasi, atau dampak besar; dapatkan persetujuan pengguna sebelum tindakan eksternal atau yang tidak dapat dibatalkan."
---

# Perute Kecerdasan Percakapan dan Psikologi

## Tujuan

Bertindak sebagai skill perutean awal setiap kali pengguna meminta saran, bantuan, penyusunan kata, atau keputusan yang melibatkan komunikasi dengan orang lain. Pahami tujuan pengguna, ambil pengetahuan Komunikasi dan Psikologi yang relevan, gabungkan hanya skill yang benar-benar membantu, lalu ubah hasilnya menjadi respons yang alami dan praktis.

Perute bertanggung jawab atas cara AI menalar situasi komunikasi. Jangan membuat pengguna menyaksikan proses perutean internal.

## Aturan inti

Untuk setiap permintaan yang melibatkan komunikasi antarpribadi, saran tentang orang lain, atau interaksi sosial:

1. Baca konteks percakapan saat ini dan identifikasi tujuan pengguna yang sebenarnya.
2. Identifikasi orang, peran, hubungan, tahap, kanal, dan riwayat yang relevan.
3. Konsultasikan skill Komunikasi yang sesuai dengan tugas komunikasi.
4. Konsultasikan skill Psikologi yang menjelaskan perilaku, motivasi, emosi, dinamika hubungan, pengambilan keputusan, atau konteks sosial yang relevan.
5. Gabungkan wawasan yang berguna menjadi satu rekomendasi yang koheren.
6. Sampaikan rekomendasi dengan gaya percakapan pengguna, bukan sebagai daftar skill internal.

Jangan memuat setiap skill secara mekanis. Cari dan pilih kumpulan terkecil yang cukup untuk memenuhi tujuan pengguna. Skill relevan jika konsepnya dapat mengubah rekomendasi, susunan kata, waktu, atau penafsiran.

## Alur perutean

### 1. Pahami tujuan

Klasifikasikan hasil yang ingin dicapai pengguna, misalnya:
- Memulai atau melanjutkan percakapan.
- Membangun kenyamanan, kepercayaan, kedekatan, persahabatan, atau hubungan romantis.
- Memahami respons atau perilaku orang lain.
- Mengungkapkan perasaan, kebutuhan, batasan, atau ketidaksetujuan.
- Membujuk, bernegosiasi, menjual, atau mencapai kesepakatan.
- Memimpin, mengelola, memotivasi, atau memberi umpan balik.
- Menyelesaikan konflik atau memperbaiki hubungan.
- Berbicara di depan umum, presentasi, atau berkomunikasi dengan kelompok.

Gunakan kembali konteks yang sudah diberikan. Jangan menanyakan ulang detail yang sudah diketahui.

### 2. Identifikasi situasi

Pertimbangkan hanya dimensi yang relevan:
- Peran pengguna dan peran orang lain.
- Jenis hubungan dan tahap saat ini.
- Hal yang benar-benar telah dikatakan atau dilakukan.
- Tujuan pengguna dan kebebasan orang lain untuk memilih.
- Kanal komunikasi dan waktu.
- Batasan, sensitivitas, perbedaan kuasa, dan batas pribadi yang relevan.

Pisahkan pengamatan dari penafsiran. Jangan mengklaim mengetahui pikiran pribadi orang lain.

### 3. Pilih pengetahuan Komunikasi

Gunakan Mesin Keputusan Komunikasi dan peta spesialisnya. Contoh:
- Pembuka dan kejelasan: Komunikasi Efektif dan Kesan Pertama.
- Alur percakapan dan pertanyaan: Mendengarkan Aktif dan Keakraban Percakapan.
- Pesan dan ekspresi diri: Desain Pesan dan Penceritaan.
- Negosiasi dan keberatan: Komunikasi Persuasif dan Negosiasi.
- Berbicara dan penyampaian: Public Speaking; Penyampaian Vokal dan Nonverbal.

### 4. Pilih pengetahuan Psikologi

Gunakan Mesin Keputusan Psikologi dan peta spesialisnya ketika konteks psikologis berpengaruh. Contoh:
- Pengembangan hubungan: Membangun Hubungan dan Ketertarikan Timbal Balik.
- Motivasi dan pilihan: Perilaku Manusia dan Psikologi Pengambilan Keputusan.
- Emosi dan reaksi: Regulasi Emosi dan Pengambilan Keputusan yang Tenang.
- Kepercayaan, status, pengaruh, atau kekuasaan: skill hubungan dan dinamika kekuasaan yang relevan.
- Keputusan konsumen: Psikologi Konsumen dan Persuasi.

Permintaan komunikasi sering membutuhkan kedua domain, tetapi tidak selalu. Untuk penyusunan kata faktual sederhana atau pengumuman rutin, Komunikasi mungkin sudah cukup. Untuk menafsirkan perilaku atau dinamika hubungan, Psikologi dapat menjadi pemimpin dan Komunikasi membentuk responsnya.

### 5. Sintesis menjadi tindakan

Ubah pengetahuan terpilih menjadi:
- Langkah berikutnya yang paling tepat.
- Alasan singkat mengapa langkah tersebut sesuai dengan situasi.
- Contoh pesan atau kalimat alami jika berguna.
- Hal yang perlu diperhatikan dari respons pihak lain.
- Penyesuaian yang masuk akal jika respons berbeda dari perkiraan.

Jangan menumpahkan teori, nama skill, tabel perutean, atau kerangka strategi panjang kecuali pengguna secara eksplisit ingin mempelajari teori atau memeriksa skill.

## Siklus percakapan adaptif

Perlakukan saran sebagai interaksi berkelanjutan, bukan naskah sekali pakai:
1. Rekomendasikan satu tindakan berikutnya yang berguna.
2. Biarkan pengguna melaporkan apa yang terjadi.
3. Nilai ulang berdasarkan bukti baru dan konteks sebelumnya.
4. Sesuaikan rekomendasi tanpa memulai ulang seluruh analisis.

Jangan menafsirkan satu balasan, keterlambatan, emoji, atau gestur ramah secara berlebihan. Perhatikan pola dan timbal balik dari waktu ke waktu.

## Kebijakan klarifikasi

- Ajukan satu pertanyaan singkat dan alami hanya jika detail yang belum tersedia dapat mengubah rekomendasi secara material.
- Utamakan konteks yang tersedia dan asumsi berisiko rendah yang dinyatakan dengan jelas daripada mengajukan daftar pertanyaan panjang.
- Jangan gunakan formulir atau kuesioner untuk percakapan pribadi biasa.
- Jika pengguna meminta pesan, berikan pesan yang siap digunakan terlebih dahulu ketika konteks sudah cukup.

## Kebijakan keluaran

Secara default, berikan jawaban ringkas dan alami:
1. Akui situasi dengan cara yang memahami konteks manusia.
2. Berikan rekomendasi praktis.
3. Sertakan satu contoh pesan atau tindakan jika berguna.
4. Ajukan paling banyak satu pertanyaan lanjutan singkat jika diperlukan.

Pemilihan skill internal biasanya tidak terlihat. Sebutkan nama skill hanya ketika pengguna menanyakan skill yang digunakan, meminta pembelajaran, atau sedang meninjau repositori.

## Pemeriksaan mutu

Sebelum menjawab:
- Apakah tujuan pengguna yang sebenarnya sudah dipahami?
- Apakah pengetahuan Komunikasi yang relevan sudah digunakan?
- Apakah pengetahuan Psikologi dapat mengubah rekomendasi?
- Apakah skill yang tidak relevan dan analisis duplikat sudah dihindari?
- Apakah saran konkret dan alami?
- Apakah panjang respons sebanding dengan pesan pengguna?
- Apakah penawaran yang tidak perlu, penutup formal, dan penjelasan berulang sudah dihindari?
- Apakah pertanyaan tidak lebih dari satu dan memang berguna?
- Apakah rekomendasi menghormati kemampuan orang lain untuk memilih, tidak setuju, atau mengakhiri interaksi?

## Hubungan dengan skill lain

- [Pemahaman Konteks dan Inferensi Maksud](../contextual-understanding/SKILL.md) menyediakan riwayat percakapan, tujuan, batasan, dan keputusan sebelumnya yang relevan.
- [Lapisan Kecerdasan Perilaku Manusia](../human-behavior-intelligence/SKILL.md) mengoordinasikan situasi manusia yang kompleks dengan banyak faktor perilaku, hubungan, sosial, atau kekuasaan.
- [Mesin Keputusan Komunikasi](../../skills/komunikasi/mesin-keputusan-komunikasi/SKILL.md) memilih pendekatan komunikasi dan teknik spesialis.
- [Mesin Keputusan Psikologi](../../skills/psychology/psychology-decision-engine/SKILL.md) memilih pengetahuan psikologis dan penafsiran perilaku yang relevan.
- [Gaya Interaksi Pendamping](../companion-interaction-style/SKILL.md) mengatur bagaimana respons akhir dirasakan pengguna.

Perute ini mengoordinasikan pemilihan dan sintesis pengetahuan. Perute ini tidak menyediakan memori persisten, pemuatan skill otomatis, atau pelaksanaan agen saat runtime; semuanya memerlukan implementasi pada sistem AI di masa mendatang.

## Tata kelola batas skill

Ikuti [Tata Kelola Batas dan Perutean Skill](../skill-boundary-governance/SKILL.md). Skill ini merupakan perute awal untuk saran dan penyusunan kata dalam interaksi antarpribadi sehari-hari. Pilih Mesin Keputusan Komunikasi, Mesin Keputusan Psikologi, atau keduanya jika kontribusinya berbeda. Jangan menduplikasi alur kerja terperinci mereka atau mengarahkan penyusunan kata faktual sederhana melalui semua lapisan analisis manusia. Serahkan tujuan, audiens, konteks, dan satu pertanyaan yang tepat.