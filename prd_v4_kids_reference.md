# Product Requirement Document (PRD) & Game Design Document
**Project Title:** War of Realms: Pixel Lane Defense (Kids Math Edition)  
**Document Version:** 4.0 (revisi atas v3.0, lihat Lampiran A)  
**Status:** Draft untuk review  
**Terakhir diperbarui:** 21 Oktober 2026  
**Target Platform:** Mobile Browser / PWA, paket Android & iOS via Capacitor, dan Desktop Web (Landscape)  
**Target Pengguna:** Anak usia 5–10 tahun. Konten MVP setara TK B hingga SD Kelas 2 (Fase A Kurikulum Merdeka; *verifikasi capaian pembelajaran ke dokumen resmi Kemendikdasmen*). Kelas 3–4 dilayani lewat Mode Tantangan (v1.1).  
**Tech Stack (keputusan):** TypeScript + Phaser 3 + Vite, dengan PWA offline-first. Canvas 2D native tidak dipilih karena scene, scaling, audio, input, dan tween di Phaser menghemat waktu tim kecil. Contoh kode di dokumen ini ditulis JavaScript ES2020 + JSDoc supaya mudah dimigrasi ke TS.  
**Monetisasi:** Gratis, tanpa iklan, tanpa pembelian dalam aplikasi, tanpa tautan keluar tanpa Parent Gate. Model keberlanjutan (donasi/lisensi sekolah) di luar cakupan MVP.

---

## 0. Tujuan, Pengguna, dan Cakupan

### 0.1. Visi
Game strategi jalur yang seru di mana **matematika adalah senjatanya**: menjawab soal memberi Mana dan menyembuhkan benteng, bukan menjadi interupsi yang menghentikan permainan.

### 0.2. Tujuan Terukur (target awal, divalidasi saat playtest)

| Area | Metrik | Target |
| --- | --- | --- |
| Belajar | Akurasi kuis rata-rata per level | >= 70% |
| Keterlibatan | Anak penguji menyelesaikan Level 1 tanpa bantuan dewasa | >= 80% |
| Keterlibatan | Kuis dijawab per pertempuran | >= 3 |
| Kenyamanan | Anak menjawab "mau main lagi" (skala wajah senyum) | >= 85% |
| Teknis | Frame rate pada Android 3 GB RAM | 60 FPS stabil |
| Teknis | Waktu muat awal / crash-free session | <= 3 dtk / >= 99% |

**Non-tujuan (v1.0):** multiplayer, chat, akun online, iklan, IAP, konten di atas Kelas 2.

### 0.3. Pengguna
* **Anak (pemain utama):** belum tentu lancar membaca, sehingga **setiap soal wajib punya narasi suara**.
* **Orang tua / guru (pengawas):** butuh kontrol (Mode Santai, batas waktu main) dan laporan belajar sederhana.

### 0.4. User Stories Inti
1. Sebagai anak, saya ingin memanggil pasukan dengan satu ketukan agar pertempuran terasa langsung.
2. Sebagai anak, saya ingin soal dibacakan suara agar saya tetap bisa main walau belum lancar membaca.
3. Sebagai anak, saya ingin salah menjawab tidak membuat saya kalah atau dimarahi, supaya saya berani mencoba lagi.
4. Sebagai orang tua, saya ingin pengaturan dan tautan keluar dilindungi Parent Gate agar anak tidak salah ketuk.
5. Sebagai orang tua, saya ingin melihat topik hitung mana yang masih sulit bagi anak.
6. Sebagai guru, saya ingin materi tiap level selaras dengan urutan belajar di kelas.

### 0.5. Kebutuhan Fungsional & Prioritas

| ID | Kebutuhan | Prioritas |
| --- | --- | --- |
| FR-01 | Pertempuran jalur 1D: panggil unit, jalan otomatis, serang, kastel hancur memicu menang/kalah | P0 |
| FR-02 | Mana pasif, biaya unit, cooldown panggil, batas 12 unit per tim | P0 |
| FR-03 | Kuis Mana dengan reward bertingkat | P0 |
| FR-04 | Kuis Obati Base (+20% HP, maks 3x per pertempuran) | P0 |
| FR-05 | Slow-motion 0,1x saat kuis; timer kuis berjalan di waktu nyata | P0 |
| FR-06 | Narasi suara tiap soal + tombol "ulangi suara" | P0 |
| FR-07 | Generator soal Level 1–10, distraktor berbasis miskonsepsi, anti-ulang | P0 |
| FR-08 | Wave musuh berbasis data JSON per level | P0 |
| FR-09 | Peta pulau 10 level, kunci berurutan, 1–3 bintang (MVP: Level 1–5) | P0 |
| FR-10 | Simpan progres lokal, berjalan offline | P0 |
| FR-11 | Pause, toggle 1x/2x, minimap | P1 |
| FR-12 | Koin dan upgrade pasukan/markas | P1 |
| FR-13 | Bantuan Peri (anti-frustrasi) | P1 |
| FR-14 | Parent Gate + pengaturan (Mode Santai, suara, pengingat istirahat) | P1 |
| FR-15 | Laporan belajar untuk orang tua | P2 |
| FR-16 | Soal adaptif (naik/turun sub-tingkat) | P2 |
| FR-17 | Pilih 5 dari 8 unit untuk deck | P2 |

### 0.6. Cakupan Rilis
* **MVP:** Level 1–5, 5 unit, kuis Mana + Obati, simpan lokal, narasi angka, Parent Gate dasar.
* **v1.0:** Level 6–10, koin & upgrade, Bantuan Peri.
* **v1.1:** 3 unit tambahan + pemilihan deck, Mode Tantangan Kelas 3–4, laporan orang tua.
