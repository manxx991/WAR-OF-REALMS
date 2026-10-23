/**
 * AssetLoader.js
 * Modul pemuat aset gambar dan audio opsional.
 * Jika file belum tersedia di folder assets/, sistem otomatis menggunakan fallback
 * procedural pixel-rendering tanpa error atau crash.
 */

export class AssetLoader {
  constructor() {
    this.images = new Map();
    this.loadedCount = 0;
    this.totalCount = 0;
    this.isReady = false;
  }

  loadImage(key, src) {
    this.totalCount++;
    return new Promise((resolve) => {
      const img = new Image();
      img.onload = () => {
        this.images.set(key, img);
        this.loadedCount++;
        resolve(img);
      };
      img.onerror = () => {
        // Fallback: simpan null agar renderer tahu menggunakan procedural sprite
        this.images.set(key, null);
        this.loadedCount++;
        resolve(null);
      };
      img.src = src;
    });
  }

  async loadAll() {
    const assetManifest = [
      { key: 'bg_sky', src: 'assets/background/bg_sky_cyber.png' },
      { key: 'bg_far', src: 'assets/background/bg_far_cyber_city.png' },
      { key: 'bg_mid', src: 'assets/background/bg_mid_pylons.png' },
      { key: 'tile_lane', src: 'assets/background/tilesets/tile_cyber_lane.png' },
      { key: 'hero_swordsman', src: 'assets/sprites/heroes/hero_swordsman.png' },
      { key: 'hero_archer', src: 'assets/sprites/heroes/hero_archer.png' },
      { key: 'hero_mage', src: 'assets/sprites/heroes/hero_mage.png' },
      { key: 'hero_pony', src: 'assets/sprites/heroes/hero_pony.png' },
      { key: 'hero_golem', src: 'assets/sprites/heroes/hero_golem.png' },
      { key: 'enemy_slime', src: 'assets/sprites/enemies/enemy_slime.png' },
      { key: 'enemy_bunny', src: 'assets/sprites/enemies/enemy_bunny.png' },
      { key: 'enemy_pebble', src: 'assets/sprites/enemies/enemy_pebble.png' },
      { key: 'boss_croc', src: 'assets/sprites/enemies/boss_croc.png' },
      { key: 'boss_dragon', src: 'assets/sprites/enemies/boss_dragon.png' },
      { key: 'castle_player', src: 'assets/sprites/buildings/castle_player.png' },
      { key: 'castle_player_damaged', src: 'assets/sprites/buildings/castle_player_damaged.png' },
      { key: 'castle_enemy', src: 'assets/sprites/buildings/castle_enemy.png' },
      { key: 'castle_enemy_damaged', src: 'assets/sprites/buildings/castle_enemy_damaged.png' },
      { key: 'bg_sky_sunset', src: 'assets/background/bg_sky_sunset.png' },
      { key: 'bg_far_hills', src: 'assets/background/bg_far_hills.png' },
      { key: 'vfx_bubble_pop', src: 'assets/sprites/vfx/vfx_bubble_pop.png' },
      { key: 'vfx_poof', src: 'assets/sprites/vfx/vfx_poof_cloud.png' },
      { key: 'vfx_sparks', src: 'assets/sprites/vfx/vfx_sparks.png' },
      { key: 'vfx_meteor_fire_rain', src: 'assets/sprites/vfx/vfx_meteor_fire_rain.png' },
      { key: 'vfx_hero_regen_aura', src: 'assets/sprites/vfx/vfx_hero_regen_aura.png' },
      { key: 'avatar_hero_swordsman', src: 'assets/ui/avatar_hero_swordsman.png' },
      { key: 'avatar_hero_archer', src: 'assets/ui/avatar_hero_archer.png' },
      { key: 'avatar_hero_mage', src: 'assets/ui/avatar_hero_mage.png' },
      { key: 'avatar_hero_pony', src: 'assets/ui/avatar_hero_pony.png' },
      { key: 'avatar_hero_golem', src: 'assets/ui/avatar_hero_golem.png' },
      { key: 'icon_btn_mana_quiz', src: 'assets/ui/icon_btn_mana_quiz.png' },
      { key: 'icon_btn_heal_base', src: 'assets/ui/icon_btn_heal_base.png' },
      { key: 'icon_btn_fire_rain', src: 'assets/ui/icon_btn_fire_rain.png' },
      { key: 'icon_btn_hero_regen', src: 'assets/ui/icon_btn_hero_regen.png' },
      { key: 'btn_quiz_opt_a', src: 'assets/ui/btn_quiz_opt_a.png' },
      { key: 'btn_quiz_opt_b', src: 'assets/ui/btn_quiz_opt_b.png' },
      { key: 'btn_quiz_opt_c', src: 'assets/ui/btn_quiz_opt_c.png' },
      { key: 'btn_quiz_opt_d', src: 'assets/ui/btn_quiz_opt_d.png' },
      { key: 'hud_mana_tube', src: 'assets/ui/hud_mana_tube.png' },
      { key: 'hud_hp_bar', src: 'assets/ui/hud_hp_bar.png' },
      { key: 'hud_hp_bar_player', src: 'assets/ui/hud_hp_bar_player.png' },
      { key: 'hud_hp_bar_enemy', src: 'assets/ui/hud_hp_bar_enemy.png' },
      { key: 'hud_hp_bar_frame_player', src: 'assets/ui/hud_hp_bar_frame_player.png' },
      { key: 'hud_hp_bar_frame_enemy', src: 'assets/ui/hud_hp_bar_frame_enemy.png' },
      { key: 'icon_shield_player', src: 'assets/ui/icon_shield_player.png' },
      { key: 'icon_shield_enemy', src: 'assets/ui/icon_shield_enemy.png' },
      { key: 'hud_radar_frame', src: 'assets/ui/hud_radar_frame.png' },
      { key: 'card_unit_frame', src: 'assets/ui/card_unit_frame.png' },
      { key: 'card_unit_frame_active', src: 'assets/ui/card_unit_frame_active.png' },
      { key: 'popup_quiz_dialog', src: 'assets/ui/popup_quiz_dialog.png' }
    ];

    await Promise.all(assetManifest.map(item => this.loadImage(item.key, item.src)));
    this.isReady = true;
    return this.images;
  }

  getImage(key) {
    return this.images.get(key) || null;
  }
}
