# Product Requirement Document (PRD) & Game Design Document
**Project Title:** War of Realms: Math Combat Arena (SMA/SMK dan Mahasiswa Baru Edition)  
**Document Version:** 4.0 (Master Integrated Specification - High School and Freshman Edition, revisi atas v3.0)  
**Status:** Approved for Production  
**Terakhir Diperbarui:** 21 Oktober 2026  
**Target Platform:** Mobile Browser / PWA, paket Android dan iOS via Capacitor, dan Desktop Web (Landscape)  
**Target Pengguna:** Siswa SMA/SMK (Kelas 10-12) dan Mahasiswa Baru (TPB / Semester 1-2), rentang usia 15-19 tahun. Materi mencakup Aljabar Linear, Eksponen, Logaritma, Persamaan Kuadrat, Barisan dan Deret, Trigonometri, Matriks, Kombinatorika, Modulo dan Vektor, hingga Pengantar Kalkulus (Turunan dan Limit).  
**Tech Stack (Keputusan):** TypeScript / JavaScript (ES2020+ Modular) + Phaser 3 / HTML5 Canvas 2D Pixel-Perfect + Vite + Web Audio API.  
**Monetisasi:** 100% Gratis, Tanpa Iklan Invasif, Tanpa Pay-to-Win, Murni Skill Taktis dan Kecepatan Kalkulasi Matematika.

---

## 0. Tujuan, Pengguna, dan Cakupan

### 0.1. Visi Produk
Game strategi jalur horizontal (*lane defense / tug-of-war*) bertempo cepat dengan tema **Cyber-Arcade Pixel Art 16-bit**, di mana **kalkulasi matematika tingkat menengah dan tinggi adalah senjatanya**: menyelesaikan persamaan memberi gelombang *Overdrive Mana* instan dan pemulihan perisai benteng (*base repair*), bukan interupsi yang membosankan.

### 0.2. Tujuan Terukur (Target Metrik Kinerja dan UX)

| Area | Metrik | Target |
| --- | --- | --- |
| Belajar dan Kecepatan | Akurasi kuis rata-rata per sektor | >= 70% |
| Kecepatan Respons | Waktu rata-rata penyelesaian soal matematika | <= 8 detik |
| Keterlibatan | Kuis dijawab per pertempuran | >= 3 kali |
| Keterlibatan | Pemain menyelesaikan Sektor 1 pada percobaan pertama | >= 85% |
| Teknis | Frame rate pada perangkat standar (Android 3 GB RAM / Desktop) | 60 FPS stabil |
| Teknis | Waktu muat awal / crash-free session | <= 2 detik / >= 99% |

**Non-tujuan (v1.0):** multiplayer real-time online, global chat, microtransaction/IAP, cloud save wajib.

### 0.3. Persona Pengguna
* **Siswa SMA/SMK (Pemain Utama):**
  * Mempersiapkan diri menghadapi ujian sekolah, asesmen nasional, dan seleksi masuk perguruan tinggi (UTBK-SNBT).
  * Menyukai game bertempo cepat, respons kontrol instan (*hotkeys*), dan tantangan intelektual yang memacu adrenalin.
* **Mahasiswa Baru / Tingkat Pertama (Pemain Lanjutan):**
  * Membutuhkan pengasahan intuisi matematika dasar untuk mata kuliah Kalkulus 1, Aljabar Linear Elementer, dan Matematika Diskrit.
* **Guru / Dosen / Pengajar:**
  * Memerlukan instrumen gamifikasi edukasi yang berbobot secara akademis dan dapat dimainkan langsung di peramban tanpa instalasi rumit.

