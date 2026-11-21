---
name: intelijen-sumber-terbuka-dan-jejak-digital
title: Intelijen Sumber Terbuka dan Jejak Digital
category: research
language: Indonesian
description: "Melakukan riset sumber terbuka yang sah, mengumpulkan bukti publik, memetakan jejak digital, dan menilai paparan."
triggers: ["jejak digital", "OSINT", "cek informasi publik", "verifikasi informasi publik", "pemetaan aset digital"]
out_of_scope: "Akses tanpa izin, penguntitan, doxing, pengumpulan data pribadi tak relevan, atau klaim identitas tanpa bukti."
escalation: "Gunakan Penilaian Risiko untuk dampak hukum/keselamatan. Serahkan akses tanpa izin, penguntitan, dan klaim identitas kepada keahlian terkait."
---

# Intelijen Sumber Terbuka dan Jejak Digital

## Tujuan dan batas kepemilikan

Mengubah informasi publik menjadi gambaran yang dapat ditelusuri tentang entitas, infrastruktur, referensi daring, dan paparan yang teramati.

**Memiliki:** perencanaan riset sah, pengumpulan pasif, normalisasi, korelasi, validasi bukti, penilaian paparan, dan pelaporan. **Tidak memiliki:** akses sistem privat, penguntitan, doxing, penetapan identitas tanpa bukti, atau tindakan ofensif. Gunakan Pengambilan Pengetahuan Dinamis untuk sumber/alat terkini dan Penilaian Risiko untuk isu hukum, privasi, serta keselamatan.

## Konsep inti

- **Pengumpulan:** catatan publik, DNS, sertifikat, mesin pencari, situs, repositori kode, dan penyedia intelijen.
- **Normalisasi:** menyeragamkan domain, IP, host, surel, waktu, dan metadata sumber.
- **Korelasi:** menghubungkan observasi sambil menjaga tingkat keyakinan dan asal bukti.
- **Pengayaan:** menambah konteks hosting, teknologi, reputasi, dan riwayat.
- **Validasi:** membedakan observasi langsung, klaim penyedia, data usang, inferensi, dan positif palsu.

## Alur kerja

1. **Tujuan dan izin:** rumuskan pertanyaan, alasan sah, batas cakupan, dan tindakan terlarang.
2. **Pengenal:** catat domain, organisasi, alamat publik, atau pengenal relevan beserta alasan cakupannya.
3. **Sumber/metode:** pilih sumber publik yang sesuai; utamakan pengumpulan pasif.
4. **Kumpulkan:** catat sumber, waktu, kueri, hasil, dan ketentuan penggunaan. Jangan melewati autentikasi atau pembatasan akses.
5. **Normalisasi/korelasi:** hubungkan domain, IP, host, teknologi, dan referensi; simpan tautan bukti. Nama mirip bukan bukti entitas sama.
6. **Validasi:** cari konfirmasi independen; periksa kontradiksi, usia data, shared hosting, IP daur ulang, layanan privasi, dan positif palsu.
7. **Nilai paparan:** urutkan berdasarkan kemungkinan, dampak, dan keyakinan. Bedakan risiko terbukti dari hipotesis.
8. **Laporkan:** pisahkan observasi terkonfirmasi, klaim penyedia, hipotesis, dan hal tak diketahui. Sertakan bukti, waktu, metode, serta batasan.
9. **Mitigasi:** sarankan pengamanan aset pengguna dan pengurangan paparan yang tidak perlu.

## Rujukan: SpiderFoot

[SpiderFoot](https://github.com/smicallef/spiderfoot) adalah platform otomasi OSINT dengan antarmuka web, CLI, modul pengumpulan, korelasi, visualisasi, dan ekspor CSV/JSON/GEXF. Gunakan sebagai rujukan alur modular, bukan jaminan semua sumber tersedia. Periksa versi, konfigurasi modul, kebutuhan API, dan ketentuan sumber data. Tidak semua modul gratis atau berjalan tanpa kredensial.

## Bukti, privasi, dan keselamatan

Simpan sumber asli dan waktu pengumpulan. Satu hasil penyedia bukan bukti identitas/kepemilikan. Beri label keyakinan dan jelaskan dasar korelasi. Waspadai shared hosting, IP daur ulang, DNS usang, dan entitas bernama mirip.

Kumpulkan hanya data pribadi yang relevan dengan tujuan sah. Jangan publikasikan alamat, nomor kontak, kredensial, atau data sensitif. Untuk target individu, batasi riset pada informasi yang diperlukan dan tersedia secara sah; jangan menyusun profil untuk mengganggu atau mengintimidasi. Jangan lakukan akses tanpa izin.

## Format keluaran dan gerbang mutu

Laporan memuat tujuan/batas izin, pengenal, sumber/waktu, temuan terkonfirmasi, klaim/hipotesis, keyakinan/kontradiksi, paparan/dampak, mitigasi, dan batasan.

Pastikan tujuan sah, cakupan jelas, metode pasif diprioritaskan, sumber dapat ditelusuri, korelasi bukan identitas pasti, data usang/positif palsu dipertimbangkan, data pribadi diminimalkan, dan tidak ada akses tanpa izin.

## Sumber dan atribusi

Sintesis orisinal berdasarkan dokumentasi publik [SpiderFoot](https://github.com/smicallef/spiderfoot), berlisensi MIT. Tidak menyalin kode atau modul proyek tersebut.