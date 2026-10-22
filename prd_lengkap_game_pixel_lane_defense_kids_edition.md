# Product Requirement Document (PRD) & Game Design Document
**Project Title:** War of Realms: Pixel Lane Defense (Kids Math Edition)  
**Document Version:** 3.0 (Master Integrated Specification)  
**Target Platform:** Mobile Browser / Hybrid App (Capacitor/Cordova/PWA) & Desktop Web (Landscape)  
**Target Audience:** Anak-anak usia 6–10 tahun (Jenjang TK B hingga SD Kelas 1–4)  
**Primary Engine / Tech Stack:** JavaScript (ES6+) / TypeScript dengan Phaser 3 atau Native HTML5 Canvas 2D  
**Monetisasi:** 100% Bebas Pay-to-Win, Bebas Iklan Invasif (Murni Skill & Edukasi Ceria)  

---

## 1. Analisis Referensi & Evaluasi Kloning (Kingdom Wars Analysis)

### 1.1. Review Game Referensi
Game referensi (*Kingdom Wars* oleh Springcomes) mengusung genre *horizontal lane defense / tug-of-war strategy*:
* **Kelebihan:** Kontrol intuitif, loop pertempuran cepat (2–3 menit), ukuran file ringan, variasi unit beragam.
* **Kelemahan Klasik:** Kurva kesulitan sengaja dibuat melonjak (*paywall spike*) demi mendorong pembelian diamond/permata secara berulang (*Pay-to-Win*), serta frekuensi iklan video yang mengganggu.

### 1.2. Arah Diferensiasi & Transformasi Produk
Game ini mempertahankan serunya adu strategi jalur horizontal, namun dengan perombakan menyeluruh:
1. **Transformasi Gaya Visual:** Dari kartun vektor generik menjadi **Retro Pixel Art 16-bit Ceria** (*chunky, colorful, cute fantasy*).
2. **Pemberantasan Pay-to-Win:** Segala bentuk booster instan berbasis uang ditiadakan.
3. **Mekanisme Edutainment Interaktif:** Penambahan Mana instan dan pemulihan HP benteng diperoleh murni melalui penyelesaian soal hitung matematika dasar yang menyenangkan di tengah pertempuran.

---

## 2. Standar Teknis Visual & Orientasi Landscape

### 2.1. Spesifikasi Layar & Pixel-Perfect Rendering
* **Orientasi:** Fixed Landscape (mudah dan stabil digenggam dengan dua tangan di tablet atau smartphone).
* **Native Internal Canvas:** **480 × 216 px** (Rasio 20:9 native; kompatibel dinamis ke 384 × 216 px untuk rasio 16:9).
* **Upscaling:** Integer Scaling (×5) menuju resolusi 2400 × 1080 (FHD+) dengan CSS `image-rendering: pixelated;` dan WebGL context `antialias: false` agar garis piksel tetap tajam tanpa distorsi atau *shimmering*.
* **Frame Rate:** Target 60 FPS untuk rendering, dengan kecepatan animasi internal spritesheet karakter pada **8–12 FPS** bergaya arkade retro.

### 2.2. Pembagian Grid Layout Layar Landscape (480 × 216 px)

```text
┌───────────────────────────────────────────────────────────────────────────────┐
│ [PAUSE]  [HP KASTEL KITA]           [MINIMAP RADAR]   [HP KASTEL MUSUH] [2X]  │ ◄── Top HUD (24 px)
├───────────────────────────────────────────────────────────────────────────────┤
│                                                                               │
│                                (ARENA PERTEMPURAN)                            │
│                                                                               │
│  [Kastel Kita]     ◄─── Unit Prajurit / Monster Lucu ───►       [Kastel Musuh]│ ◄── Combat Lane
│  (Titik X: 24)                                                 (Titik X: Lvl) │     (136 px)
│                                                                               │
├───────────────────────────────────────────────────────────────────────────────┤
│ [MANA TANYA] [MANA BAR] [UNIT 1][UNIT 2][UNIT 3][UNIT 4][UNIT 5] [OBATI BASE] │ ◄── Bottom Deck
│ [ + BINTANG] [ 85/100 ] [  20  ][  35  ][  50  ][  80  ][ 150  ] [ + HP BINT]│     (56 px)
└───────────────────────────────────────────────────────────────────────────────┘
```

