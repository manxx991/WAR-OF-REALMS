/**
 * LaneCombatSystem.js
 * Modul pergerakan 1D, State Machine, dan Sistem Tempur Game Lane Defense Pixel Art.
 * Didesain untuk canvas native 480 x 216 px.
 * Sesuai spesifikasi PRD Bab 2, 3, 5, dan 8.2
 */

export const LANE_CONFIG = {
  GROUND_Y_BASE: 144,       // Garis tengah kaki unit (v4.0 standard: di dalam combat lane 24-160)
  DEPTH_OFFSET_MAX: 4,      // Pseudo-depth Y jitter: 140px - 148px (tidak menembus deck)
  BOUNDS_MIN_X: 56,         // Titik X Kastel Pemain (pusat kastel lebar 96)
  CASTLE_WIDTH: 96,         // Lebar kastel
  CASTLE_HALF_WIDTH: 48,    // Setengah lebar untuk hitungan celah tepi-ke-tepi
  MAX_UNITS_PER_TEAM: 12,   // Batas unit aktif per tim
  DEFAULT_TRACK_LENGTH: 850 // Panjang lintasan default Sektor 1
};

export const UNIT_TYPES = {
  // --- KANDIDAT PASUKAN PEMAIN ---
  hero_swordsman: {
    key: 'hero_swordsman',
    name: 'Prajurit Cyber',
    cost: 20,
    cooldown: 2.5,
    hp: 130,
    damage: 16,
    speed: 42,
    attackRange: 24,
    attackCooldown: 1.1,
    size: 32,
    attackType: 'melee',
    sfx: 'laser_swing'
  },
  hero_archer: {
    key: 'hero_archer',
    name: 'Pemanah Plasma',
    cost: 35,
    cooldown: 4.0,
    hp: 75,
    damage: 13,
    speed: 36,
    attackRange: 115,
    attackCooldown: 1.6,
    size: 32,
    attackType: 'projectile_bubble',
    sfx: 'plasma_shot'
  },
  hero_mage: {
    key: 'hero_mage',
    name: 'Teknopenyihir Matrix',
    cost: 50,
    cooldown: 6.0,
    hp: 65,
    damage: 26,
    speed: 32,
    attackRange: 95,
    attackCooldown: 2.0,
    size: 32,
    attackType: 'projectile_star',
    sfx: 'star_pop'
  },
  hero_pony: {
    key: 'hero_pony',
    name: 'Ksatria Kuda Cyber',
    cost: 80,
    cooldown: 8.5,
    hp: 210,
    damage: 32,
    speed: 78,
    attackRange: 28,
    attackCooldown: 1.3,
    size: 48,
    attackType: 'melee',
    sfx: 'laser_swing'
  },
  hero_golem: {
    key: 'hero_golem',
    name: 'Robot Titan Golem',
    cost: 150,
    cooldown: 14.0,
    hp: 520,
    damage: 48,
    speed: 22,
    attackRange: 32,
    attackCooldown: 2.2,
    size: 64,
    attackType: 'ground_slam',
    sfx: 'stomp_thud'
  },

  // --- KANDIDAT MONSTER MUSUH ---
  enemy_slime: {
    key: 'enemy_slime',
    name: 'Void Slime',
    hp: 70,
    damage: 8,
    speed: 38,
    attackRange: 20,
    attackCooldown: 1.3,
    size: 32,
    attackType: 'melee',
    sfx: 'slime_boing'
  },
  enemy_bunny: {
    key: 'enemy_bunny',
    name: 'Cyber Rogue Beast',
    hp: 95,
    damage: 14,
    speed: 68,
    attackRange: 22,
    attackCooldown: 1.1,
    size: 32,
    attackType: 'melee',
    sfx: 'laser_swing'
  },
  enemy_pebble: {
    key: 'enemy_pebble',
    name: 'Armored Stone Drone',
    hp: 200,
    damage: 12,
    speed: 26,
    attackRange: 22,
    attackCooldown: 1.8,
    size: 32,
    attackType: 'melee',
    sfx: 'stomp_thud'
  },
  boss_croc: {
    key: 'boss_croc',
    name: 'Heavy Cyber Croc (Mini Boss)',
    hp: 500,
    damage: 36,
    speed: 24,
    attackRange: 34,
    attackCooldown: 2.0,
    size: 64,
    attackType: 'ground_slam',
    sfx: 'stomp_thud'
  },
  boss_dragon: {
    key: 'boss_dragon',
    name: 'Singularity Dragon King (Boss)',
    hp: 1300,
    damage: 52,
    speed: 18,
    attackRange: 65,
    attackCooldown: 2.4,
    size: 96,
    attackType: 'projectile_star',
    sfx: 'star_pop'
  }
};

