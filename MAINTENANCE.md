# Catatan Pemeliharaan Repositori

## Mutu pengetahuan dan pengelolaan sumber

Untuk setiap video, artikel, buku, atau sumber baru:
- Catat jenis sumber, judul atau akun/penulis, serta tautan atau rincian pengenal jika tersedia.
- Ambil klaim dan contoh yang benar-benar disampaikan sumber tanpa menyajikannya sebagai fakta yang telah diverifikasi secara independen.
- Pisahkan gagasan yang berasal dari sumber dengan analisis atau kerangka tambahan yang dibuat AI.
- Beri label yang jelas pada angka ilustratif dan asumsi.
- Jelaskan mekanismenya: mengapa gagasan tersebut mungkin berhasil dan dalam kondisi apa.
- Sertakan keterbatasan, risiko, kondisi kegagalan, dan situasi ketika metode tersebut tidak boleh digunakan.
- Tambahkan langkah praktis, kriteria keputusan, dan metode validasi terukur jika relevan.
- Hindari menyalin bagian besar dari materi berhak cipta; rangkum dengan susunan kata sendiri.
- Jangan mengubah alegori, anekdot, atau video singkat menjadi kesimpulan ilmiah tanpa bukti pendukung.

### Audit sumber: pengambilan pengetahuan dinamis

