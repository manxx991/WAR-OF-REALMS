# Master Asset Generation Prompt Catalog
**Game Title:** War of Realms: Pixel Lane Defense (Kids Math Edition)  
**Target File:** `C:\GAME\assets.md`  
**Spesifikasi Umum:** 16-bit Retro Pixel Art Ceria, Native Resolution 480 × 216 px (Upscale Integer 5x), Tanpa Anti-Aliasing, Palet Pastel Cerah, Ramah Anak (6–10 Tahun).

---

## 1. Master Parameter & Panduan Styling AI

### 1.1. Parameter Global Gambar (Image Generation: Midjourney / SDXL / DALL-E 3)
* **Master Style Suffix:**  
  `16-bit pixel art style, vibrant pastel and rich retro color palette, clean black outlines, cute chibi proportions, kids video game asset, sharp pixel edges, no anti-aliasing, side-scrolling orthographic 2D perspective, flat cartoon lighting --ar 16:9`
* **Master Negative Prompt:**  
  `3D render, realistic, photorealistic, cinematic lighting, blurry, smooth gradient shading, high-poly, vector art, muddy colors, dark, gritty, scary, terrifying, violent, gore, blood, weapons with blood, modern realism, anti-aliased, isometric perspective, isometric view, dithering, text, watermark, signature`
* **Format Output yang Ditargetkan:**
  * Background: Seamless tileable horizontal, tinggi base 216 px.
  * Spritesheet: Grid baris animasi berlatar belakang solid chroma key (`#00FF00` pure green atau `#FF00FF` pure magenta) untuk kemudahan ekstraksi transparansi.

---

## 2. Aset Background & Environment (Paralaks 4-Layer)

Format kanvas internal: Tinggi 216 px, seamless horizontal tiling.

### 2.1. Layer 1: Skybox (Langit & Awan)

#### [BG-01A] Skybox Siang Ceria (Bright Day)
* **Deskripsi:** Langit biru muda cerah dengan matahari tersenyum ramah dan gumpalan awan kapas empuk.
* **Prompt AI:**  
  > `Pixel art skybox background layer for 2D side-scrolling kids game, bright cheerful cyan blue sky, fluffy chunky white pixel clouds like cotton candy, tiny floating golden star glimmers, gentle smiling cartoon warm sun in the upper corner, seamless horizontal looping, 16-bit retro arcade style, clean vibrant pastel palette, strictly flat 2D side view --ar 16:9 --no ground, no characters, no trees, no mountains`

#### [BG-01B] Skybox Senja Manis (Pastel Sunset)
* **Deskripsi:** Langit senja dengan gradasi warna pastel jingga, merah muda lembut, dan ungu muda.
* **Prompt AI:**  
  > `Pixel art skybox background layer for 2D side-scrolling kids defense game, pastel sunset sky with gentle soft pink, peach orange and lavender purple tones, chunky pixel clouds tinted in warm gold, twinkling evening stars, seamless horizontal repeating, 16-bit retro aesthetic, cute and calming kids atmosphere, side-scrolling 2D --ar 16:9 --no ground, no characters, no terrain`

#### [BG-01C] Skybox Malam Bintang Manis (Sweet Night)
* **Deskripsi:** Langit malam ungu tua manis dengan bulan sabit tersenyum dan rasi bintang lucu.
* **Prompt AI:**  
  > `Pixel art skybox background layer for kids 2D side-scrolling game, sweet deep violet and dark indigo night sky, friendly smiling crescent moon wearing a tiny nightcap, clusters of cute twinkling yellow and cyan stars, gentle dreamy feel, seamless horizontal tile, 16-bit pixel art, crisp sharp pixels --ar 16:9 --no ground, no silhouettes, no characters`

---

### 2.2. Layer 2: Far Scenery (Pemandangan Jauh)

#### [BG-02A] Perbukitan Bulat & Kastel Fantasi (Lembah Ceria)
* **Deskripsi:** Siluet perbukitan hijau bulat dengan kastel fantasi mini berkubah bundar di kejauhan.
* **Prompt AI:**  
  > `Pixel art distant far background layer for 2D side-scroller, gentle rolling green hills with smooth round shapes, miniature pastel fairy-tale castles with round towers and colorful conical roofs in the distance, tiny windmills, soft haze effect, seamless horizontal tiling, 16-bit retro pixel art, clean outlines, flat orthographic side view, solid transparent or green background at base --ar 16:9 --no foreground ground, no characters`

