# =====================================================
#  Setting karakter
# =====================================================
init -1 python:
    def loncat_bicara(tag):
        def callback(event, interact=True, **kwargs):
            if event == "begin" and interact:
                slot = {
                    "danisa": sprite_kiri,
                    "joko": sprite_tengah,
                    "rara": sprite_kanan_dalam,
                    "kenzie": sprite_kanan,
                }.get(tag)
                attrs = renpy.get_attributes(tag)
                # Perbaikan: kalau sprite belum tampil, jangan dipaksa show (bisa error)
                if slot is not None and attrs is not None:
                    nama_dengan_atribut = tag if not attrs else tag + " " + " ".join(attrs)
                    renpy.show(nama_dengan_atribut, at_list=[slot, talk_bounce])
            return None
        return callback

define rara = Character("Rara", color="#ff07c5", callback=loncat_bicara("rara"))
define kenzie = Character("Kenzie", color="#0857cf", callback=loncat_bicara("kenzie"))
define danisa = Character("Danisa", color="#ff0000", callback=loncat_bicara("danisa"))
define pak_joko = Character("Pak Joko", color="#10fa56", callback=loncat_bicara("joko"))

# Background sekolah MI
image bg lorong = "images/background/lorong_kelas.png"
image bg kelas = "images/background/ruang_kelas.png"
image bg halaman = "images/background/halaman_sekolah.png"
image bg lapangan = "images/background/lapangan_sekolah.png"
image bg jalan = "images/background/jalanan_desa.png"
image bg rumah = "images/background/halaman_rumah.png"
image bg taman = "images/background/taman.png"
image bg kantor_guru = "images/background/kantor_guru.png"

# Musik
define audio.bgm_pagi   = "audio/happy.mp3"
define audio.bgm_sekolah = "audio/happy.mp3"
define audio.bgm_tegang = "audio/tegang.mp3"
define audio.bgm_sedih  = "audio/sedih.mp3"
define audio.bgm_happy  = "audio/happy.mp3"
define audio.bgm_ending_baik = "audio/ending_baik.mp3"
define audio.bgm_ending_buruk = "audio/ending_buruk.mp3"

# Efek suara
define audio.bel_sekolah = "audio/bel.mp3"

# CG ending
image cg ending_baik = "images/cg/ending_baik.png"
image cg ending_buruk = "images/cg/ending_buruk.png"
image cg ending_normal = "images/cg/ending_normal.png"

# Sprite karakter rara
image rara normal = "images/characters/rara/rara_netral.png"
image rara sedih = "images/characters/rara/rara_sedih.png"
image rara bosan = "images/characters/rara/rara_bosan.png"
image rara kaget = "images/characters/rara/rara_kaget.png"
image rara kecewa = "images/characters/rara/rara_kecewa.png"
image rara curiga = "images/characters/rara/rara_curiga.png"
image rara takut = "images/characters/rara/rara_takut.png"
image rara marah_besar = "images/characters/rara/rara_sangat_marah.png"
image rara senang = "images/characters/rara/rara_senang.png"
image rara panik = "images/characters/rara/rara_panik.png"
image rara kesal = "images/characters/rara/rara_kesal.png"
image rara capek = "images/characters/rara/rara_capek.png"
image rara tertawa = "images/characters/rara/rara_tertawa.png"
image rara marah = "images/characters/rara/rara_marah.png"

# sprite karakter kenzie
image kenzie normal = "images/characters/Kenzie/k_netral.png"
image kenzie sedih = "images/characters/Kenzie/k_sedih.png"
image kenzie bosan = "images/characters/Kenzie/k_bosan.png"
image kenzie kaget = "images/characters/Kenzie/k_kaget.png"
image kenzie kecewa = "images/characters/Kenzie/k_kecewa.png"
image kenzie curiga = "images/characters/Kenzie/k_curiga.png"
image kenzie takut = "images/characters/Kenzie/k_takut.png"
image kenzie marah_besar = "images/characters/Kenzie/k_sangat_marah.png"
image kenzie senang = "images/characters/Kenzie/k_senang.png"
image kenzie panik = "images/characters/Kenzie/k_panik.png"
image kenzie kesal = "images/characters/Kenzie/k_kesal.png"
image kenzie tidur = "images/characters/Kenzie/k_tidur.png"
image kenzie menangis = "images/characters/Kenzie/k_menangis.png"

