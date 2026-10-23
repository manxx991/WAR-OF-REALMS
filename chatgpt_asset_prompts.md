 # Master Prompt Generator Aset (Format Khusus ChatGPT / DALL-E 3)
**Game Title:** War of Realms: Math Combat Arena (SMA/SMK & Mahasiswa Baru Edition)  
**Target Engine AI:** ChatGPT (GPT-4o / DALL-E 3 Image Generation)  
**Gaya Visual:** 16-bit Cyber-Arcade Pixel Art, Dark Mode Sci-Fi Fantasy, Neon Cyan (`#00f2fe`), Electric Gold (`#ffd200`), Obsidian Dark Slate, Sharp Pixel Edges, Strictly 2D Side-View Orthographic.

---

## 📌 Panduan Penggunaan di ChatGPT

1. **Cara Mengirim Prompt:**  
   Salin teks prompt di dalam blok kutipan (`>`) langsung ke kolom chat ChatGPT.
2. **Kunci Warna Latar Belakang (Chroma Key):**  
   Semua prompt karakter/objek diatur menggunakan latar belakang **Solid Pure Magenta (`#FF00FF`)**. Warna magenta dipilih agar tidak bentrok dengan elemen warna hijau, biru, atau kuning pada karakter.
3. **Aturan Penting untuk DALL-E 3:**  
   DALL-E 3 tidak menggunakan sintaks Midjourney seperti `--ar 16:9` atau `--no ...`. Formula prompt di bawah ini sudah disesuaikan dengan instruksi bahasa alami yang paling dipatuhi oleh DALL-E 3.

---

## 1. Background & Environment Paralaks (4 Layers)

### [BG-01] Layer 1: Skybox Cyber Grid & Nebula Digital
* **Lokasi Simpan:** `assets/background/bg_sky_cyber.png`
* **Prompt ChatGPT:**
> Generate a seamless horizontally loopable 2D side-scrolling skybox background for a retro cyber arcade pixel art game. Theme: deep dark indigo and obsidian night sky with a glowing digital wireframe grid horizon, distant digital neon nebula clouds in cyan and purple, faint floating pixel data stars, retro 16-bit pixel art aesthetic with sharp pixel edges and no anti-aliasing. Strictly flat 2D side view, perfectly horizontal alignment. No ground, no characters, no terrain, wide landscape ratio.

### [BG-02] Layer 2: Scenery Jauh - Siluet Megacity & Menara Server
* **Lokasi Simpan:** `assets/background/bg_far_cyber_city.png`
* **Prompt ChatGPT:**
> Generate a seamless horizontally tileable distant background layer for a 2D side-scrolling pixel art game. Theme: silhouettes of a futuristic dark cyberpunk megacity and massive computing monolith towers in the far distance, glowing neon windows and antenna lights in teal and magenta, faint atmospheric scanline haze. 16-bit retro arcade style, strictly flat orthographic 2D perspective. The bottom of the layer sits on a transparent or solid magenta background. No foreground characters, no road.

### [BG-03] Layer 3: Midground - Pilar Sirkuit & Pylon Energi
* **Lokasi Simpan:** `assets/background/bg_mid_pylons.png`
* **Prompt ChatGPT:**
> A 2D side-scroller midground scenery layer in 16-bit pixel art style, seamless horizontal looping. Featuring technological glowing energy pylons, exposed cybernetic conduits, floating holographic data glyphs, and pulse capacitors along the path. Dark slate metallic structures with bright electric cyan and neon amber light trims. Clean pixel art, no 3D rendering, flat side view. Isolated on solid pure magenta `#FF00FF` background at the bottom. No walking characters.

