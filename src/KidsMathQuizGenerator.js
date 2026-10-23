/**
 * KidsMathQuizGenerator.js
 * Generator Kuis Cerdas Matematika & Pengetahuan Umum (Level 1 - 10)
 * Edisi Mudah, Cepat, Edukatif & Taktis untuk Lane Defense Combat.
 */

export const QuizType = {
  MANA: 'MANA',
  FORTIFY: 'FORTIFY'
};

export const MASTER_QUIZ_CATALOG = [
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
];

export class KidsMathQuizGenerator {
  static getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
  }

  static shuffleArray(array) {
    const arr = [...array];
    for (let i = arr.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [arr[i], arr[j]] = [arr[j], arr[i]];
    }
    return arr;
  }

  static generateQuestion(level, quizType) {
    const clampedLevel = Math.min(Math.max(level, 1), 10);
    const levelData = MASTER_QUIZ_CATALOG.find(lvl => lvl.level === clampedLevel) || MASTER_QUIZ_CATALOG[0];
    
    // Pilih 1 dari 10 soal acak pada level ini
    const qList = levelData.questions;
    const q = qList[this.getRandomInt(0, qList.length - 1)];

    // Acak urutan 4 opsi jawaban agar tidak statis di tombol yang sama
    const shuffledOptions = this.shuffleArray(q.opts);
    const correctIndex = shuffledOptions.indexOf(q.ans);

    return {
      id: `${clampedLevel}_${q.id}`,
      type: quizType,
      level: clampedLevel,
      category: q.type, // 'MTK' atau 'PU'
      topic: `${levelData.topic} [${q.type === 'MTK' ? 'MATEMATIKA' : 'PENGETAHUAN UMUM'}]`,
      questionText: q.q,
      options: shuffledOptions,
      correctIndex: correctIndex,
      correctAnswer: q.ans,
      explanation: q.exp,
      timeLimit: 15 // 15 detik waktu berpikir santai & taktis
    };
  }
}