# sprite karakter danisa
image danisa normal = "images/characters/Danisa/Danisa_netral.png"
image danisa senyum = "images/characters/Danisa/Danisa_senyum.png"
image danisa mengejek = "images/characters/Danisa/Danisa_mengejek.png"
image danisa marah = "images/characters/Danisa/Danisa_marah.png"
image danisa bosan = "images/characters/Danisa/Danisa_bosan.png"
image danisa angkuh = "images/characters/Danisa/Danisa_angkuh.png"
image danisa buang_muka = "images/characters/Danisa/Danisa_buang_muka.png"
image danisa cemas = "images/characters/Danisa/Danisa_cemas.png"
image danisa sinis = "images/characters/Danisa/Danisa_sinis.png"
image danisa meremehkan = "images/characters/Danisa/Danisa_meremehkan.png"
image danisa menunjuk = "images/characters/Danisa/Danisa_menunjuk.png"
image danisa dingin = "images/characters/Danisa/Danisa_dingin.png"
image danisa kesal = "images/characters/Danisa/Danisa_kesal.png"
image danisa minum = "images/characters/Danisa/Danisa_minum.png"
image danisa terpesona = "images/characters/Danisa/Danisa_terpesona.png"
image danisa sombong = "images/characters/Danisa/Danisa_sombong.png"
image danisa pusing = "images/characters/Danisa/Danisa_pusing.png"
image danisa senyum_palsu = "images/characters/Danisa/Danisa_senyum_palsu.png"
image danisa jahil = "images/characters/Danisa/Danisa_jahil.png"
image danisa curiga = "images/characters/Danisa/Danisa_curiga.png"

# sprite karakter pak joko
image joko normal = "images/characters/Pak_joko/j_netral.png"
image joko sapa = "images/characters/Pak_joko/j_sapa.png"
image joko marah = "images/characters/Pak_joko/j_marah.png"
image joko tersenyum = "images/characters/Pak_joko/j_tersenyum.png"
image joko berpikir = "images/characters/Pak_joko/j_berpikir.png"
image joko curiga = "images/characters/Pak_joko/j_curiga.png"
image joko mengedip_tersenyum = "images/characters/Pak_joko/j_kedip.png"
image joko jempol = "images/characters/Pak_joko/j_jempol.png"
image joko pose_serius = "images/characters/Pak_joko/j_pose_dagu.png"
image joko kaget = "images/characters/Pak_joko/j_kaget.png"
image joko mengajar = "images/characters/Pak_joko/j_mengajar.png"

# Transform dan posisi sprite
define tinggi_sprite = int(config.screen_height * 0.40)
define lebar_sprite = int(tinggi_sprite * 0.85)
define dasar_sprite = -gui.textbox_height

transform talk_bounce:
    yoffset 0
    easeout 0.08 yoffset -14
    easein 0.10 yoffset 0

transform sprite_kiri:
    fit "contain"
    xysize (lebar_sprite, tinggi_sprite)
    xalign 0.12
    yalign 1.0
    yoffset dasar_sprite

transform sprite_tengah:
    fit "contain"
    xysize (lebar_sprite, tinggi_sprite)
    xalign 0.40
    yalign 1.0
    yoffset dasar_sprite

transform sprite_kanan_dalam:
    fit "contain"
    xysize (lebar_sprite, tinggi_sprite)
    xalign 0.65
    yalign 1.0
    yoffset dasar_sprite

transform sprite_kanan:
    fit "contain"
    xysize (lebar_sprite, tinggi_sprite)
    xalign 0.88
    yalign 1.0
    yoffset dasar_sprite

# Variabel
default pilihan = 0