### [BG-04] Layer 4: Lintasan Pijakan - Cyber Circuit Road & Cross Section
* **Lokasi Simpan:** `assets/background/tilesets/tile_cyber_lane.png`
* **Prompt ChatGPT:**
> A horizontal ground tileset strip for a 2D side-scrolling tactical defense game in 16-bit pixel art style. The walking surface is a flat, dark titanium metal plate with glowing cyan circuit lines and pulse nodes running through it. Below the surface is a cross-section showing exposed dark futuristic motherboard layers, copper data traces, and tiny fiber-optic filaments. Perfectly straight horizontal plane, perfectly seamless horizontal looping, crisp pixel borders, no slopes. No characters, flat 2D side cutaway view.

---

## 2. Spritesheet Pasukan Pemain (Player Units)

Semua karakter pemain menghadap ke **kanan**.

### [HERO-01] Prajurit Pedang Cyber (Melee Vanguard - 32x32 px)
* **Deskripsi:** Prajurit infanteri berzirah nano gelap dengan pedang laser plasma cyan dan perisai hologram.
* **Lokasi Simpan:** `assets/sprites/heroes/hero_swordsman.png`
* **Prompt ChatGPT:**
> Full character spritesheet for a 2D side-scrolling tactical pixel art game, facing right. Character: a sleek futuristic cyber warrior wearing dark charcoal tactical armor with neon cyan trim, glowing visor helmet, wielding a radiant cyan energy sword and a small hexagonal hard-light holographic shield. Arrange the spritesheet in clean, organized horizontal animation rows on a solid pure magenta `#FF00FF` background:
> - Row 1: Idle animation (4 frames, subtle breathing and energy sword pulsing)
> - Row 2: Running forward (6 frames, dynamic combat run)
> - Row 3: Sword slash attack (4 frames, fast forward slash leaving a neon energy arc)
> - Row 4: Hit reaction (2 frames, flickering red and white shield impact)
> - Row 5: Defeat animation (4 frames, armor breaks into dissolving cyan data particles)
> Style: 16-bit retro arcade pixel art, crisp sharp pixels, no anti-aliasing, no 3D shading, perfectly equal frame sizing.

### [HERO-02] Pemanah Plasma (Ranged DPS - 32x32 px)
* **Deskripsi:** Penembak jitu cyber berkerudung taktis dengan busur medan gaya elektromagnetik yang melontarkan anak panah plasma biru.
* **Lokasi Simpan:** `assets/sprites/heroes/hero_archer.png`
* **Prompt ChatGPT:**
> Full character spritesheet for a 2D side-scrolling pixel art defense game, facing right. Character: a high-tech female cyber archer wearing a dark hooded tactical bodysuit with glowing turquoise circuitry, holding a sleek carbon-composite recurve bow powered by electromagnetic coils. Arranged in clean animation strips on a solid pure magenta `#FF00FF` background:
> - Row 1: Idle (4 frames, hovering aim stance, bow energy humming)
> - Row 2: Walk (6 frames, agile tactical sprint)
> - Row 3: Shooting attack (5 frames, drawing the bowstring, charging electric tension, and firing a bright blue plasma arrow projectile)
> - Row 4: Hurt (2 frames, staggered backward with electric sparks)
> - Row 5: Defeat (4 frames, dissolving into digital pixel static)
> Style: 16-bit retro pixel art, clean sharp pixels, side-view orthographic, flat lighting.

### [HERO-03] Teknopenyihir Matrix (AoE Technomage - 32x32 px)
* **Deskripsi:** Penyihir data berjubah sirkuit dengan tongkat pemancar gelombang elektromagnetik dan kembang api partikel kuantum.
* **Lokasi Simpan:** `assets/sprites/heroes/hero_mage.png`
* **Prompt ChatGPT:**
> Full character spritesheet for a 2D horizontal lane battle game, facing right. Character: an elite cyber technomage wearing an oversized dark violet matrix coat with glowing golden binary code runes flowing on the fabric, cybernetic eye optic, holding a staff topped with a rotating floating geometric star core. Spritesheet grid on solid pure magenta `#FF00FF` background:
> - Row 1: Idle (4 frames, hovering geometric star humming with golden sparks)
> - Row 2: Walk (6 frames, floating forward hover step with coat billowing)
> - Row 3: Spell cast attack (5 frames, raises staff overhead, releasing an explosive cluster of radiant gold starfire energy)
> - Row 4: Hurt (2 frames, optic glitches with yellow noise)
> - Row 5: Defeat (4 frames, collapses and shatters into a burst of golden polygon shards)
> Style: 16-bit arcade pixel art, crisp pixel boundaries, zero anti-aliasing.