- **GoogleChrome, Modern Web Guidance** ([skill yang diterbitkan](https://github.com/GoogleChrome/modern-web-guidance), [repositori sumber](https://github.com/GoogleChrome/modern-web-guidance-src), ditinjau 2026-11-19). Skill sumber mendokumentasikan pencarian katalog terarah, pengambilan ID panduan yang tepat, pengungkapan informasi bertahap, pemeriksaan implementasi, dan alternatif dukungan peramban. [Pembahasan teknis mendalam](https://developer.chrome.com/blog/mwg-technical-deep-dive) oleh Paul Irish menjelaskan pendekatan pencarian lokal dan alasannya. Wealth Building mengadopsi alur pengambilan tersebut dan membuat adaptor bukti/kepemilikan lintas domain yang orisinal; repositori ini tidak menyalin atau menyertakan kumpulan panduan maupun CLI sumber. CLI sumber tidak dipasang oleh repositori ini dan memerlukan runtime yang kompatibel, akses jaringan, serta izin.

### Audit sumber: pembentukan kebiasaan dan keunggulan bersaing

- **Wendy Wood, *Good Habits, Bad Habits: The Science of Making Positive Changes That Stick* (2019).** Ringkasan penerbit dan kutipan yang tersedia untuk umum telah ditinjau. Tema yang didukung sumber: pembentukan kebiasaan tidak dapat direduksi menjadi kemauan semata; konteks, pengulangan, dan imbalan berperan; hambatan lingkungan dan pemicu memengaruhi perilaku berulang. Skill baru merupakan sintesis pembinaan orisinal, bukan ekstraksi seluruh buku atau protokol klinis. [Ringkasan penerbit](https://us.macmillan.com/books/9781250159083/goodhabitsbadhabits/).
- **Peter Thiel bersama Blake Masters, *Zero to One: Notes on Startups, or How to Build the Future* (2014).** Deskripsi penerbit dan teks sumber telah ditinjau. Tema yang didukung sumber: menciptakan sesuatu yang benar-benar baru, memilih pasar awal yang terfokus, membangun posisi pasar yang khas, serta teknologi eksklusif, efek jaringan, skala ekonomi, dan merek sebagai sumber daya tahan yang potensial. Skill baru merupakan sintesis strategi orisinal; pernyataan 10x diperlakukan sebagai heuristik, sedangkan bahasa monopoli dibatasi oleh persaingan yang sah dan bermanfaat bagi pelanggan. [Halaman penerbit](https://www.penguinrandomhouse.com/books/234730/zero-to-one-by-peter-thiel-with-blake-masters/).

Sumber-sumber tersebut tidak diperlakukan sebagai bukti bahwa satu metode kebiasaan cocok untuk semua orang atau bahwa setiap bisnis dapat maupun seharusnya mencapai monopoli. Tidak ada kutipan panjang berhak cipta yang disalin.

### Audit sumber: pola paginasi

- **Video yang diberikan pengguna 67567.mp4** (tanda air kreator terlihat sebagai @kodebin; tidak ada URL sumber publik). Peninjauan bingkai secara langsung menemukan tiga pola yang ditampilkan: Masukan Lompat Halaman, Pratinjau Halaman, dan Paginasi Geser. Video menyarankan pertimbangan paginasi tingkat lanjut untuk jumlah halaman yang sangat besar atau konten visual yang mendapat manfaat dari pratinjau, sambil mempertahankan paginasi sederhana ketika jumlah halaman sedikit dan fungsi lebih penting. Panduan aksesibilitas, backend, kinerja, kasus tepi, dan pengujian dalam skill merupakan sintesis operasional tambahan; video tidak menyediakan kode implementasi atau pengukuran kegunaan.

### Audit sumber: pola navigasi ekspresif

- **Video yang diberikan pengguna 67562.mp4** (tanda air kreator terlihat sebagai @kodebin; tidak ada URL sumber publik). Peninjauan bingkai secara langsung menemukan Bilah Samping Radial, Navigasi Tipografi Vertikal, dan Navigasi Progres Gulir. Video secara eksplisit menyebut Bilah Samping Radial cocok untuk portofolio kreatif dan halaman utama eksperimental; video juga menampilkan label bagian dengan tipografi vertikal serta jalur progres gulir dengan penanda aktif yang mengikuti posisi gulir dan dapat diklik untuk berpindah ke bagian tertentu. Video tidak menyediakan riset kegunaan, kode implementasi, atau hasil terukur. Panduan responsif, aksesibilitas, pemilihan pola, dan implementasi dalam skill yang diperluas merupakan sintesis operasional.

### Audit sumber: siklus pengembangan aplikasi Replica Skill

- **Jakeschincariol/replica-skill** (repositori berlisensi MIT; README dan seluruh sebelas berkas `replica-*/SKILL.md` ditinjau pada 2026-11-18): alur sumber mencakup pengintaian referensi, perencanaan arsitektur, rekonstruksi sistem desain, implementasi layar demi layar, integrasi backend, QA, perbandingan fitur/tata letak, analisis ulasan publik, perubahan merek, persiapan peluncuran, dan deployment.
- Penambahan pada Wealth Building merupakan adaptasi orisinal dari konsep alur kerja dan batas tanggung jawab, bukan salinan teks skill, skrip, templat, atau implementasi eksklusif. Pemilik yang sudah ada digunakan kembali untuk rekonstruksi, desain, merek, dan penemuan pelanggan; skill baru hanya ditambahkan untuk tanggung jawab berbeda dalam arsitektur, implementasi, backend, QA, kesesuaian, rilis, orkestrasi, dan perencanaan peluncuran.
- Batas kerja bersih, privasi, akses berizin, larangan mengarang, persetujuan pengguna, dan tinjauan hukum tetap dipertahankan serta diselaraskan dengan tata kelola Wealth Building dan Penilaian Risiko. Perangkat dari repositori sumber tidak dipasang dan tidak boleh dianggap tersedia di sini.

### Audit sumber: Kecerdasan Suara Pelanggan Berbasis AI

- **Video yang diberikan pengguna 68199.mp4** (ditinjau 2026-11-22). Skenario ilustratif menampilkan kumpulan data berlabel 200 ulasan pelanggan, perintah untuk menemukan keluhan yang muncul lebih dari tiga kali, serta jumlah yang ditampilkan untuk waktu tunggu lama (87), tempat duduk terbatas (21), dan parkir sulit (9). Video juga membandingkan contoh persiapan minuman selama 15 menit dengan hasil berikutnya selama 3 menit serta menggambarkan pelanggan yang kembali setelah tiga bulan. Video tidak menampilkan ulasan mentah, periode pengambilan sampel, metode penghitungan, intervensi operasional yang tepat, atau data retensi yang diverifikasi secara independen. Skill mempertahankan alur kerja—menggabungkan umpan balik, mengurutkan masalah berulang, memvalidasi penyebab operasional, menguji perbaikan terarah, dan mengukur hasil—seraya memperlakukan seluruh angka dan hasil yang ditampilkan sebagai ilustrasi, bukan bukti terverifikasi. Tanggung jawabnya dipisahkan dari Pemulihan Layanan yang menangani solusi keluhan individual dan balasan publik.

## Protokol pembaruan repositori

**Setiap kali skill ditambahkan, diubah, dipindahkan, atau dihapus, perbarui README ini dalam sesi kerja yang sama.** README merupakan dokumen orientasi bagi orang dan asisten AI yang membuka repositori dalam percakapan baru.

Untuk setiap pembaruan skill:

1. Tambahkan, revisi, pindahkan, atau hapus berkas skill terkait.
2. Perbarui tabel pustaka skill dan pohon folder.
3. Perbarui aturan alur kerja AI jika skill baru mengubah cara mentor melakukan penalaran.
4. Perbarui peta jalan jika kemampuan baru telah ditambahkan atau celah tertentu menjadi lebih penting.
5. Tambahkan catatan changelog bertanggal dengan uraian ringkas.
6. Pastikan semua tautan README dan lokasi skill tersedia serta tidak ada lokasi lama yang tertinggal.

## Kemampuan yang akan dibangun berikutnya

Bagian ini memuat bidang pengetahuan yang direncanakan, bukan klaim bahwa skill lengkap sudah tersedia. Tambahkan secara bertahap ketika sumber yang berguna dan contoh praktis telah ditinjau.

1. **Riset Pelanggan dan Validasi Permintaan** — wawancara pelanggan, kesediaan membayar, ukuran pasar, riset kompetitor, dan bukti permintaan.
2. **Model Bisnis dan Ekonomi Unit** — harga, margin kontribusi, analisis titik impas, biaya akuisisi pelanggan, nilai pelanggan sepanjang hubungan, dan konversi kas. Diferensiasi strategis dan daya tahan keunggulan kini ditangani oleh Strategi Inovasi dan Keunggulan Bersaing.
3. **Pemasaran, Penjualan, dan Distribusi** — cakupan dasar kini meliputi Perencanaan Peluncuran Produk dan Strategi Masuk Pasar bersama Strategi Mendapatkan Daya Tarik Pasar, Kerangka Bullseye, pemilihan kanal, eksperimen pertumbuhan, pertumbuhan rujukan, kemitraan, dan metrik pertumbuhan. Pengembangan berikutnya dapat memperdalam posisi merek, perancangan penawaran, proses penjualan, pemasaran siklus pelanggan, dan retensi.
4. **Pengembangan Produk dan Penawaran** — kesesuaian produk-pasar, diferensiasi, mutu, kemasan, dan pengalaman pelanggan.
5. **Operasional dan Sistem Bisnis** — prosedur operasi standar, tenaga kerja, persediaan, kendali mutu, kapasitas, dan perbaikan proses. Cakupan inti telah ditambahkan melalui Operasional dan Pengembangan Skala Bisnis.
6. **Manajemen Keuangan** — cakupan dasar kini meliputi Kecerdasan Finansial, Analisis Aset dan Liabilitas, Pengelolaan Arus Kas, Dahulukan Membayar Diri Sendiri, dan Literasi Laporan Keuangan. Pengembangan berikutnya dapat memperdalam perencanaan pajak, pengelolaan utang, dan kendali keuangan.
7. **Pertumbuhan dan Alokasi Modal** — prioritas investasi kembali, imbal hasil atas modal yang diinvestasikan, aset produktif, keputusan ekspansi, dan penggunaan daya ungkit secara bertanggung jawab.
8. **Risiko, Ketahanan, dan Kepatuhan** — perencanaan skenario buruk, asuransi, pencegahan penipuan, persyaratan hukum, pajak, dan kesinambungan bisnis.
9. **Keuangan Pribadi dan Pelestarian Kekayaan** — cakupan dasar kini meliputi perencanaan pendapatan menjadi aset, alokasi tabungan, analisis aset/liabilitas, dan evaluasi investasi. Pengembangan berikutnya dapat memperdalam rancangan dana darurat, diversifikasi, perencanaan pensiun, dan pelestarian kekayaan.
10. **Komunikasi dan Efektivitas Interpersonal** — cakupan dasar ditambahkan melalui enam skill Komunikasi berdasarkan *Bicara Itu Ada Seninya*: komunikasi efektif, mendengarkan aktif, persuasi dan negosiasi, perancangan pesan, penyampaian vokal, dan berbicara di depan umum.
11. **Pelaksanaan dan Pendampingan Kemajuan** — penetapan tujuan, penentuan prioritas, akuntabilitas, tinjauan kemajuan, dan penyesuaian rencana berdasarkan hasil. Perancangan kebiasaan umum nonfinansial kini ditangani oleh Pembentukan Kebiasaan Umum dan Perubahan Perilaku; rutinitas keuangan tetap ditangani oleh Pembentukan Kebiasaan Finansial.
12. **Desain dan Pengembangan Produk Digital** — diperluas melalui Orkestrator Pengembangan dan Pengiriman Aplikasi, Perencanaan Arsitektur Aplikasi, Rekayasa Aplikasi Full-Stack, Rekayasa Backend dan Integrasi, Pengujian Perangkat Lunak dan QA, Evaluasi Kesesuaian Aplikasi, serta Rekayasa Deployment dan Rilis Aplikasi.
13. **Produksi Kreatif dan Identitas Merek** — alur kerja pembuatan gambar, desain visual, sistem logo, identitas merek, dan arahan kreatif yang konsisten.

## Pendekatan repositori

Pangkalan pengetahuan ini berkembang secara bertahap seiring peninjauan sumber yang berguna. Setiap skill harus menyumbangkan prinsip atau metode yang dapat digunakan kembali untuk membantu mentor AI di masa depan memberikan panduan yang berlandaskan bukti, memahami konteks, dan dapat ditindaklanjuti.

Tujuannya bukan mengumpulkan skill sebanyak mungkin. Tujuannya adalah membangun pengetahuan tepercaya yang meningkatkan kualitas keputusan AI dan kemampuan pengguna untuk bertindak.

## Catatan Penamaan Perusahaan AI di Masa Depan

Nama-nama berikut disimpan sebagai identitas yang diusulkan untuk agen departemen AI di masa depan. Ini hanya catatan perencanaan; bukan berarti agen atau struktur organisasi tersebut sudah diterapkan.

| Nama AI | Departemen yang Direncanakan |
|---|---|
| Mekki | Pemasaran |
| Tachy | Teknologi |
| Fini | Keuangan |
| Operi | Operasional |
| Hura | Sumber Daya Manusia |
| Straty | Strategi dan Pertumbuhan |
| Puddi | Produk |

Nama CEO dan struktur organisasi final masih harus ditentukan. Nama-nama ini perlu dipertahankan untuk arsitektur Perusahaan AI di masa depan dan ditinjau kembali ketika lapisan organisasi mulai dirancang.
