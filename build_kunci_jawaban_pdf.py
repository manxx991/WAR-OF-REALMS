import os
import sys
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
)
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica-Bold", 7.5)
        self.setFillColor(colors.HexColor("#475569"))

        # Header (pages > 1)
        if self._pageNumber > 1:
            self.drawString(
                36, 808, "WAR OF REALMS: MATH COMBAT ARENA  |  KUNCI JAWABAN KUIS MANA & REPARASI"
            )
            self.drawRightString(559, 808, "SMA/SMK & MAHASISWA BARU EDITION")
            self.setStrokeColor(colors.HexColor("#CBD5E1"))
            self.setLineWidth(0.6)
            self.line(36, 802, 559, 802)

        # Footer (all pages)
        self.setStrokeColor(colors.HexColor("#CBD5E1"))
        self.setLineWidth(0.6)
        self.line(36, 40, 559, 40)

        self.setFont("Helvetica", 7.5)
        self.setFillColor(colors.HexColor("#64748B"))
        self.drawString(36, 28, "Buku Kunci Jawaban Resmi | Path Proyek: C:\\GAME | Engine: HTML5 Canvas 2D")
        page_str = f"Halaman {self._pageNumber} dari {page_count}"
        self.drawRightString(559, 28, page_str)
        self.restoreState()