* **Top HUD (Tinggi 24 px):** Status bar HP Kastel Pemain (kiri), HP Kastel Lawan (kanan), strip radar minimap 2 px (tengah), tombol Jeda (*Pause*), dan Toggle Kecepatan (1x / 2x).
* **Mid Combat Lane (Tinggi 136 px):** Jalur pertempuran 1D, area benturan proyektil gelembung/bintang, dan latar paralaks 4-layer.
* **Bottom Deck Bar (Tinggi 56 px):**
  * Sisi Kiri: Tombol **"Mana Tanya"** (+Bintang Mana via kuis berbatas waktu).
  * Bagian Tengah: Tabung indikator Mana serta 5 slot tombol kartu pasukan (Deck Spawner).
  * Sisi Kanan: Tombol **"Obati Base"** (+Perbaikan HP kastel darurat).

---

## 3. Core Gameplay Loop & State Management

```text
[Menu Utama / Peta Pulau (Level 1-10)]
               │
               ▼
   [Pilih 5 Pasukan Favorit ke Deck]
               │
               ▼
┌──────────────┴───────────────────────────────────────────────────────┐
│                      IN-GAME BATTLE LOOP                             │
│                                                                      │
│  Mana Pasif / Detik ──► Panggil Pasukan ──► Berjalan Otomatis (1D)   │
│         ▲                                             │              │
│         │ (Jawaban Benar)                             ▼              │
│  [KUIS BINTANG / PERBAIKI] ◄── [Situasi Darurat] ◄── Benturan Pasukan│
└──────────────┬───────────────────────────────────────────────────────┘
               │
       ┌───────┴────────┐
       ▼                ▼
  [Kastel Kalah]   [Kastel Musuh Roboh]
       │                │
       ▼                ▼
 [Coba Lagi Tanpa   [Menang! Raih 3 Bintang & Koin]
   Rasa Frustrasi]      │
                        ▼
            [Naikkan Level Pasukan & Markas]
                        │
                        ▼
             [Buka Level Cerita Baru]
```

### 3.1. Finite State Machine (FSM) Entitas Unit
Setiap unit (kawan maupun monster) berjalan berdasarkan state machine berikut:
* `WALK`: Melangkah lurus horizontal ke arah benteng lawan dengan kecepatan gerak tetap.
* `ATTACK`: Berhenti melangkah saat mendeteksi hitbox lawan dalam jarak jangkauan (*range*). Memutar animasi serang kartun dan memicu damage frame.
* `KNOCKBACK`: Mundur beberapa piksel ke belakang saat menerima pukulan telak.
* `DIE`: Memutar animasi kepulan awan asap (*poof*) bersama taburan bintang tanpa visual darah atau kekerasan gore.

---

## 4. Mekanisme Kuis Matematika Ramah Anak (Kids Math System)

Sistem kuis dirancang agar anak merasa terhibur (*gamified learning*), percaya diri, dan tidak merasa tertekan:

### 4.1. Parameter Desain Kuis
* **Batas Waktu Ramah Anak:** 10 detik per pertanyaan (cukup santai untuk anak usia dini).
* **Super Slow-Motion:** Saat dialog soal kuis aktif, game melambat ke `0.1x` speed agar benteng pemain tidak kebobolan saat anak sedang berpikir.
* **Format Jawaban:** 4 tombol pilihan ganda berukuran besar dengan 4 warna berbeda (Merah, Biru, Kuning, Hijau) dan angka piksel berukuran besar (16–20 pt).
* **Penalti Lembut:** Jika salah menjawab atau waktu habis, tombol hanya berkedip merah selama 3 detik tanpa mengunci permanen.
* **Reward:**
  * Kuis Mana: Memberikan instan **+30 hingga +100 Mana**.
  * Kuis Obati Base: Memulihkan **+20% HP Kastel** (maksimal 2–3 kali per pertempuran).