export class Projectile {
  constructor(config) {
    this.x = config.x;
    this.y = config.y;
    this.targetX = config.targetX;
    this.targetY = config.targetY !== undefined ? config.targetY : config.y;
    this.targetEntity = config.targetEntity;
    this.speed = config.speed || 180;
    this.damage = config.damage;
    this.team = config.team;
    this.type = config.type; // 'bubble' | 'star' | 'laser_cyan' | 'laser_red'
    this.isDead = false;
    this.direction = config.team === 'player' ? 1 : -1;
  }

  update(dt) {
    this.x += this.direction * this.speed * dt;
    // Lerp ketinggian target Y jika proyektil menembak ke bawah/atas dari menara
    if (this.targetEntity && !this.targetEntity.isDead) {
      const targetY = this.targetEntity.y - (this.targetEntity.isBuilding ? 40 : 12);
      this.y += (targetY - this.y) * Math.min(1, 6 * dt);
    }
    // Cek tabrakan target
    if (this.targetEntity && !this.targetEntity.isDead) {
      const dist = Math.abs(this.targetEntity.x - this.x);
      if (dist < 14) {
        this.targetEntity.takeDamage(this.damage);
        this.isDead = true;
      }
    } else {
      // Jika target musnah, jalan sampai batas target
      if ((this.x - this.targetX) * this.direction >= 0) {
        this.isDead = true;
      }
    }
    // Batas aman lintasan
    if (this.x < -100 || this.x > 5000) {
      this.isDead = true;
    }
  }
}

export class LaneEntity {
  constructor(config) {
    this.id = config.id || Math.random().toString(36).substr(2, 9);
    this.key = config.key || 'unit';
    this.name = config.name || 'Unit';
    this.team = config.team; // 'player' | 'enemy'
    this.x = config.x;
    
    // Pseudo-depth Y agar tidak bertumpuk kaku
    const randomOffset = (Math.random() * 2 - 1) * LANE_CONFIG.DEPTH_OFFSET_MAX;
    this.y = config.isBuilding ? LANE_CONFIG.GROUND_Y_BASE : LANE_CONFIG.GROUND_Y_BASE + randomOffset;
    
    this.hp = config.hp;
    this.maxHp = config.hp;
    this.damage = config.damage;
    this.speed = config.isBuilding ? 0 : config.speed;
    this.attackRange = config.attackRange;
    this.attackCooldown = config.attackCooldown;
    this.attackType = config.attackType || 'melee';
    this.size = config.size || 32;
    this.isBuilding = config.isBuilding || false;
    this.sfx = config.sfx || 'wood_swing';

    this.halfWidth = config.halfWidth || (config.isBuilding ? LANE_CONFIG.CASTLE_HALF_WIDTH : (config.size ? config.size / 2 : 16));

    // FSM State: 'WALK', 'ATTACK', 'KNOCKBACK', 'DYING', 'IDLE'
    this.state = this.isBuilding ? 'IDLE' : 'WALK';
    this.target = null;
    this.attackTimer = 0.2; // Sedikit jeda saat pertama spawn
    this.isDead = false;
    this.deathTimer = 0;
    this.poofSpawned = false;
    this.animTimer = 0;
    this.hitFlashTimer = 0;
    this.knockbackTimer = 0;

    // Arah gerak: Player ke kanan (+1), Musuh ke kiri (-1)
    this.direction = this.team === 'player' ? 1 : -1;
  }

  isInFront(other) {
    if (!other) return false;
    return (other.x - this.x) * this.direction >= 0;
  }

  getGap(other) {
    if (!other) return Infinity;
    return (other.x - this.x) * this.direction - this.halfWidth - other.halfWidth;
  }

  getDistanceTo(targetEntity) {
    return this.getGap(targetEntity);
  }

