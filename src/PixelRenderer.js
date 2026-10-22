/**
 * PixelRenderer.js
 * Modul Renderer Canvas 2D Pixel-Perfect untuk canvas native 480 × 216 px.
 * Menangani latar paralaks 4-layer, unit animasi, proyektil, partikel, minimap radar,
 * serta fallback procedural pixel art jika spritesheet belum terpasang.
 */

import { LANE_CONFIG } from './LaneCombatSystem.js';

export class PixelRenderer {
  constructor(canvas, assetLoader) {
    this.canvas = canvas;
    this.ctx = canvas.getContext('2d');
    this.assetLoader = assetLoader;

    // Pastikan tidak ada anti-aliasing / interpolasi kabur
    this.ctx.imageSmoothingEnabled = false;

    this.confettiParticles = [];
    this.floatingTexts = [];
  }

  addFloatingText(text, x, y, color = '#FFD700') {
    this.floatingTexts.push({
      text,
      x,
      y,
      vy: -25,
      life: 0.8,
      maxLife: 0.8,
      color
    });
  }

  triggerVictoryConfetti() {
    this.confettiParticles = [];
    const colors = ['#FF4757', '#FFA502', '#2ED573', '#1E90FF', '#9B59B6', '#FFFFFF'];
    for (let i = 0; i < 70; i++) {
      this.confettiParticles.push({
        x: Math.random() * 480,
        y: -10 - Math.random() * 50,
        vx: (Math.random() - 0.5) * 40,
        vy: 35 + Math.random() * 45,
        w: 3 + Math.floor(Math.random() * 3),
        h: 2 + Math.floor(Math.random() * 4),
        color: colors[Math.floor(Math.random() * colors.length)],
        rot: Math.random() * Math.PI * 2,
        vRot: (Math.random() - 0.5) * 8
      });
    }
  }

  clear() {
    this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
  }

  render(combatManager, cameraX, hudState, dt) {
    this.clear();

    const trackLength = combatManager.trackLength;

    // 1. Gambar Parallax Background (4 Layers)
    this.drawParallaxBackground(cameraX, trackLength);

    // 2. Gambar Lintasan & Dekorasi Tanah (Combat Lane)
    this.drawCombatLane(cameraX, trackLength);

    // 3. Gambar Entitas (Kastel & Pasukan) Terurut Z (Depth)
    const renderList = combatManager.getSortedRenderList();
    for (const entity of renderList) {
      if (entity.isDead && entity.state !== 'DIE') continue;
      this.drawEntity(entity, cameraX);
    }

    // 4. Gambar Proyektil
    this.drawProjectiles(combatManager.projectiles, cameraX);

    // 5. Gambar Partikel VFX (Poof, Spark, Dust)
    this.drawParticles(combatManager.particles, cameraX);

    // 6. Gambar Floating Damage Texts
    this.updateAndDrawFloatingTexts(cameraX, dt);

    // 7. Gambar Confetti jika Menang
    if (hudState.isVictory) {
      this.updateAndDrawConfetti(dt);
    }

    // 8. Gambar Top HUD (Status HP, Minimap Radar, 1x/2x, Pause)
    this.drawTopHud(combatManager, cameraX, hudState);
  }

  // ==========================================
  // PARALLAX BACKGROUND
  // ==========================================
  drawParallaxBackground(cameraX, trackLength) {
    const ctx = this.ctx;
    const w = 480;
    const h = 216;

    // --- Layer 1: Skybox Cyber Grid & Nebula (Paralaks 0.1x) ---
    const skyImg = this.assetLoader.getImage('bg_sky');
    if (skyImg) {
      const scrollOffset = (cameraX * 0.1) % skyImg.width;
      for (let sx = -scrollOffset; sx < w; sx += skyImg.width) {
        ctx.drawImage(skyImg, sx, 0, skyImg.width, h);
      }
    } else {
      const skyGrad = ctx.createLinearGradient(0, 0, 0, 160);
      skyGrad.addColorStop(0, '#070a12');
      skyGrad.addColorStop(0.7, '#0b132b');
      skyGrad.addColorStop(1, '#1c2541');
      ctx.fillStyle = skyGrad;
      ctx.fillRect(0, 0, w, 160);
    }

    // --- Layer 2: Far Scenery Cyber City (Paralaks 0.3x) ---
    const farImg = this.assetLoader.getImage('bg_far');
    if (farImg) {
      const scrollOffset = (cameraX * 0.3) % farImg.width;
      for (let fx = -scrollOffset; fx < w; fx += farImg.width) {
        ctx.drawImage(farImg, fx, 0, farImg.width, h);
      }
    } else {
      ctx.fillStyle = '#1e293b';
      const hillOffset = (cameraX * 0.22) % 180;
      for (let hx = -hillOffset - 60; hx < w + 120; hx += 140) {
        ctx.beginPath();
        ctx.arc(hx, 155, 65, Math.PI, 0);
        ctx.fill();
      }
    }

    // --- Layer 3: Midground Pylons & Conduits (Paralaks 0.6x) ---
    const midImg = this.assetLoader.getImage('bg_mid');
    if (midImg) {
      const scrollOffset = (cameraX * 0.6) % midImg.width;
      for (let mx = -scrollOffset; mx < w; mx += midImg.width) {
        ctx.drawImage(midImg, mx, 0, midImg.width, h);
      }
    }
  }