---

## 5. Rincian 10 Level Kesulitan & Kurva Jarak Jalur

Panjang jalur horizontal bertambah bertahap dari 800 px hingga 3.600 px. Makin panjang jalur, waktu tempuh pasukan makin lama, sehingga anak diajak mengatur komposisi pasukan lari cepat dan pasukan penahan.

| Level | Nama Area / Tema | Panjang Jalur (Native Px) | Rasio Layar (480px Viewport) | Materi Matematika Ceria | Contoh Soal | Karakter & Monster |
|---|---|---|---|---|---|---|
| **Level 1** | Kebun Wortel | **800 px** | ~1.7 Layar | Tambah & Kurang Sangat Dasar ($\le 5$) | $2 + 1 = \dots$ / $4 - 1 = \dots$ | Jamur Mini & Kura-Kura Pelan |
| **Level 2** | Hutan Kupu-Kupu | **1.000 px** | ~2.1 Layar | Penjumlahan Satuan ($\le 10$) | $4 + 3 = \dots$ / $5 + 4 = \dots$ | Kelinci Nakal pelari cepat |
| **Level 3** | Lembah Pelangi | **1.200 px** | ~2.5 Layar | Pengurangan Satuan Sederhana | $8 - 3 = \dots$ / $9 - 5 = \dots$ | Monster Batu Bertameng Kayu |
| **Level 4** | Pantai Kelapa | **1.450 px** | ~3.0 Layar | Hitung Belasan Sederhana ($10 + x$) | $10 + 6 = \dots$ / $17 - 10 = \dots$ | Burung Pelikan penembak biji kelapa |
| **Level 5** | Rawa Balon Permen | **1.700 px** | ~3.5 Layar | Pola Angka Berurutan ($+1$) | $5, 6, 7, \dots?$ Angka berikutnya? | **Mini Boss Buaya Gendut**: HP tebal |
| **Level 6** | Goa Kristal Bintang | **2.000 px** | ~4.2 Layar | Penjumlahan Belasan Bersahabat ($\le 20$) | $8 + 7 = \dots$ / $11 + 4 = \dots$ | Kelelawar Ungu berterbangan |
| **Level 7** | Puncak Es Krim Salju | **2.350 px** | ~4.9 Layar | Kelipatan 2 & 5 yang Mudah | $2 \times 4 = \dots$ / $5 \times 3 = \dots$ | Orang-orangan Salju pembeku langkah |
| **Level 8** | Kastel Awan Permen | **2.700 px** | ~5.6 Layar | Pengurangan Belasan Ringan | $15 - 4 = \dots$ / $18 - 5 = \dots$ | Pasukan Kucing Berzirah Baja |
| **Level 9** | Gerbang Naga Ramah | **3.100 px** | ~6.5 Layar | Pola Lompat Angka ($+2$ atau $+5$) | $5, 10, 15, \dots?$ / $4, 6, 8, \dots?$ | Meriam Pelontar Gelembung Sabun |
| **Level 10** | Istana Bintang Ajaib | **3.600 px** | ~7.5 Layar | Perkalian Ceria Tabel 2, 3, dan 10 | $3 \times 4 = \dots$ / $10 \times 4 = \dots$ | **Raja Boneka Raksasa Bermahkota**: Boss Ceria |

---

## 6. Spesifikasi Kebutuhan Seluruh Aset (Asset Requirements)