#### [BG-02B] Pegunungan Es Krim Salju (Puncak Dingin Ceria)
* **Deskripsi:** Gunung bersalju yang menyerupai es krim vanila dan stroberi dengan lelehan glasir gula.
* **Prompt AI:**  
  > `Pixel art distant mountain scenery for 2D kids platformer, whimsical snow mountains shaped like scoops of vanilla and strawberry soft-serve ice cream, dripping pink sugar glaze, sugar cube rocks, pastel blue and lavender distant skyline, seamless horizontal loop, 16-bit arcade pixel art style, crisp edges --ar 16:9 --no ground tiles, no characters`

---

### 2.3. Layer 3: Midground (Pohon & Landmark Lucu)

#### [BG-03A] Hutan Balon & Lolipop Raksasa
* **Deskripsi:** Pohon-pohon berdaun bulat hijau cerah, lolipop raksasa tertancap, bendera piksel segitiga berkibar.
* **Prompt AI:**  
  > `Pixel art midground scenery layer for 2D horizontal lane game, row of cheerful round leafy trees with cute apples, giant swirling rainbow lollipops planted into tiny grassy mounds, colorful party bunting flags fluttering between wooden poles, seamless horizontal loop, 16-bit pixel art, vibrant bright colors, clean outlines, isolated on solid chroma green background `#00FF00` --ar 16:9 --no main ground road, no walking characters`

---

### 2.4. Layer 4: Foreground & Ground Tileset (Jalur Pertempuran 1D)

#### [TILE-01] Tileset Jalur Rumput Kebun Wortel (Level 1–3)
* **Deskripsi:** Strip jalur tanah datar dengan rumput hijau di atasnya, irisan tanah kartun dengan batu kerikil kecil.
* **Prompt AI:**  
  > `2D side-scrolling pixel art ground tileset strip for kids fantasy game, 32x32 modular tileset, flat smooth dirt walking path on top bordered by bright lime green grass tufts and tiny white daisies, cutaway side cross-section showing rich warm brown cartoon soil with embedded tiny harmless rounded pebbles, perfectly seamless horizontal looping, 16-bit retro arcade aesthetic, vibrant cute palette, clean pixel edges, straight horizontal alignment --ar 16:9 --no characters, no slopes, no curves`

#### [TILE-02] Tileset Jalur Pasir Pantai Kelapa (Level 4)
* **Deskripsi:** Jalur pasir pantai kuning emas cerah dengan hiasan cangkang kerang kecil dan bintang laut mini.
* **Prompt AI:**  
  > `2D side-scrolling pixel art ground tileset strip, sunny tropical beach sandy lane, flat smooth bright yellow sand walking surface with tiny pink seashells and orange starfish decorations, cutaway layer of moist packed sand below, seamless horizontal repeating, 16-bit retro pixel art style, cheerful kids aesthetic, straight horizontal lane --ar 16:9 --no water waves, no characters`

#### [TILE-03] Tileset Jalur Biskuit & Kue Cokelat (Level 5 & 8)
* **Deskripsi:** Jalur kue cokelat manis dengan taburan sprinkle warna-warni dan lapisan krim vanila.
* **Prompt AI:**  
  > `2D side-scrolling pixel art ground tileset strip for sweet candy world, flat chocolate wafer biscuit walking surface topped with rainbow sprinkles and white icing cream trim, cross-section showing fudge brownie cake layers underneath, seamless horizontal looping, 16-bit cute pixel art, bright edible colors --ar 16:9 --no characters, no slopes`

#### [PROP-01] Dekorasi Pinggir Jalur (Set Objek Jalur)
* **Deskripsi:** Bunga piksel kuning tersenyum, jamur merah bintik putih, kristal pelangi bercahaya, wortel mini tertanam.
* **Prompt AI:**  
  > `Pixel art decorative prop spritesheet for kids game lane, containing individual sprites: friendly smiling yellow sunflower, cute red mushroom with white polka dots, glowing rainbow crystal shard, tiny orange carrot sticking out of dirt, wooden signpost with arrow. 16-bit pixel art, chunky black outlines, bright cheerful colors, arranged on solid chroma green `#00FF00` background grid --ar 16:9`

---

## 3. Aset Pasukan Pahlawan Cilik (Player Units Spritesheets)

Spesifikasi Animasi:
* Orientasi: Hadap kanan.
* Grid Spritesheet: 5 baris animasi (Idle 4 frame, Walk 6-8 frame, Attack 4-6 frame, Hit Flash 2 frame, Die Poof 4 frame).
* Background: Solid Chroma Green (`#00FF00`).