  drawPixelCloud(x, y) {
    const ctx = this.ctx;
    ctx.fillStyle = '#FFFFFF';
    ctx.fillRect(x + 8, y, 20, 8);
    ctx.fillRect(x + 2, y + 4, 32, 10);
    ctx.fillRect(x, y + 8, 36, 8);
  }

  // ==========================================
  // COMBAT LANE & GROUND
  // ==========================================
  drawCombatLane(cameraX, trackLength) {
    const ctx = this.ctx;
    const w = 480;
    const groundY = LANE_CONFIG.GROUND_Y_BASE; // 144px (v4.0 standard)

    // Layer 4: Lintasan Pijakan (World-synchronized 1.0x Parallax)
    const laneImg = this.assetLoader.getImage('tile_lane');
    if (laneImg) {
      const scrollOffset = (cameraX * 1.0) % laneImg.width;
      for (let lx = -scrollOffset; lx < w; lx += laneImg.width) {
        ctx.drawImage(laneImg, lx, groundY, laneImg.width, 72);
      }
      return;
    }

    // Irisan tanah (Cross section procedural fallback)
    ctx.fillStyle = '#1e293b'; // Lapisan tanah cyber dark slate
    ctx.fillRect(0, groundY, w, 216 - groundY);

    // Permukaan tanah jalur (Lapis neon grid)
    ctx.fillStyle = '#0f172a';
    ctx.fillRect(0, groundY - 3, w, 5);
    ctx.fillStyle = '#00f2fe';
    ctx.fillRect(0, groundY - 4, w, 2);

    // Ornamen sirkuit neon & garis lintasan
    const startTile = Math.floor(cameraX / 16);
    const endTile = Math.ceil((cameraX + w) / 16);

    for (let t = startTile; t <= endTile; t++) {
      const screenX = t * 16 - cameraX;
      // Grid lintasan
      if (t % 4 === 0) {
        ctx.fillStyle = '#38bdf8';
        ctx.fillRect(screenX, groundY - 6, 2, 3);
      }
      // Titik pulse energi
      if (t % 8 === 2) {
        ctx.fillStyle = '#ffd200';
        ctx.fillRect(screenX + 2, groundY - 7, 3, 3);
      }
      // Garis data cyber di bawah tanah
      if (t % 6 === 1) {
        ctx.fillStyle = '#334155';
        ctx.fillRect(screenX + 4, groundY + 8, 8, 2);
      }
    }
  }

  // ==========================================
  // DRAW ENTITY (CASTLE & UNITS)
  // ==========================================
  drawEntity(entity, cameraX) {
    const ctx = this.ctx;
    const screenX = Math.round(entity.x - cameraX);
    const screenY = Math.round(entity.y);

    // Cek apakah entitas berada di dalam jangkauan layar
    if (screenX < -120 || screenX > 480 + 120) return;

    ctx.save();

    // Efek kilau putih/merah saat terkena pukulan
    if (entity.hitFlashTimer > 0) {
      ctx.filter = 'brightness(1.8) drop-shadow(0 0 2px red)';
    }

    if (entity.isBuilding) {
      this.drawCastle(entity, screenX, screenY);
    } else {
      this.drawUnitSprite(entity, screenX, screenY);
    }

    ctx.restore();

    // Gambar Bar HP Mini di atas kepala unit (jika darah berkurang)
    if (!entity.isBuilding && entity.hp < entity.maxHp) {
      this.drawUnitHpBar(entity, screenX, screenY);
    }
  }