### 6.1. Aset Background & Environment (Pixel Parallax Ceria)
Format: Seamless looping horizontal, tinggi kanvas 216 px, multi-layer:
* **Layer 1 (Skybox - Statis / Panning Lambat):**
  * Langit biru terang dengan awan putih empuk seperti permen kapas.
  * Langit senja merah muda (*pastel sunset*).
  * Langit malam ungu manis dengan bulan sabit tersenyum dan bintang berkedip (3 frame loop).
* **Layer 2 (Far Scenery - Paralaks Lambat):**
  * Siluet perbukitan hijau bulat, gunung es krim vanila, dan kastel fantasi di kejauhan.
* **Layer 3 (Midground - Paralaks Sedang):**
  * Pohon berdaun bundar cerah, lolipop raksasa tertancap, bendera piksel segitiga berkibar ceria.
* **Layer 4 (Foreground / Jalur Pasukan - Paralaks Cepat):**
  * Tileset tanah `16×16 px` atau `32×32 px` (Jalur rumput hijau terang, jalan pasir pantai cerah, jalan kue cokelat).
  * Hiasan pinggir jalur: Bunga piksel kuning tersenyum, jamur merah bintik putih, kristal pelangi bercahaya.

### 6.2. Aset Pasukan, Monster & Kastel (Pixel Spritesheets)
Orientasi default: Hadap kanan untuk pemain, dibalik (*flip-X*) untuk musuh. Standar animasi: Idle (4 frame), Walk (6-8 frame), Attack (4-6 frame), Hit Flash (2 frame), Die Poof (4 frame).

* **Kubu Pahlawan Cilik (Player Units):**
  1. *Prajurit Pedang Kayu* (`32×32 px`): Anak berbaju zirah mainan membawa tameng kayu bermotif senyum.
  2. *Pemanah Gelembung* (`32×32 px`): Peri berkerudung hijau penembak panah gelembung air transparan.
  3. *Penyihir Bintang* (`32×32 px`): Jubah ungu dengan topi kerucut bertabur bintang yang melontarkan proyektil kembang api mini.
  4. *Ksatria Kuda Poni* (`48×48 px`): Ksatria cilik menunggang kuda poni putih yang berlari kencang.
  5. *Robot Mainan Golem* (`64×64 px`): Robot kaleng bermata bundar ramah yang menghentak tanah (*ground slam*).
* **Kubu Musuh (Monster Menggemaskan):**
  1. *Jelly Slime*: Lendir hijau melompat kenyal.
  2. *Kelinci Wortel*: Kelinci bertelinga panjang berlarilincah.
  3. *Batuan Cilik*: Monster batu mini berwajah lucu bertameng kayu.
  4. *Buaya Gendut (Mini Boss)*: Buaya berbadan bulat membawa sendok raksasa.
  5. *Raja Boneka / Naga Ungu (Boss)* (`96×96 px`): Karakter boss gemuk menggemaskan bermahkota emas.
* **Kastel:**
  * *Kastel Pemain* (`96×160 px`): Menara batu bata putih cerah beratap genteng merah dan pintu gerbang kayu tersenyum.
  * *Kastel Musuh* (`96×160 px`): Benteng rumah jamur atau benteng kue ungu dengan bendera tengkorak kartun.
* **Visual Effects (Pixel VFX):**
  * Percikan bintang emas berkilau (*twinkling sparks*).
  * Pecahan gelembung air (*bubble pop*).
  * Letupan asap awan putih kartun (*poof cloud*) saat unit gugur.
  * Hujan pita warna-warni (*confetti*) saat menang.

### 6.3. Aset UI & UX Ramah Anak
* **Font:** Font piksel bertepi bulat tebal (*Chunky Pixel Font*), mudah dibaca anak, ukuran angka kuis minimal 16–20 pt.
* **HUD Game:**
  * Tabung Mana kaca transparan dengan cairan biru berkilau dan indikator angka tebal.
  * Bar HP Kastel strip panjang berwarna hijau cerah dengan ikon hati berdenyut.
  * Tombol kartu panggil unit `32×32 px` berbingkai emas dengan bayangan cooldown gelap transparan.