### [HERO-01] Prajurit Pedang Kayu (Little Wooden Swordsman)
* **Ukuran Frame:** 32 × 32 px
* **Peran:** Pasukan Melee garis depan penahan laju musuh.
* **Visual:** Bocah berkepala besar (chibi) mengenakan helm ember perak dengan bulu biru, memegang pedang kayu mainan dan perisai bundar bertuliskan gambar senyum.
* **Prompt AI:**  
  > `Full character spritesheet for 2D side-scrolling kids game, cute chibi kid knight in shiny silver tin armor, oversized blue plume on knight helmet, holding wooden toy sword and round wooden shield with happy smiley face emblem. Spritesheet layout arranged in clean organized horizontal animation strips on solid pure green background `#00FF00`: Row 1 Idle (4 frames breathing/blinking), Row 2 Running forward (6 frames bouncing run), Row 3 Swinging wooden sword attack (4 frames comical slash), Row 4 Hurt reaction (2 frames blinking white/red), Row 5 Cheerful defeat disappearing into white poof cloud and yellow stars (4 frames). 16-bit pixel art, vibrant retro palette, no anti-aliasing --ar 16:9`

### [HERO-02] Pemanah Gelembung (Bubble Archer Fairy)
* **Ukuran Frame:** 32 × 32 px
* **Peran:** Penyerang jarak jauh (Ranged Damage).
* **Visual:** Peri cilik bertopi daun hijau, membawa busur dari ranting melengkung, menembakkan panah berujung gelembung sabun transparan.
* **Prompt AI:**  
  > `Full character spritesheet for 2D kids side-scroller game, adorable chibi forest fairy girl with pointy ears, leafy green hood, holding curved wooden bow made of twigs. Animation sequences arranged in grid on solid pure green `#00FF00` background: Row 1 Idle (4 frames gentle hovering flutter wings), Row 2 Walk (6 frames skipping forward), Row 3 Shooting bubble arrow (5 frames draw string, release shiny blue soap bubble projectile), Row 4 Hurt (2 frames spin backward), Row 5 Defeat (4 frames turns into popping bubbles and sparkles). 16-bit pixel art, bright pastel colors, clean pixel lines --ar 16:9`

### [HERO-03] Penyihir Bintang (Star Mage)
* **Ukuran Frame:** 32 × 32 px
* **Peran:** Magic Area of Effect (AoE) penembak kembang api.
* **Visual:** Anak berjubah ungu kebesaran dengan topi kerucut bertabur bintang emas, memegang tongkat sihir berujung bintang bersinar.
* **Prompt AI:**  
  > `Full character spritesheet for 2D kids lane defense game, cute chibi little wizard boy wearing oversized dark purple starry robe and pointy wizard hat covering eyes, holding wooden wand topped with glowing yellow star. Spritesheet on solid chroma green background `#00FF00`: Row 1 Idle (4 frames wand bobbing with star sparks), Row 2 Walk (6 frames cute waddling run with robe swaying), Row 3 Magic Cast Attack (5 frames waving wand overhead, launching rainbow star burst projectile), Row 4 Hurt (2 frames hat flies up briefly), Row 5 Defeat (4 frames poofs into cloud of colorful star sparks). 16-bit retro pixel art, crisp sharp pixels --ar 16:9`

### [HERO-04] Ksatria Kuda Poni (Pony Cavalier)
* **Ukuran Frame:** 48 × 48 px
* **Peran:** Pasukan berkuda lari cepat (Speed Flanker).
* **Visual:** Ksatria cilik mengenakan mantel merah gagah menunggangi kuda poni putih berambut merah muda yang berlari riang.
* **Prompt AI:**  
  > `Full character spritesheet for 2D side-scrolling game, cute chibi kid knight wearing red cape riding adorable chubby white pony with pastel pink mane and tail. Spritesheet grid on solid pure green `#00FF00` background: Row 1 Idle (4 frames pony stomping hooves happily), Row 2 Galloping Fast Walk (6 frames energetic joyful pony gallop), Row 3 Lance Charge Attack (4 frames pointing foam-tipped toy lance forward), Row 4 Hurt (2 frames pony rears back surprised), Row 5 Defeat (4 frames pony turns into cartoon cloud poof with tiny horse shoes floating). 16-bit pixel art, vibrant colors, clear sprite outlines --ar 16:9`