  drawCastle(castle, x, y) {
    const ctx = this.ctx;
    const isPlayer = castle.team === 'player';
    const imgKey = isPlayer ? 'castle_player' : 'castle_enemy';
    const castleImg = this.assetLoader.getImage(imgKey);

    if (castleImg) {
      // Benteng 96x112 px ditaruh di atas ground line (y)
      ctx.drawImage(castleImg, x - 48, y - 112, 96, 112);
      return;
    }

    if (isPlayer) {
      // --- BENTENG CYBER PEMAIN (Tinggi maks 108px, batas atas y - 108 = 36px) ---
      // Menara utama
      ctx.fillStyle = '#0f172a';
      ctx.fillRect(x - 24, y - 72, 48, 72);
      ctx.strokeStyle = '#00f2fe';
      ctx.lineWidth = 1;
      ctx.strokeRect(x - 24, y - 72, 48, 72);

      // Gerbang energi
      ctx.fillStyle = '#1e293b';
      ctx.fillRect(x - 12, y - 26, 24, 26);
      ctx.fillStyle = '#00f2fe';
      ctx.fillRect(x - 8, y - 16, 16, 4); // Garis neon gerbang

      // Puncak menara prisma cyber
      ctx.fillStyle = '#0284c7';
      ctx.beginPath();
      ctx.moveTo(x - 26, y - 72);
      ctx.lineTo(x, y - 96);
      ctx.lineTo(x + 26, y - 72);
      ctx.fill();

      // Antena sinyal & suar energi
      ctx.fillStyle = '#38bdf8';
      ctx.fillRect(x - 1, y - 108, 2, 12);
      ctx.fillStyle = '#00f2fe';
      ctx.beginPath();
      ctx.arc(x, y - 108, 4, 0, Math.PI * 2);
      ctx.fill();

      // Inti reaktor menyala
      ctx.fillStyle = '#38bdf8';
      ctx.fillRect(x - 6, y - 56, 12, 14);
    } else {
      // --- BENTENG CYBER MUSUH (Tinggi maks 108px) ---
      // Dinding benteng gelap aksen merah
      ctx.fillStyle = '#18181b';
      ctx.fillRect(x - 26, y - 68, 52, 68);
      ctx.strokeStyle = '#f43f5e';
      ctx.lineWidth = 1;
      ctx.strokeRect(x - 26, y - 68, 52, 68);

      // Kubah energi merah
      ctx.fillStyle = '#be123c';
      ctx.beginPath();
      ctx.arc(x, y - 68, 24, Math.PI, 0);
      ctx.fill();

      // Pintu gerbang besi
      ctx.fillStyle = '#09090b';
      ctx.fillRect(x - 12, y - 26, 24, 26);
      ctx.fillStyle = '#f43f5e';
      ctx.fillRect(x - 8, y - 16, 16, 4);

      // Antena emiter musuh
      ctx.fillStyle = '#e11d48';
      ctx.fillRect(x - 1, y - 106, 2, 14);
      ctx.fillStyle = '#f43f5e';
      ctx.beginPath();
      ctx.arc(x, y - 106, 4, 0, Math.PI * 2);
      ctx.fill();
    }
  }