  update(dt, onAttackCallback) {
    if (this.state === 'DYING') {
      this.deathTimer -= dt;
      return;
    }
    if (this.isDead) return;

    this.animTimer += dt;
    if (this.hitFlashTimer > 0) this.hitFlashTimer -= dt;

    if (this.attackTimer > 0) {
      this.attackTimer -= dt;
    }

    if (this.knockbackTimer > 0) {
      this.knockbackTimer -= dt;
      this.x -= this.direction * 35 * dt; // Dorongan mundur
      return;
    }

    if (this.target) {
      const gap = this.getGap(this.target);
      if (!this.target.isAlive || gap > this.attackRange || !this.isInFront(this.target)) {
        this.target = null;
        this.state = this.isBuilding ? 'IDLE' : 'WALK';
      } else {
        this.state = 'ATTACK';
        if (this.attackTimer <= 0) {
          if (onAttackCallback) onAttackCallback(this, this.target);
          this.executeAttack(this.target);
          this.attackTimer = this.attackCooldown;
        }
        return;
      }
    }

    if (this.state === 'WALK' && !this.isBuilding) {
      this.x += this.direction * this.speed * dt;
    }
  }

  get isAlive() {
    return this.hp > 0 && this.state !== 'DYING';
  }

  executeAttack(target) {
    if (this.attackType === 'melee' || this.attackType === 'ground_slam') {
      target.takeDamage(this.damage);
    }
    // Proyektil dihandle oleh manager di onAttackCallback
  }

  takeDamage(amount) {
    if (this.hp <= 0) return;
    this.hp -= amount;
    this.hitFlashTimer = 0.15; // Kilau putih/merah saat kena pukulan
    
    // Knockback kecil untuk unit non-bangunan dan non-boss (threshold damage >= 15% maxHp)
    if (!this.isBuilding && this.size < 64 && amount >= this.maxHp * 0.15) {
      this.knockbackTimer = 0.14;
    }

    if (this.hp <= 0) {
      this.hp = 0;
      this.state = 'DYING';
      this.deathTimer = 0.4; // 0.4s animasi sebelum dihapus
      this.isDead = true;
      this.target = null;
    }
  }
}

export class LaneCombatManager {
  constructor(trackLength = LANE_CONFIG.DEFAULT_TRACK_LENGTH, onSfxCallback = null, level = 1) {
    this.trackLength = trackLength;
    this.onSfxCallback = onSfxCallback;
    this.level = level;
    this.playerUnits = [];
    this.enemyUnits = [];
    this.projectiles = [];
    this.particles = []; // Visual VFX (poof, sparks, bubbles)

    this.initCastles();
  }

  setTrackLength(trackLength) {
    this.trackLength = trackLength;
    this.initCastles();
  }

  initCastles() {
    const baseDamage = 18 + Math.min(10, this.level || 1) * 2;
    this.playerCastle = new LaneEntity({
      id: 'castle_player',
      key: 'castle_player',
      name: 'Kastel Pemain',
      team: 'player',
      x: LANE_CONFIG.BOUNDS_MIN_X,
      hp: 1000,
      damage: baseDamage,
      speed: 0,
      attackRange: 155,
      attackCooldown: 1.6,
      size: 96,
      attackType: 'projectile_laser',
      sfx: 'base_laser',
      isBuilding: true
    });

    this.enemyCastle = new LaneEntity({
      id: 'castle_enemy',
      key: 'castle_enemy',
      name: 'Kastel Musuh',
      team: 'enemy',
      x: this.trackLength - LANE_CONFIG.BOUNDS_MIN_X,
      hp: 1000,
      damage: baseDamage,
      speed: 0,
      attackRange: 155,
      attackCooldown: 1.6,
      size: 96,
      attackType: 'projectile_laser',
      sfx: 'base_laser',
      isBuilding: true
    });
  }

  spawnUnit(typeKey, team = 'player') {
    const config = UNIT_TYPES[typeKey];
    if (!config) return null;

    const list = team === 'player' ? this.playerUnits : this.enemyUnits;
    if (list.length >= (LANE_CONFIG.MAX_UNITS_PER_TEAM || 12)) return null;

    const startX = team === 'player' 
      ? LANE_CONFIG.BOUNDS_MIN_X + 28
      : this.trackLength - (LANE_CONFIG.BOUNDS_MIN_X + 28);

    const entity = new LaneEntity({
      ...config,
      team,
      x: startX
    });

    if (team === 'player') {
      this.playerUnits.push(entity);
    } else {
      this.enemyUnits.push(entity);
    }

    return entity;
  }