### [HERO-05] Robot Mainan Golem (Toy Tin Golem)
* **Ukuran Frame:** 64 × 64 px
* **Peran:** Tanker berat dan penghentak tanah (Ground Slam).
* **Visual:** Robot kaleng bulat bergaya mainan mekanik tempo dulu dengan mata bulat menyala ramah, dada berkaca indikator, dan kunci putar di punggung.
* **Prompt AI:**  
  > `Full character spritesheet for 2D kids lane defense game, bulky but friendly cute retro tin toy robot golem, rounded metallic body painted in mint green and yellow, glowing cheerful round electric eyes, brass wind-up key turning on back. Spritesheet on solid chroma green `#00FF00` background: Row 1 Idle (4 frames antenna blinking, slight steam puff), Row 2 Stomp Walk (6 frames heavy rhythmic stomping), Row 3 Ground Slam Attack (6 frames raises big metal fists and slams the dirt sending mini cartoon dust wave), Row 4 Hurt (2 frames electric cartoon spark wobble), Row 5 Defeat (4 frames falling apart into playful colorful toy bolts and smoke poof). 16-bit pixel art, clean sharp pixels --ar 16:9`

---

## 4. Aset Monster Menggemaskan (Enemy Monsters Spritesheets)

Spesifikasi Animasi:
* Orientasi: Hadap kiri (menyerang kastel pemain di kiri).
* Grid Spritesheet: Idle, Walk, Attack, Hit, Die.
* Background: Solid Chroma Green (`#00FF00`).

### [MOB-01] Jelly Slime Hijau
* **Ukuran Frame:** 32 × 32 px
* **Karakteristik:** Lendir hijau berwajah imut yang melompat-lompat kenyal.
* **Prompt AI:**  
  > `Full enemy monster spritesheet for 2D kids side-scroller, cute bouncy lime green gelatin slime blob with big smiling cartoon eyes and pink blushing cheeks, facing left. Spritesheet arranged on solid pure green `#00FF00` background: Row 1 Idle (4 frames squishing down and stretching up), Row 2 Bouncing Walk (6 frames leaping forward like a rubber ball), Row 3 Headbutt Attack (4 frames stretching body forward to smack opponent), Row 4 Hurt (2 frames flattening flat on ground with swirl eyes), Row 5 Defeat (4 frames splitting into harmless tiny jelly droplets with a pop). 16-bit retro pixel art, vibrant bright colors --ar 16:9`

### [MOB-02] Kelinci Wortel Lincah (Carrot Bunny)
* **Ukuran Frame:** 32 × 32 px
* **Karakteristik:** Kelinci cokelat muda memakai bandana merah, berlari kencang sambil menggenggam wortel.
* **Prompt AI:**  
  > `Full enemy monster spritesheet for kids defense game, naughty cute chibi brown bunny rabbit wearing red pirate bandana, holding large orange carrot like a club, facing left. Grid on solid pure green `#00FF00` background: Row 1 Idle (4 frames twitching long ears and wiggling nose), Row 2 Sprint Walk (6 frames rapid hopping zig-zag run), Row 3 Carrot Whack Attack (4 frames swinging carrot downwards), Row 4 Hurt (2 frames ears flapping backward in shock), Row 5 Defeat (4 frames turning into white cartoon puff cloud with dropped carrot). 16-bit pixel art, cute chibi arcade style --ar 16:9`

### [MOB-03] Batuan Cilik Bertameng Kayu (Baby Pebble Golem)
* **Ukuran Frame:** 32 × 32 px
* **Karakteristik:** Monster batu mini bulat berwajah ramah membawa papan kayu kecil sebagai perisai.
* **Prompt AI:**  
  > `Full enemy monster spritesheet for 2D horizontal lane game, adorable miniature round pebble stone creature with short stubby legs, big round glowing yellow eyes, holding tiny wooden plank shield, facing left. Spritesheet on solid pure green `#00FF00`: Row 1 Idle (4 frames shifting weight), Row 2 Waddling Walk (6 frames funny heavy waddle), Row 3 Shield Push Attack (4 frames thrusting wooden shield forward), Row 4 Hurt (2 frames stumbling backward with chips flying), Row 5 Defeat (4 frames crumbling into harmless tiny pebbles and star sparks). 16-bit pixel art style, rich earthy palette --ar 16:9`