  drawUnitSprite(unit, x, y) {
    const ctx = this.ctx;
    const dir = unit.direction; // 1 = kanan, -1 = kiri
    const anim = Math.sin(unit.animTimer * 12);
    const bobY = unit.state === 'WALK' ? Math.abs(anim) * 2 : 0;

    // 1. Gambar menggunakan Spritesheet Karakter jika aset tersedia
    const sheet = this.assetLoader.getImage(unit.key);
    if (sheet) {
      const cellSize = unit.size || 32;
      let rowIdx = 1; // Default WALK
      let frameCount = 6;
      let fps = 8;

      if (unit.state === 'IDLE') {
        rowIdx = 0;
        frameCount = 4;
        fps = 4;
      } else if (unit.state === 'WALK') {
        rowIdx = 1;
        frameCount = 6;
        fps = 9;
      } else if (unit.state === 'ATTACK') {
        rowIdx = 2;
        frameCount = 4;
        fps = 7;
      } else if (unit.state === 'KNOCKBACK') {
        rowIdx = 3;
        frameCount = 2;
        fps = 6;
      } else if (unit.state === 'DYING') {
        rowIdx = 4;
        frameCount = 4;
        fps = 10;
      }

      const frameIdx = Math.floor(unit.animTimer * fps) % frameCount;
      const sx = frameIdx * cellSize;
      const sy = rowIdx * cellSize;

      ctx.save();
      ctx.translate(x, y - bobY);

      // Hero menghadap kanan secara default, balik jika bergerak kiri
      // Monster menghadap kiri secara default, balik jika bergerak kanan
      if (unit.team === 'player' && dir === -1) {
        ctx.scale(-1, 1);
      } else if (unit.team === 'enemy' && dir === 1) {
        ctx.scale(-1, 1);
      }

      ctx.drawImage(sheet, sx, sy, cellSize, cellSize, -cellSize / 2, -cellSize, cellSize, cellSize);
      ctx.restore();
      return;
    }

    // 2. Procedural Fallback (jika aset spritesheet belum termuat)
    ctx.save();
    ctx.translate(x, y - bobY);

    // Balik X jika menghadap kiri
    if (dir === -1) {
      ctx.scale(-1, 1);
    }

    switch (unit.key) {
      // --- PASUKAN PEMAIN ---
      case 'hero_swordsman': { // Prajurit Kayu
        // Kaki & Sepatu
        ctx.fillStyle = '#2C3E50';
        ctx.fillRect(-6, -4, 4, 4);
        ctx.fillRect(2, -4, 4, 4);
        // Tubuh zirah perak
        ctx.fillStyle = '#BDC3C7';
        ctx.fillRect(-7, -18, 14, 14);
        // Wajah chibi
        ctx.fillStyle = '#FFDBAC';
        ctx.fillRect(-5, -28, 10, 10);
        ctx.fillStyle = '#2C3E50';
        ctx.fillRect(1, -25, 2, 2); // Mata dot
        // Helm perak & bulu biru
        ctx.fillStyle = '#95A5A6';
        ctx.fillRect(-7, -31, 14, 6);
        ctx.fillStyle = '#0984E3';
        ctx.fillRect(-4, -36, 8, 6);
        // Tameng senyum
        ctx.fillStyle = '#D35400';
        ctx.fillRect(-9, -16, 5, 10);
        ctx.fillStyle = '#F39C12';
        ctx.fillRect(-8, -14, 3, 6);
        // Pedang kayu
        const swing = unit.state === 'ATTACK' ? -Math.PI / 3 : 0;
        ctx.save();
        ctx.translate(6, -12);
        ctx.rotate(swing);
        ctx.fillStyle = '#8B5A2B';
        ctx.fillRect(0, -10, 4, 12);
        ctx.fillStyle = '#D35400';
        ctx.fillRect(-2, -2, 8, 3);
        ctx.restore();
        break;
      }

      case 'hero_archer': { // Pemanah Gelembung
        // Jubah hijau & kerudung peri
        ctx.fillStyle = '#27AE60';
        ctx.fillRect(-6, -18, 12, 14);
        // Wajah
        ctx.fillStyle = '#FFDBAC';
        ctx.fillRect(-4, -26, 8, 8);
        ctx.fillStyle = '#2C3E50';
        ctx.fillRect(0, -24, 2, 2);
        // Kerudung lancip
        ctx.fillStyle = '#2ECC71';
        ctx.beginPath();
        ctx.moveTo(-6, -26);
        ctx.lineTo(4, -34);
        ctx.lineTo(6, -26);
        ctx.fill();
        // Sayap peri mungil
        ctx.fillStyle = '#E8F8F5';
        ctx.fillRect(-11, -20, 6, 8);
        // Busur ranting
        ctx.strokeStyle = '#8B5A2B';
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.arc(6, -14, 8, -Math.PI / 3, Math.PI / 3);
        ctx.stroke();
        break;
      }

      case 'hero_mage': { // Penyihir Bintang
        // Jubah ungu panjang
        ctx.fillStyle = '#6C5CE7';
        ctx.fillRect(-7, -20, 14, 20);
        ctx.fillStyle = '#F1C40F';
        ctx.fillRect(-3, -12, 6, 2); // Garis emas
        // Topi kerucut menutupi mata
        ctx.fillStyle = '#4834D4';
        ctx.beginPath();
        ctx.moveTo(-9, -20);
        ctx.lineTo(2, -37);
        ctx.lineTo(9, -20);
        ctx.fill();
        // Tongkat bintang
        ctx.fillStyle = '#8B5A2B';
        ctx.fillRect(7, -24, 3, 24);
        ctx.fillStyle = '#F1C40F';
        ctx.fillRect(6, -28, 5, 5);
        break;
      }

      case 'hero_pony': { // Ksatria Kuda Poni
        // Badan poni putih
        ctx.fillStyle = '#FFFFFF';
        ctx.fillRect(-14, -18, 28, 14);
        // 4 kaki
        ctx.fillRect(-12, -4, 4, 6);
        ctx.fillRect(-6, -4, 4, 6);
        ctx.fillRect(4, -4, 4, 6);
        ctx.fillRect(10, -4, 4, 6);
        // Surai & ekor pink pastel
        ctx.fillStyle = '#FF9FF3';
        ctx.fillRect(-18, -16, 5, 8); // Ekor
        ctx.fillRect(10, -28, 5, 12); // Surai
        // Kepala poni
        ctx.fillStyle = '#FFFFFF';
        ctx.fillRect(8, -26, 12, 10);
        ctx.fillStyle = '#2C3E50';
        ctx.fillRect(16, -24, 2, 2);
        // Ksatria cilik di atas
        ctx.fillStyle = '#E74C3C'; // Jubah merah
        ctx.fillRect(-4, -30, 8, 12);
        ctx.fillStyle = '#FFDBAC';
        ctx.fillRect(-2, -36, 6, 6);
        ctx.fillStyle = '#BDC3C7';
        ctx.fillRect(-3, -40, 8, 5); // Helm
        break;
      }

      case 'hero_golem': { // Robot Mainan Golem
        // Kaki tebal
        ctx.fillStyle = '#16A085';
        ctx.fillRect(-12, -8, 8, 8);
        ctx.fillRect(4, -8, 8, 8);
        // Tubuh kaleng hijau mint
        ctx.fillStyle = '#1ABC9C';
        ctx.fillRect(-18, -38, 36, 30);
        // Kaca perut indikator
        ctx.fillStyle = '#FFEAA7';
        ctx.fillRect(-8, -26, 16, 10);
        // Mata ramah bersinar
        ctx.fillStyle = '#FFFFFF';
        ctx.fillRect(-10, -34, 6, 6);
        ctx.fillRect(4, -34, 6, 6);
        ctx.fillStyle = '#3498DB';
        ctx.fillRect(-8, -32, 2, 2);
        ctx.fillRect(6, -32, 2, 2);
        // Kunci putar kuningan di punggung
        ctx.fillStyle = '#F39C12';
        ctx.fillRect(-24, -28, 6, 8);
        // Tangan kepalan besar
        ctx.fillStyle = '#16A085';
        ctx.fillRect(16, -28, 10, 10);
        break;
      }

      // --- MONSTER & BOSS MUSUH ---
      case 'enemy_slime': { // Slime Hijau Bouncy
        const squish = Math.sin(unit.animTimer * 10) * 3;
        ctx.fillStyle = '#2ED573';
        ctx.beginPath();
        ctx.ellipse(0, -10 + squish / 2, 12 + squish, 10 - squish, 0, 0, Math.PI * 2);
        ctx.fill();
        // Wajah imut
        ctx.fillStyle = '#FFFFFF';
        ctx.fillRect(2, -14, 3, 3);
        ctx.fillRect(7, -14, 3, 3);
        ctx.fillStyle = '#2C3E50';
        ctx.fillRect(3, -13, 2, 2);
        ctx.fillRect(8, -13, 2, 2);
        // Pipi merah merona
        ctx.fillStyle = '#FF6B81';
        ctx.fillRect(1, -9, 3, 2);
        ctx.fillRect(9, -9, 3, 2);
        break;
      }

      case 'enemy_bunny': { // Kelinci Wortel
        // Badan kelinci
        ctx.fillStyle = '#D2B48C';
        ctx.fillRect(-8, -16, 16, 14);
        ctx.fillRect(-6, -24, 12, 10); // Kepala
        // Telinga panjang
        ctx.fillStyle = '#D2B48C';
        ctx.fillRect(-4, -36, 3, 12);
        ctx.fillRect(1, -36, 3, 12);
        ctx.fillStyle = '#FF9FF3';
        ctx.fillRect(-3, -34, 1, 8);
        ctx.fillRect(2, -34, 1, 8);
        // Bandana merah
        ctx.fillStyle = '#FF4757';
        ctx.fillRect(-7, -18, 14, 4);
        // Wortel besar
        ctx.fillStyle = '#E67E22';
        ctx.fillRect(6, -16, 6, 14);
        ctx.fillStyle = '#2ECC71';
        ctx.fillRect(7, -20, 4, 4);
        break;
      }

      case 'enemy_pebble': { // Batuan Cilik
        // Tubuh batu abu-abu bulat
        ctx.fillStyle = '#7F8C8D';
        ctx.beginPath();
        ctx.arc(0, -14, 13, 0, Math.PI * 2);
        ctx.fill();
        // Mata kuning bersinar
        ctx.fillStyle = '#F1C40F';
        ctx.fillRect(1, -16, 4, 4);
        ctx.fillRect(7, -16, 4, 4);
        // Tameng kayu mini
        ctx.fillStyle = '#8B5A2B';
        ctx.fillRect(9, -16, 5, 12);
        break;
      }

      case 'boss_croc': { // Buaya Gendut Mini Boss
        // Ekor tebal
        ctx.fillStyle = '#16A085';
        ctx.fillRect(-22, -18, 12, 10);
        // Perut bulat toska
        ctx.fillStyle = '#1ABC9C';
        ctx.beginPath();
        ctx.ellipse(0, -24, 20, 22, 0, 0, Math.PI * 2);
        ctx.fill();
        // Celemek makan putih polkadot
        ctx.fillStyle = '#FFFFFF';
        ctx.fillRect(-10, -32, 20, 16);
        ctx.fillStyle = '#E74C3C';
        ctx.fillRect(-6, -26, 3, 3);
        ctx.fillRect(2, -26, 3, 3);
        // Mulut buaya kartun
        ctx.fillStyle = '#16A085';
        ctx.fillRect(8, -32, 16, 12);
        ctx.fillStyle = '#2C3E50';
        ctx.fillRect(12, -36, 4, 4);
        // Sendok raksasa perak
        ctx.fillStyle = '#BDC3C7';
        ctx.fillRect(18, -48, 4, 38);
        ctx.beginPath();
        ctx.arc(20, -50, 7, 0, Math.PI * 2);
        ctx.fill();
        break;
      }

      case 'boss_dragon': { // Raja Boneka Naga Ungu
        // Badan naga gemuk ungu
        ctx.fillStyle = '#8E44AD';
        ctx.beginPath();
        ctx.ellipse(0, -38, 30, 36, 0, 0, Math.PI * 2);
        ctx.fill();
        // Perut pastel pink
        ctx.fillStyle = '#F368E0';
        ctx.beginPath();
        ctx.ellipse(8, -34, 16, 24, 0, 0, Math.PI * 2);
        ctx.fill();
        // Sayap kelelawar kecil lucu
        ctx.fillStyle = '#5F27CD';
        ctx.fillRect(-32, -48, 14, 18);
        // Kepala naga
        ctx.fillStyle = '#8E44AD';
        ctx.fillRect(10, -60, 24, 22);
        // Mahkota emas miring
        ctx.fillStyle = '#F1C40F';
        ctx.fillRect(14, -72, 16, 12);
        ctx.fillStyle = '#E74C3C';
        ctx.fillRect(21, -68, 3, 3); // Permata
        // Mata kartun bulat
        ctx.fillStyle = '#FFFFFF';
        ctx.fillRect(18, -54, 6, 6);
        ctx.fillStyle = '#2C3E50';
        ctx.fillRect(21, -52, 3, 3);
        break;
      }

      default:
        ctx.fillStyle = '#E74C3C';
        ctx.fillRect(-8, -16, 16, 16);
        break;
    }

    ctx.restore();
  }