### [HERO-04] Ksatria Kuda Cyber (Fast Cavalier - 48x48 px)
* **Deskripsi:** Ksatria tempur cepat menunggangi kuda mecha berbadan logam titanium putih dengan surai serat optik bercahaya.
* **Lokasi Simpan:** `assets/sprites/heroes/hero_pony.png`
* **Prompt ChatGPT:**
> Full character spritesheet for a 2D side-scrolling strategy game, facing right. Character: an armored cyber lancer mounted on a robotic mecha steed with white titanium plating, glowing electric-pink fiber-optic mane and exhaust thrusters, carrying a high-frequency shock lance. Spritesheet arranged on solid pure magenta `#FF00FF` background:
> - Row 1: Idle (4 frames, mechanical horse hooves adjusting, slight steam vents)
> - Row 2: Fast galloping run (6 frames, high-speed rhythmic mechanical gallop with booster trails)
> - Row 3: Lance charge attack (4 frames, thrusting the charged lance forward with an electric shockwave)
> - Row 4: Hurt (2 frames, mecha horse rearing back with sparks)
> - Row 5: Defeat (4 frames, mecha steed and rider disintegrate into a clean white and pink pixel explosion)
> Style: 16-bit retro arcade pixel art, perfectly proportioned, no blur.

### [HERO-05] Robot Titan Golem (Heavy Tanker - 64x64 px)
* **Deskripsi:** Mecha raksasa lapis baja berat dengan reaktor dada bercahaya dan tinju hidrolik penghentak tanah.
* **Lokasi Simpan:** `assets/sprites/heroes/hero_golem.png`
* **Prompt ChatGPT:**
> Full large character spritesheet for a 2D side-scrolling defense game, facing right. Character: a heavy industrial combat mech golem made of dark gunmetal and olive-green composite armor, massive hydraulic arms, a glowing amber circular reactor core in its chest, and twin exhaust smokestacks on its shoulders. Spritesheet grid on solid pure magenta `#FF00FF` background:
> - Row 1: Idle (4 frames, heavy chassis vibration, reactor pulsing, exhaust venting)
> - Row 2: Heavy walk (6 frames, powerful stomping stride shaking the ground)
> - Row 3: Ground slam attack (6 frames, raises giant mechanical fists high and slams the floor, radiating a forward cybernetic shockwave)
> - Row 4: Hurt (2 frames, armor plates rattle with electric discharge)
> - Row 5: Defeat (4 frames, reactor destabilizes and explodes into mechanical scrap parts and smoke puff)
> Style: 16-bit pixel art, chunky sharp silhouette, side view.

---

## 3. Spritesheet Monster & Boss (Enemy Entities)

Semua karakter musuh menghadap ke **kiri**.

### [MOB-01] Void Slime (32x32 px)
* **Deskripsi:** Makhluk lendir digital hitam transparan dengan inti kode virus merah menyala.
* **Lokasi Simpan:** `assets/sprites/enemies/enemy_slime.png`
* **Prompt ChatGPT:**
> Full enemy spritesheet for a 2D retro side-scroller game, facing left. Character: a digital corruption void slime blob made of dark translucent obsidian liquid with a glowing crimson red viral core pulsating inside and jagged digital glitch spikes. Spritesheet on solid pure magenta `#FF00FF` background:
> - Row 1: Idle (4 frames, fluid body compressing and stretching)
> - Row 2: Bouncing move (6 frames, fast aggressive rubbery leap forward)
> - Row 3: Spike lash attack (4 frames, morphing front body into sharp digital needles)
> - Row 4: Hurt (2 frames, splashes flat with glitch static)
> - Row 5: Defeat (4 frames, pops and evaporates into dissolving red glitch pixels)
> Style: 16-bit retro arcade pixel art, high contrast, clean outlines.