* **Dialog Kuis Pop-Up (`260 × 150 px`):**
  * Panel kayu/kertas kartun lucu di tengah layar.
  * 4 Tombol Pilihan Jawaban berukuran besar (`52 × 28 px`):
    * Tombol A: Merah cerah
    * Tombol B: Biru toska
    * Tombol C: Kuning ceria
    * Tombol D: Hijau segar

### 6.4. Aset Audio & Musik (Cheerful Chiptune)
* **BGM (16-bit Synth Ceria):**
  * `BGM_Title`: Lagu pembuka riang bertempo santai dengan tiupan suling synth.
  * `BGM_Battle_Fun`: Beat drum ceria berpadu melodi 8-bit cerah yang membangkitkan semangat.
  * `BGM_Boss_Playful`: Musik arkade bertempo lebih cepat namun tetap playful dan tidak menakutkan.
  * `Jingle_Victory`: Melodi terompet perayaan ceria diiringi suara sorak tepuk tangan anak-anak.
* **SFX Lucu (Synthesized Chiptune):**
  * Serangan: Ayunan kayu *whoosh*, tembakan gelembung *plop*, ledakan kembang api mini *pop-pop!*.
  * Interaksi: Suara lompatan pegas *boing!*, koin bintang *ting-ting!*, jawaban benar *chime arpeggio* merdu, jawaban salah suara kartun *wah-wah* lembut.

---

## 7. Arsitektur Kode JavaScript (ES6+ Ready Modules)

Di bawah ini adalah 3 modul JavaScript mandiri yang dapat langsung diintegrasikan ke dalam game loop HTML5 Canvas atau Phaser 3:

### 7.1. Modul Generator Soal Prosedural Ramah Anak (`KidsMathQuizGenerator.js`)

