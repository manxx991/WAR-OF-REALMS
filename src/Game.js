/**
 * Game.js
 * Master Controller untuk War of Realms: Pixel Lane Defense (Kids Math Edition)
 * Mengatur Game Loop, FSM Game, Deck Pasukan, Sistem Mana, Spawner Musuh Level 1–10,
 * dan Integrasi Kuis Matematika Ramah Anak.
 */

import { KidsMathQuizGenerator, QuizType } from './KidsMathQuizGenerator.js';
import { LaneCombatManager, UNIT_TYPES } from './LaneCombatSystem.js';
import { KidsCameraHelper } from './KidsCameraHelper.js';
import { PixelRenderer } from './PixelRenderer.js';
import { SoundManager } from './SoundManager.js';
import { AssetLoader } from './AssetLoader.js';

export const LEVEL_DATA = [
  {
    level: 1,
    name: 'Cyber Gate',
    topic: 'Hitung Cepat & Sains Alam',
    trackLength: 850,
    spawnInterval: 5.5,
    enemies: ['enemy_slime'],
    boss: null
  },
  {
    level: 2,
    name: 'Quantum Core',
    topic: 'Perkalian & Tata Surya',
    trackLength: 1050,
    spawnInterval: 4.8,
    enemies: ['enemy_slime', 'enemy_bunny'],
    boss: null
  },
  {
    level: 3,
    name: 'Nexus Nebula',
    topic: 'Pembagian & Geografi Dunia',
    trackLength: 1250,
    spawnInterval: 4.5,
    enemies: ['enemy_slime', 'enemy_pebble'],
    boss: null
  },
  {
    level: 4,
    name: 'Parabola Rift',
    topic: 'Geometri & Penemu Sains',
    trackLength: 1500,
    spawnInterval: 4.2,
    enemies: ['enemy_bunny', 'enemy_pebble'],
    boss: null
  },
  {
    level: 5,
    name: 'Binary Valley',
    topic: 'Pecahan & Dunia Komputer',
    trackLength: 1750,
    spawnInterval: 4.0,
    enemies: ['enemy_slime', 'enemy_pebble'],
    boss: 'boss_croc'
  },
  {
    level: 6,
    name: 'Trigon Citadel',
    topic: 'Akar Kuadrat & Tubuh Manusia',
    trackLength: 2050,
    spawnInterval: 3.8,
    enemies: ['enemy_slime', 'enemy_bunny', 'enemy_pebble'],
    boss: null
  },
  {
    level: 7,
    name: 'Matrix Horizon',
    topic: 'Pola Bilangan & Hewan Fauna',
    trackLength: 2400,
    spawnInterval: 3.5,
    enemies: ['enemy_bunny', 'enemy_pebble'],
    boss: null
  },
  {
    level: 8,
    name: 'Chrono Portal',
    topic: 'Satuan Waktu & Sejarah Nasional',
    trackLength: 2750,
    spawnInterval: 3.2,
    enemies: ['enemy_slime', 'enemy_pebble', 'boss_croc'],
    boss: null
  },
  {
    level: 9,
    name: 'Modulo Bastion',
    topic: 'Aljabar Ringan & Fakta Sains',
    trackLength: 3150,
    spawnInterval: 3.0,
    enemies: ['enemy_bunny', 'boss_croc'],
    boss: null
  },
  {
    level: 10,
    name: 'Singularity Apex',
    topic: 'Cerdas Cepat & Wawasan Dunia',
    trackLength: 3600,
    spawnInterval: 2.8,
    enemies: ['enemy_slime', 'enemy_bunny', 'enemy_pebble'],
    boss: 'boss_dragon'
  }
];

export class Game {
  constructor() {
    this.canvas = document.getElementById('gameCanvas');
    this.assetLoader = new AssetLoader();
    this.soundManager = new SoundManager();
    this.renderer = new PixelRenderer(this.canvas, this.assetLoader);

    this.currentLevel = 1;
    this.state = 'MENU'; // 'MENU' | 'BATTLE' | 'VICTORY' | 'DEFEAT'
    this.timeScale = 1.0;
    this.isPaused = false;

    // Sistem Mana
    this.mana = 60;
    this.maxMana = 200; // Standar v4.0 (cukup untuk unit heavy 150 Mana + support)
    this.manaRate = 8.0; // Mana pasif per detik

    // Kartu Pasukan di Deck Pemain
    this.deck = [
      { key: 'hero_swordsman', cooldownTimer: 0 },
      { key: 'hero_archer', cooldownTimer: 0 },
      { key: 'hero_mage', cooldownTimer: 0 },
      { key: 'hero_pony', cooldownTimer: 0 },
      { key: 'hero_golem', cooldownTimer: 0 }
    ];

    // Status Kuis Aktif
    this.activeQuiz = null;
    this.quizTimer = 0;
    this.quizType = null;
    this.healUsageCount = 0; // Maksimal 3 kali per pertempuran

    // Spawner Musuh
    this.enemySpawnTimer = 0;
    this.bossSpawned = false;
    this.battleTimer = 0;

    // Kontrol Input Kamera & Drag
    this.keysDown = new Set();
    this.isDragging = false;
    this.dragStartX = 0;
    this.dragStartScrollX = 0;

    // Sistem Level Unlock & Stars
    this.loadProgress();

    // Skill Taktis Khusus: Hujan Api (Cooldown 30s) & Regen Hero (Cooldown 25s)
    this.fireRainCooldown = 30.0;
    this.fireRainTimer = 0.0;
    this.heroRegenCooldown = 25.0;
    this.heroRegenTimer = 0.0;

    this.lastFrameTime = performance.now();
    this.initCombat();
    this.initUI();
  }