### [MOB-02] Cyber Rogue Beast / Kelinci Nakal (32x32 px)
* **Deskripsi:** Monster kelinci mutan cybernetic bertelinga panjang berpelindung baja dengan pedang gergaji mini, berlari lincah.
* **Lokasi Simpan:** `assets/sprites/enemies/enemy_bunny.png`
* **Prompt ChatGPT:**
> Full enemy spritesheet for 2D side-scrolling lane battle game, facing left. Character: a fast cybernetic mutant scout beast resembling a ferocious robotic rabbit with sleek chrome armor, glowing red bionic eyes, elongated mechanical ears that pivot, and carrying an energized high-speed carbon blade. Grid on solid pure magenta `#FF00FF` background:
> - Row 1: Idle (4 frames, ears twitching, scanning lasers from eyes)
> - Row 2: Sprint (6 frames, lightning-fast bounding run)
> - Row 3: Blade slash attack (4 frames, furious downward double slash)
> - Row 4: Hurt (2 frames, knocked back with spark bursts)
> - Row 5: Defeat (4 frames, chassis shorts out and disappears into white smoke cloud)
> Style: 16-bit retro pixel art, sharp pixel lines, flat 2D side view.

### [MOB-03] Armored Stone Drone / Batuan Bertameng (32x32 px)
* **Deskripsi:** Dron batu basal bertameng pelat baja komposit tebal penahan serangan.
* **Lokasi Simpan:** `assets/sprites/enemies/enemy_pebble.png`
* **Prompt ChatGPT:**
> Full enemy spritesheet for 2D horizontal lane defense game, facing left. Character: a floating basalt stone drone entity encased in reinforced composite alloy plates, single glowing amber cyclops sensor in center, holding a massive rectangular ballistic riot shield. Spritesheet on solid pure magenta `#FF00FF` background:
> - Row 1: Idle (4 frames, heavy hovering bob, shield humming)
> - Row 2: Advance (6 frames, steady heavy floating march pushing forward)
> - Row 3: Shield bash attack (4 frames, violently rams the heavy alloy shield forward)
> - Row 4: Hurt (2 frames, stone chips and sparks fly off armor)
> - Row 5: Defeat (4 frames, breaks apart into falling stone fragments and dissipating smoke)
> Style: 16-bit arcade pixel art, rich dark metallic and rock textures.

### [MOB-04] Heavy Cyber Croc (Mini Boss - 64x64 px)
* **Deskripsi:** Cyborg buaya raksasa dengan rahang baja hidrolik dan meriam mortir di punggungnya.
* **Lokasi Simpan:** `assets/sprites/enemies/boss_croc.png`
* **Prompt ChatGPT:**
> Full mini-boss character spritesheet for a 2D side-scrolling pixel art defense game, facing left. Character: a monstrous cybernetic crocodile brute with dark armored scales, massive motorized steel jaw with razor teeth, cybernetic tail with energy bludgeon, and a heavy mortar cannon mounted on its armored back. Spritesheet grid on solid pure magenta `#FF00FF` background:
> - Row 1: Idle (4 frames, heavy breathing, cannon steam venting, tail twitching)
> - Row 2: Lumbering walk (6 frames, menacing heavy forward crawl shaking the ground)
> - Row 3: Jaw crush attack (5 frames, rears back and violently snaps massive steel jaws shut with explosive force)
> - Row 4: Hurt (2 frames, head recoils back, armor plates flashing red)
> - Row 5: Defeat (4 frames, cannon backfires, collapsing into a large dramatic cybernetic explosion with flying metal bolts and smoke)
> Style: 16-bit pixel art, high detail, side-view orthographic.