  drawUnitHpBar(unit, x, y) {
    const ctx = this.ctx;
    const barW = Math.max(16, unit.size * 0.7);
    const barH = 3;
    const barX = x - barW / 2;
    const barY = y - unit.size - 6;

    const hpRatio = Math.max(0, Math.min(1, unit.hp / unit.maxHp));

    ctx.fillStyle = 'rgba(0, 0, 0, 0.6)';
    ctx.fillRect(barX - 1, barY - 1, barW + 2, barH + 2);

    ctx.fillStyle = hpRatio > 0.4 ? '#2ECC71' : '#E74C3C';
    ctx.fillRect(barX, barY, Math.round(barW * hpRatio), barH);
  }

  // ==========================================
  // PROJECTILES & PARTICLES
  // ==========================================
  drawProjectiles(projectiles, cameraX) {
    const ctx = this.ctx;
    for (const p of projectiles) {
      const sx = Math.round(p.x - cameraX);
      const sy = Math.round(p.y);

      if (p.type === 'bubble') {
        ctx.fillStyle = 'rgba(72, 219, 251, 0.75)';
        ctx.beginPath();
        ctx.arc(sx, sy, 5, 0, Math.PI * 2);
        ctx.fill();
        ctx.fillStyle = '#FFFFFF';
        ctx.fillRect(sx - 2, sy - 2, 2, 2); // Highlight
      } else if (p.type === 'star') {
        ctx.fillStyle = '#FFD700';
        ctx.beginPath();
        ctx.arc(sx, sy, 4, 0, Math.PI * 2);
        ctx.fill();
        ctx.fillStyle = '#FFFFFF';
        ctx.fillRect(sx - 1, sy - 1, 2, 2);
      }
    }
  }

