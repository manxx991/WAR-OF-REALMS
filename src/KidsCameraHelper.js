/**
 * KidsCameraHelper.js (v4.0 Smart Combat Camera)
 * Kamera landscape garis depan: memusatkan pandangan secara adaptif
 * di antara barisan depan pemain dan musuh terdekat.
 */
const clamp = (v, lo, hi) => Math.min(Math.max(v, lo), hi);

export class KidsCameraHelper {
  constructor(canvasWidth, trackLength, { smoothing = 5.5, lookAhead = 0.15 } = {}) {
    this.canvasWidth = canvasWidth;
    this.trackLength = trackLength;
    this.smoothing = smoothing;
    this.lookAhead = lookAhead;
    this.scrollX = 0;
    this.holdTimer = 0; // Detik jika di-pan manual
    this.isDragging = false;
  }

  get maxScroll() {
    return Math.max(0, this.trackLength - this.canvasWidth);
  }

  setTrackLength(newLength) {
    this.trackLength = newLength;
    this.scrollX = clamp(this.scrollX, 0, this.maxScroll);
  }

  setDragging(isDragging) {
    this.isDragging = Boolean(isDragging);
    if (this.isDragging) {
      this.holdTimer = 2.5; // Tahan auto-follow selama sedang di-drag
    }
  }

  panBy(dx) {
    this.scrollX = clamp(this.scrollX + dx, 0, this.maxScroll);
    this.holdTimer = 2.5; // Tahan 2.5 detik sebelum auto-follow kembali
  }

  panTo(targetX) {
    this.scrollX = clamp(targetX, 0, this.maxScroll);
    this.holdTimer = 2.5;
  }

  computeFocusX(combatManager) {
    if (!combatManager) return this.canvasWidth * 0.5;

    const p = combatManager.playerUnits ? combatManager.playerUnits.filter(u => u.isAlive) : [];
    const e = combatManager.enemyUnits ? combatManager.enemyUnits.filter(u => u.isAlive) : [];
    const frontP = p.length ? Math.max(...p.map(u => u.x)) : null;
    const frontE = e.length ? Math.min(...e.map(u => u.x)) : null;
    const home = combatManager.playerCastle ? combatManager.playerCastle.x : 56;

    // 1. Jika ada unit di kedua belah pihak:
    if (frontP !== null && frontE !== null) {
      const distance = frontE - frontP;
      // Jika kedua garis depan berdekatan (dalam jarak benturan <= 70% layar):
      if (distance <= this.canvasWidth * 0.7 && distance >= -100) {
        return (frontP + frontE) / 2;
      }
      // Jika masih saling berjauhan, fokus ke garis depan pasukan kita yang bergerak maju
      return frontP + this.canvasWidth * this.lookAhead;
    }
    // 2. Hanya ada pasukan kita: lihat ke depan
    if (frontP !== null) {
      return frontP + this.canvasWidth * this.lookAhead;
    }
    // 3. Pasukan musuh mendekati markas kita
    if (frontE !== null) {
      return Math.min(frontE, home + this.canvasWidth * 0.5);
    }
    // 4. Kondisi awal pertempuran: fokus di dekat benteng kita
    return home + this.canvasWidth * 0.25;
  }

  update(dt, combatManagerOrUnits) {
    if (this.isDragging) {
      this.holdTimer = 2.5;
      return Math.round(this.scrollX);
    }

    if (this.holdTimer > 0) {
      this.holdTimer -= dt;
      return Math.round(this.scrollX);
    }

    let focusX = 0;
    if (combatManagerOrUnits && combatManagerOrUnits.playerUnits) {
      focusX = this.computeFocusX(combatManagerOrUnits);
    } else if (Array.isArray(combatManagerOrUnits)) {
      // Fallback jika hanya dilempar array playerUnits
      const alive = combatManagerOrUnits.filter(u => u.isAlive);
      focusX = alive.length > 0 ? Math.max(...alive.map(u => u.x)) : 56;
    } else {
      focusX = 56;
    }

    const targetScroll = clamp(focusX - (this.canvasWidth / 2), 0, this.maxScroll);
    const k = 1 - Math.exp(-this.smoothing * dt);
    this.scrollX += (targetScroll - this.scrollX) * k;

    return Math.round(this.scrollX);
  }
}
