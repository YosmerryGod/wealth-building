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
Input nomor halaman untuk data besar saat pengguna mengetahui tujuan. Validasi bilangan bulat/rentang; navigasi melalui Enter atau tombol Go, bukan setiap ketikan. Pertahankan filter/sortir/pencarian dan beri feedback nilai invalid. Hindari untuk koleksi kecil atau urutan yang sering berubah.

### 2. Page Preview
Thumbnail, judul, atau cuplikan untuk galeri, editorial, peta, atau katalog visual. Preview harus konten nyata, ringan, berlabel, dapat dipilih lewat keyboard/touch, dan memiliki fallback. Hindari bila data repetitif atau preview tidak membantu.

### 3. Sliding Pagination
Jendela nomor terbatas yang bergeser untuk koleksi panjang. Bedakan halaman aktif, tentukan perilaku batas, gunakan elipsis untuk rentang yang dilewati, dan pertahankan fokus. Jangan bergantung pada swipe/drag saja.

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

Jangan mengambil semua halaman untuk menggambar kontrol/preview. Gunakan paginasi server sesuai kontrak; API cursor tidak boleh diberi nomor/total rekaan. Tentukan perilaku nol/satu halaman, total tak diketahui, data terhapus, filter berubah, tautan usang, dan nomor invalid. Cegah request duplikat/respons usang serta gunakan urutan stabil.

## Checklist

Pola sesuai jumlah halaman/konten/tugas; pola sederhana telah dipertimbangkan; halaman aktif dan total akurat; batas/invalid konsisten; filter/sortir tetap; keyboard/touch/screen reader/fokus/reduced motion berfungsi; preview relevan dan efisien; kontrak backend sesuai; mobile jelas; loading/kosong/error/data usang diuji.

## Aturan implementasi AI

Periksa aplikasi, sumber data, routing, dan kontrak paginasi sebelum mengubah kode. Jangan menambahkan tiga pola hanya karena ada di video. Pertahankan filter, sortir, route, dan UI lain. Jangan mengklaim preview atau total halaman tanpa dukungan data. Ubah ruang lingkup paginasi yang diminta saja dan uji state terkait.

## Hubungan dan batas

Pola Navigasi Web Modern memiliki navigasi antarbagian; Desain Frontend memiliki arah visual; Micro-Interactions memiliki feedback; AI Interface Design mengaudit kompleksitas dekoratif; Rekayasa Balik memiliki bukti referensi. Skill ini memiliki pemilihan pola dan perilaku navigasi halaman dalam koleksi, bukan query backend atau implementasi umum.