### 0.4. User Stories Inti
1. Sebagai siswa SMA/SMK, saya ingin memanggil unit pasukan dengan hotkey angka (1-5) agar komando strategi di garis depan terasa responsif dan cepat.
2. Sebagai pemain, saya ingin memicu terminal kuis matematika dengan hotkey kilat (Q untuk Mana, E untuk Repair) di momen genting untuk membalikkan keadaan.
3. Sebagai pemain, saya ingin menjawab soal menggunakan tombol keyboard (A/B/C/D atau 1/2/3/4) dalam hitungan detik agar tempo pertempuran tidak terhenti lama.
4. Sebagai pembelajar, saya ingin salah menjawab tidak langsung membuat saya kalah seketika, melainkan memberi feedback visual yang jelas agar saya bisa memperbaiki kalkulasi di wave berikutnya.
5. Sebagai mahasiswa baru, saya ingin materi soal mencakup konsep riil yang relevan (seperti matriks determinan, logaritma, trigonometri, dan turunan kalkulus).

### 0.5. Kebutuhan Fungsional dan Prioritas

| ID | Kebutuhan Fungsional | Prioritas |
| --- | --- | --- |
| FR-01 | Pertempuran jalur 1D: panggil unit, jalan otomatis, serang, benteng hancur memicu menang/kalah | P0 |
| FR-02 | Mana pasif (8/dtk), kapasitas 200 Mana, biaya unit (20-150), cooldown panggil, batas 12 unit/tim | P0 |
| FR-03 | Kuis Mana Overdrive (+45 s/d +90 Mana) dengan generator soal dinamis | P0 |
| FR-04 | Kuis Repair Base (+25% HP benteng, batas 3x per battle) | P0 |
| FR-05 | Slow-motion 0,1x saat terminal kuis aktif; timer kuis 14 detik di waktu nyata | P0 |
| FR-06 | Kontrol Hotkey Cepat: 1-5 (panggil unit), Q (Mana), E (Repair), A/B/C/D (pilihan jawaban), Spasi (Pause) | P0 |
| FR-07 | Generator soal 10 Sektor SMA/SMK, distraktor pintar (miskonsepsi), anti-ulang | P0 |
| FR-08 | Sistem wave musuh terstruktur per sektor (Level 1-10) | P0 |
| FR-09 | Peta Sektor 10 Level, penguncian berurutan (Level Lock), 1-3 Bintang dan Gelar Akademik | P0 |
| FR-10 | Simpan progres lokal (localStorage) dengan fallback aman, berjalan 100% offline | P0 |
| FR-11 | Top HUD: Status HP kedua benteng, radar minimap 6 px, toggle kecepatan (1x/2x), pause | P1 |
| FR-12 | Deteksi jarak serang tepi-ke-tepi (edge-to-edge gap) dan batas ground line y=144 px | P1 |
| FR-13 | State DYING (buffer 0.4s sebelum pembersihan entitas) untuk animasi partikel kehancuran | P1 |
| FR-14 | Kamera pintar adaptif (Clash-Focus Camera) yang memusatkan pandangan di antara benturan garis depan | P1 |
| FR-15 | Reset progress petualangan via menu utama | P2 |
| FR-16 | Mode Tantangan Waktu (Speedrun Math Defense) | P2 |

---

## 1. Analisis Referensi dan Diferensiasi Produk

### 1.1. Review Game Referensi (Kingdom Wars Genre)
Game referensi (*Kingdom Wars*, Springcomes) mengusung genre *horizontal lane defense / tug-of-war strategy*:
* **Kelebihan:** Kontrol intuitif, loop pertempuran cepat (2-3 menit), variasi unit beragam.
* **Kelemahan Klasik:** Kurva kesulitan sengaja dibuat melonjak (*paywall spike*) demi mendorong pembelian diamond/permata secara berulang (*Pay-to-Win*), serta frekuensi iklan video yang mengganggu.