```javascript
/**
 * Modul Generator Soal Matematika Prosedural Ramah Anak (Level 1 - 10)
 */
export const QuizType = {
  MANA: 'MANA',
  FORTIFY: 'FORTIFY'
};

export class KidsMathQuizGenerator {
  static getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
  }

  static generateQuestion(level, quizType) {
    const clampedLevel = Math.min(Math.max(level, 1), 10);
    let questionText = '';
    let correctAnswer = 0;

    switch (clampedLevel) {
      case 1: { // Tambah-Kurang Sangat Dasar (Hasil <= 5)
        const a = this.getRandomInt(1, 3);
        const b = this.getRandomInt(1, 2);
        if (quizType === QuizType.MANA || a <= b) {
          questionText = `${a} + ${b} = ?`;
          correctAnswer = a + b;
        } else {
          questionText = `${a} - ${b} = ?`;
          correctAnswer = a - b;
        }
        break;
      }

      case 2: { // Penjumlahan Satuan (Hasil <= 10)
        const a = this.getRandomInt(2, 6);
        const b = this.getRandomInt(1, 4);
        questionText = `${a} + ${b} = ?`;
        correctAnswer = a + b;
        break;
      }

      case 3: { // Pengurangan Satuan Sederhana (Angka 1 - 10)
        const b = this.getRandomInt(1, 5);
        const a = b + this.getRandomInt(1, 4);
        questionText = `${a} - ${b} = ?`;
        correctAnswer = a - b;
        break;
      }

      case 4: { // Menghitung Belasan (10 + Satuan)
        const unit = this.getRandomInt(1, 9);
        if (quizType === QuizType.MANA) {
          questionText = `10 + ${unit} = ?`;
          correctAnswer = 10 + unit;
        } else {
          questionText = `${10 + unit} - 10 = ?`;
          correctAnswer = unit;
        }
        break;
      }

      case 5: { // Tebak Angka Maju Berurutan (Pola +1)
        const start = this.getRandomInt(1, 15);
        questionText = `${start}, ${start + 1}, ${start + 2}, ...?`;
        correctAnswer = start + 3;
        break;
      }

      case 6: { // Penjumlahan Belasan Bersahabat (Hasil <= 20)
        const a = this.getRandomInt(5, 10);
        const b = this.getRandomInt(2, 8);
        questionText = `${a} + ${b} = ?`;
        correctAnswer = a + b;
        break;
      }

      case 7: { // Kelipatan 2 & 5 yang Mudah
        const base = Math.random() > 0.5 ? 2 : 5;
        const multiplier = this.getRandomInt(2, 5);
        questionText = `${base} × ${multiplier} = ?`;
        correctAnswer = base * multiplier;
        break;
      }

      case 8: { // Pengurangan Belasan Sederhana (Belasan - Satuan)
        const b = this.getRandomInt(2, 6);
        const a = 10 + this.getRandomInt(2, 8);
        questionText = `${a} - ${b} = ?`;
        correctAnswer = a - b;
        break;
      }

      case 9: { // Pola Lompat Angka 2 atau 5
        const step = Math.random() > 0.5 ? 2 : 5;
        const start = this.getRandomInt(1, 4) * step;
        questionText = `${start}, ${start + step}, ${start + step * 2}, ...?`;
        correctAnswer = start + step * 3;
        break;
      }

      case 10: { // Perkalian Ceria Tabel 2, 3, dan 10
        const tables = [2, 3, 10];
        const a = tables[this.getRandomInt(0, tables.length - 1)];
        const b = this.getRandomInt(2, 6);
        questionText = `${a} × ${b} = ?`;
        correctAnswer = a * b;
        break;
      }
    }

    const { options, correctIndex } = this.generateKidsDistractors(correctAnswer);

    return {
      questionText,
      options,
      correctIndex,
      timeLimit: 10 // Batas waktu 10 detik ramah anak
    };
  }

  static generateKidsDistractors(correct) {
    const picked = new Set([correct]);
    const deltas = [-1, 1, -2, 2, -3, 3];

    while (picked.size < 4) {
      const delta = deltas[this.getRandomInt(0, deltas.length - 1)];
      let candidate = correct + delta;
      if (candidate <= 0 || picked.has(candidate)) {
        candidate = correct + this.getRandomInt(1, 4);
      }
      if (candidate > 0) {
        picked.add(candidate);
      }
    }

    picked.delete(correct);
    const options = Array.from(picked).map(String);
    const correctIndex = this.getRandomInt(0, 3);
    options.splice(correctIndex, 0, String(correct));

    return { options, correctIndex };
  }
}
```

### 7.2. Logika State Machine Pasukan (`LaneUnit.js`)