### [MOB-05] Singularity Dragon King (Final Boss - 96x96 px)
* **Deskripsi:** Naga kosmik cybernetic ungu tua bermahkota kuantum emas dengan sayap energi plasma dan napas gelombang singularitas.
* **Lokasi Simpan:** `assets/sprites/enemies/boss_dragon.png`
* **Prompt ChatGPT:**
> Full main boss character spritesheet for a 2D side-scrolling tactical defense game, facing left. Character: a colossal dark-matter cybernetic dragon emperor with deep violet and obsidian armored scales, an ornate golden crown forged of quantum circuits hovering above its horned head, large wings made of glowing neon magenta plasma ribs, and a glowing singularity core in its chest. Spritesheet on solid pure magenta `#FF00FF` background:
> - Row 1: Idle (4 frames, massive plasma wings slowly flapping, tail swaying, crown glowing)
> - Row 2: Stomp march (6 frames, earth-shaking dominant forward strides)
> - Row 3: Singularity breath attack (6 frames, deep energy inhale charging core, unleashing three expanding rings of purple dark-energy fireballs)
> - Row 4: Hurt (2 frames, crown flickers, roaring with glitch distortions)
> - Row 5: Defeat (5 frames, wings dissolve, chest core collapses into a black hole vortex, culminating in a giant celebration fireworks confetti explosion)
> Style: 16-bit retro arcade pixel art, ultra-crisp edges, no 3D rendering.

---

## 4. Markas Benteng (Fortress Buildings)

Dimensi: Lebar 96 px, **Tinggi maksimal 112 px** (agar tidak menyentuh HUD atas pada kanvas 216 px).

### [CASTLE-01] Benteng Cyber Pemain (Player Command Bastion)
* **Lokasi Simpan:** `assets/sprites/buildings/castle_player.png`
* **Prompt ChatGPT:**
> Pixel art building sprite asset for a 2D side-scrolling tactical sci-fi game, player command fortress base, 96 pixels wide by 112 pixels tall, facing right. Constructed with dark obsidian carbon-composite walls, glowing neon cyan architectural trims, reinforced arched energy blast-door gate at the base, upper defensive radar parapet with a pulsating holographic command beacon antenna at the top. Clean 16-bit arcade pixel art style, high contrast, isolated on solid pure magenta `#FF00FF` background. Strictly 2D flat orthographic side-view.

### [CASTLE-02] Benteng Void Musuh (Enemy Void Monolith)
* **Lokasi Simpan:** `assets/sprites/buildings/castle_enemy.png`
* **Prompt ChatGPT:**
> Pixel art building sprite asset for a 2D side-scrolling tactical defense game, enemy fortress base, 96 pixels wide by 112 pixels tall, facing left. Designed as an alien dark-matter obelisk combined with industrial cybernetic battlements, jagged metal buttresses, glowing sinister crimson-red circuit conduits, fortified armored hangar door at the ground, and an emitting dark-energy transmitter sphere on the highest point. 16-bit retro pixel art, non-blurry, isolated on solid pure magenta `#FF00FF` background. Flat 2D side view.

---

## 5. Visual Effects (VFX Partikel Piksel)

### [VFX-01] Letupan Partikel Kehancuran (Data Dissolve Poof Cloud - 32x32 px)
* **Lokasi Simpan:** `assets/sprites/vfx/vfx_poof_cloud.png`
* **Prompt ChatGPT:**
> Pixel art VFX animation spritesheet of a futuristic data dissolve explosion, 5 frame horizontal sequence. A clean expanding cloud of white and cyan geometric pixel blocks and glowing electric sparks that rapidly disintegrate into fading digital static. 32x32 pixels per frame, 16-bit retro arcade video game particle effect, isolated on solid pure magenta `#FF00FF` background. No dark smoke, clean sci-fi aesthetic.

