# -*- coding: utf-8 -*-
"""
build_kunci_jawaban_pdf.py
Script Generator Dokumen PDF Resmi:
KUNCI JAWABAN & PEMBAHASAN LENGKAP KUIS TAKTIS MANA & REPARASI
War of Realms: Math & General Knowledge Arena (Level 1 - 10)
"""

import os
import sys
import json
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
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
                36, 808, "WAR OF REALMS: MATH & GENERAL KNOWLEDGE ARENA  |  KUNCI JAWABAN KUIS TAKTIS"
            )
            self.drawRightString(559, 808, "EDISI MATEMATIKA RINGAN & PENGETAHUAN UMUM")
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

def build_pdf(filename, catalog):
    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        leftMargin=36,
        rightMargin=36,
        topMargin=46,
        bottomMargin=46,
        title="Kunci Jawaban Kuis Taktis - War of Realms: Math & General Knowledge Arena",
        author="War of Realms Game Development & Curriculum Team"
    )

    styles = getSampleStyleSheet()

    c_primary = colors.HexColor("#0F172A")    # Slate 900
    c_accent = colors.HexColor("#0284C7")     # Sky 600
    c_header_bg = colors.HexColor("#1E293B")  # Slate 800
    c_dark = colors.HexColor("#1E293B")
    c_bg_alt = colors.HexColor("#F8FAFC")
    c_border = colors.HexColor("#CBD5E1")
    c_correct = colors.HexColor("#059669")

    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=17,
        leading=21,
        textColor=c_primary,
        spaceAfter=2
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

    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=11.5,
        textColor=c_dark,
        spaceAfter=4
    )

    table_header = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7.5,
        leading=10,
        textColor=colors.white,
        alignment=1
    )

    table_cell = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7,
        leading=9.5,
        textColor=c_dark
    )

    table_cell_bold = ParagraphStyle(
        'TableCellBold',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7,
        leading=9.5,
        textColor=c_dark
    )

    table_cell_center = ParagraphStyle(
        'TableCellCenter',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7,
        leading=9.5,
        textColor=c_dark,
        alignment=1
    )

    table_cell_center_bold = ParagraphStyle(
        'TableCellCenterBold',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7,
        leading=9.5,
        textColor=c_dark,
        alignment=1
    )

    table_cell_ans = ParagraphStyle(
        'TableCellAns',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7.5,
        leading=10,
        textColor=c_correct,
        alignment=1
    )

    def section_banner(title_text, subtitle_text="", bg_color=c_header_bg):
        sub_html = f"<br/><font size='7' color='#94A3B8'>{subtitle_text}</font>" if subtitle_text else ""
        p = Paragraph(f"<b>{title_text.upper()}</b>{sub_html}", ParagraphStyle(
            'BannerStyle',
            fontName='Helvetica-Bold',
            fontSize=9,
            leading=12,
            textColor=colors.white
        ))
        t = Table([[p]], colWidths=[523])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), bg_color),
            ('TOPPADDING', (0,0), (-1,-1), 4),
            ('BOTTOMPADDING', (0,0), (-1,-1), 4),
            ('LEFTPADDING', (0,0), (-1,-1), 6),
            ('RIGHTPADDING', (0,0), (-1,-1), 6),
            ('BOX', (0,0), (-1,-1), 0.5, c_border),
        ]))
        return t

    story = []

    # =========================================================================
    # HEADER DOKUMEN & METADATA RESMI
    # =========================================================================
    story.append(Paragraph("WAR OF REALMS: MATH & GENERAL KNOWLEDGE ARENA", title_style))
    story.append(Paragraph("BUKU KUNCI JAWABAN & PEMBAHASAN RESMI KUIS TAKTIS (SEKTOR 1 - 10)", subtitle_style))

    meta_data = [
        [
            Paragraph("<b>Status:</b> Produksi Resmi (Master Catalog)", table_cell),
            Paragraph("<b>Platform:</b> Web Browser (Port 8080) & Standalone", table_cell),
            Paragraph("<b>Total Level:</b> 10 Sektor Lengkap", table_cell)
        ],
        [
            Paragraph("<b>Kurikulum:</b> MTK Ringan & Pengetahuan Umum", table_cell),
            Paragraph("<b>Format Kuis:</b> 4 Pilihan Ganda (Hotkey A-D / 1-4)", table_cell),
            Paragraph("<b>Total Soal:</b> 100 Soal Terkurasi (10/Lvl)", table_cell)
        ]
    ]
    meta_table = Table(meta_data, colWidths=[174, 175, 174])
    meta_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F1F5F9")),
        ('BOX', (0,0), (-1,-1), 0.8, c_accent),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 6))

    # =========================================================================
    # BAB 1: MEKANISME DUAL KUIS (MANA BURST & BASE REPAIR)
    # =========================================================================
    story.append(section_banner("1. MEKANISME KUIS TAKTIS: MANA BURST [Q] & REPARASI BENTENG [E]", "Sistem Cerdas Penunjang Pertempuran Lane Defense"))
    story.append(Spacer(1, 3))

    story.append(Paragraph(
        "Di dalam <b>War of Realms</b>, kecepatan berpikir dan wawasan adalah amunisi tempur utama. "
        "Pemain dibekali 2 tombol kuis pada dek tempur yang memicu modal kuis taktis secara instan. "
        "Pertanyaan diambil dari koleksi 10 soal di sektor aktif (kombinasi 5 soal hitung cepat matematika + 5 soal pengetahuan umum).",
        body_style
    ))
    story.append(Spacer(1, 2))

    t_cmp = Table([
        [
            Paragraph("Parameter Taktis", table_header),
            Paragraph("Kuis Tambah Mana (MANA BURST)", table_header),
            Paragraph("Kuis Reparasi Benteng (BASE REPAIR)", table_header)
        ],
        [
            Paragraph("<b>Pemicu & Hotkey</b>", table_cell_bold),
            Paragraph("Tombol <b>[Q]</b> keyboard (atau klik tombol petir kiri dek)", table_cell),
            Paragraph("Tombol <b>[E]</b> keyboard (atau klik tombol hati kanan dek)", table_cell)
        ],
        [
            Paragraph("<b>Batas Penggunaan</b>", table_cell_bold),
            Paragraph("<b>Tanpa Batas</b> (bebas dipicu sepanjang pertempuran)", table_cell),
            Paragraph("<b>Maksimal 3 Kali</b> per level pertempuran", table_cell)
        ],
        [
            Paragraph("<b>Reward Jawaban Benar</b>", table_cell_bold),
            Paragraph("Mana Instan: <b>+40 + (Level × 5) Mana</b><br/>"
                      "Contoh: Level 1 (+45), Level 5 (+65), Level 10 (+90)", table_cell),
            Paragraph("Heal Base: <b>+25% dari Max HP Benteng Pemain</b><br/>"
                      "Sangat krusial mempertahankan HP >= 70% demi 3 Bintang!", table_cell)
        ],
        [
            Paragraph("<b>Waktu Berpikir & Tempo</b>", table_cell_bold),
            Paragraph("<b>15 Detik</b> dengan efek slow-motion (game melambat ke 0.1x)", table_cell),
            Paragraph("<b>15 Detik</b> dengan efek slow-motion (game melambat ke 0.1x)", table_cell)
        ],
        [
            Paragraph("<b>Koreksi Taktis (Salah)</b>", table_cell_bold),
            Paragraph("Dialog bergetar, tombol jawaban benar disorot hijau menyala.", table_cell),
            Paragraph("Dialog bergetar, kuota 3x tidak berkurang jika salah/timeout.", table_cell)
        ]
    ], colWidths=[115, 204, 204])
    t_cmp.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_header_bg),
        ('BOX', (0,0), (-1,-1), 0.8, c_border),
        ('INNERGRID', (0,0), (-1,-1), 0.5, c_border),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, c_bg_alt]),
        ('TOPPADDING', (0,0), (-1,-1), 2.2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.2),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(t_cmp)
    story.append(Spacer(1, 8))

    # =========================================================================
    # BAB 2: KUNCI JAWABAN LENGKAP LEVEL 1 - 10 (100 SOAL LENGKAP)
    # =========================================================================
    story.append(section_banner("2. KUNCI JAWABAN LENGKAP & PEMBAHASAN PER SEKTOR (LEVEL 1 - 10)", "Katalog Master 100 Pertanyaan (50 Soal Matematika + 50 Soal Pengetahuan Umum)"))
    story.append(Spacer(1, 4))

    for lvl_idx, lvl in enumerate(catalog, start=1):
        lvl_num = lvl["level"]
        lvl_name = lvl["name"]
        lvl_topic = lvl["topic"]

        # Level Sub-banner
        sub_banner = section_banner(
            f"SEKTOR {lvl_num}: {lvl_name} — {lvl_topic}",
            f"Reward Sektor: +{40 + lvl_num * 5} Mana  |  +25% Heal Base  |  10 Soal Master",
            colors.HexColor("#0284C7") if lvl_num % 2 == 1 else colors.HexColor("#0F766E")
        )
        
        table_rows = [
            [
                Paragraph("No", table_header),
                Paragraph("Tipe", table_header),
                Paragraph("Pertanyaan Kuis", table_header),
                Paragraph("Opsi Pilihan (A, B, C, D)", table_header),
                Paragraph("Kunci", table_header),
                Paragraph("Pembahasan / Fakta Edukatif", table_header)
            ]
        ]

        for q in lvl["questions"]:
            opts_formatted = " &bull; ".join(q["opts"])
            type_label = "<font color='#0284C7'><b>[MTK]</b></font>" if q["type"] == "MTK" else "<font color='#D97706'><b>[PU]</b></font>"
            table_rows.append([
                Paragraph(f"<b>{q['id']}</b>", table_cell_center_bold),
                Paragraph(type_label, table_cell_center),
                Paragraph(q["q"], table_cell_bold),
                Paragraph(opts_formatted, table_cell),
                Paragraph(f"<b>{q['ans']}</b>", table_cell_ans),
                Paragraph(q["exp"], table_cell)
            ])

        lvl_table = Table(table_rows, colWidths=[20, 32, 140, 120, 65, 146])
        lvl_table.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), c_header_bg),
            ('BOX', (0,0), (-1,-1), 0.8, c_border),
            ('INNERGRID', (0,0), (-1,-1), 0.5, c_border),
            ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, c_bg_alt]),
            ('TOPPADDING', (0,0), (-1,-1), 2),
            ('BOTTOMPADDING', (0,0), (-1,-1), 2),
            ('LEFTPADDING', (0,0), (-1,-1), 3),
            ('RIGHTPADDING', (0,0), (-1,-1), 3),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ]))

        story.append(KeepTogether([sub_banner, Spacer(1, 2), lvl_table, Spacer(1, 6)]))

    # =========================================================================
    # BAB 3: QUICK ANSWER MATRIX (KISI-KISI KUNCI KILAT)
    # =========================================================================
    story.append(PageBreak())
    story.append(section_banner("3. TABEL MATRIKS JAWABAN CEPAT (QUICK ANSWER MATRIX)", "Referensi Kilat Kunci Jawaban Soal 1 s.d. 10 di Seluruh Sektor", colors.HexColor("#1E293B")))
    story.append(Spacer(1, 3))

    matrix_headers = [Paragraph("Sektor", table_header), Paragraph("Topik Utama", table_header)]
    for i in range(1, 11):
        matrix_headers.append(Paragraph(f"Q{i}", table_header))

    matrix_rows = [matrix_headers]
    for lvl in catalog:
        row = [
            Paragraph(f"<b>Lvl {lvl['level']}</b>", table_cell_center_bold),
            Paragraph(lvl['topic'], table_cell)
        ]
        for q in lvl["questions"]:
            row.append(Paragraph(f"<b>{q['ans']}</b>", table_cell_center))
        matrix_rows.append(row)

    col_widths = [36, 127] + [36] * 10
    matrix_table = Table(matrix_rows, colWidths=col_widths)
    matrix_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_header_bg),
        ('BOX', (0,0), (-1,-1), 0.8, c_border),
        ('INNERGRID', (0,0), (-1,-1), 0.5, c_border),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, c_bg_alt]),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 2),
        ('RIGHTPADDING', (0,0), (-1,-1), 2),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(matrix_table)
    story.append(Spacer(1, 8))

    # =========================================================================
    # BAB 4: PANDUAN HOTKEY KEYBOARD & ERGONOMI KONTROL
    # =========================================================================
    story.append(section_banner("4. PANDUAN KONTROL HOTKEY KEYBOARD LENGKAP", "Ergonomi Bermain Cepat Desktop / Web Browser", colors.HexColor("#0284C7")))
    story.append(Spacer(1, 3))

    hotkey_data = [
        [
            Paragraph("Tombol Hotkey", table_header),
            Paragraph("Aksi & Fungsi di Pertempuran", table_header),
            Paragraph("Tips Eksekusi Cepat & Keunggulan", table_header)
        ],
        [
            Paragraph("<b>[ Q ]</b>", table_cell_center_bold),
            Paragraph("<b>Buka Kuis Tambah Mana (Mana Burst)</b>", table_cell),
            Paragraph("Picu setiap mana menipis (&lt; 40) untuk segera summon prajurit robot golem atau pemanah.", table_cell)
        ],
        [
            Paragraph("<b>[ E ]</b>", table_cell_center_bold),
            Paragraph("<b>Buka Kuis Reparasi Benteng (Base Repair)</b>", table_cell),
            Paragraph("Picu saat HP benteng berkurang di bawah 75% untuk mengembalikan 25% HP benteng.", table_cell)
        ],
        [
            Paragraph("<b>[ A ] / [ 1 ]</b>", table_cell_center_bold),
            Paragraph("Pilih Opsi Jawaban Pertama (Kiri Atas - Merah)", table_cell),
            Paragraph("Gunakan jari manis/kelingking kiri untuk memilih opsi A secara kilat tanpa mouse.", table_cell)
        ],
        [
            Paragraph("<b>[ B ] / [ 2 ]</b>", table_cell_center_bold),
            Paragraph("Pilih Opsi Jawaban Kedua (Kanan Atas - Biru)", table_cell),
            Paragraph("Gunakan jari telunjuk/tengah untuk memilih opsi B seketika.", table_cell)
        ],
        [
            Paragraph("<b>[ C ] / [ 3 ]</b>", table_cell_center_bold),
            Paragraph("Pilih Opsi Jawaban Ketiga (Kiri Bawah - Kuning)", table_cell),
            Paragraph("Pilih opsi C secara akurat menggunakan keyboard.", table_cell)
        ],
        [
            Paragraph("<b>[ D ] / [ 4 ]</b>", table_cell_center_bold),
            Paragraph("Pilih Opsi Jawaban Keempat (Kanan Bawah - Hijau)", table_cell),
            Paragraph("Pilih opsi D langsung tanpa perlu menggeser kursor mouse.", table_cell)
        ],
        [
            Paragraph("<b>[ 1 ] - [ 5 ]</b>", table_cell_center_bold),
            Paragraph("Summon Pasukan Deck (Swordsman s/d Golem)", table_cell),
            Paragraph("Panggil pasukan tempur secara beruntun saat mana melimpah.", table_cell)
        ],
        [
            Paragraph("<b>[ Space ]</b>", table_cell_center_bold),
            Paragraph("Jeda / Lanjutkan Pertempuran (Pause Toggle)", table_cell),
            Paragraph("Gunakan spasi untuk mengevaluasi posisi formasi lawan dan merencanakan strategi.", table_cell)
        ]
    ]
    t_hotkey = Table(hotkey_data, colWidths=[65, 190, 268])
    t_hotkey.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_header_bg),
        ('BOX', (0,0), (-1,-1), 0.8, c_border),
        ('INNERGRID', (0,0), (-1,-1), 0.5, c_border),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, c_bg_alt]),
        ('TOPPADDING', (0,0), (-1,-1), 2.2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.2),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(t_hotkey)

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"PDF berhasil dibuat: {filename}")