  loadProgress() {
    this.storageFallback = this.storageFallback || {};
    try {
      if (typeof window !== 'undefined' && window.localStorage) {
        const saved = parseInt(window.localStorage.getItem('war_of_realms_unlocked_level'), 10);
        this.unlockedLevel = Number.isInteger(saved) && saved >= 1 ? Math.min(10, saved) : 1;
        this.levelStars = JSON.parse(window.localStorage.getItem('war_of_realms_stars')) || {};
        return;
      }
    } catch (e) {
      // Storage sandbox fallback
    }

    // In-memory fallback
    const saved = parseInt(this.storageFallback['war_of_realms_unlocked_level'], 10);
    this.unlockedLevel = Number.isInteger(saved) && saved >= 1 ? Math.min(10, saved) : 1;
    this.levelStars = this.storageFallback['war_of_realms_stars'] || {};
  }

  saveProgress() {
    this.storageFallback = this.storageFallback || {};
    this.storageFallback['war_of_realms_unlocked_level'] = this.unlockedLevel.toString();
    this.storageFallback['war_of_realms_stars'] = { ...this.levelStars };

    try {
      if (typeof window !== 'undefined' && window.localStorage) {
        window.localStorage.setItem('war_of_realms_unlocked_level', this.unlockedLevel.toString());
        window.localStorage.setItem('war_of_realms_stars', JSON.stringify(this.levelStars));
      }
    } catch (e) {
      // Ignored safely
    }
  }

  resetProgress() {
    this.unlockedLevel = 1;
    this.levelStars = {};
    this.saveProgress();
    this.renderLevelMenu();
  }

  async init() {
    await this.assetLoader.loadAll();
    this.bindEvents();
    this.updateDeckUI();
    this.renderLevelMenu();
    requestAnimationFrame((t) => this.loop(t));
  }

  initCombat() {
    const levelInfo = LEVEL_DATA[this.currentLevel - 1] || LEVEL_DATA[0];
    this.combatManager = new LaneCombatManager(levelInfo.trackLength, (sfx) => {
      this.soundManager.playSfx(sfx);
    }, this.currentLevel);
    this.camera = new KidsCameraHelper(480, levelInfo.trackLength);
    this.enemySpawnTimer = 2.0; // Musuh pertama muncul setelah 2 detik
    this.bossSpawned = false;
    this.battleTimer = 0;
    this.healUsageCount = 0;
    this.mana = 60;
    this.timeScale = 1.0;
    this.isPaused = false;
    this.fireRainTimer = 0.0;
    this.heroRegenTimer = 0.0;
    this.updateSkillCooldownUI();
  }

  startLevel(lvl) {
    this.currentLevel = Math.max(1, Math.min(10, lvl));
    this.initCombat();
    this.state = 'BATTLE';
    this.hideOverlayModals();
    this.soundManager.startBgm('battle');
  }

  // ==========================================
  // GAME LOOP
  // ==========================================
  loop(now) {
    const rawDt = Math.min(0.1, (now - this.lastFrameTime) / 1000);
    this.lastFrameTime = now;

    if (this.state === 'BATTLE' && !this.isPaused) {
      // Efek Super Slow-Motion 0.1x saat sedang mengerjakan kuis
      const effectiveTimeScale = this.activeQuiz ? 0.1 : this.timeScale;
      const dt = rawDt * effectiveTimeScale;

      this.updateBattle(dt, rawDt);
    }

    // Render Canvas
    const hudState = {
      isVictory: this.state === 'VICTORY',
      isDefeat: this.state === 'DEFEAT'
    };
    const camX = this.camera ? this.camera.scrollX : 0;
    this.renderer.render(this.combatManager, camX, hudState, rawDt);

    requestAnimationFrame((t) => this.loop(t));
  }