### [VFX-02] Percikan Percikan Plasma & Bintang Emas (16x16 px)
* **Lokasi Simpan:** `assets/sprites/vfx/vfx_sparks.png`
* **Prompt ChatGPT:**
> Pixel art VFX spritesheet of radiant golden and cyan plasma starburst sparks, 6 frame horizontal sequence. Tiny bright energy particles bursting outward, spinning rapidly, glowing intensely, and shrinking into sparkle dust. 16x16 pixel frame size, 16-bit video game combat hit particle, isolated on solid black background.

### [VFX-03] Hujan Meteor Api & Ledakan Kawah (Fire Rain & Impact - 32x32 px per frame)
* **Lokasi Simpan:** `assets/sprites/vfx/vfx_meteor_fire_rain.png`
* **Prompt ChatGPT:**
> Pixel art VFX spritesheet of a fiery sci-fi meteor strike and impact explosion, 6 frame horizontal sequence. Frame 1-2: diagonal descending flaming meteor rock with blazing red-orange fire trail and white-hot core. Frame 3-4: violent ground impact explosion with expanding fiery shockwave ring and scattered amber embers. Frame 5-6: dissipating flame burst and glowing smoky pixel debris. Exactly 32x32 pixels per frame, 16-bit arcade video game visual effect, isolated on solid pure magenta `#FF00FF` background. Sharp pixel borders, zero blur.

### [VFX-04] Pilar Cahaya Suci & Aura Pemulihan Hero (Regen Aura - 32x48 px per frame)
* **Lokasi Simpan:** `assets/sprites/vfx/vfx_hero_regen_aura.png`
* **Prompt ChatGPT:**
> Pixel art VFX spritesheet of a magical high-tech health regeneration aura, 6 frame horizontal sequence. A vertical column of translucent emerald-green divine light rising upwards from a glowing cybernetic rune circle on the ground, surrounded by floating golden sparkles and rising green healing plus-cross symbols (+). Exactly 32x48 pixels per frame, 16-bit retro arcade game spell effect, isolated on solid pure magenta `#FF00FF` background. Vibrant neon green and cyan glow accents, crisp pixel boundaries.

---

## 6. Antarmuka Pengguna (UI & HUD)

### [UI-01] Tabung Reaktor Mana & Bar HP Benteng
* **Lokasi Simpan:** `assets/ui/hud_mana_tube.png` & `assets/ui/hud_hp_bar.png`
* **Prompt ChatGPT:**
> A set of 2D pixel art UI game elements in cyber arcade aesthetic:
> 1. Vertical high-tech cylindrical glass energy battery tube (24x48 px), framed in dark steel and brass, filled with bubbling radiant sapphire-cyan liquid plasma with bright energy reflection stripes.
> 2. Horizontal titanium health bar frame (90x14 px) with a vibrant emerald-green neon segmented health fill strip and an accompanying glowing cybernetic shield-core icon (16x16 px).
> 16-bit pixel art, crisp sharp pixels, isolated on solid pure magenta `#FF00FF` background.

### [UI-02] Bingkai Kartu Pasukan (Deck Card - 32x32 px)
* **Lokasi Simpan:** `assets/ui/card_unit_frame.png`
* **Prompt ChatGPT:**
> Pixel art UI card icon frame for summoning units in a 2D sci-fi strategy game, 32x32 pixel square card. Featuring a beveled dark titanium frame with glowing golden cyber corners, a circular blue mana-cost badge at the top-left corner, and an inner dark hologram display window. Includes a variant showing a dark 50% opacity cooldown radial wipe overlay. 16-bit pixel art, isolated on pure magenta `#FF00FF` background.

### [UI-03] Terminal Pop-Up Kuis Matematika Taktis (260x100 px)
* **Lokasi Simpan:** `assets/ui/popup_quiz_dialog.png`
* **Prompt ChatGPT:**
> Pixel art UI popup dialog box for a tactical math calculation terminal, exactly 260x100 pixels dimensions. Futuristic dark slate terminal frame with glowing cyan corner brackets, top banner labeled 'TACTICAL CALCULATION', dark central blackboard readout screen for displaying math equations, and 4 pill-shaped answer button frames below in 4 distinct high-tech neon colors: Crimson Red (A), Sky Blue (B), Electric Amber (C), and Emerald Green (D). 16-bit retro game interface, clean sharp borders, on solid magenta `#FF00FF` background.