```javascript
/**
 * Kelas Unit Jalur 1D (State Machine: Walk, Attack, Die)
 */
export class LaneUnit {
  constructor(config) {
    this.id = config.id || Math.random().toString(36).substr(2, 9);
    this.name = config.name;
    this.isPlayer = config.isPlayer; // true = pahlawan, false = musuh
    this.x = config.x;
    this.y = config.y || 160;
    this.hp = config.hp;
    this.maxHp = config.hp;
    this.atk = config.atk;
    this.speed = config.speed;
    this.range = config.range;
    this.atkCooldown = config.atkCooldown || 1.5;
    this.timeSinceLastAtk = 0;
    this.state = 'WALK'; // WALK | ATTACK | DIE
  }

  update(dt, targets, enemyCastleX) {
    if (this.hp <= 0) {
      this.state = 'DIE';
      return;
    }

    this.timeSinceLastAtk += dt;

    // Cari target terdekat di hadapan unit
    const nearestTarget = this.findNearestTarget(targets, enemyCastleX);

    if (nearestTarget && nearestTarget.dist <= this.range) {
      this.state = 'ATTACK';
      if (this.timeSinceLastAtk >= this.atkCooldown) {
        this.performAttack(nearestTarget.entity);
        this.timeSinceLastAtk = 0;
      }
    } else {
      this.state = 'WALK';
      const moveDirection = this.isPlayer ? 1 : -1;
      this.x += moveDirection * this.speed * dt;
    }
  }

  findNearestTarget(targets, castleX) {
    let nearest = null;
    let minDistance = Infinity;

    // Cek jarak ke unit lawan
    for (const target of targets) {
      if (target.hp <= 0) continue;
      const dist = this.isPlayer ? (target.x - this.x) : (this.x - target.x);
      if (dist >= 0 && dist < minDistance) {
        minDistance = dist;
        nearest = { entity: target, dist: dist };
      }
    }

    // Cek jarak ke benteng lawan
    const castleDist = this.isPlayer ? (castleX - this.x) : (this.x - castleX);
    if (castleDist >= 0 && castleDist < minDistance) {
      minDistance = castleDist;
      nearest = { entity: { isCastle: true, takeDamage: (dmg) => {} }, dist: castleDist };
    }

    return nearest;
  }

  performAttack(target) {
    if (typeof target.takeDamage === 'function') {
      target.takeDamage(this.atk);
    }
  }

  takeDamage(amount) {
    this.hp = Math.max(0, this.hp - amount);
    if (this.hp === 0) {
      this.state = 'DIE';
    }
  }
}
```

### 7.3. Modul Kamera Pintar Auto-Follow (`KidsCameraHelper.js`)

```javascript
/**
 * Modul Kamera Pintar Landscape untuk Anak (Otomatis Mengikuti Garis Depan)
 */
export class KidsCameraHelper {
  constructor(canvasWidth, trackLength) {
    this.canvasWidth = canvasWidth;
    this.trackLength = trackLength;
    this.scrollX = 0;
  }

  autoFollowLeadingUnit(playerUnits, fallbackBaseX = 0) {
    const aliveUnits = playerUnits.filter(u => u.hp > 0);
    
    if (aliveUnits.length > 0) {
      // Temukan koordinat X paling depan dari pasukan pemain
      const leadingX = Math.max(...aliveUnits.map(u => u.x));
      // Pusatkan pandangan layar di titik depan pasukan
      const targetScroll = leadingX - (this.canvasWidth / 2);
      this.scrollX = Math.min(Math.max(targetScroll, 0), this.trackLength - this.canvasWidth);
    } else {
      // Jika belum ada pasukan, fokus di benteng sendiri
      this.scrollX = Math.min(Math.max(fallbackBaseX, 0), this.trackLength - this.canvasWidth);
    }
    
    return this.scrollX;
  }
}
```

---

## 8. Milestone Rencana Kerja (Production Roadmap)

1. **Milestone 1 - Core Arena & 1D Mechanics (Minggu 1):**
   * Setup viewport landscape 480 × 216 px dengan integer scaling.
   * Implementasi FSM unit (Walk, Attack, Die), pergerakan proyektil, dan penghancuran benteng.
2. **Milestone 2 - Kids Quiz Engine & Time Scale (Minggu 2):**
   * Integrasi modul generator soal matematika ceria Level 1–10.
   * Implementasi UI pop-up kuis 4 tombol warna-warni, efek slow-motion 0.1x, dan penambahan Mana/HP.
3. **Milestone 3 - Visual Spritesheet & Audio Overhaul (Minggu 3–4):**
   * Integrasi aset pixel art ramah anak (Pahlawan Cilik, Slime, Monster Gendut, Latar Paralaks).
   * Integrasi efek suara chiptune ceria dan musik latar 16-bit.
4. **Milestone 4 - Kid Playtesting & Balancing (Minggu 5):**
   * Uji coba bermain langsung bersama target anak usia 6–10 tahun untuk memastikan soal matematika mudah dipahami, kontrol kamera nyaman, dan game menyenangkan untuk dimainkan berulang kali.