  updateBattle(dt, rawDt) {
    this.battleTimer += dt;

    // 1. Regenerasi Mana Pasif
    if (this.mana < this.maxMana) {
      this.mana = Math.min(this.maxMana, this.mana + this.manaRate * dt);
    }
    this.updateManaDisplay();

    // 2. Update Cooldown Kartu Deck
    for (const card of this.deck) {
      if (card.cooldownTimer > 0) {
        card.cooldownTimer -= dt;
      }
    }
    this.updateDeckUI();

    // Update Cooldown Skill Taktis (Hujan Api & Regen Hero)
    if (this.fireRainTimer > 0) {
      this.fireRainTimer = Math.max(0, this.fireRainTimer - dt);
    }
    if (this.heroRegenTimer > 0) {
      this.heroRegenTimer = Math.max(0, this.heroRegenTimer - dt);
    }
    this.updateSkillCooldownUI();

    // 3. Spawner Pasukan Musuh
    this.updateEnemySpawner(dt);

    // 4. Update Logika Tempur 1D
    this.combatManager.update(dt);

    // Kontrol Geser Kamera Manual via Tombol Panah / A / D saat kuis tidak aktif
    if (!this.activeQuiz && !this.isDragging) {
      if (this.keysDown.has('ArrowLeft') || this.keysDown.has('a') || this.keysDown.has('A')) {
        this.camera.panBy(-320 * dt);
      }
      if (this.keysDown.has('ArrowRight') || this.keysDown.has('d') || this.keysDown.has('D')) {
        this.camera.panBy(320 * dt);
      }
    }

    // 5. Update Kamera Auto-Follow (Smart Combat Clash Focus)
    this.camera.update(dt, this.combatManager);

    // 6. Update Timer Kuis (Menggunakan rawDt agar waktu kuis tetap adil dan santai)
    if (this.activeQuiz) {
      this.quizTimer -= rawDt;
      this.updateQuizTimerBar();
      if (this.quizTimer <= 0) {
        this.handleQuizTimeout();
      }
    }

    // 7. Evaluasi Kemenangan / Kekalahan
    if (this.combatManager.enemyCastle.hp <= 0 && this.state !== 'VICTORY') {
      this.handleVictory();
    } else if (this.combatManager.playerCastle.hp <= 0 && this.state !== 'DEFEAT') {
      this.handleDefeat();
    }
  }

  updateEnemySpawner(dt) {
    const levelInfo = LEVEL_DATA[this.currentLevel - 1];
    this.enemySpawnTimer -= dt;

    if (this.enemySpawnTimer <= 0) {
      const enemyPool = levelInfo.enemies;
      const randomEnemy = enemyPool[Math.floor(Math.random() * enemyPool.length)];
      this.combatManager.spawnUnit(randomEnemy, 'enemy');
      this.enemySpawnTimer = levelInfo.spawnInterval * (0.85 + Math.random() * 0.3);
    }

    // Spawn Boss jika ada dan waktu battle > 25s
    if (levelInfo.boss && !this.bossSpawned && this.battleTimer > 25) {
      this.bossSpawned = true;
      this.combatManager.spawnUnit(levelInfo.boss, 'enemy');
      this.renderer.addFloatingText('⚠️ BOSS MUNCUL! ⚠️', this.combatManager.trackLength - 80, 100, '#FF4757');
      this.soundManager.startBgm('boss');
    }
  }

  // ==========================================
  // SUMMON PASUKAN PEMAIN
  // ==========================================
  summonUnit(index) {
    if (this.state !== 'BATTLE' || this.isPaused) return;
    const card = this.deck[index];
    if (!card) return;

    const unitDef = UNIT_TYPES[card.key];
    if (this.mana >= unitDef.cost && card.cooldownTimer <= 0) {
      this.mana -= unitDef.cost;
      card.cooldownTimer = unitDef.cooldown;

      const spawned = this.combatManager.spawnUnit(card.key, 'player');
      this.soundManager.playSfx(unitDef.sfx);
      this.renderer.addFloatingText(`-${unitDef.cost}`, spawned.x, spawned.y - 30, '#54A0FF');
      this.updateDeckUI();
      this.updateManaDisplay();
    }
  }

  // ==========================================
  // SISTEM KUIS MATEMATIKA RAMAH ANAK
  // ==========================================
  openQuiz(type) {
    if (this.activeQuiz || this.state !== 'BATTLE') return;

    if (type === QuizType.FORTIFY && this.healUsageCount >= 3) {
      this.renderer.addFloatingText('Batas Obati Base Habis!', 60, 120, '#FFA502');
      return;
    }

    this.soundManager.resume();
    this.quizType = type;
    const q = KidsMathQuizGenerator.generateQuestion(this.currentLevel, type);
    this.activeQuiz = q;
    this.quizTimer = q.timeLimit;

    this.showQuizModal(q);
  }

  submitAnswer(choiceIndex) {
    if (!this.activeQuiz) return;

    const modal = document.getElementById('quizModal');
    const isCorrect = choiceIndex === this.activeQuiz.correctIndex;
    const buttons = document.querySelectorAll('.quiz-opt-btn');

    if (buttons && buttons[choiceIndex]) {
      buttons[choiceIndex].classList.add(isCorrect ? 'btn-opt-correct' : 'btn-opt-wrong');
    }

    if (isCorrect) {
      this.soundManager.playSfx('quiz_correct');

      if (this.quizType === QuizType.MANA) {
        const bonusMana = 40 + this.currentLevel * 5;
        this.mana = Math.min(this.maxMana, this.mana + bonusMana);
        this.renderer.addFloatingText(`+${bonusMana} BINTANG MANA! ⭐`, 120, 120, '#FFD700');
      } else if (this.quizType === QuizType.FORTIFY) {
        this.healUsageCount++;
        const healAmt = Math.round(this.combatManager.playerCastle.maxHp * 0.25);
        this.combatManager.playerCastle.hp = Math.min(
          this.combatManager.playerCastle.maxHp,
          this.combatManager.playerCastle.hp + healAmt
        );
        this.renderer.addFloatingText(`+${healAmt} HP BASE TEROBATI! ❤️`, 60, 100, '#2ED573');
      }

      setTimeout(() => {
        this.closeQuizModal();
      }, 250);
    } else {
      // Tampilkan koreksi taktis: sorot jawaban yang benar
      if (buttons && buttons[this.activeQuiz.correctIndex]) {
        buttons[this.activeQuiz.correctIndex].classList.add('btn-opt-correct');
      }
      this.soundManager.playSfx('quiz_wrong');
      const dialog = document.getElementById('quizDialog');
      dialog.classList.add('shake-wrong');
      setTimeout(() => {
        dialog.classList.remove('shake-wrong');
        this.closeQuizModal();
      }, 700);
    }
  }

