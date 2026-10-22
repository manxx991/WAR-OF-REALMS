/**
 * SoundManager.js
 * Modul Audio 16-bit Chiptune menggunakan Web Audio API.
 * Menghasilkan SFX retro dan BGM sintetis secara langsung tanpa ketergantungan file eksternal,
 * serta mendukung pemutaran file audio eksternal jika tersedia di assets/audio/.
 */

export class SoundManager {
  constructor() {
    this.ctx = null;
    this.masterGain = null;
    this.bgmGain = null;
    this.sfxGain = null;
    this.muted = false;
    this.bgmPlaying = false;
    this.bgmInterval = null;
    this.currentTrack = null;
    this.audioCache = new Map();
  }

  init() {
    if (this.ctx) return;
    try {
      const AudioCtx = window.AudioContext || window.webkitAudioContext;
      if (!AudioCtx) return;
      this.ctx = new AudioCtx();

      this.masterGain = this.ctx.createGain();
      this.masterGain.gain.setValueAtTime(0.7, this.ctx.currentTime);
      this.masterGain.connect(this.ctx.destination);

      this.bgmGain = this.ctx.createGain();
      this.bgmGain.gain.setValueAtTime(0.35, this.ctx.currentTime);
      this.bgmGain.connect(this.masterGain);

      this.sfxGain = this.ctx.createGain();
      this.sfxGain.gain.setValueAtTime(0.6, this.ctx.currentTime);
      this.sfxGain.connect(this.masterGain);
    } catch (e) {
      console.warn('Web Audio not initialized:', e);
    }
  }

  resume() {
    if (this.ctx && this.ctx.state === 'suspended') {
      this.ctx.resume();
    }
  }

  toggleMute() {
    this.muted = !this.muted;
    if (this.masterGain && this.ctx) {
      this.masterGain.gain.setValueAtTime(this.muted ? 0 : 0.7, this.ctx.currentTime);
    }
    return this.muted;
  }

  playSfx(type) {
    if (this.muted) return;
    this.init();
    this.resume();
    if (!this.ctx) return;

    const t = this.ctx.currentTime;

    switch (type) {
      case 'wood_swing': { // Ayunan pedang kayu (whoosh)
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.type = 'triangle';
        osc.frequency.setValueAtTime(320, t);
        osc.frequency.exponentialRampToValueAtTime(110, t + 0.12);
        gain.gain.setValueAtTime(0.5, t);
        gain.gain.linearRampToValueAtTime(0.01, t + 0.12);
        osc.connect(gain);
        gain.connect(this.sfxGain);
        osc.start(t);
        osc.stop(t + 0.12);
        break;
      }

      case 'bubble_shoot': { // Plop gelembung
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.type = 'sine';
        osc.frequency.setValueAtTime(400, t);
        osc.frequency.exponentialRampToValueAtTime(880, t + 0.08);
        gain.gain.setValueAtTime(0.4, t);
        gain.gain.exponentialRampToValueAtTime(0.01, t + 0.1);
        osc.connect(gain);
        gain.connect(this.sfxGain);
        osc.start(t);
        osc.stop(t + 0.1);
        break;
      }

      case 'star_pop': { // Proyektil bintang kembang api
        const notes = [587.33, 880, 1174.66]; // D5, A5, D6
        notes.forEach((freq, idx) => {
          const osc = this.ctx.createOscillator();
          const gain = this.ctx.createGain();
          osc.type = 'square';
          osc.frequency.setValueAtTime(freq, t + idx * 0.04);
          gain.gain.setValueAtTime(0.2, t + idx * 0.04);
          gain.gain.exponentialRampToValueAtTime(0.01, t + idx * 0.04 + 0.1);
          osc.connect(gain);
          gain.connect(this.sfxGain);
          osc.start(t + idx * 0.04);
          osc.stop(t + idx * 0.04 + 0.1);
        });
        break;
      }

      case 'stomp_thud': { // Hentakan golem
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.type = 'triangle';
        osc.frequency.setValueAtTime(140, t);
        osc.frequency.exponentialRampToValueAtTime(35, t + 0.25);
        gain.gain.setValueAtTime(0.8, t);
        gain.gain.exponentialRampToValueAtTime(0.01, t + 0.25);
        osc.connect(gain);
        gain.connect(this.sfxGain);
        osc.start(t);
        osc.stop(t + 0.25);
        break;
      }

      case 'slime_boing': { // Boing kenyal karet
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.type = 'sine';
        osc.frequency.setValueAtTime(180, t);
        osc.frequency.linearRampToValueAtTime(420, t + 0.08);
        osc.frequency.linearRampToValueAtTime(260, t + 0.18);
        gain.gain.setValueAtTime(0.4, t);
        gain.gain.linearRampToValueAtTime(0.01, t + 0.2);
        osc.connect(gain);
        gain.connect(this.sfxGain);
        osc.start(t);
        osc.stop(t + 0.2);
        break;
      }

      case 'base_laser': { // Laser pertahanan benteng (retro sci-fi zap)
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.type = 'sawtooth';
        osc.frequency.setValueAtTime(700, t);
        osc.frequency.exponentialRampToValueAtTime(120, t + 0.15);
        gain.gain.setValueAtTime(0.35, t);
        gain.gain.exponentialRampToValueAtTime(0.01, t + 0.15);
        osc.connect(gain);
        gain.connect(this.sfxGain);
        osc.start(t);
        osc.stop(t + 0.15);
        break;
      }

      case 'star_coin': { // Koin bintang ting-ting!
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.type = 'square';
        osc.frequency.setValueAtTime(987.77, t); // B5
        osc.frequency.setValueAtTime(1318.51, t + 0.07); // E6
        gain.gain.setValueAtTime(0.3, t);
        gain.gain.exponentialRampToValueAtTime(0.01, t + 0.25);
        osc.connect(gain);
        gain.connect(this.sfxGain);
        osc.start(t);
        osc.stop(t + 0.25);
        break;
      }

      case 'quiz_correct': { // Kuis benar: akord ceria naik
        const arpeggio = [523.25, 659.25, 783.99, 1046.50]; // C5, E5, G5, C6
        arpeggio.forEach((f, i) => {
          const osc = this.ctx.createOscillator();
          const gain = this.ctx.createGain();
          osc.type = 'triangle';
          osc.frequency.setValueAtTime(f, t + i * 0.06);
          gain.gain.setValueAtTime(0.35, t + i * 0.06);
          gain.gain.exponentialRampToValueAtTime(0.01, t + i * 0.06 + 0.2);
          osc.connect(gain);
          gain.connect(this.sfxGain);
          osc.start(t + i * 0.06);
          osc.stop(t + i * 0.06 + 0.22);
        });
        break;
      }

      case 'quiz_wrong': { // Kuis salah: nada kartun lembut wah-wah
        const notes = [320, 290, 260];
        notes.forEach((f, i) => {
          const osc = this.ctx.createOscillator();
          const gain = this.ctx.createGain();
          osc.type = 'sawtooth';
          osc.frequency.setValueAtTime(f, t + i * 0.12);
          gain.gain.setValueAtTime(0.2, t + i * 0.12);
          gain.gain.linearRampToValueAtTime(0.01, t + i * 0.12 + 0.11);
          osc.connect(gain);
          gain.connect(this.sfxGain);
          osc.start(t + i * 0.12);
          osc.stop(t + i * 0.12 + 0.12);
        });
        break;
      }

      case 'victory': { // Jingle kemenangan ceria
        const fanfare = [
          { f: 523.25, d: 0.12 }, // C5
          { f: 659.25, d: 0.12 }, // E5
          { f: 783.99, d: 0.12 }, // G5
          { f: 1046.50, d: 0.35 } // C6
        ];
        let offset = 0;
        fanfare.forEach(item => {
          const osc = this.ctx.createOscillator();
          const gain = this.ctx.createGain();
          osc.type = 'square';
          osc.frequency.setValueAtTime(item.f, t + offset);
          gain.gain.setValueAtTime(0.3, t + offset);
          gain.gain.linearRampToValueAtTime(0.01, t + offset + item.d);
          osc.connect(gain);
          gain.connect(this.sfxGain);
          osc.start(t + offset);
          osc.stop(t + offset + item.d);
          offset += item.d;
        });
        break;
      }

      default:
        break;
    }
  }