  update(dt) {
    const handleAttack = (attacker, target) => {
      if (this.onSfxCallback && attacker.sfx) {
        this.onSfxCallback(attacker.sfx);
      }

      if (attacker.attackType === 'projectile_bubble') {
        this.projectiles.push(new Projectile({
          x: attacker.x + (attacker.direction * 14),
          y: attacker.y - 12,
          targetX: target.x,
          targetEntity: target,
          damage: attacker.damage,
          team: attacker.team,
          type: 'bubble',
          speed: 210
        }));
      } else if (attacker.attackType === 'projectile_star') {
        this.projectiles.push(new Projectile({
          x: attacker.x + (attacker.direction * 14),
          y: attacker.y - 16,
          targetX: target.x,
          targetEntity: target,
          damage: attacker.damage,
          team: attacker.team,
          type: 'star',
          speed: 230
        }));
      } else if (attacker.attackType === 'projectile_laser') {
        // Serangan Meriam / Laser Menara Pertahanan Benteng
        const isPlayer = attacker.team === 'player';
        const spawnX = attacker.x + (attacker.direction * (attacker.isBuilding ? 24 : 14));
        const spawnY = attacker.isBuilding ? attacker.y - 65 : attacker.y - 14;
        this.projectiles.push(new Projectile({
          x: spawnX,
          y: spawnY,
          targetX: target.x,
          targetY: target.y - (target.isBuilding ? 40 : 12),
          targetEntity: target,
          damage: attacker.damage,
          team: attacker.team,
          type: isPlayer ? 'laser_cyan' : 'laser_red',
          speed: 280
        }));
        this.spawnVfx(isPlayer ? 'sparks_cyan' : 'sparks_red', spawnX, spawnY);
      } else if (attacker.attackType === 'ground_slam') {
        // Efek AoE kecil di sekitar target
        this.spawnVfx('slam', target.x, LANE_CONFIG.GROUND_Y_BASE + 8);
        const opposing = attacker.team === 'player' ? this.enemyUnits : this.playerUnits;
        opposing.forEach(u => {
          if (!u.isDead && Math.abs(u.x - target.x) < 32) {
            u.takeDamage(Math.floor(attacker.damage * 0.4));
          }
        });
      }
    };

    // 1. Evaluasi target & update status Kastel Pertahanan
    if (this.playerCastle.isAlive) {
      this.evaluateTarget(this.playerCastle, this.enemyUnits, null);
      this.playerCastle.update(dt, handleAttack);
    }
    if (this.enemyCastle.isAlive) {
      this.evaluateTarget(this.enemyCastle, this.playerUnits, null);
      this.enemyCastle.update(dt, handleAttack);
    }

    // 2. Evaluasi target & update player units
    for (const unit of this.playerUnits) {
      if (unit.isDead) continue;
      this.evaluateTarget(unit, this.enemyUnits, this.enemyCastle);
      unit.update(dt, handleAttack);
    }

    // 3. Evaluasi target & update enemy units
    for (const enemy of this.enemyUnits) {
      if (enemy.isDead) continue;
      this.evaluateTarget(enemy, this.playerUnits, this.playerCastle);
      enemy.update(dt, handleAttack);
    }

    // 4. Update projectiles
    for (const p of this.projectiles) {
      p.update(dt);
      if (p.isDead) {
        if (p.type === 'bubble') {
          this.spawnVfx('bubble_pop', p.x, p.y);
        } else if (p.type === 'star') {
          this.spawnVfx('star_pop', p.x, p.y);
        } else if (p.type === 'laser_cyan') {
          this.spawnVfx('sparks_cyan', p.x, p.y);
        } else if (p.type === 'laser_red') {
          this.spawnVfx('sparks_red', p.x, p.y);
        }
      }
    }
    this.projectiles = this.projectiles.filter(p => !p.isDead);

    // 5. Tangani unit mati & spawn efek 'poof cloud' saat masuk DYING
    const handleUnitDeath = (u) => {
      if (u.state === 'DYING' && !u.poofSpawned) {
        u.poofSpawned = true;
        this.spawnVfx('poof', u.x, u.y - 10);
      }
    };
    this.playerUnits.forEach(handleUnitDeath);
    this.enemyUnits.forEach(handleUnitDeath);

    // Hapus dari memori hanya setelah animasi dying selesai (deathTimer <= 0)
    this.playerUnits = this.playerUnits.filter(u => !(u.state === 'DYING' && u.deathTimer <= 0));
    this.enemyUnits = this.enemyUnits.filter(e => !(e.state === 'DYING' && e.deathTimer <= 0));

    // 6. Update particles
    for (const pt of this.particles) {
      pt.life -= dt;
      pt.x += pt.vx * dt;
      pt.y += pt.vy * dt;
    }
    this.particles = this.particles.filter(pt => pt.life > 0);
  }