  handleQuizTimeout() {
    this.soundManager.playSfx('quiz_wrong');
    this.closeQuizModal();
  }

  closeQuizModal() {
    this.activeQuiz = null;
    const modal = document.getElementById('quizModal');
    if (modal) modal.style.display = 'none';
  }

  // ==========================================
  // HASIL PERTEMPURAN (VICTORY / DEFEAT)
  // ==========================================
  handleVictory() {
    this.state = 'VICTORY';
    this.soundManager.playVictoryJingle();
    this.renderer.triggerVictoryConfetti();

    // Hitung perolehan bintang berdasarkan sisa HP kastel
    const castle = this.combatManager.playerCastle;
    const hpRatio = castle.hp / castle.maxHp;
    const stars = hpRatio >= 0.7 ? 3 : (hpRatio >= 0.35 ? 2 : 1);

    // Simpan bintang terbaik untuk level ini
    const prevStars = this.levelStars[this.currentLevel] || 0;
    this.levelStars[this.currentLevel] = Math.max(prevStars, stars);

    // Buka level berikutnya jika belum terbuka
    let newUnlocked = false;
    if (this.currentLevel >= this.unlockedLevel && this.currentLevel < 10) {
      this.unlockedLevel = this.currentLevel + 1;
      newUnlocked = true;
    }
    this.saveProgress();

    setTimeout(() => {
      const victoryModal = document.getElementById('victoryModal');
      const starRating = document.getElementById('victoryStars');
      const victoryMsg = document.getElementById('victoryMessage');
      const btnNext = document.getElementById('btnNextLevel');

      starRating.textContent = '⭐'.repeat(stars) + '☆'.repeat(3 - stars);

      if (this.currentLevel < 10) {
        btnNext.style.display = 'inline-block';
        btnNext.textContent = `Level ${this.currentLevel + 1} ➔`;
        if (victoryMsg) {
          victoryMsg.innerHTML = `Kastel lawan berhasil kamu taklukkan!<br><span style="color:#2ECC71; font-weight:700;">Level ${this.currentLevel + 1} Terbuka! 🔓</span>`;
        }
      } else {
        btnNext.style.display = 'none';
        if (victoryMsg) {
          victoryMsg.innerHTML = `🏆 <strong>LUAR BIASA!</strong> Kamu telah menyelesaikan seluruh 10 Level Petualangan! 🏆`;
        }
      }

      victoryModal.style.display = 'flex';
    }, 1200);
  }

  handleDefeat() {
    this.state = 'DEFEAT';
    this.soundManager.stopBgm();
    this.soundManager.playSfx('quiz_wrong');

    setTimeout(() => {
      const defeatModal = document.getElementById('defeatModal');
      defeatModal.style.display = 'flex';
    }, 1000);
  }

  // ==========================================
  // EVENT LISTENER & DOM INTEGRATION
  // ==========================================
  initUI() {
    this.manaBar = document.getElementById('manaFill');
    this.manaText = document.getElementById('manaText');
    this.deckContainer = document.getElementById('deckContainer');
  }

  updateManaDisplay() {
    if (this.manaBar && this.manaText) {
      const pct = Math.floor((this.mana / this.maxMana) * 100);
      this.manaBar.style.width = `${pct}%`;
      this.manaText.textContent = `${Math.floor(this.mana)} / ${this.maxMana}`;
    }
  }

  updateDeckUI() {
    const buttons = document.querySelectorAll('.card-btn');
    buttons.forEach((btn, idx) => {
      const card = this.deck[idx];
      if (!card) return;
      const unitDef = UNIT_TYPES[card.key];
      const cdOverlay = btn.querySelector('.cd-overlay');

      const isAffordable = this.mana >= unitDef.cost;
      const isCooldown = card.cooldownTimer > 0;

      if (!isAffordable || isCooldown) {
        btn.classList.add('disabled');
      } else {
        btn.classList.remove('disabled');
      }

      if (cdOverlay) {
        if (isCooldown) {
          const ratio = card.cooldownTimer / unitDef.cooldown;
          cdOverlay.style.height = `${Math.round(ratio * 100)}%`;
        } else {
          cdOverlay.style.height = '0%';
        }
      }
    });
  }

