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
  }

  get maxScroll() {
    return Math.max(0, this.trackLength - this.canvasWidth);
  }

  setTrackLength(newLength) {
    this.trackLength = newLength;
    this.scrollX = clamp(this.scrollX, 0, this.maxScroll);
  }

  panBy(dx) {
    this.scrollX = clamp(this.scrollX + dx, 0, this.maxScroll);
    this.holdTimer = 2.0; // Tahan 2 detik sebelum auto-follow kembali
  }

  computeFocusX(combatManager) {
    if (!combatManager) return this.canvasWidth * 0.5;

    const p = combatManager.playerUnits ? combatManager.playerUnits.filter(u => u.isAlive) : [];
    const e = combatManager.enemyUnits ? combatManager.enemyUnits.filter(u => u.isAlive) : [];
    const frontP = p.length ? Math.max(...p.map(u => u.x)) : null;
    const frontE = e.length ? Math.min(...e.map(u => u.x)) : null;
    const home = combatManager.playerCastle ? combatManager.playerCastle.x : 56;

    // 1. Ada benturan: pusatkan di tengah garis depan pemain dan musuh
    if (frontP !== null && frontE !== null) {
      return (frontP + frontE) / 2;
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
    if (this.holdTimer > 0) {
      this.holdTimer -= dt;
    } else {
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
    }

    return Math.round(this.scrollX);
  }
}