### 1.2. Arah Diferensiasi dan Transformasi Produk (v4.0 SMA/SMK Edition)
1. **Transformasi Estetika:** Mengusung gaya **Cyber-Arcade Pixel Art Dark Mode** dengan palet Obsidian, Neon Cyan (`#00f2fe`), Electric Gold (`#ffd200`), dan Cyber Red (`#f43f5e`).
2. **Kalkulasi Matematika sebagai Amunisi Taktis:** Soal matematika bukan interupsi yang membosankan, melainkan sumber daya strategis (*instant mana overdrive* dan *base structural repair*).
3. **Ergonomi Input Desktop dan Mobile:** Didukung hotkey keyboard lengkap (`1-5` panggil unit, `Q` kuis mana, `E` kuis repair, `A/B/C/D` atau `1/2/3/4` eksekusi kilat jawaban kuis, `Spasi` jeda).
4. **Bebas Pay-to-Win:** Kemenangan ditentukan murni oleh strategi komposisi pasukan dan kecepatan kalkulasi matematis pemain.

---

## 2. Standar Teknis Visual dan Orientasi Landscape

### 2.1. Spesifikasi Layar dan Pixel-Perfect Rendering
* **Orientasi:** Fixed Landscape. Pada Android dikunci via manifest/Capacitor; pada iOS Safari ditampilkan overlay "Putar perangkatmu" saat portrait.
* **Tinggi Logis Tetap 216 px; Lebar Logis Dinamis 384-480 px.** (480x216 rasio 20:9 native; 384x216 rasio 16:9).
* **Upscaling:** Integer Scaling (x2 hingga x5) dengan CSS `image-rendering: pixelated;` dan konteks canvas `imageSmoothingEnabled = false` agar garis piksel tajam tanpa distorsi atau shimmering.
* **Frame Rate:** Target 60 FPS untuk rendering; logika game memakai *fixed timestep* 60 Hz accumulator agar deterministik; animasi spritesheet 8-12 FPS.

```javascript
// Algoritma Skala Integer dan Lebar Logis Dinamis
export function computeViewport(screenW, screenH) {
  const LOGICAL_H = 216, MIN_W = 384, MAX_W = 480;
  const scale = Math.max(1, Math.min(
    Math.floor(screenH / LOGICAL_H),
    Math.floor(screenW / MIN_W)
  ));
  const logicalW = Math.min(MAX_W, Math.max(MIN_W, Math.floor(screenW / scale)));
  return {
    scale, logicalW, logicalH: LOGICAL_H,
    offsetX: Math.floor((screenW - logicalW * scale) / 2),
    offsetY: Math.floor((screenH - LOGICAL_H * scale) / 2),
  };
}
```

### 2.2. Grid Layout Layar Landscape (480 x 216 px)

```text
+-------------------------------------------------------------------------------+
| [PAUSE] [HP BENTENG KITA]          [MINIMAP RADAR 6px]  [HP BENTENG LAWAN][2X]| <-- Top HUD (24 px)
+-------------------------------------------------------------------------------+
|                                                                               |
|                              (COMBAT ARENA 1D)                                |
|                                                                               |
|  [Benteng Kita]     <--- Pasukan Cyber vs Monster Void --->   [Benteng Musuh] | <-- Combat Lane (136 px)
|  (Pusat X: 56)                                       (Pusat X: TrackL - 56)   |     Kaki unit y=144 px
|                                                                               |
+-------------------------------------------------------------------------------+
| [MANA Q]  [MANA 85/200] [UNIT 1][UNIT 2][UNIT 3][UNIT 4][UNIT 5] [REPAIR E]   | <-- Bottom Deck (56 px)
| [ SOAL ]  [  tabung   ] [  20 ][  35 ][  50 ][  80 ][ 150 ]      [ BASE ]     |     y 160-216 px
+-------------------------------------------------------------------------------+
```

* **Top HUD (Tinggi 24 px, y: 0-24):** Status bar HP Benteng Kawan, HP Benteng Lawan, Minimap Radar 6 px, tombol Pause [Spasi], dan Toggle Kecepatan (1x / 2x).
* **Mid Combat Lane (Tinggi 136 px, y: 24-160):** Jalur pertempuran 1D. Garis pijakan kaki unit berada tepat pada **y = 144 px** (dengan pseudo-depth jitter +-4 px: 140-148 px). Tinggi benteng dibatasi **maksimal 112 px** sehingga tidak pernah menabrak Top HUD maupun Bottom Deck.
* **Bottom Deck Bar (Tinggi 56 px, y: 160-216):**
  * Sisi Kiri: Tombol **"MANA SOAL [Q]"** (+Bintang Mana instan).
  * Bagian Tengah: Tabung indikator Mana (Kapasitas 200) serta 5 slot tombol kartu pasukan (biaya 20, 35, 50, 80, 150).
  * Sisi Kanan: Tombol **"REPAIR BASE [E]"** (+Pemulihan perisai benteng 25%).