  updateSkillCooldownUI() {
    // 1. Skill Hujan Api (Kiri)
    const btnFire = document.getElementById('btnFireRain');
    const overlayFire = document.getElementById('fireRainCdOverlay');
    const textFire = document.getElementById('fireRainCdText');
    if (btnFire && overlayFire && textFire) {
      if (this.fireRainTimer > 0) {
        btnFire.classList.add('is-cooldown');
        const ratio = this.fireRainTimer / this.fireRainCooldown;
        overlayFire.style.height = `${Math.round(ratio * 100)}%`;
        textFire.textContent = `${Math.ceil(this.fireRainTimer)}s`;
      } else {
        btnFire.classList.remove('is-cooldown');
        overlayFire.style.height = '0%';
        textFire.textContent = '';
      }

      // Deteksi krisis: jika hero kalah/gugur semua saat musuh sedang berkerumun
      if (this.combatManager) {
        const livingHeroes = this.combatManager.playerUnits.filter(u => u.isAlive && u.state !== 'DYING');
        const livingEnemies = this.combatManager.enemyUnits.filter(e => e.isAlive && e.state !== 'DYING');
        const isCrisis = livingHeroes.length === 0 && livingEnemies.length > 0 && this.fireRainTimer <= 0;
        btnFire.classList.toggle('hero-crisis', isCrisis);
      }
    }

    // 2. Skill Regen Hero (Kanan)
    const btnRegen = document.getElementById('btnHeroRegen');
    const overlayRegen = document.getElementById('heroRegenCdOverlay');
    const textRegen = document.getElementById('heroRegenCdText');
    if (btnRegen && overlayRegen && textRegen) {
      if (this.heroRegenTimer > 0) {
        btnRegen.classList.add('is-cooldown');
        const ratio = this.heroRegenTimer / this.heroRegenCooldown;
        overlayRegen.style.height = `${Math.round(ratio * 100)}%`;
        textRegen.textContent = `${Math.ceil(this.heroRegenTimer)}s`;
      } else {
        btnRegen.classList.remove('is-cooldown');
        overlayRegen.style.height = '0%';
        textRegen.textContent = '';
      }
    }
  }

  triggerFireRain() {
    if (this.state !== 'BATTLE') return;
    const camX = this.camera ? this.camera.scrollX : 0;
    if (this.fireRainTimer > 0) {
      this.renderer.addFloatingText(`Hujan Api Cooldown: ${Math.ceil(this.fireRainTimer)}s`, camX + 140, 90, '#FFA502');
      return;
    }

    this.fireRainTimer = this.fireRainCooldown;
    this.soundManager.playSfx('fire_rain');
    this.renderer.triggerScreenShake(0.7, 5);
    this.renderer.triggerFireRainVfx(this.combatManager, camX);

    // Hanguskan seluruh musuh di medan tempur
    let hitCount = 0;
    for (const enemy of this.combatManager.enemyUnits) {
      if (!enemy.isAlive || enemy.state === 'DYING') continue;
      enemy.takeDamage(320);
      this.renderer.addFloatingText('-320 🔥', enemy.x, enemy.y - 32, '#FF4757');
      hitCount++;
    }

    this.renderer.addFloatingText('🔥 HUJAN API DILUNCURKAN! 🔥', camX + 240, 50, '#FF4757');
    this.updateSkillCooldownUI();
  }

  triggerHeroRegen() {
    if (this.state !== 'BATTLE') return;
    const camX = this.camera ? this.camera.scrollX : 0;
    if (this.heroRegenTimer > 0) {
      this.renderer.addFloatingText(`Regen Hero Cooldown: ${Math.ceil(this.heroRegenTimer)}s`, camX + 340, 90, '#FFA502');
      return;
    }

    this.heroRegenTimer = this.heroRegenCooldown;
    this.soundManager.playSfx('hero_regen');
    this.renderer.triggerHeroRegenVfx(this.combatManager.playerUnits);

    let healedCount = 0;
    for (const hero of this.combatManager.playerUnits) {
      if (!hero.isAlive || hero.state === 'DYING') continue;
      const healAmount = Math.round(hero.maxHp * 0.5) + 60;
      hero.hp = Math.min(hero.maxHp, hero.hp + healAmount);
      this.renderer.addFloatingText(`+${healAmount} HP 💚`, hero.x, hero.y - 32, '#10B981');
      healedCount++;
    }

    if (healedCount > 0) {
      this.renderer.addFloatingText(`💚 +REGEN ${healedCount} HERO DIPULIHKAN! 💚`, camX + 240, 50, '#10B981');
    } else {
      this.renderer.addFloatingText('💚 REGEN HERO DIAKTIFKAN! 💚', camX + 240, 50, '#10B981');
    }
    this.updateSkillCooldownUI();
  }