  drawParticles(particles, cameraX) {
    const ctx = this.ctx;
    const poofSheet = this.assetLoader.getImage('vfx_poof');
    const sparksSheet = this.assetLoader.getImage('vfx_sparks');

    for (const pt of particles) {
      const sx = Math.round(pt.x - cameraX);
      const sy = Math.round(pt.y);
      const alpha = Math.max(0, pt.life / pt.maxLife);
      const progress = 1.0 - alpha; // 0.0 -> 1.0

      // Render VFX Animasi jika sheet tersedia
      if (pt.type === 'poof' && poofSheet) {
        const frameIdx = Math.min(4, Math.floor(progress * 5));
        ctx.save();
        ctx.globalAlpha = alpha;
        ctx.drawImage(poofSheet, frameIdx * 32, 0, 32, 32, sx - 16, sy - 16, 32, 32);
        ctx.restore();
        continue;
      }

      if (pt.type === 'star' && sparksSheet) {
        const frameIdx = Math.min(6, Math.floor(progress * 7));
        ctx.save();
        ctx.globalAlpha = alpha;
        ctx.drawImage(sparksSheet, frameIdx * 16, 0, 16, 16, sx - 8, sy - 8, 16, 16);
        ctx.restore();
        continue;
      }

      ctx.save();
      ctx.globalAlpha = alpha;
      ctx.fillStyle = pt.color;

      if (pt.type === 'poof') {
        ctx.beginPath();
        ctx.arc(sx, sy, pt.size, 0, Math.PI * 2);
        ctx.fill();
      } else {
        ctx.fillRect(sx - pt.size / 2, sy - pt.size / 2, pt.size, pt.size);
      }
      ctx.restore();
    }
  }