### [UI-04] Ikon Tombol Aksi Hujan Api (Emergency Fire Rain Skill - 40x40 px)
* **Lokasi Simpan:** `assets/ui/icon_btn_fire_rain.png`
* **Prompt ChatGPT:**
> Pixel art game UI icon of an emergency orbital fire rain meteor strike ability, 40x40 pixels square icon. An ornate circular tactical button frame made of dark titanium metal with glowing molten amber-red border rivets. Inside is a flaming meteor rock hurtling downwards with blazing orange and crimson plasma trails, surrounded by fiery solar flare sparks. 16-bit retro arcade interface style, high contrast, vivid fiery red and golden glow, isolated on solid pure magenta `#FF00FF` background.

### [UI-05] Ikon Tombol Aksi Regen Hero (Troop Healing & Regeneration - 40x40 px)
* **Lokasi Simpan:** `assets/ui/icon_btn_hero_regen.png`
* **Prompt ChatGPT:**
> Pixel art game UI icon of a troop healing and regeneration skill, 40x40 pixels square icon. An ornate circular tactical button frame made of dark obsidian metal with glowing emerald-green circuit trims. Inside is a glowing jade-green medical cross and winged heart emblem radiating upward beams of holy light and sparkling digital health motes. 16-bit retro video game UI icon, bright high-contrast green and cyan glow, isolated on solid pure magenta `#FF00FF` background.

---

## 7. Prompt Generator Musik & SFX (Suno AI / ElevenLabs)

Jika ingin membuat musik dan suara sendiri, salin prompt berikut ke **Suno AI** (untuk lagu) dan **ElevenLabs SFX** (untuk efek suara):

### Musik Latar (BGM di Suno AI / Udio)
1. **Lagu Layar Menu (`BGM_Title`):**
   > `16-bit retro synthwave chiptune, dark synth, futuristic cyber adventure, catchy FM synth melody, warm bassline, arcade title screen, 110 BPM, nostalgic SNES / Genesis sound chip, loopable`
2. **Lagu Pertempuran (`BGM_Battle_Fun`):**
   > `Fast-paced 16-bit arcade combat chiptune, driving electro-march drums, high-energy square wave arpeggios, pulsing synth bass, intense yet fun tactical lane defense battle, 134 BPM, video game soundtrack`
3. **Lagu Pertarungan Boss (`BGM_Boss_Playful`):**
   > `Epic 16-bit retro boss battle theme, dramatic fast cyber funk tempo, heavy 8-bit drum fills, aggressive synth brass stabs, adrenaline pumping, 140 BPM, loopable arcade duel`
4. **Jingle Kemenangan (`Jingle_Victory`):**
   > `Short 7-second 16-bit triumph victory fanfare, ascending bright brass chimes, sparkling arpeggio, celebratory arcade stage clear sound`

### Efek Suara (SFX di ElevenLabs Sound Effects)
* **Ayunan Laser/Pedang:** `Retro 16-bit video game laser sword whoosh swing sound effect, crisp electric slash`
* **Tembakan Proyektil:** `High-tech plasma blaster shoot plop sound, 8-bit arcade laser burst`
* **Hentakan Golem:** `Heavy mecha robot footstep thud ground slam, low frequency hydraulic impact`
* **Kuis Benar:** `Magical harmonic chime arpeggio ascending, pleasant high-pitched correct answer reward chime`
* **Kuis Salah:** `Gentle low frequency cartoon sawtooth buzz error sound, soft failure tone`
* **Hujan Api & Ledakan:** `Heavy 16-bit arcade meteor fall whistling descent followed by a deep rumbling fire explosion and sizzling flame crackle`
* **Regen Hero:** `Magical 16-bit ascending crystalline chime arpeggio with shimmering holy light resonance, uplifting health restoration sound`