  showQuizModal(q) {
    const modal = document.getElementById('quizModal');
    const questionText = document.getElementById('quizQuestionText');
    const topicBadge = document.getElementById('quizTopicBadge');
    const optionsContainer = document.getElementById('quizOptions');

    if (topicBadge) {
      topicBadge.textContent = `⚡ TOPIK: ${q.topic.toUpperCase()} ⚡`;
    }
    questionText.textContent = q.questionText;
    optionsContainer.innerHTML = '';

    const colors = ['btn-cyber-red', 'btn-cyber-blue', 'btn-cyber-yellow', 'btn-cyber-green'];
    const keys = ['A', 'B', 'C', 'D'];

    q.options.forEach((opt, idx) => {
      const btn = document.createElement('button');
      btn.className = `quiz-opt-btn ${colors[idx % colors.length]} opt-${keys[idx].toLowerCase()}`;
      btn.innerHTML = `<span class="opt-key-badge">${keys[idx]}</span> <span class="opt-val-text">${opt}</span>`;
      btn.onclick = () => this.submitAnswer(idx);
      optionsContainer.appendChild(btn);
    });

    modal.style.display = 'flex';
  }

  updateQuizTimerBar() {
    const timerFill = document.getElementById('quizTimerFill');
    if (timerFill && this.activeQuiz) {
      const pct = Math.max(0, (this.quizTimer / this.activeQuiz.timeLimit) * 100);
      timerFill.style.width = `${pct}%`;
    }
  }

  hideOverlayModals() {
    document.getElementById('menuModal').style.display = 'none';
    document.getElementById('quizModal').style.display = 'none';
    document.getElementById('victoryModal').style.display = 'none';
    document.getElementById('defeatModal').style.display = 'none';
    document.getElementById('pauseModal').style.display = 'none';
  }

  renderLevelMenu() {
    const list = document.getElementById('levelList');
    if (!list) return;
    list.innerHTML = '';

    const totalStars = Object.values(this.levelStars).reduce((a, b) => a + b, 0);
    const rankBadge = document.getElementById('playerRankBadge');
    const statsText = document.getElementById('playerStatsText');

    let rankTitle = 'Kadet Cerdas (Level 1)';
    if (totalStars >= 27) rankTitle = 'Grandmaster Singularity & Wawasan Dunia';
    else if (totalStars >= 20) rankTitle = 'Komandan Taktis & Wawasan Global';
    else if (totalStars >= 13) rankTitle = 'Perwira Logika & Sains Nusantara';
    else if (totalStars >= 6) rankTitle = 'Penjelajah Cerdas & Pengetahuan Alam';

    if (rankBadge) rankBadge.textContent = rankTitle;
    if (statsText) {
      statsText.innerHTML = `⭐ <strong>${totalStars}/30</strong> Bintang &nbsp;•&nbsp; 🔓 Sektor: <strong>${this.unlockedLevel}/10</strong>`;
    }

    LEVEL_DATA.forEach(lvl => {
      const btn = document.createElement('button');
      const isUnlocked = lvl.level <= this.unlockedLevel;
      const stars = this.levelStars[lvl.level];
      const starText = stars ? '⭐'.repeat(stars) : (isUnlocked ? '☆☆☆' : '🔒');

      if (isUnlocked) {
        btn.className = 'level-select-btn unlocked';
        btn.innerHTML = `
          <div class="lvl-badge">SEKTOR ${lvl.level}</div>
          <div class="lvl-title">${lvl.name}</div>
          <div class="lvl-topic-tag">${lvl.topic}</div>
          <div class="level-stars">${starText}</div>
        `;
        btn.onclick = () => this.startLevel(lvl.level);
      } else {
        btn.className = 'level-select-btn locked';
        btn.disabled = true;
        btn.innerHTML = `
          <div class="lvl-badge locked-badge">🔒 SEKTOR ${lvl.level}</div>
          <div class="lvl-title">Terkunci</div>
          <div class="lvl-topic-tag locked">${lvl.topic}</div>
          <div class="level-stars-locked">Tuntaskan Sektor ${lvl.level - 1}</div>
        `;
      }

      list.appendChild(btn);
    });
  }