### [MOB-04] Buaya Gendut Bersendok (Chubby Spoon Croc - Mini Boss)
* **Ukuran Frame:** 64 × 64 px
* **Karakteristik:** Buaya gemuk berbadan bulat warna toska yang mengenakan celemek makan dan membawa sendok raksasa.
* **Prompt AI:**  
  > `Full mini-boss character spritesheet for 2D kids lane defense game, chubby friendly cartoon turquoise crocodile with huge round belly, wearing white polka-dot bib around neck, holding giant silver dessert spoon, facing left. Grid on solid pure green background `#00FF00`: Row 1 Idle (4 frames heavy belly breathing), Row 2 Stomping Walk (6 frames funny lumbering forward walk), Row 3 Giant Spoon Slam Attack (5 frames rearing back and slamming spoon on ground), Row 4 Hurt (2 frames funny shocked face with tongue out), Row 5 Defeat (4 frames spinning around dizzily and vanishing in big fluffy cloud with candy stars). 16-bit retro arcade pixel art --ar 16:9`

### [MOB-05] Raja Boneka Naga Ungu (Chubby Dragon King - Final Boss)
* **Ukuran Frame:** 96 × 96 px
* **Karakteristik:** Naga gemuk berwarna ungu pastel dengan mahkota emas miring, sayap mungil bergetar, meniupkan bola api kartun mini.
* **Prompt AI:**  
  > `Full main boss character spritesheet for 2D side-scrolling kids game, huge chubby pastel purple plush dragon boss wearing tilted golden crown with red ruby, tiny comical fluttering bat wings on back, round chubby belly, facing left. Spritesheet organized in clean rows on solid pure chroma green `#00FF00` background: Row 1 Idle (4 frames flapping tiny wings, tail swishing), Row 2 Royal March Walk (6 frames heavy stomping steps shaking the earth), Row 3 Puff Flame Attack (6 frames deep inhale, puffing three cute orange cartoon fireball rings), Row 4 Hurt (2 frames crown bounces in air, dizzy spiral eyes), Row 5 Cheerful Defeat (5 frames dragon sits down smiling, waving white surrender flag as confetti bursts). 16-bit pixel art, ultra-clean edges --ar 16:9`

---

## 5. Aset Kastel & Bangunan Markas (Base Castles)

Ukuran Kanvas Base: 96 × 160 px, Full Orthographic Side-View.

### [CASTLE-01] Kastel Pemain (Player Toy Fortress)
* **Deskripsi:** Menara batu bata putih cerah beratap genteng merah cerah, bendera biru berkibar, pintu gerbang kayu bundar tersenyum ramah, balkon pemanah di atas.
* **Variasi:** 
  1. Kondisi Utuh (Full HP).
  2. Kondisi Sedikit Retak / Plester Lucu (HP < 50%).
* **Prompt AI:**  
  > `Pixel art castle building asset for 2D side-scrolling kids defense game, player base fortress, 96x160 px dimensions, facing right. Built with bright white clean stone bricks, bright cherry red tiled conical roofs, friendly open wooden arched gate with cartoon eyes and smile, fluttering sky blue flag on tallest tower spire, wooden upper parapet, cozy glowing window. Clean 16-bit pixel art, vibrant fairytale colors, isolated on solid pure chroma green background `#00FF00` --ar 9:16 --no realistic damage, no dark gothic elements`

### [CASTLE-02] Kastel Rumah Jamur / Kue Musuh (Enemy Monster Base)
* **Deskripsi:** Benteng unik berbentuk rumah jamur raksasa berwarna ungu dengan jendela bintik kuning atau benteng kue dengan bendera bajak laut kartun yang lucu.
* **Variasi:**
  1. Kondisi Utuh (Full HP).
  2. Kondisi Retak Gula / Miring Lucu (HP < 50%).
* **Prompt AI:**  
  > `Pixel art enemy castle fortress for 2D kids side-scroller game, 96x160 px dimensions, facing left. Designed as a giant whimsical dark purple toadstool mushroom castle combined with fantasy candy bricks, twisted chimney puffing lavender smoke, round wooden door with silly cartoon skull decoration wearing party hat, fluttering pastel magenta flag on peak. 16-bit retro arcade aesthetic, cute and non-threatening, isolated on solid chroma green background `#00FF00` --ar 9:16 --no blood, no terrifying horror elements`

---

## 6. Aset Efek Visual Piksel (Pixel VFX Spritesheets)

Format: Spritesheet transparan horizontal strip atau grid chroma green.

### [VFX-01] Percikan Bintang Emas (Twinkling Sparks)
* **Ukuran Frame:** 16 × 16 px (4–6 Frame)
* **Kegunaan:** Efek saat serangan sihir kena musuh atau saat menjawab kuis dengan benar.
* **Prompt AI:**  
  > `Pixel art VFX spritesheet of twinkling golden star sparks, 6 frame horizontal sequence, tiny bright yellow and white stars bursting, spinning, glowing, and shrinking away into sparkle dust, 16x16 pixel size per frame, 16-bit arcade video game particle effect, isolated on solid pure black or green background --ar 16:9`