# =====================================================
#  PROLOG
#  Kamu adalah Rara, sahabat Kenzie di kelas 5 MI.
# =====================================================
label start:
    scene bg jalan
    with fade

    # MUSIK: pagi yang tenang dan ceria
    play music bgm_pagi fadein 1.5

    "Senin pagi di perkampungan. Udara masih sejuk, dan embun belum sepenuhnya hilang dari daun-daun."
    "Kamu, Rara, berjalan ke Madrasah bersama sahabatmu, Kenzie."

    show rara normal at sprite_kanan_dalam
    show kenzie normal at sprite_kanan
    with dissolve

    rara "Kenzie, PR menggambar dari Pak Joko sudah selesai?"
    show kenzie senang at sprite_kanan
    kenzie "Sudah! Semalam aku menggambar sampai larut. Gambar masjid di tengah sawah, dengan matahari terbit."
    show rara senang at sprite_kanan_dalam
    rara "Wah, pasti bagus! Gambarmu kan selalu bagus."
    show kenzie sedih at sprite_kanan
    kenzie "Semoga... Tapi, Ra, hari ini aku agak deg-degan. Aku nggak mau ketemu Danisa."
    show rara curiga at sprite_kanan_dalam
    rara "Dia ganggu kamu lagi, ya?"
    show kenzie takut at sprite_kanan
    kenzie "Sudah seminggu ini. Katanya seragamku kusam, tasku jelek. Padahal aku sudah mencucinya sendiri tiap malam."
    show rara sedih at sprite_kanan_dalam
    rara "Jangan dipikirkan dulu. Ayo, kita jalan bareng. Aku ada di sebelahmu."
    show kenzie normal at sprite_kanan
    kenzie "Makasih, Ra."

    # ---------- Halaman sekolah ----------
    scene bg halaman
    with fade

    # MUSIK: masih lanjut ceria (tidak diulang dari awal karena if_changed)
    play music bgm_sekolah fadeout 1.0 fadein 1.0 if_changed

    "Di gerbang madrasah, seseorang sudah menunggu dengan tas baru berkilau dan botol minum bergambar karakter lucu."

    show danisa minum at sprite_kiri
    show rara normal at sprite_kanan_dalam
    show kenzie normal at sprite_kanan
    with dissolve

    # MUSIK: berubah tegang begitu Danisa mulai mengejek
    play music bgm_tegang fadeout 1.0 fadein 1.0
    danisa "Eh, lihat siapa yang datang. Kenzie! Seragammu itu nggak pernah ganti, ya? Jangan-jangan cuma punya satu."
    show kenzie takut at sprite_kanan
    kenzie "A-aku ganti kok... cuma memang sudah lama dipakai."
    show danisa mengejek at sprite_kiri
    danisa "Hahaha! Lihat tasnya juga. Itu tas zaman kapan? Nenekku saja nggak mau pakai."
    show rara kesal at sprite_kanan_dalam
    rara "Danisa, itu nggak lucu."
    show danisa sinis at sprite_kiri
    danisa "Ih, jangan sensitif gitu. Aku cuma bercanda. Kalian saja yang terlalu baper."

    # EFEK SUARA: bel
    play sound bel_sekolah
    "Bel masuk berbunyi. Danisa berlalu sambil tersenyum puas. Kenzie menunduk, jari-jarinya meremas tali tas yang sudah kusam."

    # ---------- Kelas: kejadian pemicu ----------
    scene bg kelas
    with fade

    # MUSIK: tetap tegang di kelas
    play music bgm_tegang fadeout 1.0 fadein 1.0 if_changed

    "Di kelas, semua murid mengeluarkan PR menggambar. Kenzie dengan hati-hati membuka map plastiknya."

    show danisa jahil at sprite_kiri
    show rara normal at sprite_kanan_dalam
    show kenzie senang at sprite_kanan
    with dissolve

    kenzie "Ini dia... akhirnya selesai."
    danisa "Coba lihat."
    show kenzie kaget at sprite_kanan
    kenzie "Eh, jangan! Nanti kusut..."
    show danisa mengejek at sprite_kiri
    danisa "Wah, katanya gambar masjid. Kok matahari-nya kayak telur dadar? Hahaha!"
    "Danisa mengangkat gambar itu tinggi-tinggi supaya seisi kelas bisa melihatnya. Beberapa anak mulai terkikik."

    # MUSIK: sedih saat Kenzie menangis dan sampai pilihan
    play music bgm_sedih fadeout 1.0 fadein 1.0
    show kenzie menangis at sprite_kanan
    kenzie "Kembalikan... tolong... itu aku kerjakan semalaman..."
    show danisa meremehkan at sprite_kiri
    danisa "Oh, semalaman? Pantas hasilnya segini."

    "Kenzie menunduk. Bahunya bergetar. Seisi kelas tiba-tiba terasa sangat sunyi, dan semua mata seolah menunggu apa yang akan kamu lakukan."

    jump pilihan_awal