CATALOG = [
    {
        "level": 1,
        "name": "Cyber Gate",
        "topic": "Hitung Cepat & Sains Alam",
        "questions": [
            {
                "id": 1,
                "type": "MTK",
                "q": "Hitung: 15 + 27 = ?",
                "opts": [
                    "42",
                    "32",
                    "45",
                    "52"
                ],
                "ans": "42",
                "exp": "15 + 27 = 42. (15 + 25 = 40, lalu + 2 = 42)."
            },
            {
                "id": 2,
                "type": "MTK",
                "q": "Berapa hasil dari 50 - 18?",
                "opts": [
                    "32",
                    "28",
                    "34",
                    "42"
                ],
                "ans": "32",
                "exp": "50 - 18 = 32. (50 - 20 = 30, lalu + 2 = 32)."
            },
            {
                "id": 3,
                "type": "MTK",
                "q": "Hitung cepat: 8 + 7 + 5 = ?",
                "opts": [
                    "20",
                    "19",
                    "21",
                    "22"
                ],
                "ans": "20",
                "exp": "8 + 7 = 15, lalu 15 + 5 = 20."
            },
            {
                "id": 4,
                "type": "MTK",
                "q": "Berapakah 100 - 35?",
                "opts": [
                    "65",
                    "55",
                    "75",
                    "60"
                ],
                "ans": "65",
                "exp": "100 - 35 = 65. (100 - 30 = 70, lalu 70 - 5 = 65)."
            },
            {
                "id": 5,
                "type": "MTK",
                "q": "Jika kamu punya 12 bintang lalu dapat 19 lagi, total bintangmu?",
                "opts": [
                    "31",
                    "29",
                    "30",
                    "32"
                ],
                "ans": "31",
                "exp": "12 + 19 = 31 bintang total."
            },
            {
                "id": 6,
                "type": "PU",
                "q": "Planet terdekat dari Matahari dalam Tata Surya adalah?",
                "opts": [
                    "Merkurius",
                    "Venus",
                    "Mars",
                    "Bumi"
                ],
                "ans": "Merkurius",
                "exp": "Merkurius adalah planet terdekat dari Matahari dengan jarak rata-rata 58 juta km."
            },
            {
                "id": 7,
                "type": "PU",
                "q": "Zat hijau pada daun yang berperan penting dalam fotosintesis adalah?",
                "opts": [
                    "Klorofil",
                    "Stomata",
                    "Hemoglobin",
                    "Karoten"
                ],
                "ans": "Klorofil",
                "exp": "Klorofil berfungsi menangkap energi cahaya matahari untuk fotosintesis tumbuhan."
            },
            {
                "id": 8,
                "type": "PU",
                "q": "Rumus kimia dari molekul air murni adalah?",
                "opts": [
                    "H2O",
                    "CO2",
                    "O2",
                    "NaCl"
                ],
                "ans": "H2O",
                "exp": "Air tersusun atas 2 atom Hidrogen dan 1 atom Oksigen (H2O)."
            },
            {
                "id": 9,
                "type": "PU",
                "q": "Hewan darat tercepat di dunia saat berlari adalah?",
                "opts": [
                    "Cheetah",
                    "Singa",
                    "Kuda",
                    "Elang"
                ],
                "ans": "Cheetah",
                "exp": "Cheetah mampu berlari hingga kecepatan 100-120 km/jam di daratan terbuka."
            },
            {
                "id": 10,
                "type": "PU",
                "q": "Satelit alami yang berputar mengelilingi planet Bumi adalah?",
                "opts": [
                    "Bulan",
                    "Titan",
                    "Phobos",
                    "Ganymede"
                ],
                "ans": "Bulan",
                "exp": "Bulan adalah satu-satunya satelit alami milik planet Bumi."
            }
        ]
    },
    {
        "level": 2,
        "name": "Quantum Core",
        "topic": "Perkalian & Tata Surya",
        "questions": [
            {
                "id": 1,
                "type": "MTK",
                "q": "Berapa hasil dari 7 × 8?",
                "opts": [
                    "56",
                    "54",
                    "58",
                    "64"
                ],
                "ans": "56",
                "exp": "7 × 8 = 56."
            },
            {
                "id": 2,
                "type": "MTK",
                "q": "Hitung: 6 × 9 = ?",
                "opts": [
                    "54",
                    "56",
                    "48",
                    "63"
                ],
                "ans": "54",
                "exp": "6 × 9 = 54."
            },
            {
                "id": 3,
                "type": "MTK",
                "q": "Berapa hasil dari 12 × 5?",
                "opts": [
                    "60",
                    "50",
                    "70",
                    "55"
                ],
                "ans": "60",
                "exp": "12 × 5 = 60."
            },
            {
                "id": 4,
                "type": "MTK",
                "q": "Jika satu regu berisi 4 prajurit, berapa prajurit di 9 regu?",
                "opts": [
                    "36",
                    "32",
                    "40",
                    "28"
                ],
                "ans": "36",
                "exp": "4 × 9 = 36 prajurit total."
            },
            {
                "id": 5,
                "type": "MTK",
                "q": "Hitung cepat: 15 × 4 = ?",
                "opts": [
                    "60",
                    "45",
                    "65",
                    "70"
                ],
                "ans": "60",
                "exp": "15 × 4 = 60."
            },
            {
                "id": 6,
                "type": "PU",
                "q": "Planet terbesar di Tata Surya kita adalah?",
                "opts": [
                    "Yupiter",
                    "Saturnus",
                    "Neptunus",
                    "Uranus"
                ],
                "ans": "Yupiter",
                "exp": "Yupiter adalah planet raksasa gas terbesar di Tata Surya."
            },
            {
                "id": 7,
                "type": "PU",
                "q": "Planet yang dijuluki sebagai 'Planet Merah' adalah?",
                "opts": [
                    "Mars",
                    "Venus",
                    "Merkurius",
                    "Yupiter"
                ],
                "ans": "Mars",
                "exp": "Mars berwarna kemerahan karena kaya kandungan debu besi oksida (karat)."
            },
            {
                "id": 8,
                "type": "PU",
                "q": "Planet di Tata Surya yang terkenal memiliki cincin paling indah adalah?",
                "opts": [
                    "Saturnus",
                    "Yupiter",
                    "Neptunus",
                    "Mars"
                ],
                "ans": "Saturnus",
                "exp": "Saturnus dikelilingi ribuan cincin es dan bebatuan memukau."
            },
            {
                "id": 9,
                "type": "PU",
                "q": "Bintang yang menjadi pusat peredaran Tata Surya kita adalah?",
                "opts": [
                    "Matahari",
                    "Sirius",
                    "Polaris",
                    "Proxima Centauri"
                ],
                "ans": "Matahari",
                "exp": "Matahari memegang 99,8% massa seluruh sistem Tata Surya kita."
            },
            {
                "id": 10,
                "type": "PU",
                "q": "Perputaran planet Bumi pada porosnya sendiri disebut?",
                "opts": [
                    "Rotasi",
                    "Revolusi",
                    "Gerhana",
                    "Presesi"
                ],
                "ans": "Rotasi",
                "exp": "Rotasi Bumi membutuhkan waktu 24 jam dan menyebabkan pergantian siang dan malam."
            }
        ]
    },
    {
        "level": 3,
        "name": "Nexus Nebula",
        "topic": "Pembagian & Geografi Dunia",
        "questions": [
            {
                "id": 1,
                "type": "MTK",
                "q": "Berapakah hasil dari 72 ÷ 8?",
                "opts": [
                    "9",
                    "8",
                    "7",
                    "6"
                ],
                "ans": "9",
                "exp": "72 ÷ 8 = 9 (karena 9 × 8 = 72)."
            },
            {
                "id": 2,
                "type": "MTK",
                "q": "Hitung: 48 ÷ 6 = ?",
                "opts": [
                    "8",
                    "7",
                    "9",
                    "6"
                ],
                "ans": "8",
                "exp": "48 ÷ 6 = 8."
            },
            {
                "id": 3,
                "type": "MTK",
                "q": "Jika 60 kristal dibagi rata ke 5 robot, masing-masing dapat?",
                "opts": [
                    "12",
                    "10",
                    "15",
                    "14"
                ],
                "ans": "12",
                "exp": "60 ÷ 5 = 12 kristal per robot."
            },
            {
                "id": 4,
                "type": "MTK",
                "q": "Berapakah hasil dari 100 ÷ 4?",
                "opts": [
                    "25",
                    "20",
                    "30",
                    "24"
                ],
                "ans": "25",
                "exp": "100 ÷ 4 = 25."
            },
            {
                "id": 5,
                "type": "MTK",
                "q": "Hitung: 84 ÷ 2 = ?",
                "opts": [
                    "42",
                    "41",
                    "44",
                    "48"
                ],
                "ans": "42",
                "exp": "84 ÷ 2 = 42."
            },
            {
                "id": 6,
                "type": "PU",
                "q": "Benua terluas di dunia adalah Benua?",
                "opts": [
                    "Asia",
                    "Afrika",
                    "Amerika",
                    "Eropa"
                ],
                "ans": "Asia",
                "exp": "Benua Asia mencakup 44,58 juta km² (sekitar 30% luas daratan Bumi)."
            },
            {
                "id": 7,
                "type": "PU",
                "q": "Gunung tertinggi di dunia di atas permukaan laut adalah?",
                "opts": [
                    "Everest",
                    "K2",
                    "Kilimanjaro",
                    "Fuji"
                ],
                "ans": "Everest",
                "exp": "Puncak Gunung Everest di Pegunungan Himalaya tingginya 8.848 meter dpl."
            },
            {
                "id": 8,
                "type": "PU",
                "q": "Samudra terluas dan terdalam di permukaan Bumi adalah Samudra?",
                "opts": [
                    "Pasifik",
                    "Atlantik",
                    "Hindia",
                    "Arktik"
                ],
                "ans": "Pasifik",
                "exp": "Samudra Pasifik menutupi lebih dari 30% seluruh permukaan Bumi."
            },
            {
                "id": 9,
                "type": "PU",
                "q": "Sungai terpanjang di Benua Afrika yang mengalir ke Laut Tengah adalah?",
                "opts": [
                    "Sungai Nil",
                    "Sungai Amazon",
                    "Sungai Yangtze",
                    "Sungai Kongo"
                ],
                "ans": "Sungai Nil",
                "exp": "Sungai Nil membentang sepanjang 6.650 km melintasi berbagai negara Afrika."
            },
            {
                "id": 10,
                "type": "PU",
                "q": "Negara dengan wilayah terluas di dunia adalah?",
                "opts": [
                    "Rusia",
                    "Kanada",
                    "Tiongkok",
                    "Amerika Serikat"
                ],
                "ans": "Rusia",
                "exp": "Rusia membentang di Eropa Timur dan Asia Utara dengan luas 17,1 juta km²."
            }
        ]
    },
    {
        "level": 4,
        "name": "Parabola Rift",
        "topic": "Geometri & Penemu Sains",
        "questions": [
            {
                "id": 1,
                "type": "MTK",
                "q": "Jumlah seluruh sudut dalam sebuah bangun segitiga adalah?",
                "opts": [
                    "180°",
                    "360°",
                    "90°",
                    "270°"
                ],
                "ans": "180°",
                "exp": "Jumlah tiga sudut dalam pada segitiga selalu tepat 180°."
            },
            {
                "id": 2,
                "type": "MTK",
                "q": "Keliling persegi yang memiliki panjang sisi 7 cm adalah?",
                "opts": [
                    "28 cm",
                    "49 cm",
                    "21 cm",
                    "14 cm"
                ],
                "ans": "28 cm",
                "exp": "Keliling persegi = 4 × sisi = 4 × 7 = 28 cm."
            },
            {
                "id": 3,
                "type": "MTK",
                "q": "Luas persegi panjang berukuran panjang 9 cm dan lebar 6 cm adalah?",
                "opts": [
                    "54 cm²",
                    "30 cm²",
                    "45 cm²",
                    "60 cm²"
                ],
                "ans": "54 cm²",
                "exp": "Luas = panjang × lebar = 9 × 6 = 54 cm²."
            },
            {
                "id": 4,
                "type": "MTK",
                "q": "Lingkaran memiliki jari-jari r = 10 cm. Berapakah panjang diameternya?",
                "opts": [
                    "20 cm",
                    "15 cm",
                    "25 cm",
                    "30 cm"
                ],
                "ans": "20 cm",
                "exp": "Diameter = 2 × jari-jari = 2 × 10 = 20 cm."
            },
            {
                "id": 5,
                "type": "MTK",
                "q": "Berapa banyak sisi yang dimiliki oleh bangun datar heksagon?",
                "opts": [
                    "6 sisi",
                    "5 sisi",
                    "7 sisi",
                    "8 sisi"
                ],
                "ans": "6 sisi",
                "exp": "Heksagon adalah bangun segi enam beraturan (6 sisi)."
            },
            {
                "id": 6,
                "type": "PU",
                "q": "Tokoh penemu lampu pijar listrik praktis yang terkenal adalah?",
                "opts": [
                    "Thomas Alva Edison",
                    "Alexander Graham Bell",
                    "Nikola Tesla",
                    "Albert Einstein"
                ],
                "ans": "Thomas Alva Edison",
                "exp": "Thomas Edison mengembangkan dan mematenkan lampu pijar praktis pada 1879."
            },
            {
                "id": 7,
                "type": "PU",
                "q": "Penemu pesawat terbang bermesin pertama di dunia adalah?",
                "opts": [
                    "Wright Bersaudara",
                    "James Watt",
                    "Galileo Galilei",
                    "Isaac Newton"
                ],
                "ans": "Wright Bersaudara",
                "exp": "Orville dan Wilbur Wright berhasil menerbangkan pesawat Flyer I pada 1903."
            },
            {
                "id": 8,
                "type": "PU",
                "q": "Ilmuwan perumus Hukum Gravitasi Universal dan Tiga Hukum Gerak adalah?",
                "opts": [
                    "Sir Isaac Newton",
                    "Albert Einstein",
                    "Stephen Hawking",
                    "Michael Faraday"
                ],
                "ans": "Sir Isaac Newton",
                "exp": "Newton merumuskan gaya gravitasi yang mengatur gerak benda di Bumi dan antariksa."
            },
            {
                "id": 9,
                "type": "PU",
                "q": "Tokoh yang dikenal luas sebagai 'Bapak Komputer' dunia adalah?",
                "opts": [
                    "Charles Babbage",
                    "Alan Turing",
                    "Bill Gates",
                    "Steve Jobs"
                ],
                "ans": "Charles Babbage",
                "exp": "Charles Babbage merancang Analytical Engine, cikal bakal konsep komputer mekanis."
            },
            {
                "id": 10,
                "type": "PU",
                "q": "Penemu perangkat telepon pertama yang dipatenkan secara resmi adalah?",
                "opts": [
                    "Alexander Graham Bell",
                    "Guglielmo Marconi",
                    "Samuel Morse",
                    "Nikola Tesla"
                ],
                "ans": "Alexander Graham Bell",
                "exp": "Alexander Graham Bell mematenkan penemuan telepon pada tahun 1876."
            }
        ]
    },
    {
        "level": 5,
        "name": "Binary Valley",
        "topic": "Pecahan & Dunia Komputer",
        "questions": [
            {
                "id": 1,
                "type": "MTK",
                "q": "Berapakah nilai dari 50% dari 120?",
                "opts": [
                    "60",
                    "50",
                    "70",
                    "80"
                ],
                "ans": "60",
                "exp": "50% = setengah (1/2), maka 120 ÷ 2 = 60."
            },
            {
                "id": 2,
                "type": "MTK",
                "q": "Hitung: 1/4 dari 80 adalah?",
                "opts": [
                    "20",
                    "25",
                    "15",
                    "30"
                ],
                "ans": "20",
                "exp": "80 × 1/4 = 80 ÷ 4 = 20."
            },
            {
                "id": 3,
                "type": "MTK",
                "q": "Berapakah 25% dari 200?",
                "opts": [
                    "50",
                    "25",
                    "75",
                    "40"
                ],
                "ans": "50",
                "exp": "25% = 1/4, maka 200 ÷ 4 = 50."
            },
            {
                "id": 4,
                "type": "MTK",
                "q": "Bentuk desimal dari pecahan 1/2 adalah?",
                "opts": [
                    "0.5",
                    "0.2",
                    "0.25",
                    "0.05"
                ],
                "ans": "0.5",
                "exp": "1 dibagi 2 = 0.5."
            },
            {
                "id": 5,
                "type": "MTK",
                "q": "Hitung: 10% dari 350 = ?",
                "opts": [
                    "35",
                    "3.5",
                    "70",
                    "25"
                ],
                "ans": "35",
                "exp": "10% dari 350 = 350 ÷ 10 = 35."
            },
            {
                "id": 6,
                "type": "PU",
                "q": "Sistem bilangan biner pada komputer hanya terdiri dari dua angka, yaitu?",
                "opts": [
                    "0 dan 1",
                    "1 dan 2",
                    "0 dan 9",
                    "A dan B"
                ],
                "ans": "0 dan 1",
                "exp": "Sistem biner (basis 2) menggunakan digit bit 0 dan 1."
            },
            {
                "id": 7,
                "type": "PU",
                "q": "1 Byte dalam arsitektur memori komputer setara dengan berapa bit?",
                "opts": [
                    "8 bit",
                    "4 bit",
                    "16 bit",
                    "32 bit"
                ],
                "ans": "8 bit",
                "exp": "1 Byte tepat terdiri atas kumpulan 8 bit data biner."
            },
            {
                "id": 8,
                "type": "PU",
                "q": "Unit pemrosesan utama yang menjadi 'otak' komputer disebut?",
                "opts": [
                    "CPU (Processor)",
                    "RAM",
                    "Harddisk",
                    "Power Supply"
                ],
                "ans": "CPU (Processor)",
                "exp": "Central Processing Unit (CPU) bertugas mengolah seluruh logika dan instruksi."
            },
            {
                "id": 9,
                "type": "PU",
                "q": "Singkatan dari sistem jaringan 'WWW' pada alamat website adalah?",
                "opts": [
                    "World Wide Web",
                    "World Web Wide",
                    "Wide World Web",
                    "Web World Wide"
                ],
                "ans": "World Wide Web",
                "exp": "World Wide Web (WWW) diciptakan oleh Tim Berners-Lee pada 1989."
            },
            {
                "id": 10,
                "type": "PU",
                "q": "Memori komputer yang bersifat sementara dan hilang saat listrik mati adalah?",
                "opts": [
                    "RAM",
                    "ROM",
                    "Flashdisk",
                    "SSD"
                ],
                "ans": "RAM",
                "exp": "RAM (Random Access Memory) bersifat volatile (data hilang saat mati daya)."
            }
        ]
    },
    {
        "level": 6,
        "name": "Trigon Citadel",
        "topic": "Akar Kuadrat & Tubuh Manusia",
        "questions": [
            {
                "id": 1,
                "type": "MTK",
                "q": "Berapakah nilai dari √49?",
                "opts": [
                    "7",
                    "6",
                    "8",
                    "9"
                ],
                "ans": "7",
                "exp": "√49 = 7 (karena 7 × 7 = 49)."
            },
            {
                "id": 2,
                "type": "MTK",
                "q": "Berapakah nilai dari 6² (6 pangkat 2)?",
                "opts": [
                    "36",
                    "12",
                    "42",
                    "30"
                ],
                "ans": "36",
                "exp": "6² = 6 × 6 = 36."
            },
            {
                "id": 3,
                "type": "MTK",
                "q": "Hitung: √100 = ?",
                "opts": [
                    "10",
                    "20",
                    "50",
                    "5"
                ],
                "ans": "10",
                "exp": "√100 = 10 (karena 10 × 10 = 100)."
            },
            {
                "id": 4,
                "type": "MTK",
                "q": "Berapakah hasil dari 2³ (2 pangkat 3)?",
                "opts": [
                    "8",
                    "6",
                    "9",
                    "12"
                ],
                "ans": "8",
                "exp": "2³ = 2 × 2 × 2 = 8."
            },
            {
                "id": 5,
                "type": "MTK",
                "q": "Hitung cepat: √64 + √25 = ?",
                "opts": [
                    "13",
                    "11",
                    "14",
                    "15"
                ],
                "ans": "13",
                "exp": "√64 = 8, √25 = 5. Maka 8 + 5 = 13."
            },
            {
                "id": 6,
                "type": "PU",
                "q": "Organ tubuh manusia yang berfungsi utama memompa darah adalah?",
                "opts": [
                    "Jantung",
                    "Paru-paru",
                    "Ginjal",
                    "Lambung"
                ],
                "ans": "Jantung",
                "exp": "Jantung berdenyut memompa darah beroksigen ke seluruh jaringan tubuh."
            },
            {
                "id": 7,
                "type": "PU",
                "q": "Tulang terpanjang dan terkuat pada rangka tubuh manusia adalah tulang?",
                "opts": [
                    "Paha (Femur)",
                    "Betis",
                    "Lengan",
                    "Rusuk"
                ],
                "ans": "Paha (Femur)",
                "exp": "Tulang paha (femur) adalah tulang terbesar dan terkuat penyangga tubuh."
            },
            {
                "id": 8,
                "type": "PU",
                "q": "Vitamin yang dibentuk tubuh dengan bantuan paparan sinar matahari pagi adalah?",
                "opts": [
                    "Vitamin D",
                    "Vitamin C",
                    "Vitamin A",
                    "Vitamin B12"
                ],
                "ans": "Vitamin D",
                "exp": "Sinar ultraviolet membantu kulit memproduksi Vitamin D alami."
            },
            {
                "id": 9,
                "type": "PU",
                "q": "Organ tubuh yang berfungsi menetralisir racun dan memproduksi empedu adalah?",
                "opts": [
                    "Hati (Liver)",
                    "Limpa",
                    "Jantung",
                    "Pankreas"
                ],
                "ans": "Hati (Liver)",
                "exp": "Hati adalah organ kelenjar terbesar yang menyaring toksin dan menghasilkan empedu."
            },
            {
                "id": 10,
                "type": "PU",
                "q": "Gas apakah yang diserap oleh paru-paru manusia saat menarik napas?",
                "opts": [
                    "Oksigen",
                    "Karbon Dioksida",
                    "Nitrogen",
                    "Helium"
                ],
                "ans": "Oksigen",
                "exp": "Oksigen diikat sel darah merah di alveolus paru-paru untuk energi sel."
            }
        ]
    },
    {
        "level": 7,
        "name": "Matrix Horizon",
        "topic": "Pola Bilangan & Hewan Fauna",
        "questions": [
            {
                "id": 1,
                "type": "MTK",
                "q": "Tentukan angka berikutnya dari pola: 3, 6, 9, 12, ...?",
                "opts": [
                    "15",
                    "14",
                    "16",
                    "18"
                ],
                "ans": "15",
                "exp": "Pola bertambah 3 (+3), maka 12 + 3 = 15."
            },
            {
                "id": 2,
                "type": "MTK",
                "q": "Angka kelanjutan dari barisan: 5, 10, 15, 20, ... adalah?",
                "opts": [
                    "25",
                    "24",
                    "30",
                    "22"
                ],
                "ans": "25",
                "exp": "Pola kelipatan 5 (+5), maka 20 + 5 = 25."
            },
            {
                "id": 3,
                "type": "MTK",
                "q": "Tentukan angka berikutnya dari: 2, 4, 8, 16, ...?",
                "opts": [
                    "32",
                    "24",
                    "28",
                    "30"
                ],
                "ans": "32",
                "exp": "Pola dikali 2 (×2), maka 16 × 2 = 32."
            },
            {
                "id": 4,
                "type": "MTK",
                "q": "Lanjutan dari urutan bilangan: 100, 90, 80, 70, ... adalah?",
                "opts": [
                    "60",
                    "50",
                    "65",
                    "55"
                ],
                "ans": "60",
                "exp": "Pola berkurang 10 (-10), maka 70 - 10 = 60."
            },
            {
                "id": 5,
                "type": "MTK",
                "q": "Tentukan angka berikutnya: 1, 4, 9, 16, 25, ...?",
                "opts": [
                    "36",
                    "30",
                    "32",
                    "49"
                ],
                "ans": "36",
                "exp": "Pola bilangan kuadrat: 1², 2², 3², 4², 5², berikutnya 6² = 36."
            },
            {
                "id": 6,
                "type": "PU",
                "q": "Hewan mamalia terbesar yang pernah hidup di muka Bumi adalah?",
                "opts": [
                    "Paus Biru",
                    "Gajah Afrika",
                    "Hiu Paus",
                    "Jerapah"
                ],
                "ans": "Paus Biru",
                "exp": "Paus Biru dapat mencapai panjang 30 meter dan berbobot hingga 180 ton."
            },
            {
                "id": 7,
                "type": "PU",
                "q": "Hewan yang dapat hidup di dua alam (air dan darat) digolongkan sebagai?",
                "opts": [
                    "Amfibi",
                    "Reptil",
                    "Mamalia",
                    "Aves"
                ],
                "ans": "Amfibi",
                "exp": "Amfibi (seperti katak) bernapas dengan insang saat berudu dan paru-paru/kulit saat dewasa."
            },
            {
                "id": 8,
                "type": "PU",
                "q": "Burung terbesar di dunia yang tidak bisa terbang namun berlari cepat adalah?",
                "opts": [
                    "Burung Unta",
                    "Penguin",
                    "Kasuari",
                    "Kiwi"
                ],
                "ans": "Burung Unta",
                "exp": "Burung unta dapat berlari kencang hingga kecepatan 70 km/jam."
            },
            {
                "id": 9,
                "type": "PU",
                "q": "Spesies kadal terbesar di dunia yang merupakan fauna endemik Indonesia adalah?",
                "opts": [
                    "Komodo",
                    "Biawak",
                    "Iguana",
                    "Bunglon"
                ],
                "ans": "Komodo",
                "exp": "Komodo (Varanus komodoensis) hidup secara alami di kawasan Pulau Komodo, NTT."
            },
            {
                "id": 10,
                "type": "PU",
                "q": "Mamalia yang aktif mencari makan di malam hari menggunakan ekolokasi adalah?",
                "opts": [
                    "Kelelawar",
                    "Tupai Terbang",
                    "Burung Hantu",
                    "Elang"
                ],
                "ans": "Kelelawar",
                "exp": "Kelelawar memancarkan gelombang ultrasonik untuk mendeteksi mangsa dan halangan."
            }
        ]
    },
    {
        "level": 8,
        "name": "Chrono Portal",
        "topic": "Satuan Waktu & Sejarah Nasional",
        "questions": [
            {
                "id": 1,
                "type": "MTK",
                "q": "1 jam setara dengan berapa menit?",
                "opts": [
                    "60 menit",
                    "100 menit",
                    "50 menit",
                    "120 menit"
                ],
                "ans": "60 menit",
                "exp": "1 jam = 60 menit, dan 1 menit = 60 detik."
            },
            {
                "id": 2,
                "type": "MTK",
                "q": "Panjang 1 kilometer (km) sama dengan berapa meter?",
                "opts": [
                    "1.000 meter",
                    "100 meter",
                    "10.000 meter",
                    "500 meter"
                ],
                "ans": "1.000 meter",
                "exp": "Awalan 'kilo' melambangkan faktor pengali seribu (1.000 m)."
            },
            {
                "id": 3,
                "type": "MTK",
                "q": "Berapa detik total waktu yang terkandung dalam 2 menit?",
                "opts": [
                    "120 detik",
                    "100 detik",
                    "90 detik",
                    "180 detik"
                ],
                "ans": "120 detik",
                "exp": "2 menit = 2 × 60 detik = 120 detik."
            },
            {
                "id": 4,
                "type": "MTK",
                "q": "Berat 1 kilogram (kg) setara dengan berapa gram?",
                "opts": [
                    "1.000 gram",
                    "100 gram",
                    "500 gram",
                    "10.000 gram"
                ],
                "ans": "1.000 gram",
                "exp": "1 kg tepat setara dengan 1.000 gram."
            },
            {
                "id": 5,
                "type": "MTK",
                "q": "Jika pertempuran dimulai 08.00 dan berlangsung 90 menit, selesai pukul?",
                "opts": [
                    "09.30",
                    "09.00",
                    "10.00",
                    "09.15"
                ],
                "ans": "09.30",
                "exp": "90 menit = 1 jam 30 menit. 08.00 + 1 jam 30 menit = 09.30."
            },
            {
                "id": 6,
                "type": "PU",
                "q": "Kapan Hari Kemerdekaan Republik Indonesia diproklamasikan?",
                "opts": [
                    "17 Agustus 1945",
                    "17 Agustus 1944",
                    "28 Oktober 1928",
                    "20 Mei 1908"
                ],
                "ans": "17 Agustus 1945",
                "exp": "Proklamasi Kemerdekaan RI dibacakan di Jalan Pegangsaan Timur 56 Jakarta."
            },
            {
                "id": 7,
                "type": "PU",
                "q": "Tokoh yang bertugas mengetik naskah Proklamasi Kemerdekaan Indonesia adalah?",
                "opts": [
                    "Sayuti Melik",
                    "B.M. Diah",
                    "Sukarni",
                    "Chaerul Saleh"
                ],
                "ans": "Sayuti Melik",
                "exp": "Sayuti Melik mengetik naskah proklamasi berdasarkan tulisan tangan Ir. Soekarno."
            },
            {
                "id": 8,
                "type": "PU",
                "q": "Candi Buddha terbesar di dunia yang berlokasi di Magelang Jawa Tengah adalah?",
                "opts": [
                    "Candi Borobudur",
                    "Candi Prambanan",
                    "Candi Mendut",
                    "Candi Sewu"
                ],
                "ans": "Candi Borobudur",
                "exp": "Candi Borobudur didirikan sekitar abad ke-8 oleh wangsa Syailendra."
            },
            {
                "id": 9,
                "type": "PU",
                "q": "Lagu kebangsaan 'Indonesia Raya' diciptakan oleh komponis nasional bernama?",
                "opts": [
                    "Wage Rudolf Supratman",
                    "Ismail Marzuki",
                    "Cornel Simanjuntak",
                    "Ibu Sud"
                ],
                "ans": "Wage Rudolf Supratman",
                "exp": "W.R. Supratman memperdengarkan lagu Indonesia Raya di Kongres Pemuda II 1928."
            },
            {
                "id": 10,
                "type": "PU",
                "q": "Peristiwa bersejarah Kongres Pemuda yang melahirkan Sumpah Pemuda terjadi pada?",
                "opts": [
                    "28 Oktober 1928",
                    "20 Mei 1908",
                    "10 November 1945",
                    "1 Juni 1945"
                ],
                "ans": "28 Oktober 1928",
                "exp": "Sumpah Pemuda mengikrarkan satu tanah air, satu bangsa, dan satu bahasa persatuan."
            }
        ]
    },
    {
        "level": 9,
        "name": "Modulo Bastion",
        "topic": "Aljabar Ringan & Fakta Sains",
        "questions": [
            {
                "id": 1,
                "type": "MTK",
                "q": "Jika x + 7 = 15, berapakah nilai x?",
                "opts": [
                    "8",
                    "7",
                    "9",
                    "6"
                ],
                "ans": "8",
                "exp": "x = 15 - 7 = 8."
            },
            {
                "id": 2,
                "type": "MTK",
                "q": "Jika 2x = 18, berapakah nilai x?",
                "opts": [
                    "9",
                    "8",
                    "7",
                    "6"
                ],
                "ans": "9",
                "exp": "x = 18 ÷ 2 = 9."
            },
            {
                "id": 3,
                "type": "MTK",
                "q": "Selesaikan persamaan: y - 4 = 11, nilai y = ?",
                "opts": [
                    "15",
                    "14",
                    "16",
                    "7"
                ],
                "ans": "15",
                "exp": "y = 11 + 4 = 15."
            },
            {
                "id": 4,
                "type": "MTK",
                "q": "Jika 3n = 21, maka nilai n adalah?",
                "opts": [
                    "7",
                    "6",
                    "8",
                    "9"
                ],
                "ans": "7",
                "exp": "n = 21 ÷ 3 = 7."
            },
            {
                "id": 5,
                "type": "MTK",
                "q": "Jika a + a + a = 12, berapakah nilai a?",
                "opts": [
                    "4",
                    "3",
                    "5",
                    "6"
                ],
                "ans": "4",
                "exp": "3a = 12, maka a = 12 ÷ 3 = 4."
            },
            {
                "id": 6,
                "type": "PU",
                "q": "Proses perubahan wujud zat dari padat langsung menjadi gas dinamakan?",
                "opts": [
                    "Menyublim",
                    "Menguap",
                    "Mencair",
                    "Mengembun"
                ],
                "ans": "Menyublim",
                "exp": "Menyublim terjadi pada kapur barus atau es kering tanpa melewati fase cair."
            },
            {
                "id": 7,
                "type": "PU",
                "q": "Logam yang berwujud cair pada suhu ruangan normal adalah?",
                "opts": [
                    "Merkuri (Air Raksa)",
                    "Timbal",
                    "Alumunium",
                    "Tembaga"
                ],
                "ans": "Merkuri (Air Raksa)",
                "exp": "Merkuri memiliki titik leleh -38,8°C sehingga berwujud cair pada suhu kamar."
            },
            {
                "id": 8,
                "type": "PU",
                "q": "Kecepatan cahaya merambat di ruang hampa udara diperkirakan mencapai?",
                "opts": [
                    "300.000 km/detik",
                    "3.000 km/detik",
                    "340 meter/detik",
                    "1.000 km/detik"
                ],
                "ans": "300.000 km/detik",
                "exp": "Kecepatan cahaya sekitar 299.792 km/detik (dibulatkan 300.000 km/s)."
            },
            {
                "id": 9,
                "type": "PU",
                "q": "Gaya yang selalu menarik semua benda jatuh menuju pusat Bumi adalah?",
                "opts": [
                    "Gaya Gravitasi",
                    "Gaya Magnet",
                    "Gaya Gesek",
                    "Gaya Pegas"
                ],
                "ans": "Gaya Gravitasi",
                "exp": "Gravitasi Bumi memiliki percepatan rata-rata sekitar 9,8 m/s²."
            },
            {
                "id": 10,
                "type": "PU",
                "q": "Lapisan di atmosfer Bumi yang menyerap radiasi ultraviolet sinar Matahari adalah?",
                "opts": [
                    "Lapisan Ozon",
                    "Troposfer",
                    "Mesosfer",
                    "Termosfer"
                ],
                "ans": "Lapisan Ozon",
                "exp": "Molekul ozon (O3) di stratosfer menyaring radiasi UV-B matahari yang berbahaya."
            }
        ]
    },
    {
        "level": 10,
        "name": "Singularity Apex",
        "topic": "Cerdas Cepat & Wawasan Dunia",
        "questions": [
            {
                "id": 1,
                "type": "MTK",
                "q": "Berapakah nilai dari (8 × 5) + 15?",
                "opts": [
                    "55",
                    "45",
                    "50",
                    "60"
                ],
                "ans": "55",
                "exp": "Kerjakan perkalian dulu: 8 × 5 = 40, lalu 40 + 15 = 55."
            },
            {
                "id": 2,
                "type": "MTK",
                "q": "Hitung cepat: 100 - (7 × 7) = ?",
                "opts": [
                    "51",
                    "49",
                    "53",
                    "47"
                ],
                "ans": "51",
                "exp": "7 × 7 = 49. Maka 100 - 49 = 51."
            },
            {
                "id": 3,
                "type": "MTK",
                "q": "Berapakah nilai rata-rata dari tiga angka: 6, 8, dan 10?",
                "opts": [
                    "8",
                    "7",
                    "9",
                    "24"
                ],
                "ans": "8",
                "exp": "Rata-rata = (6 + 8 + 10) ÷ 3 = 24 ÷ 3 = 8."
            },
            {
                "id": 4,
                "type": "MTK",
                "q": "Keliling segitiga sama sisi yang masing-masing sisinya 12 cm adalah?",
                "opts": [
                    "36 cm",
                    "24 cm",
                    "48 cm",
                    "30 cm"
                ],
                "ans": "36 cm",
                "exp": "Keliling = 3 × 12 cm = 36 cm."
            },
            {
                "id": 5,
                "type": "MTK",
                "q": "Jika berlari dengan kecepatan 20 km/jam selama 3 jam, jarak tempuh adalah?",
                "opts": [
                    "60 km",
                    "50 km",
                    "40 km",
                    "80 km"
                ],
                "ans": "60 km",
                "exp": "Jarak = kecepatan × waktu = 20 × 3 = 60 km."
            },
            {
                "id": 6,
                "type": "PU",
                "q": "Tembok Raksasa (Great Wall) yang membentang ribuan kilometer terletak di negara?",
                "opts": [
                    "Tiongkok (Cina)",
                    "Jepang",
                    "India",
                    "Korea"
                ],
                "ans": "Tiongkok (Cina)",
                "exp": "Tembok Besar Tiongkok dibangun sebagai benteng pertahanan dinasti-dinasti kuno."
            },
            {
                "id": 7,
                "type": "PU",
                "q": "Piramida Agung Giza yang termasuk keajaiban dunia kuno berada di negara?",
                "opts": [
                    "Mesir",
                    "Yunani",
                    "Italia",
                    "Yordania"
                ],
                "ans": "Mesir",
                "exp": "Piramida Giza didirikan sebagai makam raja firaun di tepi Sungai Nil, Mesir."
            },
            {
                "id": 8,
                "type": "PU",
                "q": "Organisasi antarbangsa sedunia yang memelihara perdamaian internasional adalah?",
                "opts": [
                    "PBB",
                    "UNESCO",
                    "WHO",
                    "ASEAN"
                ],
                "ans": "PBB",
                "exp": "PBB (Perserikatan Bangsa-Bangsa / UN) didirikan pada 24 Oktober 1945."
            },
            {
                "id": 9,
                "type": "PU",
                "q": "Negara di Asia Timur yang dijuluki sebagai 'Negara Matahari Terbit' adalah?",
                "opts": [
                    "Jepang",
                    "Korea Selatan",
                    "Thailand",
                    "Filipina"
                ],
                "ans": "Jepang",
                "exp": "Nama lokal Jepang 'Nippon/Nihon' bermakna 'tanah tempat matahari terbit'."
            },
            {
                "id": 10,
                "type": "PU",
                "q": "Lautan es beku yang mengelilingi Kutub Utara Bumi adalah Samudra?",
                "opts": [
                    "Arktik",
                    "Antartika",
                    "Atlantik",
                    "Hindia"
                ],
                "ans": "Arktik",
                "exp": "Samudra Arktik adalah samudra terkecil yang mengelilingi kawasan Kutub Utara."
            }
        ]
    }
]

if __name__ == "__main__":
    out_pdf = r"C:\GAME\Kunci_Jawaban_Kuis_Mana_dan_Reparasi.pdf"
    build_pdf(out_pdf, CATALOG)