### [VFX-02] Letupan Gelembung Sabun (Bubble Pop)
* **Ukuran Frame:** 24 × 24 px (4 Frame)
* **Kegunaan:** Efek panah gelembung pecah mengenai lawan.
* **Prompt AI:**  
  > `Pixel art VFX spritesheet of cartoon water bubble popping, 4 frame animation sequence, shiny cyan soap bubble expanding slightly then bursting into tiny water droplets and glimmers, 24x24 px frame size, 16-bit cute pixel art, clean sharp pixel boundaries, solid chroma green `#00FF00` background --ar 16:9`

### [VFX-03] Awan Asap Kartun (Defeat Poof Cloud)
* **Ukuran Frame:** 32 × 32 px (5 Frame)
* **Kegunaan:** Menggantikan animasi mati berdarah; unit lenyap dalam kepulan asap awan empuk.
* **Prompt AI:**  
  > `Pixel art VFX spritesheet for friendly cartoon defeat poof effect, 5 frame horizontal sequence, sudden fluffy white smoke puff expanding outwards with tiny embedded yellow spinning stars and cartoon pop lines, then quickly evaporating cleanly, 32x32 pixel frames, 16-bit retro style, solid chroma green background --ar 16:9 --no dark smoke, no fire`

### [VFX-04] Hujan Pita Confetti Kemenangan (Victory Confetti)
* **Ukuran Frame:** Loopable Fullscreen Grid (480 × 216 px)
* **Kegunaan:** Perayaan layar kemenangan saat kastel lawan berhasil dihancurkan.
* **Prompt AI:**  
  > `Pixel art looping animation spritesheet of colorful party celebration confetti, falling spiral paper ribbons and square glitter sprinkles in red, gold, sky blue, and pink drifting gently downwards, festive celebration mood, 16-bit retro pixel art, clean particles, isolated on pure black background for blend mode --ar 16:9`

---

## 7. Aset UI & UX Ramah Anak (HUD & Menu Sprites)

### 7.1. Frame & Ikon HUD Utama

#### [UI-01] Tabung Mana Ajaib & Cairan Berkilau
* **Ukuran:** Tabung 24 × 48 px + Cairan Tileable
* **Deskripsi:** Tabung reaksi kaca bening bergaya kartun berbingkai perunggu emas dengan indikator level cairan biru bercahaya dan gelembung kecil naik.
* **Prompt AI:**  
  > `Pixel art UI game asset, vertical magic mana flask bottle, rounded clear glass test tube with ornate golden rim and cork stopper, filled with glowing sapphire blue sparkling liquid, floating tiny bubbles inside, shiny glass reflection highlight strip, 16-bit pixel art, cute arcade game interface, isolated on green background --ar 1:1`

#### [UI-02] Bar HP Kastel dengan Ikon Hati Denyut
* **Ukuran:** Bar 80 × 12 px, Ikon Hati 16 × 16 px
* **Deskripsi:** Frame kayu halus dengan bilah pengukur darah warna hijau rumput cerah dan ikon hati merah kartun bertepi putih tebal.
* **Prompt AI:**  
  > `Pixel art UI health bar asset set, horizontal wooden health frame with bright emerald green health fill strip, accompanied by separate cute 16x16 chunky red cartoon heart icon with shiny white highlight reflection and 3-frame beating animation, 16-bit retro interface, clean pixelated style, solid green background --ar 16:9`

#### [UI-03] Tombol Kartu Panggil Unit (Deck Slot)
* **Ukuran:** 32 × 32 px per kartu
* **Deskripsi:** Bingkai kartu kayu tebal berpelipit emas, sudut membulat, angka biaya mana di pojok kiri atas dalam lingkaran biru, bayangan transparan untuk status cooldown.
* **Prompt AI:**  
  > `Pixel art UI card frame button for summoning units in 2D tower defense game, 32x32 pixel square card icon with chunky carved wooden border, golden corners, small circular blue mana cost gem in upper corner, dark semi-transparent clock wipe cooldown overlay variant, 16-bit pixel art, crisp sharp pixels, solid green background --ar 1:1`