label pilihan_awal:
    # Dipanggil juga saat pemain mengulang dari ending, jadi musik dipastikan sedih
    play music bgm_sedih fadeout 1.0 fadein 1.0 if_changed

    menu:
        "Apa yang akan Rara lakukan?"

        "Diam saja dan tidak ikut campur.":
            $ pilihan = 1
            jump ending_diam

        "Menegur Danisa dengan tegas.":
            $ pilihan = 2
            jump rute_tegur

        "Melapor ke Pak Joko.":
            $ pilihan = 3
            jump rute_lapor

# =====================================================
#  RUTE 1: DIAM  ->  BAD ENDING
# =====================================================
label ending_diam:
    scene bg kelas
    with fade

    # MUSIK: ending buruk
    play music bgm_ending_buruk fadeout 1.0 fadein 1.0

    show danisa mengejek at sprite_kiri
    show rara capek at sprite_kanan_dalam
    show kenzie menangis at sprite_kanan
    with dissolve

    "Kamu menunduk dan pura-pura sibuk membuka buku. Dadamu terasa sesak, tapi mulutmu tak mau bergerak."
    rara "(Kalau aku bicara... nanti aku yang jadi sasaran berikutnya.)"
    show danisa sinis at sprite_kiri
    danisa "Tuh, nggak ada yang protes. Berarti memang lucu, kan?"
    show kenzie sedih at sprite_kanan
    kenzie "Ra... kamu lihat, kan? Kenapa kamu diam saja?"
    show rara takut at sprite_kanan_dalam
    rara "A-aku... maaf, Kenzie."

    scene bg lorong
    with dissolve

    "Hari itu berlalu. Lalu hari berikutnya. Lalu minggu berikutnya."
    "Ejekan Danisa makin sering dan makin kasar. Tak ada lagi yang berani membela, karena semua belajar dari satu hal: diam itu aman."

    scene bg kelas
    with dissolve

    "Suatu pagi, bangku di sebelahmu kosong."
    show rara kecewa at sprite_kanan_dalam
    rara "Pak, Kenzie... nggak masuk lagi hari ini?"
    show joko berpikir at sprite_tengah
    pak_joko "Orang tuanya bilang Kenzie sudah tidak mau sekolah. Bapak sendiri baru tahu alasannya kemarin."
    show rara sedih at sprite_kanan_dalam
    rara "(Seandainya hari itu aku bicara... walau hanya satu kalimat.)"

    scene cg ending_buruk
    with Dissolve(1.5)

    "Bad Ending: Penyesalan karena menjadi bystander."
    "Karena kamu memilih diam, perundungan itu terus berlanjut sampai Kenzie kehilangan rasa amannya di sekolah."
    "Diam bukan berarti netral. Tidak ikut campur sering kali berarti membiarkan ketidakadilan terjadi."

    menu:
        "Coba lagi dari pilihan tadi?"

        "Ya, aku ingin memilih tindakan yang berbeda.":
            scene bg kelas
            with fade
            jump pilihan_awal

        "Tidak, cukup sampai di sini.":
            stop music fadeout 2.0
            return

