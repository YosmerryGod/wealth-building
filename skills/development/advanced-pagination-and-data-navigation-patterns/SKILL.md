---
name: advanced-pagination-and-data-navigation-patterns
title: Pola Paginasi dan Navigasi Data Tingkat Lanjut
category: development
source_type: user-provided-video-and-operational-framework
source: Video pengguna 67567.mp4; watermark kreator @kodebin
language: Indonesian
description: "Memilih pola paginasi, lompatan halaman, pratinjau halaman, dan navigasi halaman bergeser dalam satu koleksi."
triggers: ["pagination","paginasi","navigasi halaman","jump input","page preview","sliding pagination"]
out_of_scope: "Navigasi global, identitas visual, arsitektur query data, atau implementasi frontend umum"
escalation: "Serahkan navigasi global kepada Pola Navigasi Web Modern, arah visual kepada Desain Frontend, feedback kepada Micro-Interactions, dan implementasi kepada pemilik frontend."
---

# Pola Paginasi dan Navigasi Data Tingkat Lanjut

## Tujuan dan batas

Memilih kontrol untuk berpindah antarhalaman dalam satu kumpulan hasil atau koleksi. Bukan untuk navigasi antarbagian produk. Paginasi yang tampak canggih tidak otomatis lebih baik; pilih pola paling sederhana sesuai jumlah halaman, jenis konten, tugas, perangkat, dan kebutuhan orientasi.

## Bukti sumber

Video pengguna 67567.mp4 (watermark @kodebin) menunjukkan:
1. **Jump Input:** input nomor halaman untuk melompat langsung.
2. **Page Preview:** pemilih halaman dengan pratinjau konten visual.
3. **Sliding Pagination:** deretan nomor halaman yang bergeser mengikuti posisi.

Video menyarankan pola lanjutan dipertimbangkan untuk ratusan halaman atau konten visual yang terbantu oleh preview. Untuk koleksi kecil, paginasi sederhana tetap lebih tepat. Video tidak menyediakan kode, riset usability, atau pengukuran performa; panduan seleksi dan teknis berikut merupakan sintesis operasional.

## Pola

### 1. Jump Input
Input nomor halaman, biasanya bersama tombol sebelumnya/berikutnya dan informasi halaman aktif/total.
- Cocok untuk data besar saat pengguna mengetahui nomor tujuan: tabel admin, pesanan, log, laporan.
- Validasi bilangan bulat dan rentang. Tentukan navigasi melalui Enter atau tombol Go; jangan berpindah setiap ketikan.
- Tolak atau batasi nilai di luar rentang secara konsisten dan jelaskan rentang valid.
- Pertahankan filter, sortir, dan pencarian. Nonaktifkan tombol batas jika relevan.
- Hindari untuk koleksi kecil, tujuan tak dikenal, atau urutan yang sering berubah.

### 2. Page Preview
Pemilih tujuan dengan thumbnail, gambar, judul, atau cuplikan konten.
- Cocok untuk galeri, editorial, peta, katalog, atau koleksi visual yang identitas halamannya penting.
- Tampilkan konten tujuan yang nyata, bukan placeholder menyesatkan.
- Muat preview secara efisien, beri label dan kontrol keyboard/touch, serta fallback bila data tidak tersedia.
- Hindari jika konten repetitif/tabel, thumbnail mahal, atau preview tidak membantu membedakan halaman.

### 3. Sliding Pagination
Menampilkan jendela nomor halaman terbatas yang bergeser ketika halaman berubah.
- Cocok untuk koleksi panjang, timeline, galeri, dan katalog.
- Bedakan halaman aktif; tentukan perilaku dekat awal/akhir.
- Gunakan elipsis hanya untuk rentang yang dilewati; jadikan interaktif hanya bila fungsinya jelas.
- Pertahankan fokus saat jendela bergeser. Jangan mengandalkan swipe/drag saja.
- Hindari jika jumlah halaman sedikit atau pergeseran membuat pengguna kehilangan orientasi.

## Alur pemilihan

1. Pahami jumlah halaman, kestabilan urutan, ukuran halaman, pencarian, dan filter.
2. Bedakan data tabel/rekaman dari konten visual/editorial.
3. Tentukan apakah pengguna menjelajah halaman sekitar, mengetahui nomor tujuan, mengenali konten, atau hanya butuh sebelumnya/berikutnya.
4. Pilih pola sederhana:
   - Sedikit halaman: nomor sederhana atau sebelumnya/berikutnya.
   - Banyak halaman dan tujuan diketahui: Jump Input.
   - Konten visual: Page Preview.
   - Banyak halaman dan konteks sekitar penting: Sliding Pagination.
   - Koleksi sangat besar/dinamis: pertimbangkan pencarian, filter, cursor, atau virtualisasi.
5. Sesuaikan touch, mouse, keyboard, viewport sempit, dan teknologi bantu.
6. Validasi batas, jumlah total, persistensi filter/sortir, loading, kosong, dan error.
7. Uji dengan data realistis.

## Aksesibilitas dan fungsi

Gunakan tautan semantik jika tujuan memiliki URL stabil dan history browser penting; gunakan tombol untuk aksi state tanpa URL. Paparkan halaman aktif secara visual dan programatis (misalnya aria-current). Beri label aksesibel pada input; placeholder bukan satu-satunya label. Dukung keyboard, fokus terlihat, target sentuh, kontras, dan reduced motion. Umumkan pembaruan hasil secara wajar. Pertahankan filter, sortir, dan pencarian kecuali pengguna meresetnya.

## Data dan performa

Jangan mengambil semua halaman hanya untuk menggambar kontrol atau preview. Gunakan paginasi server untuk dataset besar bila sesuai kontrak backend. Pada API berbasis cursor, jangan mengarang nomor atau total halaman yang tidak disediakan. Definisikan perilaku untuk nol hasil, satu halaman, total tak diketahui, data terhapus, filter berubah, tautan kedaluwarsa, dan nomor di luar rentang. Cegah request duplikat dan respons usang saat navigasi cepat. Gunakan urutan stabil dengan tie-breaker deterministik.

## Checklist

- Pola sesuai jumlah halaman, konten, dan maksud pengguna.
- Pola lebih sederhana telah dipertimbangkan.
- Halaman aktif dan total/tidak diketahui dinyatakan akurat.
- Batas dan nilai invalid konsisten.
- Filter/sortir/pencarian tetap terjaga.
- Keyboard, touch, screen reader, fokus, dan reduced motion dapat digunakan.
- Preview relevan dan dimuat efisien.
- Kontrak backend sesuai dengan UI.
- Mobile tetap jelas.
- Loading, kosong, error, dan data usang diuji.

## Aturan implementasi AI

Periksa aplikasi, sumber data, routing, dan kontrak paginasi sebelum mengubah kode. Jangan menambahkan tiga pola hanya karena ada di video. Pertahankan filter, sortir, route, dan UI lain. Jangan mengklaim preview atau total halaman tanpa dukungan data. Ubah ruang lingkup paginasi yang diminta saja dan uji state terkait.

## Hubungan dan batas

Pola Navigasi Web Modern memiliki navigasi antarbagian; Desain Frontend memiliki arah visual; Micro-Interactions memiliki feedback; AI Interface Design mengaudit kompleksitas dekoratif; Rekayasa Balik memiliki bukti referensi. Skill ini memiliki pemilihan pola dan perilaku navigasi halaman dalam koleksi, bukan query backend atau implementasi umum.