  evaluateTarget(unit, opposingUnits, opposingCastle) {
    let closestTarget = null;
    let minGap = Infinity;

    for (const target of opposingUnits) {
      if (!target.isAlive || !unit.isInFront(target)) continue;
      const gap = unit.getGap(target);
      if (gap < minGap) {
        minGap = gap;
        closestTarget = target;
      }
    }

    if (opposingCastle && opposingCastle.isAlive && unit.isInFront(opposingCastle)) {
      const castleGap = unit.getGap(opposingCastle);
      if (castleGap < minGap) {
        minGap = castleGap;
        closestTarget = opposingCastle;
      }
    }

    if (closestTarget && minGap <= unit.attackRange) {
      unit.target = closestTarget;
    } else {
      unit.target = null;
      if (unit.state === 'ATTACK') {
        unit.state = 'WALK';
      }
    }
  }

  spawnVfx(type, x, y) {
    if (type === 'poof') {
      // Fluffy cartoon poof particles
      for (let i = 0; i < 6; i++) {
        const angle = (Math.PI * 2 * i) / 6;
        this.particles.push({
          type: 'poof',
          x,
          y,
          vx: Math.cos(angle) * 25,
          vy: Math.sin(angle) * 20 - 15,
          life: 0.45,
          maxLife: 0.45,
          size: 6 + Math.random() * 4,
          color: '#FFFFFF'
        });
      }
    } else if (type === 'star_pop') {
      for (let i = 0; i < 5; i++) {
        this.particles.push({
          type: 'star',
          x,
          y,
          vx: (Math.random() - 0.5) * 60,
          vy: (Math.random() - 0.5) * 60 - 20,
          life: 0.35,
          maxLife: 0.35,
          size: 3,
          color: ['#FFD700', '#FF9F43', '#54A0FF'][Math.floor(Math.random() * 3)]
        });
      }
    } else if (type === 'bubble_pop') {
      for (let i = 0; i < 4; i++) {
        this.particles.push({
          type: 'bubble',
          x,
          y,
          vx: (Math.random() - 0.5) * 40,
          vy: -20 - Math.random() * 20,
          life: 0.3,
          maxLife: 0.3,
          size: 3,
          color: '#48DBFB'
        });
      }
    } else if (type === 'slam') {
      for (let i = -1; i <= 1; i += 2) {
        this.particles.push({
          type: 'dust',
          x: x + i * 8,
          y: y - 2,
          vx: i * 40,
          vy: -15,
          life: 0.25,
          maxLife: 0.25,
          size: 4,
          color: '#D2B48C'
        });
      }
    } else if (type === 'sparks_cyan') {
      for (let i = 0; i < 5; i++) {
        this.particles.push({
          type: 'spark',
          x,
          y,
          vx: (Math.random() - 0.5) * 60,
          vy: (Math.random() - 0.5) * 60 - 10,
          life: 0.3,
          maxLife: 0.3,
          size: 3,
          color: '#00f2fe'
        });
      }
    } else if (type === 'sparks_red') {
      for (let i = 0; i < 5; i++) {
        this.particles.push({
          type: 'spark',
          x,
          y,
          vx: (Math.random() - 0.5) * 60,
          vy: (Math.random() - 0.5) * 60 - 10,
          life: 0.3,
          maxLife: 0.3,
          size: 3,
          color: '#ff4757'
        });
      }
    }
  }

  getSortedRenderList() {
    const all = [
      this.playerCastle,
      this.enemyCastle,
      ...this.playerUnits,
      ...this.enemyUnits
    ];
    return all.sort((a, b) => a.y - b.y);
  }
}