# =====================================================
#  RUTE 2: MENEGUR
# =====================================================
label rute_tegur:
    scene bg kelas
    with fade

    show danisa angkuh at sprite_kiri
    show rara normal at sprite_kanan_dalam
    show kenzie menangis at sprite_kanan
    with dissolve

    "Kamu berdiri dari bangkumu. Kakimu gemetar, tapi kamu tahu ini harus dilakukan."
    "Bagaimana caramu menegur Danisa?"

    menu:
        "Bicara keras dan tegas.":
            jump tegur_keras

        "Bicara tenang dan baik-baik.":
            jump tegur_baik

# ---------- Tegur keras -> NORMAL ENDING ----------
label tegur_keras:
    # MUSIK: tegang karena adu mulut
    play music bgm_tegang fadeout 1.0 fadein 1.0

    show rara marah at sprite_kanan_dalam
    rara "Danisa! Kembalikan gambar Kenzie sekarang juga! Kamu pikir itu lucu?!"
    show danisa meremehkan at sprite_kiri
    danisa "Wah, ada pahlawan kesiangan. Memangnya kamu siapa, mau mengatur aku?"
    show rara kesal at sprite_kanan_dalam
    rara "Aku temannya! Dan teman nggak akan menertawakan kerja keras orang lain!"
    show danisa marah at sprite_kiri
    danisa "Kamu juga sama saja! Sok baik! Awas saja, nanti aku..."
    show kenzie takut at sprite_kanan
    kenzie "Sudah, Ra... jangan berantem... aku takut..."

    "Suasana kelas makin panas. Danisa dan kamu saling menatap tajam, sementara anak-anak lain mulai berbisik."

    jump masuk_pak_joko_keras

label masuk_pak_joko_keras:
    scene bg kelas
    with fade

    show joko curiga at sprite_tengah
    show rara kesal at sprite_kanan_dalam
    show kenzie takut at sprite_kanan
    show danisa marah at sprite_kiri
    with dissolve

    pak_joko "Ada apa ini? Suara kalian terdengar sampai lorong."
    danisa "Rara yang mulai, Pak! Dia membentak aku!"
    rara "Danisa mengambil gambar Kenzie dan mengejeknya, Pak!"
    show joko marah at sprite_tengah
    pak_joko "Stop. Keduanya, ikut Bapak ke kantor guru. Kenzie, kamu juga."

    scene bg kantor_guru
    with fade

    # MUSIK: suasana mereda, jadi sedih dan reflektif
    play music bgm_sedih fadeout 1.5 fadein 1.5

    show joko pose_serius at sprite_tengah
    show rara normal at sprite_kanan_dalam
    show kenzie sedih at sprite_kanan
    show danisa buang_muka at sprite_kiri
    with dissolve

    pak_joko "Rara. Bapak bangga kamu berani membela temanmu. Tapi membentak bukan cara yang tepat. Cara itu justru memicu pertengkaran baru."
    show rara kecewa at sprite_kanan_dalam
    rara "Iya, Pak... aku terlalu emosi."
    show joko berpikir at sprite_tengah
    pak_joko "Danisa, sekarang Bapak mau mendengar kamu. Kenapa kamu melakukan itu pada Kenzie?"
    show danisa cemas at sprite_kiri
    danisa "...Aku cuma bercanda, Pak."
    show joko normal at sprite_tengah
    pak_joko "Kalau satu orang menangis dan yang lain tertawa, itu bukan bercanda. Itu menyakiti."
    show kenzie sedih at sprite_kanan
    kenzie "Aku cuma ingin bisa belajar dengan tenang, Pak."
    show danisa buang_muka at sprite_kiri
    danisa "...Maaf, Kenzie."
    show kenzie kecewa at sprite_kanan
    kenzie "Iya... terima kasih."

    "Permintaan maaf itu terdengar singkat dan datar. Danisa belum benar-benar mengerti, dan Kenzie belum benar-benar tenang."

    show joko mengajar at sprite_tengah
    pak_joko "Meminta maaf itu langkah pertama. Memperbaiki sikap, itu langkah yang sesungguhnya. Bapak akan memantau kalian semua."

    scene cg ending_normal
    with Dissolve(1.5)

    # MUSIK: normal ending tetap bernuansa sedih (belum sepenuhnya selesai)
    "Normal Ending: Perundungan berhenti untuk sementara, tetapi luka dan rasa kesal belum sepenuhnya sembuh."
    "Berani membela adalah hal yang benar. Tetapi cara yang tenang membuat orang lebih mudah mendengar, dan lebih mudah berubah."
    "Mungkin ada cara yang lebih baik untuk menyelesaikannya."

    menu:
        "Coba lagi dari pilihan tadi?"

        "Ya, aku ingin mencoba cara lain.":
            scene bg kelas
            with fade
            jump pilihan_awal

        "Tidak, cukup sampai di sini.":
            stop music fadeout 2.0
            return