#### [UI-04] Tombol Aksi Kuis & Pemulihan Base
* **Ukuran:** 40 × 40 px per tombol
* **Komponen:**
  1. Tombol "Mana Tanya": Buku mantra biru dengan bintang kuning melayang.
  2. Tombol "Obati Base": Palu kayu mainan lucu dengan pita perban putih.
* **Prompt AI:**  
  > `Pixel art UI action buttons set for kids math defense game, two large chunky circular buttons: Button 1 shows an open blue magical math book with a glowing yellow star popping out (+Mana Quiz); Button 2 shows a friendly wooden toy repair hammer with a cute white band-aid cross (+Repair Base). Chunky golden bevel border, cheerful kids game UI, 16-bit pixel art, on chroma green background --ar 16:9`

---

### 7.2. Dialog Pop-Up Kuis Matematika Ramah Anak (260 × 150 px)

#### [UI-05] Panel Dialog Kuis & 4 Tombol Pilihan Jawaban
* **Ukuran Panel:** 260 × 150 px
* **Ukuran Tombol Jawaban:** 52 × 28 px
* **Spesifikasi Warna:**
  * Tombol A: Merah Ceri (`#FF4757`)
  * Tombol B: Biru Toska (`#1E90FF`)
  * Tombol C: Kuning Mentari (`#FFA502`)
  * Tombol D: Hijau Apel (`#2ED573`)
* **Prompt AI:**  
  > `Pixel art UI math quiz pop-up dialog box for kids game, 260x150 pixel central popup frame made of cream parchment paper with sturdy rounded oak wood border, friendly cartoon star mascot holding a pencil on top corner, clean blackboard center area for math equation. Included below are 4 large chunky pill-shaped answer buttons (52x28 px) in 4 distinct bright cheerful colors: bright cherry red, vibrant sky blue, warm sunny yellow, and crisp grass green, embossed 3D button press effect, 16-bit retro game UI, solid chroma green background --ar 16:9`

---

## 8. Master Audio Prompts (Music & Sound Effects)

Target Output: 16-bit Synth Chiptune, FM Synthesis, GBA / SNES Era Aesthetic, Tanpa Suara Menakutkan.  
Platform Generator yang Direkomendasikan: **Suno AI / Udio / ElevenLabs Sound Effects / Stable Audio**.

### 8.1. Musik Latar Belakang (BGM)

#### [BGM-01] Lagu Layar Menu Utama (`BGM_Title`)
* **Platform:** Suno AI / Udio
* **Style / Genre:** 16-bit Chiptune, GBA Nostalgic Pop, Cheerful Whistle, Playful Synth Flute, Light Xylophone, 105 BPM.
* **Prompt Teks:**  
  > `Instrumental upbeat nostalgic 16-bit chiptune video game title screen music, playful synthesized flute melody, bright glockenspiel bells, bouncy bassline, warm FM synth chords, sunny morning adventure feeling, tempo 105 BPM, cute SNES era aesthetic, loopable and joyful`

#### [BGM-02] Musik Pertempuran Ceria (`BGM_Battle_Fun`)
* **Platform:** Suno AI / Udio
* **Style / Genre:** Fast Chiptune, Arcade Lane Defense, Upbeat March, 8-bit Arpeggios, Punchy Chiptune Drums, 128 BPM.
* **Prompt Teks:**  
  > `Instrumental energetic and cheerful 16-bit arcade battle theme, driving chiptune march drums, playful catchy square-wave synth lead, bouncy bass, lively arpeggiated synth bells, lighthearted medieval kids strategy game, tempo 128 BPM, motivating and fun, high energy with zero dark or scary tension`

#### [BGM-03] Musik Pertarungan Boss Ceria (`BGM_Boss_Playful`)
* **Platform:** Suno AI / Udio
* **Style / Genre:** Quirky Arcade Boss, Cartoon Fast-Paced Funk, Horns Synth, Whimsical Mallet, 136 BPM.
* **Prompt Teks:**  
  > `Instrumental playful 16-bit retro boss battle theme, quirky fast-paced cartoon energy, goofy synth brass stabs, funky slap-bass line, fast 8-bit drum roll fills, comedic mischievous melody, tempo 136 BPM, playful duel feel, kid-friendly tension, GBA game style`

#### [BGM-04] Jingle Kemenangan (`Jingle_Victory`)
* **Platform:** Suno AI / Udio
* **Durasi:** 6–8 detik
* **Style / Genre:** Fanfare, Victory Chime, Cheerful Brass, Applause.
* **Prompt Teks:**  
  > `Short 7-second 16-bit video game victory fanfare jingle, triumphant synthesized brass trumpet melody ascending, sparkling glockenspiel chimes, joyful final chord with sound of cheerful kids cheering and clapping in background, retro arcade win theme`

