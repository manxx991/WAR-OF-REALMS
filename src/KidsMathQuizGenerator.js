/**
 * KidsMathQuizGenerator.js (Advanced Edition - SMA & Mahasiswa Baru)
 * Generator Soal Matematika Tingkat Menengah & Pengantar Kuliah (Level 1 - 10)
 *
 * Kurikulum:
 * - Level 1 : Aljabar Linear Satu Variabel (SPLSV)
 * - Level 2 : Eksponen, Sifat Perpangkatan & Bentuk Akar
 * - Level 3 : Logaritma Dasar & Sifat Aljabar Logaritma
 * - Level 4 : Persamaan Kuadrat, Faktorisasi & Diskriminan
 * - Level 5 : Barisan & Deret Aritmatika & Geometri (Un & Sn)
 * - Level 6 : Trigonometri Sudut Istimewa & Identitas Dasar
 * - Level 7 : Matriks Ordo 2x2 & Determinan (ad - bc)
 * - Level 8 : Kombinatorika, Permutasi, Kombinasi & Faktorial
 * - Level 9 : Modulo Arithmetic, Fungsi Komposisi & Vektor
 * - Level 10: Pengantar Kalkulus (Turunan Polinomial & Limit Aljabar)
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
    let topic = '';
    let questionText = '';
    let correctAnswer = 0;

    switch (clampedLevel) {
      // -------------------------------------------------------------
      // LEVEL 1: ALJABAR LINEAR (SPLSV)
      // -------------------------------------------------------------
      case 1: {
        topic = 'Aljabar Linear';
        const type = this.getRandomInt(1, 3);
        if (type === 1) {
          // ax + b = c => x = (c - b) / a
          const a = this.getRandomInt(2, 6);
          const x = this.getRandomInt(2, 9);
          const b = this.getRandomInt(3, 15);
          const c = a * x + b;
          questionText = `Jika ${a}x + ${b} = ${c}, nilai x = ?`;
          correctAnswer = x;
        } else if (type === 2) {
          // ax - b = c
          const a = this.getRandomInt(2, 5);
          const x = this.getRandomInt(3, 8);
          const b = this.getRandomInt(4, 16);
          const c = a * x - b;
          questionText = `Jika ${a}x - ${b} = ${c}, nilai x = ?`;
          correctAnswer = x;
        } else {
          // 2(x + a) = b
          const a = this.getRandomInt(2, 7);
          const x = this.getRandomInt(3, 10);
          const b = 2 * (x + a);
          questionText = `Selesaikan: 2(x + ${a}) = ${b}, x = ?`;
          correctAnswer = x;
        }
        break;
      }

      // -------------------------------------------------------------
      // LEVEL 2: EKSPONEN & BENTUK AKAR
      // -------------------------------------------------------------
      case 2: {
        topic = 'Eksponen & Akar';
        const type = this.getRandomInt(1, 3);
        if (type === 1) {
          // (2^a * 2^b) / 2^c = 2^(a+b-c)
          const a = this.getRandomInt(3, 6);
          const b = this.getRandomInt(2, 4);
          const c = a + b - this.getRandomInt(2, 4);
          const resultExp = a + b - c;
          questionText = `Hitung: (2^${a} × 2^${b}) / 2^${c} = ?`;
          correctAnswer = Math.pow(2, resultExp);
        } else if (type === 2) {
          // sqrt(p) + sqrt(q)
          const squares = [4, 9, 16, 25, 36, 49, 64, 81, 100, 144, 169];
          const i1 = this.getRandomInt(2, 6);
          const i2 = this.getRandomInt(2, 7);
          const s1 = squares[i1];
          const s2 = squares[i2];
          questionText = `Hitung: √${s1} + √${s2} = ?`;
          correctAnswer = Math.round(Math.sqrt(s1) + Math.sqrt(s2));
        } else {
          // a^x = b
          const base = this.getRandomInt(2, 4);
          const exp = this.getRandomInt(2, 4);
          const val = Math.pow(base, exp);
          questionText = `Jika ${base}^(x+1) = ${val * base}, x = ?`;
          correctAnswer = exp;
        }
        break;
      }

      // -------------------------------------------------------------
      // LEVEL 3: LOGARITMA DASAR
      // -------------------------------------------------------------
      case 3: {
        topic = 'Logaritma';
        const type = this.getRandomInt(1, 3);
        if (type === 1) {
          const base = [2, 3, 5][this.getRandomInt(0, 2)];
          const exp = this.getRandomInt(2, 5);
          const val = Math.pow(base, exp);
          questionText = `Nilai dari log_${base}(${val}) = ?`;
          correctAnswer = exp;
        } else if (type === 2) {
          const expA = this.getRandomInt(2, 4);
          const expB = this.getRandomInt(1, 3);
          const valA = Math.pow(2, expA);
          const valB = Math.pow(2, expB);
          questionText = `log_2(${valA}) + log_2(${valB}) = ?`;
          correctAnswer = expA + expB;
        } else {
          const expTotal = this.getRandomInt(2, 4);
          const expB = this.getRandomInt(1, 2);
          const valB = Math.pow(3, expB);
          const valA = Math.pow(3, expTotal + expB);
          questionText = `log_3(${valA}) - log_3(${valB}) = ?`;
          correctAnswer = expTotal;
        }
        break;
      }

      // -------------------------------------------------------------
      // LEVEL 4: PERSAMAAN KUADRAT & FAKTORISASI
      // -------------------------------------------------------------
      case 4: {
        topic = 'Persamaan Kuadrat';
        const type = this.getRandomInt(1, 3);
        const r1 = this.getRandomInt(1, 6);
        const r2 = this.getRandomInt(r1 + 1, r1 + 5);
        const b = r1 + r2;
        const c = r1 * r2;

        if (type === 1) {
          questionText = `Akar terbesar dari x² - ${b}x + ${c} = 0 adalah?`;
          correctAnswer = r2;
        } else if (type === 2) {
          questionText = `Jumlah akar (x₁ + x₂) dari x² - ${b}x + ${c} = 0 adalah?`;
          correctAnswer = b;
        } else {
          questionText = `Hasil kali akar (x₁ × x₂) dari x² - ${b}x + ${c} = 0 adalah?`;
          correctAnswer = c;
        }
        break;
      }

      // -------------------------------------------------------------
      // LEVEL 5: BARISAN & DERET (ARITMATIKA / GEOMETRI)
      // -------------------------------------------------------------
      case 5: {
        topic = 'Barisan & Deret';
        const isGeo = Math.random() > 0.5;
        if (!isGeo) {
          const a = this.getRandomInt(2, 8);
          const d = this.getRandomInt(3, 6);
          const n = this.getRandomInt(5, 8);
          const seq = [a, a + d, a + 2 * d, a + 3 * d].join(', ');
          questionText = `Suku ke-${n} (U_${n}) dari barisan ${seq}, ... adalah?`;
          correctAnswer = a + (n - 1) * d;
        } else {
          const a = this.getRandomInt(2, 4);
          const r = this.getRandomInt(2, 3);
          const seq = [a, a * r, a * r * r, a * r * r * r].join(', ');
          const typeQ = this.getRandomInt(1, 2);
          if (typeQ === 1) {
            questionText = `Rasio (r) dari deret geometri ${seq}, ... adalah?`;
            correctAnswer = r;
          } else {
            questionText = `Suku ke-5 (U_5) dari deret geometri ${seq}, ... adalah?`;
            correctAnswer = a * Math.pow(r, 4);
          }
        }
        break;
      }

      // -------------------------------------------------------------
      // LEVEL 6: TRIGONOMETRI SUDUT ISTIMEWA
      // -------------------------------------------------------------
      case 6: {
        topic = 'Trigonometri';
        const pool = [
          { q: 'Nilai dari 2 · sin(30°) + 2 · cos(60°) = ?', a: 2 },
          { q: 'Nilai dari 4 · tan(45°) - 2 · sin(90°) = ?', a: 2 },
          { q: 'Nilai dari 3 · cos(0°) + 2 · sin(90°) = ?', a: 5 },
          { q: 'Hitung: 6 · (sin²(30°) + cos²(30°)) = ?', a: 6 },
          { q: 'Nilai dari 2 · tan(45°) × cos(60°) = ?', a: 1 },
          { q: 'Hitung: 4 · sin(30°) + 3 · tan(45°) = ?', a: 5 },
          { q: 'Hitung: 8 · sin(30°) · cos(60°) = ?', a: 2 },
          { q: 'Nilai dari 5 · cos(0°) - 3 · sin(0°) = ?', a: 5 }
        ];
        const pick = pool[this.getRandomInt(0, pool.length - 1)];
        questionText = pick.q;
        correctAnswer = pick.a;
        break;
      }

      // -------------------------------------------------------------
      // LEVEL 7: MATRIKS & DETERMINAN 2x2
      // -------------------------------------------------------------
      case 7: {
        topic = 'Matriks & Determinan';
        const type = this.getRandomInt(1, 3);
        if (type === 1) {
          const a = this.getRandomInt(3, 7);
          const d = this.getRandomInt(3, 6);
          const b = this.getRandomInt(1, 4);
          const c = this.getRandomInt(1, 3);
          questionText = `Determinan matriks | ${a}  ${b} | adalah?\n                   | ${c}  ${d} |`;
          correctAnswer = a * d - b * c;
        } else if (type === 2) {
          const a = this.getRandomInt(4, 9);
          const d = this.getRandomInt(3, 8);
          const b = this.getRandomInt(1, 5);
          const c = this.getRandomInt(1, 5);
          questionText = `Trace (jumlah diagonal utama) matriks:\n[ ${a}  ${b} ]\n[ ${c}  ${d} ] = ?`;
          correctAnswer = a + d;
        } else {
          const x = this.getRandomInt(2, 6);
          const d = this.getRandomInt(2, 5);
          const b = 2;
          const c = 3;
          const det = x * d - b * c;
          questionText = `Jika det | x  ${b} | = ${det}, nilai x = ?\n         | ${c}  ${d} |`;
          correctAnswer = x;
        }
        break;
      }

      // -------------------------------------------------------------
      // LEVEL 8: KOMBINATORIKA & FAKTORIAL
      // -------------------------------------------------------------
      case 8: {
        topic = 'Kombinatorika';
        const type = this.getRandomInt(1, 3);
        if (type === 1) {
          const poolFacts = [
            { q: 'Hitung: 5! / 4! = ?', a: 5 },
            { q: 'Hitung: 6! / 5! = ?', a: 6 },
            { q: 'Hitung: 5! / 3! = ?', a: 20 },
            { q: 'Hitung: 4! / 2! = ?', a: 12 },
            { q: 'Hitung: 4! = ?', a: 24 }
          ];
          const p = poolFacts[this.getRandomInt(0, poolFacts.length - 1)];
          questionText = p.q;
          correctAnswer = p.a;
        } else if (type === 2) {
          const poolC = [
            { q: 'Kombinasi C(4, 2) = ?', a: 6 },
            { q: 'Kombinasi C(5, 2) = ?', a: 10 },
            { q: 'Kombinasi C(5, 3) = ?', a: 10 },
            { q: 'Kombinasi C(6, 2) = ?', a: 15 },
            { q: 'Kombinasi C(4, 3) = ?', a: 4 }
          ];
          const p = poolC[this.getRandomInt(0, poolC.length - 1)];
          questionText = p.q;
          correctAnswer = p.a;
        } else {
          const poolP = [
            { q: 'Permutasi P(4, 2) = ?', a: 12 },
            { q: 'Permutasi P(5, 2) = ?', a: 20 },
            { q: 'Permutasi P(3, 2) = ?', a: 6 },
            { q: 'Permutasi P(5, 1) = ?', a: 5 }
          ];
          const p = poolP[this.getRandomInt(0, poolP.length - 1)];
          questionText = p.q;
          correctAnswer = p.a;
        }
        break;
      }

      // -------------------------------------------------------------
      // LEVEL 9: MODULO & FUNGSI KOMPOSISI
      // -------------------------------------------------------------
      case 9: {
        topic = 'Modulo & Komposisi';
        const type = this.getRandomInt(1, 3);
        if (type === 1) {
          const m = this.getRandomInt(5, 9);
          const q = this.getRandomInt(3, 7);
          const r = this.getRandomInt(1, m - 1);
          const num = q * m + r;
          questionText = `Hasil dari ${num} mod ${m} (sisa bagi) = ?`;
          correctAnswer = r;
        } else if (type === 2) {
          const u1 = this.getRandomInt(2, 5);
          const u2 = this.getRandomInt(1, 4);
          const v1 = this.getRandomInt(2, 4);
          const v2 = this.getRandomInt(1, 3);
          questionText = `Dot product vektor ( ${u1}, ${u2} ) · ( ${v1}, ${v2} ) = ?`;
          correctAnswer = u1 * v1 + u2 * v2;
        } else {
          const c = this.getRandomInt(1, 3);
          const a = this.getRandomInt(2, 3);
          const b = this.getRandomInt(1, 4);
          const x = this.getRandomInt(2, 4);
          const gx = x + c;
          questionText = `Jika f(x) = ${a}x + ${b} dan g(x) = x + ${c},\nnilai f(g(${x})) = ?`;
          correctAnswer = a * gx + b;
        }
        break;
      }

      // -------------------------------------------------------------
      // LEVEL 10: KALKULUS DASAR (TURUNAN & LIMIT)
      // -------------------------------------------------------------
      case 10: {
        topic = 'Kalkulus Pengantar';
        const type = this.getRandomInt(1, 3);
        if (type === 1) {
          const a = this.getRandomInt(2, 4);
          const b = this.getRandomInt(2, 6);
          const c = this.getRandomInt(1, 9);
          const x0 = this.getRandomInt(2, 4);
          questionText = `Jika f(x) = ${a}x² - ${b}x + ${c},\nnilai turunan f'(${x0}) = ?`;
          correctAnswer = 2 * a * x0 - b;
        } else if (type === 2) {
          const a = this.getRandomInt(2, 5);
          const b = this.getRandomInt(1, 6);
          questionText = `Hitung nilai: lim (x → ${a}) [ x² + ${b} ] = ?`;
          correctAnswer = a * a + b;
        } else {
          const a = this.getRandomInt(2, 5);
          const x0 = this.getRandomInt(1, 4);
          questionText = `Gradien garis singgung y = x² + ${a}x pada x = ${x0} adalah?`;
          correctAnswer = 2 * x0 + a;
        }
        break;
      }
    }

    const { options, correctIndex } = this.generateSmartDistractors(correctAnswer);

    return {
      type: quizType,
      level: clampedLevel,
      topic,
      questionText,
      options,
      correctIndex,
      correctAnswer,
      timeLimit: 14 // 14 detik untuk berpikir taktis
    };
  }

  static generateSmartDistractors(correct) {
    const picked = new Set([correct]);
    const deltas = [-1, 1, -2, 2, -3, 3, -4, 4];

    if (correct > 2 && Math.random() < 0.3) {
      picked.add(correct * 2);
    }
    if (correct > 3 && correct % 2 === 0 && Math.random() < 0.3) {
      picked.add(Math.floor(correct / 2));
    }

    while (picked.size < 4) {
      const delta = deltas[this.getRandomInt(0, deltas.length - 1)];
      let candidate = correct + delta;

      if (picked.has(candidate)) {
        candidate = correct + this.getRandomInt(5, 10) * (Math.random() > 0.5 ? 1 : -1);
      }
      picked.add(candidate);
    }

    picked.delete(correct);
    const options = Array.from(picked).slice(0, 3).map(String);
    const correctIndex = this.getRandomInt(0, 3);
    options.splice(correctIndex, 0, String(correct));

    return { options, correctIndex };
  }
}