# ---------- Tegur baik -> TRUE ENDING ----------
label tegur_baik:
    # MUSIK: tetap lembut (sedih) selama Rara bicara tenang
    play music bgm_sedih fadeout 1.0 fadein 1.0 if_changed

    show rara normal at sprite_kanan_dalam
    rara "Danisa, boleh aku bicara sebentar? Tolong kembalikan gambar Kenzie dulu."
    show danisa angkuh at sprite_kiri
    danisa "Kenapa? Aku cuma lihat-lihat."
    show rara sedih at sprite_kanan_dalam
    rara "Aku tahu kamu mungkin nggak bermaksud jahat. Tapi Kenzie menggambarnya semalaman, dan dia menangis sekarang."
    show danisa meremehkan at sprite_kiri
    danisa "Itu salah dia sendiri, terlalu sensitif."
    show kenzie sedih at sprite_kanan
    kenzie "Danisa... aku nggak minta kamu memuji. Aku cuma minta kamu nggak menertawakan. Itu saja."

    "Kenzie bicara pelan, tapi seluruh kelas mendengar. Danisa tertegun. Senyum mengejeknya perlahan menghilang."

    show danisa cemas at sprite_kiri
    danisa "..."
    show rara normal at sprite_kanan_dalam
    rara "Aku juga pernah merasa kecil kalau ditertawakan. Rasanya nggak enak, kan?"
    show danisa buang_muka at sprite_kiri
    danisa "Kamu nggak tahu apa-apa soal aku."
    show rara sedih at sprite_kanan_dalam
    rara "Kamu benar, aku nggak tahu. Kalau kamu mau cerita, aku mau dengar."

    "Tangan Danisa gemetar sedikit saat menurunkan gambar itu. Ia meletakkannya perlahan di meja Kenzie."

    jump masuk_pak_joko_baik