  updateAndDrawFloatingTexts(cameraX, dt) {
    const ctx = this.ctx;
    ctx.font = 'bold 9px monospace';
    ctx.textAlign = 'center';

    for (const ft of this.floatingTexts) {
      ft.life -= dt;
      ft.y += ft.vy * dt;
      const alpha = Math.max(0, ft.life / ft.maxLife);

      ctx.save();
      ctx.globalAlpha = alpha;
      ctx.fillStyle = '#000000';
      ctx.fillText(ft.text, ft.x - cameraX + 1, ft.y + 1);
      ctx.fillStyle = ft.color;
      ctx.fillText(ft.text, ft.x - cameraX, ft.y);
      ctx.restore();
    }
    this.floatingTexts = this.floatingTexts.filter(ft => ft.life > 0);
  }

  updateAndDrawConfetti(dt) {
    const ctx = this.ctx;
    for (const c of this.confettiParticles) {
      c.x += c.vx * dt;
      c.y += c.vy * dt;
      c.rot += c.vRot * dt;

      ctx.save();
      ctx.translate(c.x, c.y);
      ctx.rotate(c.rot);
      ctx.fillStyle = c.color;
      ctx.fillRect(-c.w / 2, -c.h / 2, c.w, c.h);
      ctx.restore();

      if (c.y > 220) {
        c.y = -10;
        c.x = Math.random() * 480;
      }
    }
  }