---

### 8.2. Efek Suara (Sound Effects - SFX)

Platform Generator: **ElevenLabs SFX / Stable Audio / SFXR / Bfxr**.

| Kode SFX | Nama Suara | Prompt Generator / Deskripsi Sintesis | Karakteristik Audio |
| :--- | :--- | :--- | :--- |
| **SFX-01** | Ayunan Pedang Kayu | `Retro 16-bit video game wooden toy sword swoosh whoosh sound, crisp clean cartoon swing` | Ringan, tumpul, tanpa bunyi bilah tajam |
| **SFX-02** | Tembakan Gelembung | `Cartoon soap bubble shoot plop popping sound, high pitched bubbly release, 8-bit arcade` | Basah, bulat, bernada tinggi (*plop!*) |
| **SFX-03** | Ledakan Kembang Api | `Mini cheerful firecracker pop pop burst sound effect, 16-bit tiny magic spark explosion, harmless party popper` | Renyah, ceria, mirip letupan petasan pesta |
| **SFX-04** | Hentakan Golem | `Chunky cartoon toy robot stomp ground thud, comical low frequency wooden box drop, harmless bounce` | Berdentum lembut tanpa distorsi berat |
| **SFX-05** | Lompatan Pegas Slime | `Comical rubber boing bounce sound effect, retro 8-bit cartoon spring jump, cheerful elastic stretch` | Melar elastis (*boiiing!*) |
| **SFX-06** | Koin / Bintang Didapat | `Retro video game sparkling high pitch coin pickup sound, bright crystalline chime arpeggio, ting ting!` | Gemerincing merdu, frekuensi tinggi |
| **SFX-07** | Jawaban Kuis Benar | `Cheerful harmonic harp glissando chime, high-pitched magical correct answer ding, pleasant uplifting reward sound` | Akord mayor naik 3 nada merdu |
| **SFX-08** | Jawaban Kuis Salah | `Gentle soft cartoon wah-wah trombone brass sound, funny friendly mistake tone, non-punishing harmless bounce` | Komikal, bersahabat, tanpa nada buzzer kasar |

---

## 9. Struktur Folder Penyimpanan Aset Game

Setelah aset digenerate dan dipotong (*cropped*), simpan seluruh berkas ke dalam direktori berikut:

```text
C:\GAME\assets\
├── background\
│   ├── bg_sky_day.png
│   ├── bg_sky_sunset.png
│   ├── bg_sky_night.png
│   ├── bg_far_hills.png
│   ├── bg_far_snow.png
│   ├── bg_mid_trees.png
│   └── tilesets\
│       ├── tile_grass_dirt.png
│       ├── tile_beach_sand.png
│       ├── tile_cookie_road.png
│       └── props_nature.png
├── sprites\
│   ├── heroes\
│   │   ├── hero_swordsman.png
│   │   ├── hero_archer.png
│   │   ├── hero_mage.png
│   │   ├── hero_pony.png
│   │   └── hero_golem.png
│   ├── enemies\
│   │   ├── enemy_slime.png
│   │   ├── enemy_bunny.png
│   │   ├── enemy_pebble.png
│   │   ├── boss_croc.png
│   │   └── boss_dragon.png
│   ├── buildings\
│   │   ├── castle_player.png
│   │   └── castle_enemy.png
│   └── vfx\
│       ├── vfx_sparks.png
│       ├── vfx_bubble_pop.png
│       ├── vfx_poof_cloud.png
│       └── vfx_confetti.png
├── ui\
│   ├── hud_mana_tube.png
│   ├── hud_hp_bar.png
│   ├── card_unit_frame.png
│   ├── btn_mana_quiz.png
│   ├── btn_heal_base.png
│   ├── popup_quiz_dialog.png
│   └── btn_quiz_options.png
└── audio\
    ├── bgm\
    │   ├── bgm_title.mp3
    │   ├── bgm_battle_fun.mp3
    │   ├── bgm_boss_playful.mp3
    │   └── jingle_victory.mp3
    └── sfx\
        ├── sfx_wood_swing.wav
        ├── sfx_bubble_shoot.wav
        ├── sfx_star_pop.wav
        ├── sfx_stomp_thud.wav
        ├── sfx_slime_boing.wav
        ├── sfx_star_coin.wav
        ├── sfx_quiz_correct.wav
        └── sfx_quiz_wrong.wav
```