label masuk_pak_joko_baik:
    scene bg kelas
    with fade

    show joko curiga at sprite_tengah
    show rara normal at sprite_kanan_dalam
    show kenzie normal at sprite_kanan
    show danisa cemas at sprite_kiri
    with dissolve

    pak_joko "Assalamu'alaikum, anak-anak. Kenapa kelas ini begitu hening? Ada yang bisa cerita pada Bapak?"
    rara "Wa'alaikumussalam, Pak. Tadi ada masalah kecil, tapi sekarang kami sedang berusaha menyelesaikannya."
    show joko berpikir at sprite_tengah
    pak_joko "Hmm. Danisa, Rara, Kenzie, ikut Bapak ke kantor guru sebentar. Tenang saja, tidak ada yang akan dimarahi."

    scene bg kantor_guru
    with fade

    show joko normal at sprite_tengah
    show rara normal at sprite_kanan_dalam
    show kenzie normal at sprite_kanan
    show danisa cemas at sprite_kiri
    with dissolve

    pak_joko "Bapak ingin kalian bergantian bercerita, tanpa dipotong. Kenzie, kamu dulu."
    show kenzie sedih at sprite_kanan
    kenzie "Sudah seminggu ini aku sering diejek soal seragam dan tasku. Aku jadi nggak mau berangkat sekolah, tapi aku nggak berani bilang ke siapa-siapa."
    show joko normal at sprite_tengah
    pak_joko "Terima kasih sudah berani bercerita, Kenzie. Sekarang kamu, Danisa."

    show danisa pusing at sprite_kiri
    danisa "...Di rumah, aku selalu dibanding-bandingkan, Pak. Nilaiku harus selalu paling bagus, barangku harus paling bagus. Kalau nggak, Mama kecewa."
    danisa "Waktu aku mengejek orang lain, aku merasa lebih hebat. Cuma sebentar... lalu aku merasa jahat."
    show kenzie kaget at sprite_kanan
    kenzie "Danisa..."
    show danisa cemas at sprite_kiri
    danisa "Aku nggak pernah benar-benar benci kamu, Kenzie. Aku cuma... nggak tahu cara berhenti. Maaf. Maaf banget."

    show joko tersenyum at sprite_tengah
    pak_joko "Terima kasih sudah jujur, Danisa. Mengakui salah itu berat, dan kamu sudah berani melakukannya."
    show joko mengajar at sprite_tengah
    pak_joko "Tapi ingat, rasa tertekan tidak membenarkan menyakiti orang lain. Bapak ingin kamu belajar mengelola perasaan itu, dan Bapak akan bantu bicara dengan orang tuamu juga."
    show kenzie normal at sprite_kanan
    kenzie "Aku maafkan, Danisa. Tapi janji, jangan diulang ya."

    # MUSIK: berubah hangat saat Danisa berjanji dan mereka berdamai
    play music bgm_ending_baik fadeout 1.5 fadein 1.5
    show danisa senyum at sprite_kiri
    danisa "Janji."

    scene bg taman
    with fade

    show danisa senyum at sprite_kiri
    show rara senang at sprite_kanan_dalam
    show kenzie senang at sprite_kanan
    with dissolve

    "Sepulang sekolah, di taman dekat madrasah."
    danisa "Kenzie... gambarmu kemarin sebenarnya bagus. Matahari-nya... aku salah bilang kayak telur dadar."
    show kenzie senang at sprite_kanan
    kenzie "Hehe, sebenarnya memang agak mirip kok."
    show rara tertawa at sprite_kanan_dalam
    rara "Hahaha! Kali ini aku setuju!"

    scene cg ending_baik
    with Dissolve(1.5)

    "True Ending: Keberanian yang lembut mengubah satu hati."
    "Rara menegur dengan tenang, Kenzie berani bersuara, dan Pak Joko membantu menyelesaikan akar masalahnya, bukan hanya menghukum."
    "Kadang, pelaku perundungan pun sedang membawa luka. Kita bisa tegas pada perbuatannya, tapi tetap peduli pada orangnya."

    stop music fadeout 3.0
    return