def build_pdf(filename):
    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        leftMargin=36,
        rightMargin=36,
        topMargin=46,
        bottomMargin=46,
        title="Kunci Jawaban Kuis Mana & Reparasi - War of Realms: Math Combat Arena",
        author="War of Realms Academic & Game Design Team"
    )

    styles = getSampleStyleSheet()

    # Palette
    c_primary = colors.HexColor("#0F172A")    # Slate 900
    c_accent = colors.HexColor("#0284C7")     # Sky 600
    c_header_bg = colors.HexColor("#1E293B")  # Slate 800
    c_subhead_bg = colors.HexColor("#F1F5F9") # Slate 100
    c_dark = colors.HexColor("#1E293B")
    c_bg_alt = colors.HexColor("#F8FAFC")
    c_border = colors.HexColor("#CBD5E1")

    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        textColor=c_primary,
        spaceAfter=3
    )

    subtitle_style = ParagraphStyle(
        'DocSubTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=14,
        textColor=c_accent,
        spaceAfter=8
    )

    h1_style = ParagraphStyle(
        'H1_Banner',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=13,
        textColor=colors.white
    )

    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=11.5,
        textColor=c_dark,
        spaceAfter=4
    )

    table_cell = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.8,
        leading=10.8,
        textColor=c_dark
    )

    table_cell_bold = ParagraphStyle(
        'TableCellBold',
        parent=table_cell,
        fontName='Helvetica-Bold'
    )

    table_cell_center = ParagraphStyle(
        'TableCellCenter',
        parent=table_cell,
        alignment=1
    )

    table_cell_center_bold = ParagraphStyle(
        'TableCellCenterBold',
        parent=table_cell_bold,
        alignment=1
    )

    table_header = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7.8,
        leading=10.8,
        textColor=colors.white,
        alignment=1
    )

    def section_banner(title_text, subtitle_text="", bg_color=c_header_bg):
        text = f"<b>{title_text.upper()}</b>"
        if subtitle_text:
            text += f" &nbsp;|&nbsp; <font size=7 color='#94A3B8'>{subtitle_text}</font>"
        p = Paragraph(text, h1_style)
        t = Table([[p]], colWidths=[523])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), bg_color),
            ('TOPPADDING', (0,0), (-1,-1), 4),
            ('BOTTOMPADDING', (0,0), (-1,-1), 4),
            ('LEFTPADDING', (0,0), (-1,-1), 6),
            ('RIGHTPADDING', (0,0), (-1,-1), 6),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ]))
        return t

    story = []

    # =========================================================================
    # HEADER / TITLE
    # =========================================================================
    story.append(Paragraph("WAR OF REALMS: MATH COMBAT ARENA", title_style))
    story.append(Paragraph("KUNCI JAWABAN LENGKAP & PANDUAN STRATEGI KUIS TAMBAH MANA & REPARASI BENTENG", subtitle_style))

    # Meta card
    meta_table = Table([
        [
            Paragraph("<b>Target Kurikulum:</b> SMA/SMK (Kelas 10-12) & Mahasiswa Baru (TPB / Sem 1-2)", table_cell),
            Paragraph("<b>Edisi Game:</b> Versi 4.0 Master Production", table_cell)
        ],
        [
            Paragraph("<b>Direktori Proyek:</b> C:\\GAME (HTML5 Canvas 2D Lane Defense)", table_cell),
            Paragraph("<b>File Generator:</b> src/KidsMathQuizGenerator.js & src/Game.js", table_cell)
        ],
        [
            Paragraph("<b>Fitur Kuis:</b> Kuis Tambah Mana [Hotkey Q] & Kuis Reparasi Benteng [Hotkey E]", table_cell),
            Paragraph("<b>Isi Dokumen:</b> Rumus Kilat, Solusi Per Sektor, Bank Soal Eksak & Lampiran", table_cell)
        ]
    ], colWidths=[275, 248])
    meta_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), c_subhead_bg),
        ('BOX', (0,0), (-1,-1), 0.8, c_border),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#E2E8F0")),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 8))

    # =========================================================================
    # BAB 1: MEKANISME DUAL KUIS (MANA BURST & BASE REPAIR)
    # =========================================================================
    story.append(section_banner("1. MEKANISME KUIS: TAMBAH MANA [Q] & REPARASI BENTENG [E]", "Sistem Taktis Lane Defense"))
    story.append(Spacer(1, 3))

    story.append(Paragraph(
        "Di dalam <b>War of Realms</b>, kalkulasi matematika adalah amunisi taktis utama. "
        "Pemain memiliki dua aksi kuis di dek pertempuran yang dapat dipicu secara instan. "
        "Kedua tombol memanggil generator matematika yang sama (<code>KidsMathQuizGenerator.generateQuestion(level, type)</code>) "
        "sesuai sektor yang sedang aktif (Level 1 s.d. 10), namun menghasilkan efek taktis berbeda:",
        body_style
    ))
    story.append(Spacer(1, 3))

    t_cmp = Table([
        [
            Paragraph("Parameter Taktis", table_header),
            Paragraph("Kuis Tambah Mana (MANA BURST)", table_header),
            Paragraph("Kuis Reparasi Benteng (BASE REPAIR)", table_header)
        ],
        [
            Paragraph("<b>Pemicu & Hotkey</b>", table_cell_bold),
            Paragraph("Tombol <b>[Q]</b> keyboard (atau klik tombol petir di kiri dek)", table_cell),
            Paragraph("Tombol <b>[E]</b> keyboard (atau klik tombol hati di kanan dek)", table_cell)
        ],
        [
            Paragraph("<b>Batas Penggunaan</b>", table_cell_bold),
            Paragraph("<b>Tanpa Batas</b> (bebas dipicu sepanjang pertempuran berlangsung)", table_cell),
            Paragraph("<b>Maksimal 3 Kali</b> per pertempuran (menjaga keseimbangan permainan)", table_cell)
        ],
        [
            Paragraph("<b>Reward Jawaban Benar</b>", table_cell_bold),
            Paragraph("Mana Instan: <b>+40 + (Level × 5) Mana</b><br/>"
                      "- Level 1: <b>+45 Mana</b> &nbsp;|&nbsp; Level 5: <b>+65 Mana</b><br/>"
                      "- Level 10: <b>+90 Mana</b> (Kapasitas maksimum: 200 Mana)", table_cell),
            Paragraph("Heal Base: <b>+25% dari Max HP Benteng Pemain</b><br/>"
                      "<code>playerCastle.hp = min(maxHp, hp + round(maxHp * 0.25))</code><br/>"
                      "Sangat penting untuk menjaga HP &gt;= 70% demi meraih <b>[3 BINTANG]</b>", table_cell)
        ],
        [
            Paragraph("<b>Waktu Berpikir</b>", table_cell_bold),
            Paragraph("<b>14 Detik</b> (waktu nyata)", table_cell),
            Paragraph("<b>14 Detik</b> (waktu nyata)", table_cell)
        ],
        [
            Paragraph("<b>Efek Slow-Motion</b>", table_cell_bold),
            Paragraph("Game melambat ke <b>0.1x speed</b> (waktu pertempuran lambat 10x lipat)", table_cell),
            Paragraph("Game melambat ke <b>0.1x speed</b> agar pemain tenang menghitung", table_cell)
        ],
        [
            Paragraph("<b>Penalti Salah / Timeout</b>", table_cell_bold),
            Paragraph("Dialog bergetar (<i>shake-wrong</i> 0.7s), audio 'wah-wah', kuis tertutup", table_cell),
            Paragraph("Dialog bergetar, kuis tertutup; kuota 3x TIDAK berkurang jika salah/timeout", table_cell)
        ],
        [
            Paragraph("<b>Pilihan Jawaban</b>", table_cell_bold),
            Paragraph("4 Pilihan Ganda: Hotkey <b>[A], [B], [C], [D]</b> atau <b>[1], [2], [3], [4]</b>", table_cell),
            Paragraph("4 Pilihan Ganda: Hotkey <b>[A], [B], [C], [D]</b> atau <b>[1], [2], [3], [4]</b>", table_cell)
        ]
    ], colWidths=[105, 209, 209])
    t_cmp.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_header_bg),
        ('BOX', (0,0), (-1,-1), 0.8, c_border),
        ('INNERGRID', (0,0), (-1,-1), 0.5, c_border),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, c_bg_alt]),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(t_cmp)
    story.append(Spacer(1, 8))

    # =========================================================================
    # BAB 2: KUNCI JAWABAN & FORMULA CEPAT LEVEL 1 - 10
    # =========================================================================
    story.append(section_banner("2. KUNCI JAWABAN & METODE HITUNG KILAT PER SEKTOR (LEVEL 1 - 10)", "Modul: KidsMathQuizGenerator.js"))
    story.append(Spacer(1, 4))

    # LEVEL 1
    t_l1 = Table([
        [
            Paragraph("<b>SEKTOR 1: ALJABAR LINEAR (SPLSV) — [Level 1]</b><br/><i>Persamaan Linear Satu Variabel</i>", table_cell_bold),
            Paragraph("<b>Reward:</b> <font color='#0284C7'><b>+45 MANA</b></font> &nbsp;|&nbsp; <font color='#059669'><b>+25% HEAL</b></font>", table_cell_center)
        ],
        [
            Paragraph(
                "<b>Pola 1: ax + b = c</b> (a: 2..6, x: 2..9, b: 3..15)<br/>"
                "- <b>Teks Soal:</b> <i>\"Jika ax + b = c, nilai x = ?\"</i><br/>"
                "- <b>Formula Kilat:</b> <b>x = (c - b) / a</b><br/>"
                "- <i>Contoh 1:</i> Jika 3x + 12 = 27, nilai x = ? -> (27 - 12) / 3 = 15 / 3 = <b>5</b>.<br/>"
                "- <i>Contoh 2:</i> Jika 5x + 10 = 45, nilai x = ? -> (45 - 10) / 5 = 35 / 5 = <b>7</b>.<br/>"
                "- <i>Contoh 3:</i> Jika 6x + 8 = 38, nilai x = ? -> (38 - 8) / 6 = 30 / 6 = <b>5</b>.",
                table_cell
            ),
            Paragraph(
                "<b>Pola 2: ax - b = c</b> (a: 2..5, x: 3..8, b: 4..16)<br/>"
                "- <b>Teks Soal:</b> <i>\"Jika ax - b = c, nilai x = ?\"</i><br/>"
                "- <b>Formula Kilat:</b> <b>x = (c + b) / a</b><br/>"
                "- <i>Contoh 1:</i> Jika 4x - 8 = 20, nilai x = ? -> (20 + 8) / 4 = 28 / 4 = <b>7</b>.<br/>"
                "- <i>Contoh 2:</i> Jika 3x - 15 = 9, nilai x = ? -> (9 + 15) / 3 = 24 / 3 = <b>8</b>.<br/><br/>"
                "<b>Pola 3: 2(x + a) = b</b> (a: 2..7, x: 3..10)<br/>"
                "- <b>Teks Soal:</b> <i>\"Selesaikan: 2(x + a) = b, x = ?\"</i><br/>"
                "- <b>Formula Kilat:</b> <b>x = (b / 2) - a</b><br/>"
                "- <i>Contoh:</i> 2(x + 5) = 26 -> x = (26 / 2) - 5 = 13 - 5 = <b>8</b>.",
                table_cell
            )
        ]
    ], colWidths=[260, 263])
    t_l1.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#E0F2FE")),
        ('BOX', (0,0), (-1,-1), 0.8, colors.HexColor("#BAE6FD")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, c_border),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_l1)
    story.append(Spacer(1, 4))

    # Page Break to ensure Clean 5-Page Layout
    story.append(PageBreak())

    # LEVEL 2
    t_l2 = Table([
        [
            Paragraph("<b>SEKTOR 2: EKSPONEN & BENTUK AKAR — [Level 2]</b><br/><i>Perpangkatan & Penjumlahan Akar Kuadrat</i>", table_cell_bold),
            Paragraph("<b>Reward:</b> <font color='#0284C7'><b>+50 MANA</b></font> &nbsp;|&nbsp; <font color='#059669'><b>+25% HEAL</b></font>", table_cell_center)
        ],
        [
            Paragraph(
                "<b>Pola 1: (2^a × 2^b) / 2^c = 2^(a+b-c)</b><br/>"
                "- <b>Teks Soal:</b> <i>\"Hitung: (2^a × 2^b) / 2^c = ?\"</i><br/>"
                "- <b>Formula Kilat:</b> Pangkat hasil = <b>(a + b - c)</b>. Nilai = <b>2^(a+b-c)</b>.<br/>"
                "- <i>Hafalan Pangkat 2:</i> 2^1=2, 2^2=4, 2^3=8, 2^4=16, 2^5=32, 2^6=64.<br/>"
                "- <i>Contoh 1:</i> (2^5 × 2^3) / 2^6 -> 2^(5+3-6) = 2^2 = <b>4</b>.<br/>"
                "- <i>Contoh 2:</i> (2^4 × 2^4) / 2^5 -> 2^(4+4-5) = 2^3 = <b>8</b>.<br/>"
                "- <i>Contoh 3:</i> (2^6 × 2^2) / 2^4 -> 2^(6+2-4) = 2^4 = <b>16</b>.",
                table_cell
            ),
            Paragraph(
                "<b>Pola 2: Penjumlahan Akar: sqrt(s1) + sqrt(s2)</b><br/>"
                "- <i>Daftar Kuadrat Pas di Game:</i><br/>"
                "  sqrt(16)=4, sqrt(25)=5, sqrt(36)=6, sqrt(49)=7, sqrt(64)=8, sqrt(81)=9.<br/>"
                "- <i>Contoh 1:</i> sqrt(36) + sqrt(49) = 6 + 7 = <b>13</b>.<br/>"
                "- <i>Contoh 2:</i> sqrt(64) + sqrt(81) = 8 + 9 = <b>17</b>.<br/><br/>"
                "<b>Pola 3: Persamaan Eksponen: base^(x+1) = Y</b><br/>"
                "- <b>Teks Soal:</b> <i>\"Jika base^(x+1) = Y, x = ?\"</i><br/>"
                "- <b>Formula Kilat:</b> Cari pangkat Y terhadap base, kurangi 1.<br/>"
                "- <i>Contoh:</i> 2^(x+1) = 32 -> 2^(x+1) = 2^5 -> x = 5 - 1 = <b>4</b>.<br/>"
                "- <i>Contoh 2:</i> 3^(x+1) = 81 -> 3^(x+1) = 3^4 -> x = 4 - 1 = <b>3</b>.",
                table_cell
            )
        ]
    ], colWidths=[260, 263])
    t_l2.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#E0F2FE")),
        ('BOX', (0,0), (-1,-1), 0.8, colors.HexColor("#BAE6FD")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, c_border),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_l2)
    story.append(Spacer(1, 4))

    # LEVEL 3
    t_l3 = Table([
        [
            Paragraph("<b>SEKTOR 3: LOGARITMA DASAR — [Level 3]</b><br/><i>Logaritma Basis 2, 3, 5 & Sifat Aljabar</i>", table_cell_bold),
            Paragraph("<b>Reward:</b> <font color='#0284C7'><b>+55 MANA</b></font> &nbsp;|&nbsp; <font color='#059669'><b>+25% HEAL</b></font>", table_cell_center)
        ],
        [
            Paragraph(
                "<b>Pola 1: log_base(val) = ?</b> (base in {2, 3, 5})<br/>"
                "- <b>Formula:</b> Cari pangkat p sehingga base^p = val.<br/>"
                "- log_2(8)=<b>3</b>, log_2(16)=<b>4</b>, log_2(32)=<b>5</b><br/>"
                "- log_3(9)=<b>2</b>, log_3(27)=<b>3</b>, log_3(81)=<b>4</b>, log_3(243)=<b>5</b><br/>"
                "- log_5(25)=<b>2</b>, log_5(125)=<b>3</b>, log_5(625)=<b>4</b><br/>"
                "- <i>Contoh:</i> log_3(81) = ? -> 3^4 = 81 -> Jawaban: <b>4</b>.",
                table_cell
            ),
            Paragraph(
                "<b>Pola 2: log_2(A) + log_2(B) = log_2(A × B)</b><br/>"
                "- <b>Formula Kilat:</b> Pangkat A + Pangkat B.<br/>"
                "- <i>Contoh:</i> log_2(16) + log_2(8) = 4 + 3 = <b>7</b>.<br/>"
                "- <i>Contoh 2:</i> log_2(8) + log_2(4) = 3 + 2 = <b>5</b>.<br/><br/>"
                "<b>Pola 3: log_3(A) - log_3(B) = log_3(A / B)</b><br/>"
                "- <b>Formula Kilat:</b> Pangkat A - Pangkat B.<br/>"
                "- <i>Contoh:</i> log_3(81) - log_3(9) = 4 - 2 = <b>2</b>.<br/>"
                "- <i>Contoh 2:</i> log_3(243) - log_3(27) = 5 - 3 = <b>2</b>.",
                table_cell
            )
        ]
    ], colWidths=[260, 263])
    t_l3.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#E0F2FE")),
        ('BOX', (0,0), (-1,-1), 0.8, colors.HexColor("#BAE6FD")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, c_border),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_l3)
    story.append(Spacer(1, 4))

    # LEVEL 4
    t_l4 = Table([
        [
            Paragraph("<b>SEKTOR 4: PERSAMAAN KUADRAT & FAKTORISASI — [Level 4]</b><br/><i>Bentuk: x^2 - bx + c = 0 dengan akar r1 dan r2 (r2 &gt; r1)</i>", table_cell_bold),
            Paragraph("<b>Reward:</b> <font color='#0284C7'><b>+60 MANA</b></font> &nbsp;|&nbsp; <font color='#059669'><b>+25% HEAL</b></font>", table_cell_center)
        ],
        [
            Paragraph(
                "<b>Pola 1: \"Akar terbesar dari x^2 - bx + c = 0 adalah?\"</b><br/>"
                "- <b>Solusi Cepat:</b> Faktorkan menjadi (x - r1)(x - r2) = 0.<br/>"
                "  Pilih akar yang nilainya <b>LEBIH BESAR</b> (r2).<br/>"
                "- <i>Contoh 1:</i> x^2 - 7x + 10 = 0 -> (x-2)(x-5)=0 -> Jawaban: <b>5</b>.<br/>"
                "- <i>Contoh 2:</i> x^2 - 9x + 20 = 0 -> (x-4)(x-5)=0 -> Jawaban: <b>5</b>.<br/>"
                "- <i>Contoh 3:</i> x^2 - 11x + 24 = 0 -> (x-3)(x-8)=0 -> Jawaban: <b>8</b>.<br/>"
                "- <i>Contoh 4:</i> x^2 - 10x + 21 = 0 -> (x-3)(x-7)=0 -> Jawaban: <b>7</b>.",
                table_cell
            ),
            Paragraph(
                "<b>Pola 2: \"Jumlah akar (x1 + x2) dari x^2 - bx + c = 0 adalah?\"</b><br/>"
                "- <b>TRIK KILAT 1 DETIK (Teorema Vieta):</b> x1 + x2 = <b>b</b>.<br/>"
                "  Cukup lihat angka di depan x (abaikan tanda minus)!<br/>"
                "- <i>Contoh:</i> Jumlah akar x^2 - 13x + 40 = 0 -> Langsung jawab <b>13</b>!<br/><br/>"
                "<b>Pola 3: \"Hasil kali akar (x1 × x2) dari x^2 - bx + c = 0 adalah?\"</b><br/>"
                "- <b>TRIK KILAT 1 DETIK (Teorema Vieta):</b> x1 × x2 = <b>c</b>.<br/>"
                "  Cukup lihat konstanta paling belakang persamaan!<br/>"
                "- <i>Contoh:</i> Hasil kali akar x^2 - 13x + 40 = 0 -> Langsung jawab <b>40</b>!",
                table_cell
            )
        ]
    ], colWidths=[260, 263])
    t_l4.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#E0F2FE")),
        ('BOX', (0,0), (-1,-1), 0.8, colors.HexColor("#BAE6FD")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, c_border),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_l4)
    story.append(Spacer(1, 4))

    # LEVEL 5
    t_l5 = Table([
        [
            Paragraph("<b>SEKTOR 5: BARISAN & DERET (ARITMATIKA & GEOMETRI) — [Level 5]</b><br/><i>Suku ke-n Aritmatika, Rasio Geometri, & Suku ke-5</i>", table_cell_bold),
            Paragraph("<b>Reward:</b> <font color='#0284C7'><b>+65 MANA</b></font> &nbsp;|&nbsp; <font color='#059669'><b>+25% HEAL</b></font>", table_cell_center)
        ],
        [
            Paragraph(
                "<b>Kategori A: Barisan Aritmatika (Suku ke-n / Un)</b><br/>"
                "- <b>Teks Soal:</b> <i>\"Suku ke-n (Un) dari barisan a, a+d, ... adalah?\"</i><br/>"
                "- <b>Formula Kilat:</b> <b>Un = a + (n - 1) × d</b><br/>"
                "- <i>Contoh 1:</i> Barisan 3, 7, 11, 15, ... suku ke-6 (U6) = ?<br/>"
                "  a = 3, d = 4 -> U6 = 3 + (5 × 4) = 3 + 20 = <b>23</b>.<br/>"
                "- <i>Contoh 2:</i> Barisan 2, 7, 12, ... suku ke-5 (U5) = ?<br/>"
                "  a = 2, d = 5 -> U5 = 2 + (4 × 5) = 2 + 20 = <b>22</b>.<br/>"
                "- <i>Contoh 3:</i> Barisan 5, 11, 17, ... suku ke-7 (U7) = ?<br/>"
                "  a = 5, d = 6 -> U7 = 5 + (6 × 6) = 5 + 36 = <b>41</b>.",
                table_cell
            ),
            Paragraph(
                "<b>Kategori B: Deret Geometri (Rasio & Suku U5)</b><br/>"
                "- <b>Tipe 1 (Rasio r):</b> <i>\"Rasio (r) dari deret geometri ... adalah?\"</i><br/>"
                "  Formula: r = U2 / U1 (Di game r selalu <b>2</b> atau <b>3</b>).<br/>"
                "  Contoh: Deret 3, 6, 12, ... -> r = 6/3 = <b>2</b>.<br/><br/>"
                "- <b>Tipe 2 (Suku ke-5 / U5):</b> <i>\"Suku ke-5 (U_5) dari deret geometri ...?\"</i><br/>"
                "  <b>Formula Kilat:</b> <b>U5 = a × r^4</b>.<br/>"
                "  - Jika r = 2 -> r^4 = 16 -> <b>U5 = a × 16</b>.<br/>"
                "  - Jika r = 3 -> r^4 = 81 -> <b>U5 = a × 81</b>.<br/>"
                "  <i>Contoh:</i> Deret 2, 4, 8, ... -> a=2, r=2 -> U5 = 2 × 16 = <b>32</b>.<br/>"
                "  <i>Contoh:</i> Deret 3, 6, 12, ... -> a=3, r=2 -> U5 = 3 × 16 = <b>48</b>.<br/>"
                "  <i>Contoh:</i> Deret 2, 6, 18, ... -> a=2, r=3 -> U5 = 2 × 81 = <b>162</b>.",
                table_cell
            )
        ]
    ], colWidths=[260, 263])
    t_l5.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#E0F2FE")),
        ('BOX', (0,0), (-1,-1), 0.8, colors.HexColor("#BAE6FD")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, c_border),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_l5)
    story.append(Spacer(1, 6))

    # Page Break for Level 6-8
    story.append(PageBreak())

    # LEVEL 6 (TRIGONOMETRI)
    t_l6_head = Table([
        [
            Paragraph("<b>SEKTOR 6: TRIGONOMETRI SUDUT ISTIMEWA — [Level 6]</b><br/><i>Bank Soal Eksak: Generator memilih 1 dari 8 soal tetap berikut!</i>", table_cell_bold),
            Paragraph("<b>Reward:</b> <font color='#0284C7'><b>+70 MANA</b></font> &nbsp;|&nbsp; <font color='#059669'><b>+25% HEAL</b></font>", table_cell_center)
        ]
    ], colWidths=[360, 163])
    t_l6_head.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#E0F2FE")),
        ('BOX', (0,0), (-1,-1), 0.8, colors.HexColor("#BAE6FD")),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_l6_head)
    story.append(Spacer(1, 3))

    t_l6 = Table([
        [
            Paragraph("No", table_header),
            Paragraph("Teks Soal Eksak di Layar Game", table_header),
            Paragraph("Substitusi Nilai Sudut", table_header),
            Paragraph("KUNCI JAWABAN", table_header)
        ],
        [
            Paragraph("1", table_cell_center_bold),
            Paragraph("Nilai dari 2 * sin(30 deg) + 2 * cos(60 deg) = ?", table_cell),
            Paragraph("2(0.5) + 2(0.5) = 1 + 1", table_cell),
            Paragraph("<b>2</b>", table_cell_center_bold)
        ],
        [
            Paragraph("2", table_cell_center_bold),
            Paragraph("Nilai dari 4 * tan(45 deg) - 2 * sin(90 deg) = ?", table_cell),
            Paragraph("4(1) - 2(1) = 4 - 2", table_cell),
            Paragraph("<b>2</b>", table_cell_center_bold)
        ],
        [
            Paragraph("3", table_cell_center_bold),
            Paragraph("Nilai dari 3 * cos(0 deg) + 2 * sin(90 deg) = ?", table_cell),
            Paragraph("3(1) + 2(1) = 3 + 2", table_cell),
            Paragraph("<b>5</b>", table_cell_center_bold)
        ],
        [
            Paragraph("4", table_cell_center_bold),
            Paragraph("Hitung: 6 * (sin^2(30 deg) + cos^2(30 deg)) = ?", table_cell),
            Paragraph("Identitas sin^2θ + cos^2θ = 1 -> 6 * (1)", table_cell),
            Paragraph("<b>6</b>", table_cell_center_bold)
        ],
        [
            Paragraph("5", table_cell_center_bold),
            Paragraph("Nilai dari 2 * tan(45 deg) × cos(60 deg) = ?", table_cell),
            Paragraph("2(1) × 0.5 = 1", table_cell),
            Paragraph("<b>1</b>", table_cell_center_bold)
        ],
        [
            Paragraph("6", table_cell_center_bold),
            Paragraph("Hitung: 4 * sin(30 deg) + 3 * tan(45 deg) = ?", table_cell),
            Paragraph("4(0.5) + 3(1) = 2 + 3", table_cell),
            Paragraph("<b>5</b>", table_cell_center_bold)
        ],
        [
            Paragraph("7", table_cell_center_bold),
            Paragraph("Hitung: 8 * sin(30 deg) * cos(60 deg) = ?", table_cell),
            Paragraph("8 × 0.5 × 0.5 = 8 × 0.25", table_cell),
            Paragraph("<b>2</b>", table_cell_center_bold)
        ],
        [
            Paragraph("8", table_cell_center_bold),
            Paragraph("Nilai dari 5 * cos(0 deg) - 3 * sin(0 deg) = ?", table_cell),
            Paragraph("5(1) - 3(0) = 5 - 0", table_cell),
            Paragraph("<b>5</b>", table_cell_center_bold)
        ]
    ], colWidths=[28, 255, 160, 80])
    t_l6.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_header_bg),
        ('BOX', (0,0), (-1,-1), 0.8, c_border),
        ('INNERGRID', (0,0), (-1,-1), 0.5, c_border),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, c_bg_alt]),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(t_l6)
    story.append(Spacer(1, 6))

    # LEVEL 7 (MATRIKS)
    t_l7 = Table([
        [
            Paragraph("<b>SEKTOR 7: MATRIKS & DETERMINAN 2x2 — [Level 7]</b><br/><i>Matriks: M = [ [a, b], [c, d] ]</i>", table_cell_bold),
            Paragraph("<b>Reward:</b> <font color='#0284C7'><b>+75 MANA</b></font> &nbsp;|&nbsp; <font color='#059669'><b>+25% HEAL</b></font>", table_cell_center)
        ],
        [
            Paragraph(
                "<b>Pola 1: Determinan Matriks 2x2: | a b | / | c d |</b><br/>"
                "- <b>Formula Kilat:</b> <b>det = (a × d) - (b × c)</b><br/>"
                "- Kalikan diagonal utama (a*d), kurangi diagonal samping (b*c).<br/>"
                "- <i>Contoh 1:</i> | 5  2 | / | 3  4 | -> (5×4) - (2×3) = 20 - 6 = <b>14</b>.<br/>"
                "- <i>Contoh 2:</i> | 6  1 | / | 2  5 | -> (6×5) - (1×2) = 30 - 2 = <b>28</b>.<br/>"
                "- <i>Contoh 3:</i> | 7  3 | / | 2  4 | -> (7×4) - (3×2) = 28 - 6 = <b>22</b>.",
                table_cell
            ),
            Paragraph(
                "<b>Pola 2: Trace Matriks (Jumlah Diagonal Utama)</b><br/>"
                "- <b>Formula Kilat:</b> <b>Trace = a + d</b> (Abaikan b dan c!)<br/>"
                "- <i>Contoh 1:</i> Trace [ [7, 3], [2, 5] ] -> 7 + 5 = <b>12</b>.<br/>"
                "- <i>Contoh 2:</i> Trace [ [9, 4], [1, 8] ] -> 9 + 8 = <b>17</b>.<br/><br/>"
                "<b>Pola 3: Mencari Elemen x pada Determinan</b><br/>"
                "- Bentuk Soal: det | x  b | / | c  d | = det, x = ? (Di kode: b=2, c=3)<br/>"
                "- <b>Formula Kilat:</b> <b>x = (det + 6) / d</b><br/>"
                "- <i>Contoh 1:</i> Jika det | x  2 | / | 3  4 | = 10 -> x = (10+6)/4 = 16/4 = <b>4</b>.<br/>"
                "- <i>Contoh 2:</i> Jika det | x  2 | / | 3  5 | = 9 -> x = (9+6)/5 = 15/5 = <b>3</b>.",
                table_cell
            )
        ]
    ], colWidths=[260, 263])
    t_l7.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#E0F2FE")),
        ('BOX', (0,0), (-1,-1), 0.8, colors.HexColor("#BAE6FD")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, c_border),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_l7)
    story.append(Spacer(1, 6))

    # LEVEL 8 (KOMBINATORIKA)
    t_l8_head = Table([
        [
            Paragraph("<b>SEKTOR 8: KOMBINATORIKA & FAKTORIAL — [Level 8]</b><br/><i>Bank Soal Eksak: Generator memilih 1 dari 14 soal tetap di bawah ini!</i>", table_cell_bold),
            Paragraph("<b>Reward:</b> <font color='#0284C7'><b>+80 MANA</b></font> &nbsp;|&nbsp; <font color='#059669'><b>+25% HEAL</b></font>", table_cell_center)
        ]
    ], colWidths=[360, 163])
    t_l8_head.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#E0F2FE")),
        ('BOX', (0,0), (-1,-1), 0.8, colors.HexColor("#BAE6FD")),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_l8_head)
    story.append(Spacer(1, 3))

    t_l8 = Table([
        [
            Paragraph("Kategori", table_header),
            Paragraph("Teks Soal Eksak di Layar Game", table_header),
            Paragraph("Perhitungan Matematis", table_header),
            Paragraph("KUNCI JAWABAN", table_header)
        ],
        [
            Paragraph("Faktorial", table_cell_bold),
            Paragraph("Hitung: 5! / 4! = ?", table_cell),
            Paragraph("5! / 4! = 5", table_cell),
            Paragraph("<b>5</b>", table_cell_center_bold)
        ],
        [
            Paragraph("Faktorial", table_cell_bold),
            Paragraph("Hitung: 6! / 5! = ?", table_cell),
            Paragraph("6! / 5! = 6", table_cell),
            Paragraph("<b>6</b>", table_cell_center_bold)
        ],
        [
            Paragraph("Faktorial", table_cell_bold),
            Paragraph("Hitung: 5! / 3! = ?", table_cell),
            Paragraph("5 × 4 = 20", table_cell),
            Paragraph("<b>20</b>", table_cell_center_bold)
        ],
        [
            Paragraph("Faktorial", table_cell_bold),
            Paragraph("Hitung: 4! / 2! = ?", table_cell),
            Paragraph("4 × 3 = 12", table_cell),
            Paragraph("<b>12</b>", table_cell_center_bold)
        ],
        [
            Paragraph("Faktorial", table_cell_bold),
            Paragraph("Hitung: 4! = ?", table_cell),
            Paragraph("4 × 3 × 2 × 1 = 24", table_cell),
            Paragraph("<b>24</b>", table_cell_center_bold)
        ],
        [
            Paragraph("Kombinasi", table_cell_bold),
            Paragraph("Kombinasi C(4, 2) = ?", table_cell),
            Paragraph("(4 × 3) / (2 × 1) = 6", table_cell),
            Paragraph("<b>6</b>", table_cell_center_bold)
        ],
        [
            Paragraph("Kombinasi", table_cell_bold),
            Paragraph("Kombinasi C(5, 2) = ?", table_cell),
            Paragraph("(5 × 4) / (2 × 1) = 10", table_cell),
            Paragraph("<b>10</b>", table_cell_center_bold)
        ],
        [
            Paragraph("Kombinasi", table_cell_bold),
            Paragraph("Kombinasi C(5, 3) = ?", table_cell),
            Paragraph("C(5, 3) = C(5, 2) = 10", table_cell),
            Paragraph("<b>10</b>", table_cell_center_bold)
        ],
        [
            Paragraph("Kombinasi", table_cell_bold),
            Paragraph("Kombinasi C(6, 2) = ?", table_cell),
            Paragraph("(6 × 5) / (2 × 1) = 15", table_cell),
            Paragraph("<b>15</b>", table_cell_center_bold)
        ],
        [
            Paragraph("Kombinasi", table_cell_bold),
            Paragraph("Kombinasi C(4, 3) = ?", table_cell),
            Paragraph("4! / (3! * 1!) = 4", table_cell),
            Paragraph("<b>4</b>", table_cell_center_bold)
        ],
        [
            Paragraph("Permutasi", table_cell_bold),
            Paragraph("Permutasi P(4, 2) = ?", table_cell),
            Paragraph("4 × 3 = 12", table_cell),
            Paragraph("<b>12</b>", table_cell_center_bold)
        ],
        [
            Paragraph("Permutasi", table_cell_bold),
            Paragraph("Permutasi P(5, 2) = ?", table_cell),
            Paragraph("5 × 4 = 20", table_cell),
            Paragraph("<b>20</b>", table_cell_center_bold)
        ],
        [
            Paragraph("Permutasi", table_cell_bold),
            Paragraph("Permutasi P(3, 2) = ?", table_cell),
            Paragraph("3 × 2 = 6", table_cell),
            Paragraph("<b>6</b>", table_cell_center_bold)
        ],
        [
            Paragraph("Permutasi", table_cell_bold),
            Paragraph("Permutasi P(5, 1) = ?", table_cell),
            Paragraph("5", table_cell),
            Paragraph("<b>5</b>", table_cell_center_bold)
        ]
    ], colWidths=[70, 215, 158, 80])
    t_l8.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_header_bg),
        ('BOX', (0,0), (-1,-1), 0.8, c_border),
        ('INNERGRID', (0,0), (-1,-1), 0.5, c_border),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, c_bg_alt]),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(t_l8)
    story.append(Spacer(1, 6))

    # Page Break for Level 9-10 & Cheat Sheet
    story.append(PageBreak())

    # LEVEL 9 (MODULO, VEKTOR, KOMPOSISI)
    t_l9 = Table([
        [
            Paragraph("<b>SEKTOR 9: MODULO, VEKTOR & FUNGSI KOMPOSISI — [Level 9]</b><br/><i>Sisa Bagi, Perkalian Titik (Dot Product), dan Evaluasi f(g(x))</i>", table_cell_bold),
            Paragraph("<b>Reward:</b> <font color='#0284C7'><b>+85 MANA</b></font> &nbsp;|&nbsp; <font color='#059669'><b>+25% HEAL</b></font>", table_cell_center)
        ],
        [
            Paragraph(
                "<b>Pola 1: Aritmatika Modulo (Sisa Bagi)</b><br/>"
                "- <b>Teks Soal:</b> <i>\"Hasil dari N mod m (sisa bagi) = ?\"</i><br/>"
                "- <b>Formula Kilat:</b> Kurangi N dengan kelipatan m terbesar di bawah N.<br/>"
                "- <i>Contoh 1:</i> 31 mod 7 = ? -> 31 - (4×7) = 31 - 28 = <b>3</b>.<br/>"
                "- <i>Contoh 2:</i> 43 mod 8 = ? -> 43 - (5×8) = 43 - 40 = <b>3</b>.<br/>"
                "- <i>Contoh 3:</i> 52 mod 6 = ? -> 52 - (8×6) = 52 - 48 = <b>4</b>.<br/><br/>"
                "<b>Pola 2: Dot Product Vektor: ( u1, u2 ) * ( v1, v2 )</b><br/>"
                "- <b>Formula Kilat:</b> <b>u1*v1 + u2*v2</b><br/>"
                "- <i>Contoh 1:</i> ( 3, 2 ) * ( 4, 1 ) -> (3×4) + (2×1) = 12 + 2 = <b>14</b>.<br/>"
                "- <i>Contoh 2:</i> ( 4, 3 ) * ( 2, 3 ) -> (4×2) + (3×3) = 8 + 9 = <b>17</b>.<br/>"
                "- <i>Contoh 3:</i> ( 5, 2 ) * ( 3, 2 ) -> (5×3) + (2×2) = 15 + 4 = <b>19</b>.",
                table_cell
            ),
            Paragraph(
                "<b>Pola 3: Fungsi Komposisi f(g(x))</b><br/>"
                "- <b>Bentuk:</b> f(x) = ax + b dan g(x) = x + c.<br/>"
                "- <b>Teks Soal:</b> <i>\"nilai f(g(x)) = ?\"</i><br/>"
                "- <b>Formula 2 Langkah:</b><br/>"
                "  1. Hitung <b>g(x) = x + c</b>.<br/>"
                "  2. Masukkan ke f: <b>a × g(x) + b</b>.<br/>"
                "- <i>Contoh 1:</i> f(x) = 2x + 3, g(x) = x + 1, cari f(g(3)):<br/>"
                "  g(3) = 3 + 1 = 4 -> f(4) = 2(4) + 3 = 8 + 3 = <b>11</b>.<br/>"
                "- <i>Contoh 2:</i> f(x) = 3x + 2, g(x) = x + 2, cari f(g(2)):<br/>"
                "  g(2) = 2 + 2 = 4 -> f(4) = 3(4) + 2 = 12 + 2 = <b>14</b>.<br/>"
                "- <i>Contoh 3:</i> f(x) = 2x + 4, g(x) = x + 3, cari f(g(4)):<br/>"
                "  g(4) = 4 + 3 = 7 -> f(7) = 2(7) + 4 = 14 + 4 = <b>18</b>.",
                table_cell
            )
        ]
    ], colWidths=[260, 263])
    t_l9.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#E0F2FE")),
        ('BOX', (0,0), (-1,-1), 0.8, colors.HexColor("#BAE6FD")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, c_border),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_l9)
    story.append(Spacer(1, 4))

    # LEVEL 10 (KALKULUS)
    t_l10 = Table([
        [
            Paragraph("<b>SEKTOR 10: PENGANTAR KALKULUS (TURUNAN & LIMIT) — [Level 10 / APEX]</b><br/><i>Turunan Polinomial f'(x0), Limit Aljabar, Gradien Garis Singgung</i>", table_cell_bold),
            Paragraph("<b>Reward:</b> <font color='#0284C7'><b>+90 MANA (MAX)</b></font> &nbsp;|&nbsp; <font color='#059669'><b>+25% HEAL</b></font>", table_cell_center)
        ],
        [
            Paragraph(
                "<b>Pola 1: Nilai Turunan Polinomial f'(x0)</b><br/>"
                "- Fungsi: f(x) = ax^2 - bx + c.<br/>"
                "- Turunan: f'(x) = 2ax - b (Konstanta c hilang).<br/>"
                "- <b>TRIK KILAT:</b> <b>2 * a * x0 - b</b>.<br/>"
                "- <i>Contoh 1:</i> f(x) = 3x^2 - 4x + 5, cari f'(2):<br/>"
                "  f'(2) = 2(3)(2) - 4 = 12 - 4 = <b>8</b>.<br/>"
                "- <i>Contoh 2:</i> f(x) = 2x^2 - 5x + 9, cari f'(3):<br/>"
                "  f'(3) = 2(2)(3) - 5 = 12 - 5 = <b>7</b>.<br/>"
                "- <i>Contoh 3:</i> f(x) = 4x^2 - 6x + 2, cari f'(2):<br/>"
                "  f'(2) = 2(4)(2) - 6 = 16 - 6 = <b>10</b>.",
                table_cell
            ),
            Paragraph(
                "<b>Pola 2: Limit Aljabar: lim (x -> a) [ x^2 + b ]</b><br/>"
                "- <b>TRIK KILAT 1 DETIK:</b> Langsung masukkan a -> <b>a^2 + b</b>.<br/>"
                "- <i>Contoh 1:</i> lim (x -> 3) [ x^2 + 4 ] -> 3^2 + 4 = 9 + 4 = <b>13</b>.<br/>"
                "- <i>Contoh 2:</i> lim (x -> 4) [ x^2 + 5 ] -> 4^2 + 5 = 16 + 5 = <b>21</b>.<br/>"
                "- <i>Contoh 3:</i> lim (x -> 5) [ x^2 + 2 ] -> 5^2 + 2 = 25 + 2 = <b>27</b>.<br/><br/>"
                "<b>Pola 3: Gradien Garis Singgung y = x^2 + ax pada x = x0</b><br/>"
                "- Turunan: m = y' = 2x + a.<br/>"
                "- <b>TRIK KILAT:</b> <b>2 * x0 + a</b>.<br/>"
                "- <i>Contoh 1:</i> y = x^2 + 3x pada x = 2 -> 2(2) + 3 = 4 + 3 = <b>7</b>.<br/>"
                "- <i>Contoh 2:</i> y = x^2 + 4x pada x = 3 -> 2(3) + 4 = 6 + 4 = <b>10</b>.<br/>"
                "- <i>Contoh 3:</i> y = x^2 + 5x pada x = 4 -> 2(4) + 5 = 8 + 5 = <b>13</b>.",
                table_cell
            )
        ]
    ], colWidths=[260, 263])
    t_l10.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#E0F2FE")),
        ('BOX', (0,0), (-1,-1), 0.8, colors.HexColor("#BAE6FD")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, c_border),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_l10)
    story.append(Spacer(1, 8))

    # =========================================================================
    # BAB 3: CHEAT SHEET PERTEMPURAN (TABEL RANGKUMAN CEPAT)
    # =========================================================================
    story.append(section_banner("3. CHEAT SHEET TAKTIS: RUMUS MENTAL MATH KILAT (< 5 DETIK)"))
    story.append(Spacer(1, 3))

    t_cheat = Table([
        [
            Paragraph("Lvl", table_header),
            Paragraph("Materi & Sektor", table_header),
            Paragraph("Bentuk Persamaan Soal di Layar", table_header),
            Paragraph("Rumus Mental Math Instan di Otak", table_header)
        ],
        [
            Paragraph("<b>1</b>", table_cell_center_bold),
            Paragraph("Aljabar Linear", table_cell),
            Paragraph("ax + b = c &nbsp;|&nbsp; ax - b = c &nbsp;|&nbsp; 2(x+a) = b", table_cell),
            Paragraph("<b>x = (c - b)/a</b> &nbsp;|&nbsp; <b>x = (c + b)/a</b> &nbsp;|&nbsp; <b>x = (b/2) - a</b>", table_cell_bold)
        ],
        [
            Paragraph("<b>2</b>", table_cell_center_bold),
            Paragraph("Eksponen & Akar", table_cell),
            Paragraph("(2^a × 2^b)/2^c &nbsp;|&nbsp; sqrt(s1) + sqrt(s2) &nbsp;|&nbsp; base^(x+1)=Y", table_cell),
            Paragraph("<b>2^(a+b-c)</b> &nbsp;|&nbsp; <b>akar kuadrat pas</b> &nbsp;|&nbsp; <b>pangkat Y - 1</b>", table_cell_bold)
        ],
        [
            Paragraph("<b>3</b>", table_cell_center_bold),
            Paragraph("Logaritma Dasar", table_cell),
            Paragraph("log_b(val) &nbsp;|&nbsp; log_2 A + log_2 B &nbsp;|&nbsp; log_3 A - log_3 B", table_cell),
            Paragraph("<b>Pangkat basis</b> &nbsp;|&nbsp; <b>Jumlah pangkat</b> &nbsp;|&nbsp; <b>Selisih pangkat</b>", table_cell_bold)
        ],
        [
            Paragraph("<b>4</b>", table_cell_center_bold),
            Paragraph("Persamaan Kuadrat", table_cell),
            Paragraph("x^2 - bx + c = 0 (Akar terbesar, x1+x2, x1*x2)", table_cell),
            Paragraph("<b>Faktor terbesar</b> &nbsp;|&nbsp; <b>x1+x2 = b</b> &nbsp;|&nbsp; <b>x1*x2 = c</b>", table_cell_bold)
        ],
        [
            Paragraph("<b>5</b>", table_cell_center_bold),
            Paragraph("Barisan & Deret", table_cell),
            Paragraph("Aritmatika Un &nbsp;|&nbsp; Geometri Rasio & Suku U5", table_cell),
            Paragraph("<b>Un = a + (n-1)d</b> &nbsp;|&nbsp; <b>r = 2 atau 3</b> &nbsp;|&nbsp; <b>U5 = a × 16 (atau 81)</b>", table_cell_bold)
        ],
        [
            Paragraph("<b>6</b>", table_cell_center_bold),
            Paragraph("Trigonometri", table_cell),
            Paragraph("8 Soal Tetap Sudut Istimewa (0 deg, 30 deg, 45 deg, 60 deg, 90 deg)", table_cell),
            Paragraph("<b>Hafal 8 soal di Bab 2</b> (Hasilnya selalu 1, 2, 5, atau 6)", table_cell_bold)
        ],
        [
            Paragraph("<b>7</b>", table_cell_center_bold),
            Paragraph("Matriks 2x2", table_cell),
            Paragraph("det | a b | / | c d | &nbsp;|&nbsp; Trace &nbsp;|&nbsp; Cari elemen x", table_cell),
            Paragraph("<b>(a*d) - (b*c)</b> &nbsp;|&nbsp; <b>a + d</b> &nbsp;|&nbsp; <b>x = (det + 6) / d</b>", table_cell_bold)
        ],
        [
            Paragraph("<b>8</b>", table_cell_center_bold),
            Paragraph("Kombinatorika", table_cell),
            Paragraph("14 Soal Tetap: Faktorial, C(n,r), P(n,r)", table_cell),
            Paragraph("<b>Hafal 14 soal di Bab 2</b> (Hasilnya: 4, 5, 6, 10, 12, 15, 20, 24)", table_cell_bold)
        ],
        [
            Paragraph("<b>9</b>", table_cell_center_bold),
            Paragraph("Modulo & Vektor", table_cell),
            Paragraph("N mod m &nbsp;|&nbsp; (u1,u2)*(v1,v2) &nbsp;|&nbsp; f(g(x))", table_cell),
            Paragraph("<b>Sisa bagi N/m</b> &nbsp;|&nbsp; <b>u1*v1 + u2*v2</b> &nbsp;|&nbsp; <b>a*(x+c) + b</b>", table_cell_bold)
        ],
        [
            Paragraph("<b>10</b>", table_cell_center_bold),
            Paragraph("Kalkulus Pengantar", table_cell),
            Paragraph("f'(x0) dari ax^2-bx+c &nbsp;|&nbsp; lim(x^2+b) &nbsp;|&nbsp; gradien m", table_cell),
            Paragraph("<b>2*a*x0 - b</b> &nbsp;|&nbsp; <b>a^2 + b</b> &nbsp;|&nbsp; <b>2*x0 + a</b>", table_cell_bold)
        ]
    ], colWidths=[28, 92, 198, 205])
    t_cheat.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_header_bg),
        ('BOX', (0,0), (-1,-1), 0.8, c_border),
        ('INNERGRID', (0,0), (-1,-1), 0.5, c_border),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, c_bg_alt]),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(t_cheat)
    story.append(Spacer(1, 6))

    # Page Break for Lampiran & Hotkey
    story.append(PageBreak())

    # =========================================================================
    # BAB 4: LAMPIRAN REFERENSI EDISI ARSIP (KIDS EDITION / SD FASE A)
    # =========================================================================
    story.append(section_banner("4. LAMPIRAN: KUNCI JAWABAN EDISI DASAR (ARSIP KIDS EDITION / SD)", "Dokumen: prd_lengkap_game_pixel_lane_defense_kids_edition.md", colors.HexColor("#334155")))
    story.append(Spacer(1, 3))

    story.append(Paragraph(
        "Sebagai dokumentasi lengkap proyek <code>C:\\GAME</code>, berikut dicantumkan kunci jawaban "
        "dari arsip perancangan awal ketika game ditujukan untuk fase ramah anak (SD Kelas 1-2). "
        "Pada edisi arsip ini, tombol kuis Mana dan Reparasi memiliki perbedaan bentuk operasi hitung:",
        body_style
    ))
    story.append(Spacer(1, 3))

    t_kids = Table([
        [
            Paragraph("Lvl", table_header),
            Paragraph("Materi Edisi Anak", table_header),
            Paragraph("Perbedaan Soal Kuis Mana vs Reparasi (Kids)", table_header),
            Paragraph("Rumus & Kunci Jawaban Pasti", table_header)
        ],
        [
            Paragraph("<b>1</b>", table_cell_center_bold),
            Paragraph("Tambah/Kurang Sederhana (Hasil <= 5)", table_cell),
            Paragraph("- Mana: a + b = ?<br/>- Reparasi: a - b = ?", table_cell),
            Paragraph("<b>Kunci Mana:</b> a + b (hasil <= 5)<br/><b>Kunci Reparasi:</b> a - b", table_cell)
        ],
        [
            Paragraph("<b>2</b>", table_cell_center_bold),
            Paragraph("Penjumlahan Satuan (Hasil <= 10)", table_cell),
            Paragraph("Kuis Mana & Reparasi: a + b = ?", table_cell),
            Paragraph("<b>Kunci:</b> a + b (angka 2-6 ditambah 1-4)", table_cell)
        ],
        [
            Paragraph("<b>3</b>", table_cell_center_bold),
            Paragraph("Pengurangan Satuan (Angka 1-10)", table_cell),
            Paragraph("Kuis Mana & Reparasi: a - b = ?", table_cell),
            Paragraph("<b>Kunci:</b> a - b (angka selalu positif)", table_cell)
        ],
        [
            Paragraph("<b>4</b>", table_cell_center_bold),
            Paragraph("Menghitung Belasan (10 + Satuan)", table_cell),
            Paragraph("- <b>Mana:</b> 10 + unit = ?<br/>- <b>Reparasi:</b> (10 + unit) - 10 = ?", table_cell),
            Paragraph("<b>Kunci Mana:</b> 10 + unit (misal 10+7=17)<br/><b>Kunci Reparasi:</b> unit (misal 17-10=7)", table_cell)
        ],
        [
            Paragraph("<b>5</b>", table_cell_center_bold),
            Paragraph("Tebak Urutan Angka Maju (+1)", table_cell),
            Paragraph("x, x+1, x+2, ...?", table_cell),
            Paragraph("<b>Kunci:</b> x + 3 (angka lanjutan)", table_cell)
        ],
        [
            Paragraph("<b>6</b>", table_cell_center_bold),
            Paragraph("Penjumlahan Belasan (Hasil <= 20)", table_cell),
            Paragraph("a + b = ? (a: 5..10, b: 2..8)", table_cell),
            Paragraph("<b>Kunci:</b> a + b (hasil antara 7 s.d. 18)", table_cell)
        ],
        [
            Paragraph("<b>7</b>", table_cell_center_bold),
            Paragraph("Kelipatan Ceria (Tabel 2 & 5)", table_cell),
            Paragraph("base × multiplier = ? (base 2 atau 5)", table_cell),
            Paragraph("<b>Kunci:</b> base × mult (tabel perkalian 2 atau 5)", table_cell)
        ],
        [
            Paragraph("<b>8</b>", table_cell_center_bold),
            Paragraph("Pengurangan Belasan - Satuan", table_cell),
            Paragraph("a - b = ? (a: 12..18, b: 2..6)", table_cell),
            Paragraph("<b>Kunci:</b> a - b", table_cell)
        ],
        [
            Paragraph("<b>9</b>", table_cell_center_bold),
            Paragraph("Pola Loncat Bilangan (Lompat 2 atau 5)", table_cell),
            Paragraph("s, s+step, s+2*step, ...?", table_cell),
            Paragraph("<b>Kunci:</b> s + 3*step", table_cell)
        ],
        [
            Paragraph("<b>10</b>", table_cell_center_bold),
            Paragraph("Perkalian Tabel 2, 3, dan 10", table_cell),
            Paragraph("a × b = ? (a in {2, 3, 10}, b: 2..6)", table_cell),
            Paragraph("<b>Kunci:</b> a × b", table_cell)
        ]
    ], colWidths=[28, 122, 195, 178])
    t_kids.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#475569")),
        ('BOX', (0,0), (-1,-1), 0.8, c_border),
        ('INNERGRID', (0,0), (-1,-1), 0.5, c_border),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, c_bg_alt]),
        ('TOPPADDING', (0,0), (-1,-1), 2.2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.2),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(t_kids)
    story.append(Spacer(1, 10))

    # =========================================================================
    # BAB 5: PANDUAN HOTKEY & ERGONOMI KONTROL CEPAT
    # =========================================================================
    story.append(section_banner("5. PANDUAN HOTKEY KEYBOARD LENGKAP & EKSEKUSI TAKTIS", "Ergonomi Bermain Cepat Desktop/Laptop", colors.HexColor("#0284C7")))
    story.append(Spacer(1, 3))

    t_hotkey = Table([
        [
            Paragraph("Tombol Hotkey", table_header),
            Paragraph("Fungsi di Dalam Pertempuran", table_header),
            Paragraph("Rekomendasi Eksekusi & Sinergi Pasukan", table_header)
        ],
        [
            Paragraph("<b>[ Q ]</b>", table_cell_center_bold),
            Paragraph("<b>Buka Kuis Mana (MANA BURST)</b>", table_cell),
            Paragraph("Picu saat mana tipis (&lt; 50) agar bisa segera summon Robot Golem (150) atau Kuda Poni (80).", table_cell)
        ],
        [
            Paragraph("<b>[ E ]</b>", table_cell_center_bold),
            Paragraph("<b>Buka Kuis Reparasi (BASE REPAIR)</b>", table_cell),
            Paragraph("Gunakan saat benteng diserang (kuota 3x per match). Jaga HP &gt;= 70% demi rating [3 BINTANG].", table_cell)
        ],
        [
            Paragraph("<b>[ A ] / [ 1 ]</b>", table_cell_center_bold),
            Paragraph("Pilih Opsi Jawaban Pertama (Tombol Merah)", table_cell),
            Paragraph("Eksekusi kilat dalam terminal kuis matematika.", table_cell)
        ],
        [
            Paragraph("<b>[ B ] / [ 2 ]</b>", table_cell_center_bold),
            Paragraph("Pilih Opsi Jawaban Kedua (Tombol Biru)", table_cell),
            Paragraph("Eksekusi kilat dalam terminal kuis matematika.", table_cell)
        ],
        [
            Paragraph("<b>[ C ] / [ 3 ]</b>", table_cell_center_bold),
            Paragraph("Pilih Opsi Jawaban Ketiga (Tombol Kuning)", table_cell),
            Paragraph("Eksekusi kilat dalam terminal kuis matematika.", table_cell)
        ],
        [
            Paragraph("<b>[ D ] / [ 4 ]</b>", table_cell_center_bold),
            Paragraph("Pilih Opsi Jawaban Keempat (Tombol Hijau)", table_cell),
            Paragraph("Eksekusi kilat dalam terminal kuis matematika.", table_cell)
        ],
        [
            Paragraph("<b>[ SPACE ]</b>", table_cell_center_bold),
            Paragraph("Jeda Permainan (Pause / Resume)", table_cell),
            Paragraph("Gunakan jika perlu mengevaluasi formasi garis depan sebelum mengambil keputusan.", table_cell)
        ],
        [
            Paragraph("<b>[ 1 ] s.d. [ 5 ]</b>", table_cell_center_bold),
            Paragraph("Panggil Pasukan 1 s.d. 5 di Arena", table_cell),
            Paragraph("<b>1:</b> Prajurit(20), <b>2:</b> Pemanah(35), <b>3:</b> Penyihir(50), <b>4:</b> Kuda Poni(80), <b>5:</b> Robot Golem(150).", table_cell)
        ]
    ], colWidths=[85, 205, 233])
    t_hotkey.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_header_bg),
        ('BOX', (0,0), (-1,-1), 0.8, c_border),
        ('INNERGRID', (0,0), (-1,-1), 0.5, c_border),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, c_bg_alt]),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(t_hotkey)

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"PDF berhasil dibuat dengan sukses: {filename}")

if __name__ == '__main__':
    out_pdf = r"C:\GAME\Kunci_Jawaban_Kuis_Mana_dan_Reparasi.pdf"
    if len(sys.argv) > 1:
        out_pdf = sys.argv[1]
    build_pdf(out_pdf)