* **Layer Paralaks:** Layer 1 (langit cyber) 0,1x, Layer 2 (scenery jauh) 0,3x, Layer 3 (midground sirkuit) 0,6x, **Layer 4 (tanah lintasan) tepat 1,0x** terhadap koordinat dunia agar pasukan tidak meluncur.

---

## 3. Core Gameplay Loop, State Machine dan Sistem Tempur 1D

### 3.1. Finite State Machine (FSM) Entitas Unit
* `WALK`: Melangkah horizontal ke arah markas lawan dengan kecepatan konstan.
* `ATTACK`: Berhenti melangkah saat mendeteksi hitbox lawan dalam jangkauan (*attackRange*). Terdiri dari windup animasi lalu eksekusi damage pada hit frame.
* `KNOCKBACK`: Mundur beberapa piksel saat menerima pukulan telak (damage >= 15% dari max HP).
* `DYING`: Memutar animasi kehancuran partikel cyber/poof selama 0.4 detik sebelum entitas dibersihkan dari memori (mencegah bug unit lenyap seketika tanpa visual).
* `IDLE`: Khusus bangunan markas benteng.

### 3.2. Sistem Hitbox dan Jarak Serang Presisi (Edge-to-Edge Gap)
Perhitungan jarak target menggunakan selisih tepi-ke-tepi (*edge-to-edge gap*), bukan titik pusat:
`Gap = (X_target - X_unit) * Direction - HalfWidth_unit - HalfWidth_target`
Metode ini memastikan unit melee menyerang tepat di dinding benteng selebar 96 px tanpa menembus masuk atau terhenti terlalu jauh.

### 3.3. Roster Pasukan dan Atribut Tempur

| Unit Pasukan | Peran Taktis | HP | Damage | Speed | Range (Gap) | CD Serang | Biaya Mana | CD Panggil | Tipe Serangan |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Prajurit Kayu** | Melee Vanguard | 130 | 16 | 42 px/s | 24 px | 1.1 s | 20 | 2.5 s | Melee Slash |
| **Pemanah Gelembung** | Ranged DPS | 75 | 13 | 36 px/s | 115 px | 1.6 s | 35 | 4.0 s | Proyektil Cepat |
| **Penyihir Bintang** | AoE Magic | 65 | 26 | 32 px/s | 95 px | 2.0 s | 50 | 6.0 s | Proyektil Kembang Api |
| **Ksatria Poni** | Flanker Cepat | 210 | 32 | 78 px/s | 28 px | 1.3 s | 80 | 8.5 s | Melee Charge |
| **Robot Golem** | Heavy Tanker | 520 | 48 | 22 px/s | 32 px | 2.2 s | 150 | 14.0 s | Ground Slam AoE |

* **Kapasitas Mana Maksimum:** **200 Mana** (regenerasi pasif 8 Mana/detik).
* **Batas Unit Aktif:** Maksimal 12 unit per tim secara bersamaan di arena untuk menjaga stabilitas FPS dan taktikal balancing.

---

## 4. Kurikulum Matematika SMA dan Mahasiswa Baru (10 Sektor)

Tingkat kesulitan dirancang khusus untuk memicu kecepatan kalkulasi mental (*mental math agility*) dan pemahaman konseptual:

| Sektor | Nama Sektor | Materi Matematika | Parameter Soal | Contoh Bentuk Soal |
| :---: | :--- | :--- | :--- | :--- |
| **Sektor 1** | *Cyber Gate* | **Aljabar Linear (SPLSV)** | Persamaan linear ax + b = c, 2(x+a)=b | 2(x + 5) = 26, nilai x = ? |
| **Sektor 2** | *Quantum Core* | **Eksponen dan Bentuk Akar** | Sifat perpangkatan, penjumlahan akar | (2^5 x 2^4) / 2^6 = ? / sqrt(49) + sqrt(64) = ? |
| **Sektor 3** | *Nexus Nebula* | **Logaritma Dasar** | Sifat log_b(val), log(a) +- log(b) | log_3(27) - log_3(3) = ? / log_2(16) + log_2(8) = ? |
| **Sektor 4** | *Parabola Rift* | **Persamaan Kuadrat** | Faktorisasi, akar terbesar, jumlah akar | Jumlah akar dari x^2 - 12x + 32 = 0 |
| **Sektor 5** | *Binary Valley* | **Barisan dan Deret** | Suku ke-n (Un) Aritmatika dan Rasio Geometri | Suku ke-7 (U_7) dari barisan 2, 6, 10, 14, ... |
| **Sektor 6** | *Trigon Citadel* | **Trigonometri Khusus** | Sudut istimewa 0, 30, 45, 60, 90 derajat | 4 tan(45) - 2 sin(90) = ? |
| **Sektor 7** | *Matrix Horizon* | **Matriks dan Determinan** | Determinan matriks 2x2 (ad - bc), trace | det | 5  2 | | 3  4 | = ? |
| **Sektor 8** | *Chrono Portal* | **Kombinatorika** | Permutasi P(n,r), Kombinasi C(n,r), faktorial | P(5, 2) = ? / C(5, 2) = ? / 5! / 3! = ? |
| **Sektor 9** | *Modulo Bastion* | **Modulo dan Vektor** | Aritmatika modulo N mod m, dot product vektor | 31 mod 7 = ? / (5, 3) . (3, 3) = ? |
| **Sektor 10** | *Singularity Apex* | **Kalkulus Pengantar** | Turunan polinomial f'(x0), limit aljabar | Gradien singgung y = x^2 + 2x pada x=3 |

### 4.1. Parameter Desain Kuis Taktis
* **Batas Waktu:** 14 detik per soal (waktu nyata).
* **Super Slow-Motion:** Kecepatan pertempuran melambat ke `0.1x` saat terminal kuis aktif agar pemain bisa berpikir jernih tanpa kebobolan markas.
* **Opsi Jawaban dan Hotkeys:** 4 pilihan ganda dilengkapi badge tombol `[A]`, `[B]`, `[C]`, `[D]` (atau angka `[1]`, `[2]`, `[3]`, `[4]`).
* **Distraktor Pintar:** Opsi salah berbasis miskonsepsi umum (salah tanda, kelipatan, selisih +-1, +-2).
* **Reward:**
  * Kuis Mana: Memberikan instan **+45 hingga +90 Mana**.
  * Kuis Repair Base: Memulihkan **+25% HP Benteng** (maksimal 3 kali pemakaian per pertempuran).

---

## 5. Sistem Bintang, Rank Akademik dan Penyimpanan Progres

### 5.1. Kriteria Bintang (Rating 1-3 Bintang)
* **[3 Bintang]:** Sisa HP benteng >= 70%.
* **[2 Bintang]:** Sisa HP benteng 35% - 69%.
* **[1 Bintang]:** Sisa HP benteng < 35%.

### 5.2. Gelar dan Rank Akademik Pemain
Total bintang yang dikumpulkan (maksimal 30 bintang) membuka gelar akademik pada kartu profil:
1. **0 - 5 Bintang:** *Kadet Aljabar (SMA / Maba)*
2. **6 - 12 Bintang:** *Perwira Eksponen dan Kuadrat*
3. **13 - 19 Bintang:** *Strategis Trigonometri dan Deret*
4. **20 - 26 Bintang:** *Magister Vektor dan Determinan*
5. **27 - 30 Bintang:** *Grandmaster Singularity Kalkulus*