# =====================================================
#  RUTE 3: MELAPOR  ->  GOOD ENDING
# =====================================================
label rute_lapor:
    scene bg kelas
    with fade

    # MUSIK: tetap sedih saat Rara memutuskan melapor
    play music bgm_sedih fadeout 1.0 fadein 1.0 if_changed

    show danisa mengejek at sprite_kiri
    show rara normal at sprite_kanan_dalam
    show kenzie menangis at sprite_kanan
    with dissolve

    "Kamu tahu ini bukan sesuatu yang bisa kamu hadapi sendiri. Pelan-pelan, kamu menarik napas dan menggenggam tangan Kenzie."
    rara "Kenzie, ayo. Kita bicara dengan Pak Joko."
    show kenzie kaget at sprite_kanan
    kenzie "Tapi... nanti Danisa tambah marah."
    show rara normal at sprite_kanan_dalam
    rara "Melapor itu bukan mengadu. Ini supaya kamu aman. Nanti aku temani."

    scene bg kantor_guru
    with fade

    show joko sapa at sprite_tengah
    show rara normal at sprite_kanan_dalam
    show kenzie sedih at sprite_kanan
    with dissolve

    rara "Assalamu'alaikum, Pak Joko."
    pak_joko "Wa'alaikumussalam, Rara, Kenzie. Ada yang bisa Bapak bantu?"
    rara "Pak, kami ingin melapor. Danisa sudah seminggu mengejek Kenzie, dan tadi dia mengambil gambar Kenzie di depan kelas."
    show joko berpikir at sprite_tengah
    pak_joko "Terima kasih sudah datang, ya. Kenzie, kamu boleh cerita pelan-pelan. Bapak akan mendengarkan dan tidak akan menyalahkanmu."
    show kenzie takut at sprite_kanan
    kenzie "Aku takut sekolah, Pak. Rasanya... semua orang menertawakanku."
    show joko tersenyum at sprite_tengah
    pak_joko "Perasaanmu sangat penting, Nak. Kamu sudah melakukan hal yang tepat dengan datang ke sini. Bapak janji akan menanganinya dengan adil."

    scene bg kelas
    with fade

    # MUSIK: tegang sebentar saat Pak Joko menegur Danisa
    play music bgm_tegang fadeout 1.0 fadein 1.0

    show joko pose_serius at sprite_tengah
    show danisa cemas at sprite_kiri
    show rara normal at sprite_kanan_dalam
    show kenzie normal at sprite_kanan
    with dissolve

    pak_joko "Danisa, Bapak ingin bicara. Bukan untuk mempermalukanmu, tapi supaya semuanya jelas."
    danisa "Pak, aku cuma bercanda..."
    show joko marah at sprite_tengah
    pak_joko "Bercanda yang membuat teman takut berangkat sekolah itu bukan bercanda."
    show danisa buang_muka at sprite_kiri
    danisa "..."
    show joko berpikir at sprite_tengah
    pak_joko "Coba bayangkan kalau yang diperlakukan seperti itu adalah kamu. Bagaimana rasanya?"

    # MUSIK: melunak saat Danisa mulai sadar
    play music bgm_sedih fadeout 1.0 fadein 1.0
    show danisa cemas at sprite_kiri
    danisa "...Pasti sakit, Pak."
    show danisa pusing at sprite_kiri
    danisa "Aku benar-benar minta maaf, Kenzie. Aku nggak sadar seberapa dalam lukanya."

    show joko mengajar at sprite_tengah
    pak_joko "Penyesalan harus diikuti tindakan. Danisa, selama dua minggu kamu akan membantu Kenzie menyiapkan pameran gambar kelas. Rara, terima kasih sudah berani. Kalau ada kejadian lagi, langsung bilang ke Bapak."
    show kenzie senang at sprite_kanan
    kenzie "Makasih, Ra. Kamu berani banget."
    show rara senang at sprite_kanan_dalam
    rara "Kamu juga berani, Kenzie. Kamu mau cerita."

    scene bg lapangan
    with fade

    # MUSIK: good ending
    play music bgm_ending_baik fadeout 1.5 fadein 1.5

    show joko jempol at sprite_tengah
    show rara senang at sprite_kanan_dalam
    show kenzie senang at sprite_kanan
    show danisa normal at sprite_kiri
    with dissolve

    "Beberapa hari kemudian, di lapangan madrasah."
    danisa "Kenzie, ini cat air bekas punyaku. Masih bagus kok. Kalau kamu mau pakai untuk pameran."
    show kenzie kaget at sprite_kanan
    kenzie "Eh... beneran? Makasih, Danisa."
    show danisa senyum at sprite_kiri
    danisa "Sama-sama. Pelan-pelan aku belajar jadi lebih baik, ya."

    scene cg ending_baik
    with Dissolve(1.5)

    "Good Ending: Laporan diterima, dan masalah diselesaikan dengan bijaksana."
    "Melapor bukanlah mengadu. Itu cara melindungi diri dan orang lain ketika kita tidak bisa menyelesaikannya sendiri."
    "Dengan bantuan orang dewasa yang adil, korban terlindungi dan pelaku pun diberi kesempatan untuk belajar dan berubah."

    stop music fadeout 3.0
    return