  // ==========================================
  // TOP HUD (24 px)
  // ==========================================
  drawTopHud(combatManager, cameraX, hudState) {
    const ctx = this.ctx;
    const w = 480;

    // Background Top HUD transparan gelap lembut
    ctx.fillStyle = 'rgba(15, 20, 30, 0.7)';
    ctx.fillRect(0, 0, w, 24);
    ctx.fillStyle = 'rgba(255, 255, 255, 0.15)';
    ctx.fillRect(0, 23, w, 1);

    // 1. Status Bar HP Kastel Pemain (Kiri)
    const playerHp = combatManager.playerCastle.hp;
    const playerMaxHp = combatManager.playerCastle.maxHp;
    const pRatio = Math.max(0, playerHp / playerMaxHp);

    ctx.fillStyle = '#2ECC71';
    ctx.fillRect(40, 7, Math.round(75 * pRatio), 10);
    ctx.strokeStyle = '#FFFFFF';
    ctx.lineWidth = 1;
    ctx.strokeRect(40, 7, 75, 10);
    // Teks HP Kastel
    ctx.fillStyle = '#FFFFFF';
    ctx.font = 'bold 8px monospace';
    ctx.textAlign = 'left';
    ctx.fillText(`KITA: ${playerHp}`, 44, 15);

    // Ikon Hati Kita
    ctx.fillStyle = '#FF4757';
    ctx.beginPath();
    ctx.arc(32, 12, 5, 0, Math.PI * 2);
    ctx.fill();

    // 2. Status Bar HP Kastel Lawan (Kanan)
    const enemyHp = combatManager.enemyCastle.hp;
    const enemyMaxHp = combatManager.enemyCastle.maxHp;
    const eRatio = Math.max(0, enemyHp / enemyMaxHp);

    ctx.fillStyle = '#E74C3C';
    ctx.fillRect(w - 115, 7, Math.round(75 * eRatio), 10);
    ctx.strokeStyle = '#FFFFFF';
    ctx.lineWidth = 1;
    ctx.strokeRect(w - 115, 7, 75, 10);
    // Teks HP Lawan
    ctx.fillStyle = '#FFFFFF';
    ctx.font = 'bold 8px monospace';
    ctx.textAlign = 'left';
    ctx.fillText(`MUSUH: ${enemyHp}`, w - 110, 15);

    // 3. Minimap Radar (Tengah, X: 160 -> 320)
    const radarX = 160;
    const radarY = 8;
    const radarW = 160;
    const radarH = 8;
    const trackL = combatManager.trackLength;

    ctx.fillStyle = 'rgba(0, 0, 0, 0.5)';
    ctx.fillRect(radarX, radarY, radarW, radarH);
    ctx.strokeStyle = 'rgba(255, 255, 255, 0.4)';
    ctx.strokeRect(radarX, radarY, radarW, radarH);

    // Titik Kastel
    ctx.fillStyle = '#3498DB';
    ctx.fillRect(radarX + 1, radarY + 1, 3, 6);
    ctx.fillStyle = '#E74C3C';
    ctx.fillRect(radarX + radarW - 4, radarY + 1, 3, 6);

    // Titik Pasukan Pemain
    ctx.fillStyle = '#2ECC71';
    for (const u of combatManager.playerUnits) {
      const rx = radarX + (u.x / trackL) * radarW;
      ctx.fillRect(Math.round(rx), radarY + 2, 2, 4);
    }

    // Titik Pasukan Musuh
    ctx.fillStyle = '#FF9F43';
    for (const e of combatManager.enemyUnits) {
      const rx = radarX + (e.x / trackL) * radarW;
      ctx.fillRect(Math.round(rx), radarY + 2, 2, 4);
    }

    // Kotak Jendela Kamera di Radar
    const camBoxX = radarX + (cameraX / trackL) * radarW;
    const camBoxW = (480 / trackL) * radarW;
    ctx.strokeStyle = '#FFEAA7';
    ctx.lineWidth = 1;
    ctx.strokeRect(camBoxX, radarY - 1, camBoxW, radarH + 2);
  }
}