  startBgm(theme = 'battle') {
    this.init();
    this.resume();
    if (this.bgmPlaying && this.currentTrack === theme) return;
    this.stopBgm();

    this.bgmPlaying = true;
    this.currentTrack = theme;

    // Chiptune melodi ceria prosedural loop
    const melody = theme === 'title' ? [
      261.63, 329.63, 392.00, 523.25, 440.00, 392.00, 329.63, 261.63
    ] : [
      392.00, 440.00, 523.25, 587.33, 659.25, 587.33, 523.25, 440.00,
      392.00, 329.63, 349.23, 392.00, 523.25, 392.00, 349.23, 329.63
    ];

    const bassline = theme === 'title' ? [130.81, 164.81, 196.00, 130.81] : [196.00, 174.61, 164.81, 146.83];
    let step = 0;
    const stepDuration = 0.22; // ~136 BPM

    this.bgmInterval = setInterval(() => {
      if (this.muted || !this.ctx || this.ctx.state !== 'running') return;
      const t = this.ctx.currentTime;

      // Melody voice
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      osc.type = 'square';
      const freq = melody[step % melody.length];
      osc.frequency.setValueAtTime(freq, t);
      gain.gain.setValueAtTime(0.12, t);
      gain.gain.exponentialRampToValueAtTime(0.01, t + stepDuration * 0.9);
      osc.connect(gain);
      gain.connect(this.bgmGain);
      osc.start(t);
      osc.stop(t + stepDuration * 0.95);

      // Bass voice
      if (step % 2 === 0) {
        const bassOsc = this.ctx.createOscillator();
        const bassGain = this.ctx.createGain();
        bassOsc.type = 'triangle';
        const bFreq = bassline[(step / 2) % bassline.length];
        bassOsc.frequency.setValueAtTime(bFreq, t);
        bassGain.gain.setValueAtTime(0.2, t);
        bassGain.gain.exponentialRampToValueAtTime(0.01, t + stepDuration * 1.8);
        bassOsc.connect(bassGain);
        bassGain.connect(this.bgmGain);
        bassOsc.start(t);
        bassOsc.stop(t + stepDuration * 1.85);
      }

      step++;
    }, stepDuration * 1000);
  }

  stopBgm() {
    this.bgmPlaying = false;
    this.currentTrack = null;
    if (this.bgmInterval) {
      clearInterval(this.bgmInterval);
      this.bgmInterval = null;
    }
  }
}