  bindEvents() {
    // Tombol Deck
    const buttons = document.querySelectorAll('.card-btn');
    buttons.forEach((btn, idx) => {
      btn.addEventListener('click', () => this.summonUnit(idx));
    });

    // Tombol Skill Taktis Baru: Hujan Api [F] & Regen Hero [R]
    const btnFireRain = document.getElementById('btnFireRain');
    if (btnFireRain) {
      btnFireRain.addEventListener('click', () => this.triggerFireRain());
    }

    const btnHeroRegen = document.getElementById('btnHeroRegen');
    if (btnHeroRegen) {
      btnHeroRegen.addEventListener('click', () => this.triggerHeroRegen());
    }

    // Tombol Kuis Mana & Heal Base
    document.getElementById('btnManaQuiz').addEventListener('click', () => {
      this.openQuiz(QuizType.MANA);
    });

    document.getElementById('btnHealBase').addEventListener('click', () => {
      this.openQuiz(QuizType.FORTIFY);
    });

    // Tombol Pause & Speed
    const updatePauseUI = () => {
      const btn = document.getElementById('btnPause');
      if (btn) {
        btn.classList.toggle('is-paused', this.isPaused);
        const iconSpan = btn.querySelector('.hud-btn-icon');
        const textSpan = btn.querySelector('.hud-btn-text');
        if (iconSpan) iconSpan.textContent = this.isPaused ? '▶' : '⏸';
        if (textSpan) textSpan.textContent = this.isPaused ? 'LANJUT' : 'JEDA';
      }
      document.getElementById('pauseModal').style.display = this.isPaused ? 'flex' : 'none';
    };

    const updateSpeedUI = () => {
      const btn = document.getElementById('btnSpeed');
      if (btn) {
        const isFast = this.timeScale > 1.0;
        btn.classList.toggle('speed-2x', isFast);
        const textSpan = btn.querySelector('.hud-btn-text');
        if (textSpan) textSpan.textContent = `${this.timeScale}x`;
      }
    };

    document.getElementById('btnPause').addEventListener('click', () => {
      this.isPaused = !this.isPaused;
      updatePauseUI();
    });

    document.getElementById('btnResume').addEventListener('click', () => {
      this.isPaused = false;
      updatePauseUI();
    });

    document.getElementById('btnSpeed').addEventListener('click', () => {
      this.timeScale = this.timeScale === 1.0 ? 2.0 : 1.0;
      updateSpeedUI();
    });

    // Tombol Toggle Suara (Mute / Unmute)
    const btnSound = document.getElementById('btnSound');
    const updateSoundUI = () => {
      if (btnSound) {
        btnSound.classList.toggle('is-muted', this.soundManager.muted);
        const iconSpan = btnSound.querySelector('.hud-btn-icon');
        const textSpan = btnSound.querySelector('.hud-btn-text');
        if (iconSpan) iconSpan.textContent = this.soundManager.muted ? '🔇' : '🔊';
        if (textSpan) textSpan.textContent = this.soundManager.muted ? 'BUNGKAM' : 'SUARA';
      }
    };
    if (btnSound) {
      btnSound.addEventListener('click', () => {
        this.soundManager.toggleMute();
        updateSoundUI();
      });
    }

    // Audio Unlock pada interaksi pertama pemain (Browser Autoplay Policy)
    const unlockAudio = () => {
      this.soundManager.init();
      this.soundManager.resume();
      if (this.state === 'MENU' && !this.soundManager.bgmPlaying) {
        this.soundManager.startBgm('title');
      }
      window.removeEventListener('pointerdown', unlockAudio);
      window.removeEventListener('keydown', unlockAudio);
    };
    window.addEventListener('pointerdown', unlockAudio, { once: true });
    window.addEventListener('keydown', unlockAudio, { once: true });

    // Tombol Menu & Navigasi
    document.getElementById('btnNextLevel').addEventListener('click', () => {
      if (this.currentLevel < 10) {
        this.startLevel(this.currentLevel + 1);
      } else {
        this.state = 'MENU';
        document.getElementById('victoryModal').style.display = 'none';
        document.getElementById('menuModal').style.display = 'flex';
        this.renderLevelMenu();
      }
    });

    document.getElementById('btnRetry').addEventListener('click', () => {
      this.startLevel(this.currentLevel);
    });

    document.getElementById('btnBackToMenu').addEventListener('click', () => {
      this.state = 'MENU';
      document.getElementById('victoryModal').style.display = 'none';
      document.getElementById('menuModal').style.display = 'flex';
      this.renderLevelMenu();
      this.soundManager.startBgm('title');
    });

    document.getElementById('btnDefeatRetry').addEventListener('click', () => {
      this.startLevel(this.currentLevel);
    });

    const btnDefeatMenu = document.getElementById('btnDefeatMenu');
    if (btnDefeatMenu) {
      btnDefeatMenu.addEventListener('click', () => {
        this.state = 'MENU';
        document.getElementById('defeatModal').style.display = 'none';
        document.getElementById('menuModal').style.display = 'flex';
        this.renderLevelMenu();
        this.soundManager.startBgm('title');
      });
    }

    const btnPauseRestart = document.getElementById('btnPauseRestart');
    if (btnPauseRestart) {
      btnPauseRestart.addEventListener('click', () => {
        this.isPaused = false;
        document.getElementById('pauseModal').style.display = 'none';
        this.startLevel(this.currentLevel);
      });
    }

    const btnPauseMenu = document.getElementById('btnPauseMenu');
    if (btnPauseMenu) {
      btnPauseMenu.addEventListener('click', () => {
        this.isPaused = false;
        this.state = 'MENU';
        document.getElementById('pauseModal').style.display = 'none';
        document.getElementById('menuModal').style.display = 'flex';
        this.renderLevelMenu();
        this.soundManager.startBgm('title');
      });
    }

    const btnReset = document.getElementById('btnResetProgress');
    if (btnReset) {
      btnReset.addEventListener('click', () => {
        if (confirm('Ulangi petualangan dari Sektor 1? Seluruh bintang akan di-reset.')) {
          this.resetProgress();
        }
      });
    }

    // ==========================================
    // KONTROL GESER KAMERA (DRAG, SENTUH, RADAR & WHEEL)
    // ==========================================
    const getCanvasInternalCoords = (e) => {
      const rect = this.canvas.getBoundingClientRect();
      const scaleX = 480 / rect.width;
      const scaleY = 216 / rect.height;
      return {
        x: (e.clientX - rect.left) * scaleX,
        y: (e.clientY - rect.top) * scaleY,
        scaleX
      };
    };

    this.canvas.addEventListener('pointerdown', (e) => {
      if (this.state !== 'BATTLE' || !this.camera) return;

      const { x: internalX, y: internalY } = getCanvasInternalCoords(e);

      // Cek apakah pemain mengklik area Radar Minimap di bagian atas (X: 155-325, Y: 1-28)
      if (internalY >= 1 && internalY <= 28 && internalX >= 155 && internalX <= 325) {
        const ratio = Math.max(0, Math.min(1, (internalX - 160) / 160));
        const targetWorldX = ratio * this.combatManager.trackLength;
        this.camera.panTo(targetWorldX - 240);
        this.isRadarDragging = true;
        try {
          this.canvas.setPointerCapture(e.pointerId);
        } catch (_) {}
        return;
      }

      this.isDragging = true;
      this.dragStartX = e.clientX;
      this.dragStartScrollX = this.camera.scrollX;
      this.camera.setDragging(true);
      this.canvas.classList.add('dragging');
      try {
        this.canvas.setPointerCapture(e.pointerId);
      } catch (_) {}
    });

    this.canvas.addEventListener('pointermove', (e) => {
      if (!this.camera) return;

      if (this.isRadarDragging) {
        const { x: internalX } = getCanvasInternalCoords(e);
        const ratio = Math.max(0, Math.min(1, (internalX - 160) / 160));
        const targetWorldX = ratio * this.combatManager.trackLength;
        this.camera.panTo(targetWorldX - 240);
        return;
      }

      if (!this.isDragging) return;
      const rect = this.canvas.getBoundingClientRect();
      const scaleX = 480 / rect.width;
      const dx = (this.dragStartX - e.clientX) * scaleX;
      this.camera.scrollX = Math.min(Math.max(this.dragStartScrollX + dx, 0), this.camera.maxScroll);
      this.camera.holdTimer = 2.5;
    });

    const endDrag = (e) => {
      this.isRadarDragging = false;
      if (this.isDragging && this.camera) {
        this.isDragging = false;
        this.camera.setDragging(false);
        this.camera.holdTimer = 2.5;
        this.canvas.classList.remove('dragging');
        try {
          if (e && e.pointerId) this.canvas.releasePointerCapture(e.pointerId);
        } catch (_) {}
      }
    };

    this.canvas.addEventListener('pointerup', endDrag);
    this.canvas.addEventListener('pointercancel', endDrag);

    // Mouse Wheel Scroll horizontal / vertikal untuk geser medan tempur
    this.canvas.addEventListener('wheel', (e) => {
      if (this.state !== 'BATTLE' || !this.camera) return;
      e.preventDefault();
      const delta = Math.abs(e.deltaX) > Math.abs(e.deltaY) ? e.deltaX : e.deltaY;
      const rect = this.canvas.getBoundingClientRect();
      const scaleX = 480 / rect.width;
      this.camera.panBy(delta * scaleX * 0.8);
    }, { passive: false });

    // Keyboard Shortcuts Cepat untuk Siswa & Mahasiswa
    window.addEventListener('keydown', (e) => {
      this.keysDown.add(e.key);

      // Hotkey respons kuis kilat: A, B, C, D atau 1, 2, 3, 4
      if (this.activeQuiz) {
        const key = e.key.toUpperCase();
        if (key === 'A' || key === '1') { this.submitAnswer(0); return; }
        if (key === 'B' || key === '2') { this.submitAnswer(1); return; }
        if (key === 'C' || key === '3') { this.submitAnswer(2); return; }
        if (key === 'D' || key === '4') { this.submitAnswer(3); return; }
        return;
      }

      // Mencegah scroll default browser jika menekan tombol panah
      if (e.key === 'ArrowLeft' || e.key === 'ArrowRight' || e.key === 'ArrowUp' || e.key === 'ArrowDown') {
        e.preventDefault();
      }

      if (e.key >= '1' && e.key <= '5') {
        this.summonUnit(parseInt(e.key) - 1);
      } else if (e.key === 'q' || e.key === 'Q') {
        this.openQuiz(QuizType.MANA);
      } else if (e.key === 'e' || e.key === 'E') {
        this.openQuiz(QuizType.FORTIFY);
      } else if (e.key === 'f' || e.key === 'F') {
        this.triggerFireRain();
      } else if (e.key === 'r' || e.key === 'R') {
        this.triggerHeroRegen();
      } else if (e.key === ' ') {
        this.isPaused = !this.isPaused;
        updatePauseUI();
      }
    });

    window.addEventListener('keyup', (e) => {
      this.keysDown.delete(e.key);
    });

    window.addEventListener('blur', () => {
      this.keysDown.clear();
      endDrag();
    });
  }
}

// Inisialisasi Game saat DOM siap
window.addEventListener('DOMContentLoaded', () => {
  const game = new Game();
  window.__game = game;
  game.init();
});