### 5.3. Sistem Level Lock dan Penyimpanan Data
* Sektor 2 sampai 10 terkunci secara berurutan dan baru terbuka setelah sektor sebelumnya berhasil ditaklukkan.
* Progres tersimpan secara permanen di `localStorage` peramban dengan fallback memori internal.

---

## 6. Standar Audio dan Efek Suara (16-bit Synthesizer)

Menggunakan modul mandiri berbasis **Web Audio API**:
* `sfx_wood_swing`: Ayunan pedang melee (whoosh segitiga frekuensi 320 Hz ke 110 Hz).
* `sfx_bubble_shoot`: Tembakan proyektil (sine wave modulasi nada tinggi).
* `sfx_star_pop`: Ledakan kembang api (akord D5, A5, D6 square-wave).
* `sfx_stomp_thud`: Hentakan robot golem (gelombang segitiga sub-bass 140 Hz ke 35 Hz).
* `sfx_quiz_correct`: Akord mayor naik C5 - E5 - G5 - C6 (arpeggio perayaan jawaban benar).
* `sfx_quiz_wrong`: Nada kartun lembut sawtooth meluncur turun (umpan balik salah yang bersahabat).
* `victory`: Fanfare kemenangan arkade retro 4-nada bertempo cepat.
* `bgm_battle`: Musik arkade chiptune 16-bit polifonik 136 BPM yang loopable.

---

## 7. Quality Assurance dan Manajemen Risiko

### 7.1. Strategi Pengujian
* **Uji Unit Generator:** Seluruh soal terverifikasi memiliki tepat 1 jawaban benar matematika yang valid, 3 opsi distraktor unik, dan tidak ada soal identik berturut-turut.
* **Uji Unit Combat:** Tidak ada tunneling proyektil, state `DYING` memberi jeda visual sebelum pembersihan memori, batas 12 unit per tim terjaga ketat.
* **Simulasi Durasi:** Sektor 1-3 durasi 90-150 detik; Sektor 4-7 durasi 150-210 detik; Sektor 8-10 durasi 180-270 detik.

---

## Lampiran A. Riwayat Perubahan v3.0 -> v4.0

| # | Aspek | Kondisi di v3.0 | Perbaikan di v4.0 |
| --- | --- | --- | --- |
| 1 | Target Audiens | Anak TK B - SD Kelas 4 (5-10 tahun) | Siswa SMA/SMK dan Mahasiswa Baru (15-19 tahun) |
| 2 | Materi Matematika | Tambah-kurang dasar (<= 5 s/d 20) | Aljabar, Eksponen, Logaritma, Kuadrat, Deret, Trigonometri, Matriks, Kombinatorika, Modulo/Vektor, Kalkulus |
| 3 | Kapasitas Mana | Maksimal 100 Mana (Robot Golem 150 Mana tak bisa dipanggil) | Maksimal 200 Mana |
| 4 | Hitbox dan Range | Perhitungan pusat-ke-pusat (benteng 96px bermasalah) | Perhitungan celah tepi-ke-tepi (getGap) |
| 5 | Garis Pijakan (Ground Y) | y=158/160 px (jitter menembus deck bawah) | y=144 px (rapi di dalam lane 24-160 px) |
| 6 | Tinggi Benteng | 96x160 px (menutupi HUD atas) | Maksimal 112 px (bebas tumpang tindih) |
| 7 | State Kematian | Unit langsung dihapus seketika (animasi poof hilang) | State DYING dengan buffer 0.4s |
| 8 | Kamera Garis Depan | Mengekor kaku unit terdepan | Kamera pintar fokus benturan (Clash-Focus Camera) |
| 9 | Kontrol Kuis | Klik mouse pilihan ganda biasa | Hotkey respons kilat keyboard (A/B/C/D atau 1/2/3/4) |
| 10 | Estetika UI | Kartun pastel anak-anak | Cyber-Arcade Dark Mode (Neon Cyan, Obsidian, Gold) |
