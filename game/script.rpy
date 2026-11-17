# ==============================================================================
#  MATAHARI DI KERTAS GAMBAR
#  Visual Novel Edukasi Anti-Perundungan (Bystander to Upstander - Prinsip 5D)
# ==============================================================================

# ------------------------------------------------------------------------------
#  Sistem posisi dinamis & animasi bicara (rollback-safe)
# ------------------------------------------------------------------------------
init -1 python:
    def atur_posisi(**kwargs):
        for nama_karakter, nama_slot in kwargs.items():
            setattr(store, "pos_" + nama_karakter, nama_slot)

    def ambil_slot_karakter(tag):
        nama_slot = getattr(store, "pos_" + tag, None)
        peta_slot = {
            "kiri": sprite_kiri,
            "tengah_kiri": sprite_tengah_kiri,
            "tengah": sprite_tengah,
            "tengah_kanan": sprite_tengah_kanan,
            "kanan": sprite_kanan,
            "duo_kiri": sprite_duo_kiri,
            "duo_kanan": sprite_duo_kanan,
            "tiga_kiri": sprite_tiga_kiri,
            "tiga_tengah": sprite_tiga_tengah,
            "tiga_kanan": sprite_tiga_kanan,
            "empat_1": sprite_empat_1,
            "empat_2": sprite_empat_2,
            "empat_3": sprite_empat_3,
            "empat_4": sprite_empat_4,
        }
        return peta_slot.get(nama_slot)

    def loncat_bicara(tag):
        def callback(event, interact=True, **kwargs):
            if event == "begin" and interact:
                slot = ambil_slot_karakter(tag)
                attrs = renpy.get_attributes(tag)
                if slot is not None and attrs is not None:
                    nama_dengan_atribut = tag if not attrs else tag + " " + " ".join(attrs)
                    renpy.show(nama_dengan_atribut, at_list=[slot, talk_bounce])
            return None
        return callback

# Warna nama karakter lembut agar nyaman dibaca di atas textbox gelap
define rara = Character("Rara", color="#ff8ec7", callback=loncat_bicara("rara"))
define kenzie = Character("Kenzie", color="#6bb6ff", callback=loncat_bicara("kenzie"))
define danisa = Character("Danisa", color="#ff7675", callback=loncat_bicara("danisa"))
define pak_joko = Character("Pak Joko", color="#7bed9f", callback=loncat_bicara("joko"))
define teman_kelas = Character("Murid Kelas 5", color="#cbd5e1")

# ------------------------------------------------------------------------------
#  Background & varian atmosfer (di-fit ke 1920x1080 agar bebas celah tepi)
# ------------------------------------------------------------------------------
image bg rumah = Transform("images/background/halaman_rumah.png", xysize=(1920, 1080), fit="cover")
image bg rumah_sore = Transform("images/background/halaman_rumah.png", xysize=(1920, 1080), fit="cover", matrixcolor=TintMatrix("#d8a086") * BrightnessMatrix(-0.08))
image bg jalan = Transform("images/background/jalanan_desa.png", xysize=(1920, 1080), fit="cover")
image bg halaman = Transform("images/background/halaman_sekolah.png", xysize=(1920, 1080), fit="cover")
image bg lorong = Transform("images/background/lorong_kelas.png", xysize=(1920, 1080), fit="cover")
image bg kelas = Transform("images/background/ruang_kelas.png", xysize=(1920, 1080), fit="cover")
image bg kelas_kelabu = Transform("images/background/ruang_kelas.png", xysize=(1920, 1080), fit="cover", matrixcolor=TintMatrix("#9eb2cc") * SaturationMatrix(0.55) * BrightnessMatrix(-0.12))
image bg kantor_guru = Transform("images/background/kantor_guru.png", xysize=(1920, 1080), fit="cover")
image bg taman = Transform("images/background/taman.png", xysize=(1920, 1080), fit="cover")
image bg lapangan = Transform("images/background/lapangan_sekolah.png", xysize=(1920, 1080), fit="cover")

# Musik & efek suara
define audio.bgm_pagi = "audio/happy.mp3"
define audio.bgm_sekolah = "audio/happy.mp3"
define audio.bgm_tegang = "audio/tegang.mp3"
define audio.bgm_sedih = "audio/sedih.mp3"
define audio.bgm_happy = "audio/happy.mp3"
define audio.bgm_ending_baik = "audio/ending_baik.mp3"
define audio.bgm_ending_buruk = "audio/ending_buruk.mp3"
define audio.bel_sekolah = "audio/bel.mp3"

# CG Ending
image cg ending_baik = Transform("images/cg/ending_baik.png", xysize=(1920, 1080), fit="cover")
image cg ending_normal = Transform("images/cg/ending_normal.png", xysize=(1920, 1080), fit="cover")
image cg ending_buruk = Transform("images/cg/ending_buruk.png", xysize=(1920, 1080), fit="cover")

# ------------------------------------------------------------------------------
#  Sprite Karakter (path persis sesuai disk & ekspresi visual akurat)
# ------------------------------------------------------------------------------
# Rara
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
image rara menangis = "images/characters/rara/rara_menangis.png"
image rara tersedu = "images/characters/rara/rara_tersedu.png"

# Kenzie (k_kecewa = sedih lembut, k_takut/k_sedih = panik keringat)
image kenzie normal = "images/characters/Kenzie/k_netral.png"
image kenzie sedih = "images/characters/Kenzie/k_kecewa.png"
image kenzie kecewa = "images/characters/Kenzie/k_kecewa.png"
image kenzie murung = "images/characters/Kenzie/k_bosan.png"
image kenzie bosan = "images/characters/Kenzie/k_bosan.png"
image kenzie curiga = "images/characters/Kenzie/k_curiga.png"
image kenzie kaget = "images/characters/Kenzie/k_kaget.png"
image kenzie takut = "images/characters/Kenzie/k_takut.png"
image kenzie panik = "images/characters/Kenzie/k_panik.png"
image kenzie panik_keringat = "images/characters/Kenzie/k_sedih.png"
image kenzie kesal = "images/characters/Kenzie/k_kesal.png"
image kenzie marah = "images/characters/Kenzie/k_marah.png"
image kenzie marah_besar = "images/characters/Kenzie/k_sangat_marah.png"
image kenzie senang = "images/characters/Kenzie/k_senang.png"
image kenzie tertawa = "images/characters/Kenzie/k_tertawa.png"
image kenzie tidur = "images/characters/Kenzie/k_tidur.png"
image kenzie menangis = "images/characters/Kenzie/k_menangis.png"
image kenzie tersedu = "images/characters/Kenzie/k_tersedu.png"
image kenzie kacamata = "images/characters/Kenzie/k_kacamata.png"

# Danisa (folder lowercase 'danisa', perhatikan huruf kapital pada Marah & Senyum)
image danisa normal = "images/characters/danisa/danisa_netral.png"
image danisa senyum = "images/characters/danisa/Danisa_senyum.png"
image danisa terpesona = "images/characters/danisa/danisa_terpesona.png"
image danisa senyum_palsu = "images/characters/danisa/danisa_senyum_palsu.png"
image danisa gugup = "images/characters/danisa/danisa_cemas.png"
image danisa cemas = "images/characters/danisa/danisa_buang_muka.png"
image danisa buang_muka = "images/characters/danisa/danisa_buang_muka.png"
image danisa pusing = "images/characters/danisa/danisa_pusing.png"
image danisa mengejek = "images/characters/danisa/danisa_mengejek.png"
image danisa meremehkan = "images/characters/danisa/danisa_meremehkan.png"
image danisa angkuh = "images/characters/danisa/danisa_angkuh.png"
image danisa menunjuk = "images/characters/danisa/danisa_menunjuk.png"
image danisa sombong = "images/characters/danisa/danisa_sombong.png"
image danisa congkak = "images/characters/danisa/danisa_congkak.png"
image danisa sinis = "images/characters/danisa/danisa_sinis.png"
image danisa dingin = "images/characters/danisa/danisa_dingin.png"
image danisa lirik_tajam = "images/characters/danisa/danisa_lirik_tajam.png"
image danisa curiga = "images/characters/danisa/danisa_curiga.png"
image danisa jahil = "images/characters/danisa/danisa_jahil.png"
image danisa minum = "images/characters/danisa/danisa_minum.png"
image danisa kesal = "images/characters/danisa/danisa_kesal.png"
image danisa marah = "images/characters/danisa/Danisa_marah.png"

# Pak Joko
image joko normal = "images/characters/Pak_joko/j_netral.png"
image joko sapa = "images/characters/Pak_joko/j_sapa.png"
image joko tersenyum = "images/characters/Pak_joko/j_tersenyum.png"
image joko kedip = "images/characters/Pak_joko/j_kedip.png"
image joko jempol = "images/characters/Pak_joko/j_jempol.png"
image joko garuk_kepala = "images/characters/Pak_joko/j_garuk_kepala.png"
image joko mengajar = "images/characters/Pak_joko/j_mengajar.png"
image joko berpikir = "images/characters/Pak_joko/j_berpikir.png"
image joko pose_serius = "images/characters/Pak_joko/j_pose_dagu.png"
image joko curiga = "images/characters/Pak_joko/j_curiga.png"
image joko kaget = "images/characters/Pak_joko/j_kaget.png"
image joko lemas = "images/characters/Pak_joko/j_lemas.png"
image joko kertas = "images/characters/Pak_joko/j_kertas.png"
image joko kopi = "images/characters/Pak_joko/j_kopi.png"
image joko baca_buku = "images/characters/Pak_joko/j_baca_buku.png"
image joko laptop = "images/characters/Pak_joko/j_laptop.png"

# ------------------------------------------------------------------------------
#  Transform & Posisi Sprite (skala 48% layar, duduk rapi di atas textbox)
# ------------------------------------------------------------------------------
define tinggi_sprite = int(config.screen_height * 0.48)
define lebar_sprite = tinggi_sprite
define garis_dasar_sprite = config.screen_height - gui.textbox_height + 26

transform talk_bounce:
    yoffset 0
    easeout 0.08 yoffset -16
    easein 0.10 yoffset 0

transform sprite_kiri:
    fit "contain"
    xysize (lebar_sprite, tinggi_sprite)
    xalign 0.08
    ypos garis_dasar_sprite
    yanchor 1.0

transform sprite_tengah_kiri:
    fit "contain"
    xysize (lebar_sprite, tinggi_sprite)
    xalign 0.34
    ypos garis_dasar_sprite
    yanchor 1.0

transform sprite_tengah:
    fit "contain"
    xysize (lebar_sprite, tinggi_sprite)
    xalign 0.50
    ypos garis_dasar_sprite
    yanchor 1.0

transform sprite_tengah_kanan:
    fit "contain"
    xysize (lebar_sprite, tinggi_sprite)
    xalign 0.66
    ypos garis_dasar_sprite
    yanchor 1.0

transform sprite_kanan:
    fit "contain"
    xysize (lebar_sprite, tinggi_sprite)
    xalign 0.92
    ypos garis_dasar_sprite
    yanchor 1.0

transform sprite_duo_kiri:
    fit "contain"
    xysize (lebar_sprite, tinggi_sprite)
    xalign 0.24
    ypos garis_dasar_sprite
    yanchor 1.0

transform sprite_duo_kanan:
    fit "contain"
    xysize (lebar_sprite, tinggi_sprite)
    xalign 0.76
    ypos garis_dasar_sprite
    yanchor 1.0

transform sprite_tiga_kiri:
    fit "contain"
    xysize (lebar_sprite, tinggi_sprite)
    xalign 0.14
    ypos garis_dasar_sprite
    yanchor 1.0

transform sprite_tiga_tengah:
    fit "contain"
    xysize (lebar_sprite, tinggi_sprite)
    xalign 0.50
    ypos garis_dasar_sprite
    yanchor 1.0

transform sprite_tiga_kanan:
    fit "contain"
    xysize (lebar_sprite, tinggi_sprite)
    xalign 0.86
    ypos garis_dasar_sprite
    yanchor 1.0

transform sprite_empat_1:
    fit "contain"
    xysize (lebar_sprite, tinggi_sprite)
    xalign 0.02
    ypos garis_dasar_sprite
    yanchor 1.0

transform sprite_empat_2:
    fit "contain"
    xysize (lebar_sprite, tinggi_sprite)
    xalign 0.34
    ypos garis_dasar_sprite
    yanchor 1.0

transform sprite_empat_3:
    fit "contain"
    xysize (lebar_sprite, tinggi_sprite)
    xalign 0.66
    ypos garis_dasar_sprite
    yanchor 1.0

transform sprite_empat_4:
    fit "contain"
    xysize (lebar_sprite, tinggi_sprite)
    xalign 0.98
    ypos garis_dasar_sprite
    yanchor 1.0

# ------------------------------------------------------------------------------
#  Variabel Permainan (Rollback-safe)
# ------------------------------------------------------------------------------
default pos_danisa = "kiri"
default pos_joko = "tengah"
default pos_rara = "tengah_kanan"
default pos_kenzie = "kanan"

default keberanian = 0
default empati = 0
default kepercayaan_kenzie = 1
default kesadaran_danisa = 0

default tahu_bukti_sebelumnya = False
default pernah_menenangkan_kenzie = False
default tahu_alasan_danisa = False

default d_direct = False
default d_distract = False
default d_delegate = False
default d_delay = False
default d_document = False

# Snapshot checkpoint Babak 3
default cp_keberanian = 0
default cp_empati = 0
default cp_kepercayaan = 1
default cp_kesadaran = 0
default cp_direct = False
default cp_distract = False
default cp_delegate = False
default cp_delay = False
default cp_document = False
default cp_alasan_danisa = False
default cp_menenangkan = False
default cp_bukti = False

# ==============================================================================
#  BABAK 1: PAGI DI RUMAH & JALANAN DESA (BONDING & FORESHADOWING)
# ==============================================================================
label start:
    # Reset variabel tiap memulai permainan baru
    $ keberanian = 0
    $ empati = 0
    $ kepercayaan_kenzie = 1
    $ kesadaran_danisa = 0
    $ tahu_bukti_sebelumnya = False
    $ pernah_menenangkan_kenzie = False
    $ tahu_alasan_danisa = False
    $ d_direct = False
    $ d_distract = False
    $ d_delegate = False
    $ d_delay = False
    $ d_document = False

    scene bg rumah
    with fade

    play music bgm_pagi fadeout 1.0 fadein 1.5 if_changed

    "Senin pagi di perkampungan. Cahaya matahari masih hangat menyentuh pagar rumah, sementara bau tanah basah sisa embun semalam masih terasa segar."
    "Kamu, Rara, siswi kelas 5 Madrasah Ibtidaiyah, sedang terburu-buru mengikat tali sepatu di halaman rumah."

    $ atur_posisi(rara="duo_kiri", kenzie="duo_kanan")
    show rara panik at sprite_duo_kiri
    show kenzie senang at sprite_duo_kanan
    with dissolve

    rara "Aduh, ke mana penghapusku? Perasaan semalam sudah kumasukkan ke tempat pensil..."
    kenzie "Pagi, Ra! Pakai punyaku dulu saja, aku bawa dua dari rumah."
    show rara senang at sprite_duo_kiri
    rara "Kenzie! Wah, kamu penyelamat pagi ini. Makasih, ya!"

    "Kenzie tersenyum sambil memeluk sebuah map plastik bening yang sudutnya sudah sedikit lusuh, tetapi dijaga dengan sangat hati-hati."
    show kenzie tidur at sprite_duo_kanan
    kenzie "Huwaah... aku agak mengantuk sedikit, tapi puas banget. PR gambar masjid untuk seleksi Pameran Lukisan Madrasah akhirnya selesai semalam!"
    show rara tertawa at sprite_duo_kiri
    rara "Jam berapa kamu tidur? Pasti rapi banget hasilnya."
    show kenzie senang at sprite_duo_kanan
    kenzie "Hampir jam sepuluh. Sebelum tidur aku juga sempat mencuci seragamku biar pagi ini tetap bersih dan wangi."
    show rara normal at sprite_duo_kiri
    "Kamu melirik seragam Kenzie. Warnanya memang sudah sedikit memudar karena sering dipakai bergantian hanya dengan dua setel baju, tapi setrikaannya rapi sekali."
    rara "Kamu hebat, Kenz. Ayo berangkat sekarang, nanti gerbang keburu ramai."

    # ---------- Jalanan desa ----------
    scene bg jalan
    with fade

    $ atur_posisi(rara="duo_kiri", kenzie="duo_kanan")
    show rara normal at sprite_duo_kiri
    show kenzie normal at sprite_duo_kanan
    with dissolve

    "Kalian berjalan berdampingan menyusuri jalanan desa yang teduh oleh pepohonan."
    "Namun, semakin dekat ke arah madrasah, langkah Kenzie melambat. Jarinya terus meremas tali tasnya sendiri."

    show rara curiga at sprite_duo_kiri
    rara "Kenzie, kok tiba-tiba diam? Perutmu sakit atau takut tugasnya belum dinilai?"
    show kenzie murung at sprite_duo_kanan
    kenzie "Bukan, Ra... aku cuma agak malas melewati gerbang kalau sudah jam segini."
    show kenzie sedih at sprite_duo_kanan
    kenzie "Sudah seminggu ini Danisa sering menyindirku di depan anak-anak lain. Katanya seragamku kusam, tasku jadul, sampai kemarin bekal tempeku juga diketawain."
    show rara kaget at sprite_duo_kiri
    rara "Sudah seminggu?! Kenapa kamu baru cerita sekarang?"
    show kenzie normal at sprite_duo_kanan
    kenzie "Aku takut kalau aku cerita, kamu malah ikut-ikutan dijauhi Danisa..."

    menu:
        "Bagaimana kamu menanggapi curhatan Kenzie di jalan?"

        "Tanya detail kapan dan di mana saja Danisa sering mengejeknya.":
            $ empati += 1
            $ kepercayaan_kenzie += 1
            $ tahu_bukti_sebelumnya = True
            $ d_document = True
            show rara curiga at sprite_duo_kiri
            rara "Kenz, coba ceritakan kapan saja dia melakukan itu. Di gerbang tiap pagi? Atau saat istirahat di kelas?"
            show kenzie normal at sprite_duo_kanan
            kenzie "Biasanya pagi di dekat papan pengumuman, lalu pas istirahat kalau Pak Joko keluar kelas."
            show rara normal at sprite_duo_kiri
            rara "Baik, aku ingat-ingat semuanya. Kalau sewaktu-waktu kita perlu bicara ke Pak Joko, kita punya cerita yang jelas, bukan cuma mengira-ngira."
            show kenzie senang at sprite_duo_kanan
            kenzie "Rasanya lega banget ada yang mau mendengar tanpa menganggapku lebay, Ra."

        "Beri semangat supaya Kenzie tetap percaya diri berjalan di sebelahmu.":
            $ keberanian += 1
            $ kepercayaan_kenzie += 1
            show rara senang at sprite_duo_kiri
            rara "Nggak akan ada yang aku takutkan hanya gara-gara membela sahabatku sendiri. Hari ini kita jalan bareng terus, ya."
            show kenzie senang at sprite_duo_kanan
            kenzie "Makasih banyak, Ra. Mendengar itu bikin dadaku sedikit lebih ringan."

        "Sarankan agar kalian menghindar saja supaya tidak cari masalah.":
            show rara sedih at sprite_duo_kiri
            rara "Kalau ketemu dia nanti, kita langsung menunduk dan cepat masuk kelas saja, ya. Jangan dilayani biar dia bosan sendiri."
            show kenzie murung at sprite_duo_kanan
            kenzie "Iya... semoga hari ini dia sedang tidak melihat kita."
            "Kenzie mengangguk pelan, meski bahunya masih tampak menegang."

    jump babak_2_sekolah

# ==============================================================================
#  BABAK 2: GERBANG & LORONG MADRASAH (ESKALASI AWAL)
# ==============================================================================
label babak_2_sekolah:
    scene bg halaman
    with fade

    play music bgm_sekolah fadeout 1.0 fadein 1.0 if_changed

    "Setibanya di halaman madrasah, beberapa murid tampak berkumpul di dekat papan pengumuman."
    "Di sana berdiri Danisa sambil menyeruput minuman kemasan dengan tas barunya yang berkilau."

    $ atur_posisi(danisa="tiga_kiri", rara="tiga_tengah", kenzie="tiga_kanan")
    show danisa minum at sprite_tiga_kiri
    show rara normal at sprite_tiga_tengah
    show kenzie normal at sprite_tiga_kanan
    with dissolve

    play music bgm_tegang fadeout 1.0 fadein 1.0

    show danisa lirik_tajam at sprite_tiga_kiri
    danisa "Eh, lihat siapa yang datang tepat waktu dengan map plastik legendanya."
    show danisa mengejek at sprite_tiga_kiri
    danisa "Kenzie, seragammu warnanya makin pudar, ya? Jangan-jangan dari kelas empat sampai kelas lima bajumu cuma itu-itu saja!"
    show kenzie takut at sprite_tiga_kanan
    kenzie "A-aku mencucinya tiap malam kok... cuma memang sudah lama..."
    show danisa angkuh at sprite_tiga_kiri
    danisa "Hihihi, rajin sekali mencuci baju warisan. Eh, teman-teman, lihat deh tali tasnya sudah hampir putus!"
    "Beberapa anak di dekat papan pengumuman menoleh dan mulai berbisik. Kenzie menunduk dalam-dalam."

    menu:
        "Apa reaksimu melihat Danisa menyindir Kenzie di gerbang?"

        "Tegur langsung sindiran Danisa dengan tegas (Direct).":
            $ keberanian += 1
            $ kepercayaan_kenzie += 1
            $ d_direct = True
            show rara marah at sprite_tiga_tengah
            rara "Danisa, cukup! Seragam bersih nggak harus baru. Berhenti menjadikan barang teman sebagai bahan tertawaan."
            show danisa gugup at sprite_tiga_kiri
            danisa "Ih, pagi-pagi sudah galak banget. Aku kan cuma bercanda, kalian saja yang terlalu baper."
            show rara kesal at sprite_tiga_tengah
            rara "Kalau yang kamu ejek nggak ikut tertawa, itu bukan bercanda."
            show danisa sinis at sprite_tiga_kiri
            danisa "Terserah deh."

        "Alihkan perhatian dan ajak Kenzie cepat masuk ke lorong (Distract).":
            $ empati += 1
            $ kepercayaan_kenzie += 1
            $ d_distract = True
            show rara kaget at sprite_tiga_tengah
            rara "Eh, Pak Joko sudah berjalan ke arah lorong kelas membawa daftar absen! Ayo, Kenz, nanti keburu ditanya tugas!"
            show danisa curiga at sprite_tiga_kiri
            danisa "Hah? Pak Joko sudah datang?"
            show kenzie normal at sprite_tiga_kanan
            "Kamu menggandeng lengan Kenzie berjalan melewati kerumunan tanpa memberi Danisa panggung untuk melanjutkan ejekannya."
            show danisa kesal at sprite_tiga_kiri
            danisa "Cih... kabur saja bisanya."

        "Diam menunduk dan menarik baju Kenzie pelan agar segera lewat.":
            if kepercayaan_kenzie > 0:
                $ kepercayaan_kenzie -= 1
            show rara capek at sprite_tiga_tengah
            "Kamu menundukkan pandangan dan menarik ujung lengan baju Kenzie pelan tanpa mengeluarkan sepatah kata pun."
            show danisa meremehkan at sprite_tiga_kiri
            danisa "Hahaha! Benar kan, nggak ada yang membantah. Berarti memang lucu!"
            show kenzie sedih at sprite_tiga_kanan
            "Kenzie mengecilkan bahunya dan berjalan di sampingmu dalam diam."

    play sound bel_sekolah
    "Bel tanda bersiap masuk berbunyi nyaring di penjuru halaman madrasah."

    # ---------- Lorong kelas: Foreshadowing Pameran & Tekanan Danisa ----------
    scene bg lorong
    with fade

    play music bgm_pagi fadeout 1.0 fadein 1.0 if_changed

    "Di lorong kelas, suasana masih ramai oleh murid-murid yang berjalan menuju ruang masing-masing."

    $ atur_posisi(danisa="empat_1", joko="empat_2", rara="empat_3", kenzie="empat_4")
    show danisa pusing at sprite_empat_1
    show joko kertas at sprite_empat_2
    show rara normal at sprite_empat_3
    show kenzie normal at sprite_empat_4
    with dissolve

    show joko sapa at sprite_empat_2
    pak_joko "Assalamu'alaikum anak-anak kelas 5! Pagi ini kita langsung kumpulkan tugas gambar bertema lingkungan sekitar, ya."
    show joko mengajar at sprite_empat_2
    pak_joko "Ingat, lima karya paling unik akan Bapak pajang di Pameran Lukisan Madrasah minggu depan. Yang penting bukan mahalnya alat gambar, melainkan ketulusan dan ceritanya."
    show kenzie senang at sprite_empat_4
    kenzie "Wah, semoga gambarku bisa terpilih..."
    show joko kedip at sprite_empat_2
    pak_joko "Danisa, tugasmu sudah siap juga, Nak?"

    "Saat Pak Joko menoleh, Danisa yang sedari tadi memandang kertas gambarnya dengan dahi berkerut langsung buru-buru merapikan ekspresinya."
    show danisa senyum_palsu at sprite_empat_1
    danisa "P-pasti siap dong, Pak! Mama sudah membelikan cat air impor yang paling mahal. Kalau nggak masuk tiga besar, nanti Mama marah di rumah... eh, maksudku, pasti bagus kok, Pak!"
    show joko berpikir at sprite_empat_2
    pak_joko "Hmm... Bapak menilai usahamu sendiri, bukan harga catnya, ya. Bapak tunggu di kelas lima menit lagi."
    hide joko
    with dissolve

    "Pak Joko berjalan menuju kantor guru terlebih dahulu untuk mengambil absen."
    show danisa pusing at sprite_empat_1
    "Begitu Pak Joko pergi, senyum Danisa langsung luntur. Kamu sempat melihatnya menggigit bibir sambil menatap kertas gambarnya sendiri dengan gelisah sebelum ia masuk ke kelas."
    show rara curiga at sprite_empat_3
    rara "(Tadi Danisa kelihatan panik waktu menyebut mamanya...)"

    jump babak_3_insiden_kelas

# ==============================================================================
#  BABAK 3: KLIMAKS DI RUANG KELAS
# ==============================================================================
label babak_3_insiden_kelas:
    scene bg kelas
    with fade

    play music bgm_sekolah fadeout 1.0 fadein 1.0 if_changed

    "Di dalam kelas, para murid mengeluarkan tugas gambar ke atas meja sambil menunggu Pak Joko datang."
    "Kenzie membuka map plastiknya pelan-pelan dan meletakkan gambar masjid di tengah sawah dengan warna matahari terbit yang hangat."

    $ atur_posisi(danisa="tiga_kiri", rara="tiga_tengah", kenzie="tiga_kanan")
    show danisa lirik_tajam at sprite_tiga_kiri
    show rara senang at sprite_tiga_tengah
    show kenzie senang at sprite_tiga_kanan
    with dissolve

    teman_kelas "Eh, lihat punya Kenzie! Perpaduan warna langit sama sawahnya bagus banget!"
    rara "Tuh kan, aku bilang juga apa! Mataharinya kelihatan hangat banget."
    show kenzie tertawa at sprite_tiga_kanan
    kenzie "Hehe, makasih semuanya. Ini tadi warnanya aku campur pelan-pelan pakai pensil warna pendek."

    "Dari meja sebelah, Danisa menoleh tajam. Wajahnya yang tadinya murung berubah kesal mendengar teman-teman memuji gambar Kenzie."
    play music bgm_tegang fadeout 1.0 fadein 1.0
    show danisa jahil at sprite_tiga_kiri
    danisa "Mana coba lihat, katanya bagus banget."
    show kenzie kaget at sprite_tiga_kanan
    kenzie "Eh, jangan ditarik, Danisa! Nanti kertasnya kusut—"

    "SREK!" with hpunch
    "Sebelum Kenzie sempat menahan, Danisa sudah merebut kertas gambar itu dan mengangkatnya tinggi-tinggi di hadapan seisi kelas!"

    show danisa mengejek at sprite_tiga_kiri
    danisa "Hahaha! Katanya gambar masjid untuk pameran, kok mataharinya bulat oranye kayak telur dadar gosong begini?!"
    show danisa menunjuk at sprite_tiga_kiri
    danisa "Mana garis masjidnya miring lagi! Ini sih bukan karya pameran, tapi coretan anak TK!"

    teman_kelas "Hahahaha... iya juga ya, bulatnya mirip telur dadar!"
    "Beberapa murid di barisan belakang ikut terkikik karena mengira hal itu sekadar candaan lucu."

    play music bgm_sedih fadeout 1.0 fadein 1.0
    show kenzie panik at sprite_tiga_kanan
    kenzie "Kembalikan, Danisa... tolong jangan diangkat begitu... itu aku gambar semalaman..."
    show danisa meremehkan at sprite_tiga_kiri
    danisa "Oh, semalaman? Kasihan banget sudah begadang tapi hasilnya begini. Kertas lecek gini masih ngarep dipajang?"

    show kenzie menangis at sprite_tiga_kanan
    "Sudut kertas gambar itu mulai tertekuk di genggaman Danisa. Air mata Kenzie akhirnya jatuh. Bahunya bergetar menahan isakan."
    "Suasana kelas mendadak menjadi senyap. Candaan anak-anak terhenti, dan beberapa pasang mata menoleh ke arahmu—menunggu apa yang akan dilakukan sahabat terdekat Kenzie."

label simpan_checkpoint_kelas:
    $ cp_keberanian = keberanian
    $ cp_empati = empati
    $ cp_kepercayaan = kepercayaan_kenzie
    $ cp_kesadaran = kesadaran_danisa
    $ cp_direct = d_direct
    $ cp_distract = d_distract
    $ cp_delegate = d_delegate
    $ cp_delay = d_delay
    $ cp_document = d_document
    $ cp_alasan_danisa = tahu_alasan_danisa
    $ cp_menenangkan = pernah_menenangkan_kenzie
    $ cp_bukti = tahu_bukti_sebelumnya

label pilihan_awal:
    play music bgm_sedih fadeout 1.0 fadein 1.0 if_changed

    menu:
        "Semua mata tertuju pada situasi di depan. Apa yang akan Rara lakukan?"

        "Diam saja dan menunduk pura-pura membuka buku catatan.":
            jump rute_diam

        "Berdiri cepat dan membentak Danisa agar segera mengembalikannya!":
            jump rute_tegur_keras

        "Berdiri tenang, menjaga nada bicara, dan menegur Danisa dengan tegas (Direct).":
            jump rute_tegur_tenang

        "Segera mendampingi Kenzie, memutus kerumunan, dan mengajak melapor ke Pak Joko (Distract & Delegate).":
            jump rute_lapor

label muat_checkpoint_kelas:
    $ keberanian = cp_keberanian
    $ empati = cp_empati
    $ kepercayaan_kenzie = cp_kepercayaan
    $ kesadaran_danisa = cp_kesadaran
    $ d_direct = cp_direct
    $ d_distract = cp_distract
    $ d_delegate = cp_delegate
    $ d_delay = cp_delay
    $ d_document = cp_document
    $ tahu_alasan_danisa = cp_alasan_danisa
    $ pernah_menenangkan_kenzie = cp_menenangkan
    $ tahu_bukti_sebelumnya = cp_bukti

    scene bg kelas
    $ atur_posisi(danisa="tiga_kiri", rara="tiga_tengah", kenzie="tiga_kanan")
    show danisa meremehkan at sprite_tiga_kiri
    show rara normal at sprite_tiga_tengah
    show kenzie menangis at sprite_tiga_kanan
    with fade
    jump pilihan_awal

# ==============================================================================
#  CABANG 1: RUTE DIAM (BYSTANDER DILEMMA -> KESEMPATAN KEDUA)
# ==============================================================================
label rute_diam:
    scene bg kelas
    $ atur_posisi(danisa="tiga_kiri", rara="tiga_tengah", kenzie="tiga_kanan")
    show danisa meremehkan at sprite_tiga_kiri
    show rara takut at sprite_tiga_tengah
    show kenzie menangis at sprite_tiga_kanan
    with dissolve

    "Jantungmu berdegup kencang. Tenggorokanmu seakan tercekat. Kamu menunduk dan pura-pura membalik halaman buku tulis."
    rara "(Kalau aku berdiri membela sekarang... bagaimana kalau besok Danisa juga mengejekku di depan seluruh kelas?)"

    show danisa sinis at sprite_tiga_kiri
    danisa "Tuh, sahabatmu sendiri saja diam. Berarti dia juga setuju gambarmu aneh, kan?"
    "Danisa melempar kertas gambar itu kembali ke meja Kenzie begitu saja hingga sudutnya semakin terlipat."
    show kenzie sedih at sprite_tiga_kanan
    kenzie "Ra... kamu lihat semuanya, kan? Kenapa kamu cuma diam?"
    show rara capek at sprite_tiga_tengah
    rara "A-aku... maaf, Kenz. Nanti saja bicaranya..."

    if kepercayaan_kenzie > 0:
        $ kepercayaan_kenzie -= 1

    "Sesaat kemudian Pak Joko masuk ke kelas. Sepanjang pelajaran hingga jam pulang, Kenzie tak lagi menoleh ke arahmu. Saat pulang sekolah pun ia berjalan lebih dulu tanpa menunggumu."

    # ---------- Sore hari di rumah: Momen refleksi & kesempatan kedua ----------
    scene bg rumah_sore
    with fade

    play music bgm_sedih fadeout 1.0 fadein 1.0 if_changed

    $ atur_posisi(rara="tengah")
    show rara kecewa at sprite_tengah
    with dissolve

    "Sore hari di halaman rumah. Langit mulai memerah, namun hatimu terasa sesak."
    "Bayangan mata Kenzie yang berkaca-kaca saat menatapmu terus terulang di pikiranmu."
    rara "(Aku merasa tidak ikut mengejek, jadi kukira aku tidak bersalah... Tapi melihat wajah Kenzie tadi, diamku justru membuatnya merasa sendirian.)"
    rara "(Dan Danisa semakin yakin tidak ada yang berani melarangnya. Besok masih ada hari esok... apa yang harus kulakukan?)"

    menu:
        "Malam ini, apa keputusanmu untuk hari esok?"

        "Tetap diam. Mungkin besok Danisa sudah lupa dan keadaan tenang sendiri.":
            jump ending_bad

        "Aku salah sudah membeku tadi. Catat kejadian ini, minta maaf ke Kenzie besok pagi, dan laporkan ke Pak Joko.":
            jump rute_diam_bangkit

label rute_diam_bangkit:
    $ keberanian += 1
    $ empati += 1
    $ d_document = True

    show rara normal at sprite_tengah
    "Malam itu kamu mengambil buku catatan kecil dan menuliskan semua kejadian dari minggu lalu hingga insiden gambar tadi pagi agar tidak lupa kronologinya."
    rara "(Takut memang wajar, tapi membiarkan sahabatku menderita sendirian itu jauh lebih menakutkan.)"

    scene bg halaman
    with fade

    play music bgm_pagi fadeout 1.0 fadein 1.0 if_changed

    "Keesokan paginya di halaman sekolah, kamu menunggu di dekat gerbang. Tak lama, Kenzie datang berjalan pelan dengan langkah berat."

    $ atur_posisi(rara="duo_kiri", kenzie="duo_kanan")
    show rara sedih at sprite_duo_kiri
    show kenzie kecewa at sprite_duo_kanan
    with dissolve

    rara "Kenzie... tunggu sebentar."
    kenzie "Ada apa, Ra? Aku mau langsung ke kelas sebelum bel."
    show rara kecewa at sprite_duo_kiri
    rara "Aku mau minta maaf. Kemarin aku membeku karena takut, padahal seharusnya aku ada di pihakmu. Kamu pasti kecewa banget sama aku."
    show kenzie murung at sprite_duo_kanan
    kenzie "Jujur, kemarin aku merasa sendirian banget, Ra... Rasanya seluruh kelas menertawakanku."
    show rara normal at sprite_duo_kiri
    rara "Aku ngerti. Hari ini aku nggak mau diam lagi. Aku sudah mencatat kejadian seminggu terakhir. Ayo kita temui Pak Joko di kantor guru sebelum pelajaran mulai."
    show kenzie normal at sprite_duo_kanan
    kenzie "B-beneran kamu mau ikut melapor sama aku?"
    rara "Iya. Kamu nggak sendirian lagi."

    $ d_delay = True
    $ pernah_menenangkan_kenzie = True
    $ kepercayaan_kenzie += 1
    $ d_delegate = True

    scene bg kantor_guru
    with fade

    play music bgm_tegang fadeout 1.0 fadein 1.0

    $ atur_posisi(joko="tiga_kiri", rara="tiga_tengah", kenzie="tiga_kanan")
    show joko berpikir at sprite_tiga_kiri
    show rara normal at sprite_tiga_tengah
    show kenzie normal at sprite_tiga_kanan
    with dissolve

    pak_joko "Terima kasih Rara dan Kenzie sudah berani datang ke sini. Laporan tertulis Rara sangat membantu Bapak memahami bahwa ini bukan kejadian pertama."
    show joko pose_serius at sprite_tiga_kiri
    pak_joko "Bapak akan memanggil Danisa pagi ini juga untuk menindaklanjuti secara tegas."

    scene bg kelas_kelabu
    with fade

    play music bgm_sedih fadeout 1.0 fadein 1.0

    $ atur_posisi(danisa="empat_1", joko="empat_2", rara="empat_3", kenzie="empat_4")
    show danisa buang_muka at sprite_empat_1
    show joko pose_serius at sprite_empat_2
    show rara capek at sprite_empat_3
    show kenzie murung at sprite_empat_4
    with dissolve

    "Setelah dipanggil Pak Joko, ejekan Danisa memang langsung dihentikan. Danisa menyampaikan permintaan maaf singkat kepada Kenzie di ruang guru sebelum kembali ke kelas."
    show danisa buang_muka at sprite_empat_1
    danisa "...Maaf soal gambar kemarin, Kenzie."
    show kenzie normal at sprite_empat_4
    kenzie "Iya... terima kasih, Danisa."
    "Meski perundungan telah berhenti, suasana di antara kalian masih terasa canggung dan berjarak. Kenzie tetap butuh waktu untuk memulihkan rasa amannya, dan Danisa belum sepenuhnya membuka hatinya."

    $ persistent.ending_normal = True
    call screen ringkasan_ending(
        judul_ending="Normal Ending: Langkah yang Sempat Terlambat",
        kategori="ENDING 2 / 4 - NORMAL ENDING",
        warna_judul="#fbbf24",
        pesan_moral="Memperbaiki kesalahan dengan akhirnya berani melapor tetap berhasil menghentikan perundungan. Namun, keterlambatan bertindak saat kejadian berlangsung membuat proses pemulihan kepercayaan berjalan lebih lama.",
        tips_eksplorasi="Petunjuk: Cobalah bertindak langsung saat kejadian di kelas berlangsung—baik lewat jalur Melapor atau Menegur dengan Tenang—untuk membuka Good Ending atau True Ending!"
    )
    jump menu_akhir_ending

# ---------- BAD ENDING ----------
label ending_bad:
    "Kamu menarik selimut dan meyakinkan dirimu sendiri bahwa besok semua akan berlalu dengan sendirinya."

    scene bg lorong
    with fade

    play music bgm_ending_buruk fadeout 1.0 fadein 1.0

    "Hari berganti hari. Karena melihat tak seorang pun berani membela saat gambar Kenzie direbut, ejekan Danisa semakin menjadi-jadi."
    "Suatu hari tempat pensil Kenzie disembunyikan di belakang lemari kelas, dan hari lain tak ada satu pun teman yang mau satu kelompok dengannya."
    "Kamu hanya bisa menunduk setiap kali hal itu terjadi—semakin takut menjadi sasaran berikutnya."

    scene bg kelas_kelabu
    with fade

    $ atur_posisi(joko="duo_kiri", rara="duo_kanan")
    show joko lemas at sprite_duo_kiri
    show rara sedih at sprite_duo_kanan
    with dissolve

    "Seminggu kemudian, bangku di sebelahmu kosong lagi untuk hari ketiga berturut-turut."
    rara "Pak Joko... Kenzie sakit apa? Kok belum masuk juga?"
    show joko kertas at sprite_duo_kiri
    pak_joko "Orang tuanya baru mengirim surat izin pindah sementara sambil menunggu pendampingan psikolog anak. Kenzie ketakutan setiap kali melihat seragam sekolah."
    show joko lemas at sprite_duo_kiri
    pak_joko "Bapak menyesal baru tahu hal ini setelah semuanya terlanjur berat... Kenapa tidak ada yang memberi tahu Bapak sejak awal, Rara?"
    show rara menangis at sprite_duo_kanan
    rara "(Aku tahu semuanya sejak awal... tapi aku memilih diam.)"

    scene cg ending_buruk
    with Dissolve(1.5)

    "Bangku di sebelahmu terasa begitu dingin dan sunyi. Karya masjid dengan matahari terbit itu tak pernah sempat dipajang di papan pameran."
    "Diam di hadapan ketidakadilan bukanlah sikap netral. Ketika saksi mata membisu, pelaku merasa leluasa, dan korban kehilangan satu-satunya harapan."

    $ persistent.ending_bad = True
    call screen ringkasan_ending(
        judul_ending="Bad Ending: Sunyi di Bangku Sebelah",
        kategori="ENDING 1 / 4 - BAD ENDING",
        warna_judul="#f87171",
        pesan_moral="Rasa takut sebagai bystander adalah hal manusiawi, tetapi memilih diam terus-menerus membuat korban merasa sendirian hingga kehilangan rasa amannya di sekolah.",
        tips_eksplorasi="Petunjuk: Kamu bisa mengubah keadaan dengan mengambil tindakan aman—baik menegur dengan tenang, membangkitkan keberanian keesokan hari, atau melapor ke Pak Joko."
    )
    jump menu_akhir_ending

# ==============================================================================
#  CABANG 2: RUTE TEGUR KERAS
# ==============================================================================
label rute_tegur_keras:
    $ keberanian += 1
    $ d_direct = True

    scene bg kelas
    $ atur_posisi(danisa="tiga_kiri", rara="tiga_tengah", kenzie="tiga_kanan")
    show danisa meremehkan at sprite_tiga_kiri
    show rara marah_besar at sprite_tiga_tengah
    show kenzie menangis at sprite_tiga_kanan
    with dissolve

    play music bgm_tegang fadeout 0.6 fadein 0.6 if_changed

    "Darahmu terasa mendidih melihat air mata Kenzie. Kamu berdiri cepat sampai kursimu berdecit keras!"
    rara "Danisa!! Kembalikan gambar Kenzie sekarang juga! Kamu pikir kamu hebat banget bisa merendahkan orang lain?!" with vpunch

    show danisa marah at sprite_tiga_kiri
    danisa "Heh! Jangan teriak-teriak di depanku ya! Memangnya kamu siapa mau mengatur aku?!"
    show rara marah at sprite_tiga_tengah
    rara "Aku temannya! Dan cuma anak iri yang bisanya menertawakan kerja keras teman!"
    show danisa menunjuk at sprite_tiga_kiri
    danisa "Apa kamu bilang?! Sok paling suci! Awas ya, nanti—"
    show kenzie takut at sprite_tiga_kanan
    kenzie "Sudah, Ra... jangan bertengkar... semua orang jadi melihat ke sini... aku takut..."

    "Suasana kelas berubah ricuh. Murid-murid lain berbisik panik melihat kalian berdua saling menatap tajam."

    $ atur_posisi(danisa="empat_1", joko="empat_2", rara="empat_3", kenzie="empat_4")
    show danisa marah at sprite_empat_1
    show joko curiga at sprite_empat_2
    show rara kesal at sprite_empat_3
    show kenzie takut at sprite_empat_4
    with dissolve

    pak_joko "Ada keributan apa ini?! Suara teriakan kalian terdengar sampai ke ujung lorong!"
    show danisa menunjuk at sprite_empat_1
    danisa "Rara yang mulai berteriak membentak saya di depan kelas, Pak!"
    show rara kesal at sprite_empat_3
    rara "Danisa duluan yang merebut dan mengejek gambar Kenzie, Pak!"
    show joko pose_serius at sprite_empat_2
    pak_joko "Cukup! Kalian bertiga, ikut Bapak ke kantor guru sekarang juga."

    scene bg kantor_guru
    with fade

    play music bgm_sedih fadeout 1.2 fadein 1.2

    $ atur_posisi(danisa="empat_1", joko="empat_2", rara="empat_3", kenzie="empat_4")
    show danisa buang_muka at sprite_empat_1
    show joko pose_serius at sprite_empat_2
    show rara kesal at sprite_empat_3
    show kenzie sedih at sprite_empat_4
    with dissolve

    pak_joko "Di sini kita bicara tenang. Bapak tidak akan menyalahkan sebelum mendengar semuanya."
    show joko mengajar at sprite_empat_2
    pak_joko "Rara, Bapak tahu kamu membela Kenzie. Tapi membentak dan membalas dengan sindiran di depan kelas justru membuat masalah berubah menjadi pertengkaran baru."

    menu:
        "Bagaimana sikapmu menanggapi teguran Pak Joko?"

        "Tetap membela diri dengan nada kesal ('Tapi Danisa memang pantas dibentak, Pak!')":
            jump ending_normal_keras

        "Tarik napas, akui nada bicaramu terlalu emosi, lalu jelaskan kronologi secara runtut.":
            jump tegur_keras_introspeksi

label ending_normal_keras:
    show rara marah at sprite_empat_3
    rara "Tapi kalau tidak dibentak, Danisa nggak akan berhenti, Pak! Dia sudah keterlaluan!"
    show danisa sinis at sprite_empat_1
    danisa "Tuh lihat sendiri, Pak! Rara saja nggak bisa kontrol emosinya!"
    show joko pose_serius at sprite_empat_2
    pak_joko "Stop, keduanya. Perbuatan mengejek jelas salah, dan akan Bapak beri catatan pembinaan. Tetapi melawan amarah dengan amarah hanya membuat pelaku menutup telinga."
    show danisa buang_muka at sprite_empat_1
    danisa "...Ya sudah, aku minta maaf, Kenzie."
    show kenzie kecewa at sprite_empat_4
    kenzie "Iya... terima kasih."

    scene bg kelas_kelabu
    with fade

    $ atur_posisi(danisa="tiga_kiri", rara="tiga_tengah", kenzie="tiga_kanan")
    show danisa buang_muka at sprite_tiga_kiri
    show rara capek at sprite_tiga_tengah
    show kenzie murung at sprite_tiga_kanan
    with dissolve

    "Permintaan maaf itu terdengar datar dan terpaksa. Ejekan di kelas memang berhenti karena teguran guru, namun Danisa menjauh dengan rasa kesal dan Kenzie masih merasa canggung."
    "Berani membela teman adalah hal mulia, tetapi cara penyampaian yang penuh amarah membuat orang lain lebih sibuk membela diri daripada menyadari kesalahannya."

    $ persistent.ending_normal = True
    call screen ringkasan_ending(
        judul_ending="Normal Ending: Niat Baik, Cara yang Panas",
        kategori="ENDING 2 / 4 - NORMAL ENDING",
        warna_judul="#fbbf24",
        pesan_moral="Membela korban adalah tindakan benar, tetapi membalas dengan bentakan dan sindiran dapat menggeser fokus masalah menjadi pertengkaran, sehingga pelaku makin menutup diri.",
        tips_eksplorasi="Petunjuk: Coba akui kekhilafan nada bicaramu di ruang guru untuk memperbaiki keadaan, atau pilih jalur Tegur Tenang / Melapor sejak awal!"
    )
    jump menu_akhir_ending

label tegur_keras_introspeksi:
    $ empati += 1
    $ kesadaran_danisa += 1
    $ d_document = True
    $ d_delegate = True

    show rara kecewa at sprite_empat_3
    rara "Maaf, Pak... tadi aku memang terlalu terbawa emosi sampai membentak dan menyindir balik. Niatku cuma ingin menghentikan ejekan yang sudah berlangsung seminggu ini."
    show joko tersenyum at sprite_empat_2
    pak_joko "Nah, mengakui kesalahan diri sendiri seperti itu butuh keberanian besar, Rara. Sekarang Bapak bisa melihat masalah ini dengan jernih."
    show danisa pusing at sprite_empat_1
    "Danisa melirikmu sekilas, tampak terkejut karena kamu tidak terus menyerangnya."
    show joko mengajar at sprite_empat_2
    pak_joko "Danisa, mengejek karya dan kondisi teman selama seminggu hingga ia menangis bukanlah candaan. Bapak ingin kamu belajar menghargai usaha orang lain."
    pak_joko "Mulai besok, kamu Bapak tugaskan membantu Kenzie dan Rara menata papan Pameran Lukisan Kelas. Bukan untuk mempermalukanmu, melainkan agar kamu belajar bekerja sama."
    show danisa buang_muka at sprite_empat_1
    danisa "...Baik, Pak. Aku... minta maaf sudah meremehkan gambarmu tadi, Kenzie."
    show kenzie normal at sprite_empat_4
    kenzie "Iya, Danisa. Tolong bantu kami menata pamerannya dengan baik ya."

    jump rute_pameran_bersama

# ==============================================================================
#  CABANG 3: RUTE TEGUR TENANG & EMPATI
# ==============================================================================
label rute_tegur_tenang:
    $ keberanian += 1
    $ d_direct = True

    scene bg kelas
    $ atur_posisi(danisa="tiga_kiri", rara="tiga_tengah", kenzie="tiga_kanan")
    show danisa meremehkan at sprite_tiga_kiri
    show rara normal at sprite_tiga_tengah
    show kenzie menangis at sprite_tiga_kanan
    with dissolve

    "Kamu menarik napas dalam-dalam, berdiri dari bangkumu, dan melangkah ke tengah dengan suara yang jelas namun tidak berteriak."
    rara "Danisa, tolong kembalikan gambar Kenzie sekarang. Dia mengerjakannya semalaman untuk pameran, dan kamu lihat sendiri dia sedang menangis."
    show danisa angkuh at sprite_tiga_kiri
    danisa "Halah, kenapa jadi kamu yang repot? Aku kan cuma memberi komentar jujur. Memang mataharinya aneh, masa jujur dilarang?"
    show kenzie kecewa at sprite_tiga_kanan
    kenzie "Danisa... aku nggak minta kamu puji gambarku. Aku cuma minta kamu nggak menertawakannya di depan seisi kelas..."

    "Suara Kenzie pelan, tetapi cukup jernih hingga murid-murid lain terdiam. Danisa sempat mendengus, berusaha mempertahankan sikap angkuhnya."
    show danisa senyum_palsu at sprite_tiga_kiri
    danisa "Lagian nanti kalau dipajang juga paling kalah sama punyaku. Ngapain dimasukin ke hati sih?"

    menu:
        "Danisa masih bersikap defensif. Bagaimana kamu meresponsnya?"

        "Jawab tenang namun berprinsip ('Jujur itu berbeda dengan mempermalukan di depan orang banyak.')":
            jump tegur_tenang_empati

        "Balas menyindir ('Setidaknya Kenzie pakai usaha sendiri, bukan cuma pamer cat mahal dari Mama.')":
            jump tegur_tenang_sindir

label tegur_tenang_sindir:
    show rara kesal at sprite_tiga_tengah
    rara "Setidaknya Kenzie menggambar pakai usahanya sendiri, bukan cuma pamer cat air mahal dari Mama!"
    show danisa marah at sprite_tiga_kiri
    danisa "Diam kamu!! Kamu nggak tahu apa-apa soal aku dan Mamaku!" with hpunch
    "Danisa membanting kertas gambar Kenzie ke meja dan langsung bergegas keluar kelas saat bel istirahat berbunyi."
    play sound bel_sekolah

    show kenzie takut at sprite_tiga_kanan
    kenzie "Ra... kenapa tadi kamu bilang soal Mamanya?"
    show rara kecewa at sprite_tiga_tengah
    rara "Aduh... aku kelepasan menyindir dia..."
    "Karena sindiran balik itu mengenai titik sensitif Danisa, suasana menjadi beku. Akhirnya kamu mengajak Kenzie melapor ke Pak Joko agar tidak berlarut-larut."
    $ d_delegate = True
    $ d_delay = True
    $ pernah_menenangkan_kenzie = True
    $ kepercayaan_kenzie += 1

    scene bg kantor_guru
    with fade
    $ atur_posisi(joko="tiga_kiri", rara="tiga_tengah", kenzie="tiga_kanan")
    show joko pose_serius at sprite_tiga_kiri
    show rara kecewa at sprite_tiga_tengah
    show kenzie normal at sprite_tiga_kanan
    with dissolve

    pak_joko "Bapak mengerti niat Rara ingin membela Kenzie, namun membalas dengan menyindir urusan keluarga justru melukai hal lain."
    pak_joko "Bapak akan memanggil Danisa untuk mediasi dan menugaskannya membantu pameran kelas agar hubungan kalian kembali membaik."
    jump rute_pameran_bersama

label tegur_tenang_empati:
    $ empati += 1
    $ kesadaran_danisa += 1

    show rara normal at sprite_tiga_tengah
    rara "Danisa, berpendapat jujur itu memberi saran yang membangun dengan sopan, bukan mengangkatnya tinggi-tinggi supaya ditertawakan seisi kelas."
    show rara sedih at sprite_tiga_tengah
    rara "Kalau kamu yang duduk di bangku Kenzie sekarang, rasanya juga pasti sakit, kan?"
    show danisa pusing at sprite_tiga_kiri
    danisa "..."
    "Senyum angkuh Danisa perlahan menghilang. Tangan yang memegang kertas itu berhenti bergerak. Beberapa saat kemudian, ia meletakkan kembali gambar masjid itu di meja Kenzie tanpa meremukkannya."

    play sound bel_sekolah
    show danisa buang_muka at sprite_tiga_kiri
    danisa "Nih... ambil lagi."
    "Begitu bel istirahat berbunyi, Danisa berjalan cepat keluar kelas sebelum anak-anak lain berkerumun."

    # ---------- Istirahat 1: Dampingi korban terlebih dulu (Delay) ----------
    scene bg lorong
    with fade

    $ d_delay = True
    $ pernah_menenangkan_kenzie = True
    $ kepercayaan_kenzie += 1

    $ atur_posisi(rara="duo_kiri", kenzie="duo_kanan")
    show rara normal at sprite_duo_kiri
    show kenzie kecewa at sprite_duo_kanan
    with dissolve

    "Kamu tidak langsung mengejar Danisa. Kamu memastikan kondisi sahabatmu terlebih dulu di sudut lorong yang tenang."
    rara "Kenzie, kamu nggak apa-apa? Sini kita rapikan lagi sudut kertas gambarmu."
    show kenzie normal at sprite_duo_kanan
    kenzie "Untung cuma terlipat sedikit di pinggir... Makasih banyak ya, Ra. Tadi kamu nggak membentak, tapi suaramu kedengaran kuat banget."
    show rara senang at sprite_duo_kiri
    rara "Aku juga salut sama kamu. Tadi kamu berani bicara sendiri ke Danisa. Itu langkah besar, Kenz!"
    show kenzie senang at sprite_duo_kanan
    kenzie "Hehe... soalnya aku tahu ada kamu di sebelahku."

    # ---------- Istirahat 2: Melihat Danisa menyendiri di taman ----------
    scene bg taman
    with fade

    "Setelah mengantar Kenzie ke kantin bersama teman-teman yang lain, kamu melintas di dekat taman halaman sekolah."
    "Di salah satu bangku di bawah pohon, kamu melihat Danisa duduk sendirian memeluk lutut sambil menatap kosong ke arah papan tugasnya."

    $ atur_posisi(danisa="duo_kiri", rara="duo_kanan")
    show danisa pusing at sprite_duo_kiri
    show rara curiga at sprite_duo_kanan
    with dissolve

    rara "(Itu Danisa... biasanya jam istirahat dia selalu dikerumuni teman-temannya.)"

    menu:
        "Apa yang ingin kamu lakukan saat melihat Danisa duduk sendirian?"

        "Hampiri dengan pelan dan dengarkan apa yang sebenarnya sedang mengganggunya.":
            jump dialog_taman_danisa

        "Biarkan dia sendiri dulu, lalu langsung laporkan kejadian tadi ke Pak Joko agar ditangani guru.":
            $ d_delegate = True
            "Kamu memutuskan tidak memaksa berbicara empat mata sekarang, dan segera berjalan menuju kantor guru untuk meminta bantuan Pak Joko secara resmi."
            jump mediasi_pak_joko_good

label dialog_taman_danisa:
    $ tahu_alasan_danisa = True
    $ empati += 2
    $ kesadaran_danisa += 2

    show rara normal at sprite_duo_kanan
    rara "Danisa... boleh aku duduk di sebelah sini sebentar?"
    show danisa buang_muka at sprite_duo_kiri
    danisa "Ngapain ke sini? Mau lanjut menasihatiku lagi di depan semua orang?"
    show rara sedih at sprite_duo_kanan
    rara "Nggak kok. Aku cuma teringat tadi pagi di lorong... waktu kamu bilang takut Mama marah kalau gambarmu nggak masuk tiga besar. Kamu kelihatan capek banget."
    show danisa pusing at sprite_duo_kiri
    danisa "..."
    "Danisa terdiam cukup lama. Bahunya yang tegang perlahan turun. Untuk pertama kalinya, ia tidak memasang wajah mengejek maupun angkuh."

    danisa "...Kamu merhatiin sampai segitunya?"
    danisa "Di rumah, aku selalu dibanding-bandingkan sama sepupu dan kakakku. Nilai harus paling tinggi, gambar harus menang, barang harus paling bagus. Kalau kalah sedikit saja, Mama langsung kecewa dan mendiamkanku seharian."
    show rara kaget at sprite_duo_kanan
    rara "Danisa..."
    show danisa cemas at sprite_duo_kiri
    danisa "Waktu melihat anak-anak memuji gambar Kenzie yang cuma pakai pensil warna pendek... aku tiba-tiba takut gambarku dianggap biasa saja. Pas aku mengejek dia, rasanya aku kelihatan lebih hebat... cuma sebentar. Setelah itu aku malah merasa jahat banget."
    show rara sedih at sprite_duo_kanan
    rara "Aku ngerti kamu lagi tertekan di rumah. Tapi Kenzie juga punya rasa takut yang sama setiap pagi sebelum masuk gerbang."
    show danisa pusing at sprite_duo_kiri
    danisa "Iya... aku salah besar. Aku nggak tahu gimana cara minta maaf tanpa merasa malu."
    show rara senang at sprite_duo_kanan
    rara "Kita bisa bicara sama Pak Joko sama-sama. Pak Joko nggak cuma menghukum kok, beliau pasti mau membantu mencari jalan keluar—termasuk bicara ke Mamamu kalau kamu butuh."

    # ---------- Mediasi Bijak di Kantor Guru ----------
    scene bg kantor_guru
    with fade

    play music bgm_sedih fadeout 1.0 fadein 1.0 if_changed

    $ d_delegate = True

    $ atur_posisi(danisa="empat_1", joko="empat_2", rara="empat_3", kenzie="empat_4")
    show danisa cemas at sprite_empat_1
    show joko tersenyum at sprite_empat_2
    show rara normal at sprite_empat_3
    show kenzie normal at sprite_empat_4
    with dissolve

    pak_joko "Terima kasih kalian bertiga mau duduk bersama di ruangan Bapak. Kenzie, kamu boleh cerita dulu bagaimana perasaanmu seminggu ini."
    show kenzie sedih at sprite_empat_4
    kenzie "Aku sempat takut berangkat sekolah, Pak... Rasanya setiap hari ada saja yang salah dengan seragam atau gambarku."
    show joko normal at sprite_empat_2
    pak_joko "Terima kasih sudah jujur, Kenzie. Sekarang kamu, Danisa."
    show danisa pusing at sprite_empat_1
    danisa "Aku minta maaf banget, Kenzie... Aku sebenarnya iri melihat kamu menggambar dengan tenang tanpa takut dimarahi orang tua. Tapi itu nggak membenarkan aku menyakitimu. Maaf ya."
    show kenzie kaget at sprite_empat_4
    kenzie "Kamu... juga takut dimarahi di rumah?"
    show joko mengajar at sprite_empat_2
    pak_joko "Mengakui salah dan memahami batas perilaku itu langkah besar, Danisa. Rasa tertekan di rumah tidak boleh dilampiaskan ke teman. Bapak nanti akan bantu bicara baik-baik dengan orang tuamu di pertemuan wali murid."
    # Cek syarat True Ending: harus empati >= 3, kepercayaan_kenzie >= 2, tahu_alasan_danisa
    if tahu_alasan_danisa and empati >= 3 and kepercayaan_kenzie >= 2:
        show kenzie senang at sprite_empat_4
        kenzie "Aku maafkan, Danisa. Tapi janji jangan diulang ke siapa pun lagi, ya."
        show danisa senyum at sprite_empat_1
        danisa "Janji. Mulai hari ini aku mau belajar menjadi teman yang beneran baik."
        jump ending_true
    else:
        show kenzie normal at sprite_empat_4
        kenzie "Aku menghargai permintaan maafmu, Danisa... tapi hatiku masih butuh waktu untuk benar-benar percaya lagi."
        show joko mengajar at sprite_empat_2
        pak_joko "Tidak apa-apa, pemulihan kepercayaan memang bertahap. Untuk dua minggu ke depan, kalian bertiga Bapak tugaskan menyiapkan Pameran Lukisan Madrasah agar belajar bekerja sama dengan tulus."
        show danisa buang_muka at sprite_empat_1
        danisa "...Baik, Pak."
        jump rute_pameran_bersama

label mediasi_pak_joko_good:
    scene bg kantor_guru
    with fade

    $ atur_posisi(danisa="empat_1", joko="empat_2", rara="empat_3", kenzie="empat_4")
    show danisa buang_muka at sprite_empat_1
    show joko pose_serius at sprite_empat_2
    show rara normal at sprite_empat_3
    show kenzie normal at sprite_empat_4
    with dissolve

    pak_joko "Terima kasih Rara sudah melaporkan hal ini setelah memastikan Kenzie aman. Danisa, Bapak ingin kamu belajar menghargai usaha temanmu secara nyata."
    pak_joko "Selama dua minggu ke depan, kamu akan bekerja sama dengan Kenzie dan Rara menyiapkan Pameran Lukisan Madrasah."
    show danisa pusing at sprite_empat_1
    danisa "...Baik, Pak. Maaf ya, Kenzie."
    jump rute_pameran_bersama

# ==============================================================================
#  CABANG 4: RUTE MELAPOR (DISTRACT + DELEGATE)
# ==============================================================================
label rute_lapor:
    $ keberanian += 1
    $ d_distract = True
    $ d_delegate = True

    scene bg kelas
    $ atur_posisi(danisa="tiga_kiri", rara="tiga_tengah", kenzie="tiga_kanan")
    show danisa meremehkan at sprite_tiga_kiri
    show rara normal at sprite_tiga_tengah
    show kenzie menangis at sprite_tiga_kanan
    with dissolve

    "Kamu sadar berteriak di tengah kelas hanya akan membuat Kenzie semakin malu dan menjadi tontonan. Kamu segera berdiri di samping bangku Kenzie."
    rara "Danisa, kembalikan gambar itu. Kita selesaikan urusan ini dengan Pak Joko saja."
    show danisa angkuh at sprite_tiga_kiri
    danisa "Ih, mainnya lapor guru! Tukang ngadu banget sih!"
    "Danisa melempar gambar itu kembali ke meja Kenzie agar tidak tertangkap basah guru. Tanpa meladeni pancingannya, kamu merapikan gambar Kenzie dan menggenggam tangannya."

    scene bg lorong
    with fade

    $ atur_posisi(rara="duo_kiri", kenzie="duo_kanan")
    show rara normal at sprite_duo_kiri
    show kenzie takut at sprite_duo_kanan
    with dissolve

    kenzie "Ra... jangan melapor ke Pak Joko... Nanti anak-anak bilang aku tukang ngadu, terus Danisa makin benci sama aku..."
    show rara senang at sprite_duo_kiri
    rara "Kenzie, dengarkan aku. Tukang ngadu itu kalau orang mencari-cari kesalahan kecil biar temannya dihukum. Melapor ke guru saat kita disakiti berulang-ulang itu namanya menjaga diri agar aman."

    menu:
        "Kapan kamu dan Kenzie menemui Pak Joko?"

        "Langsung menuju kantor guru sekarang selagi ingatan masih segar.":
            $ keberanian += 1
            jump lapor_langsung_kantor

        "Tenangkan Kenzie sejenak di taman agar napasnya teratur, lalu lapor bersama saat istirahat.":
            $ empati += 1
            $ kepercayaan_kenzie += 1
            $ d_delay = True
            $ pernah_menenangkan_kenzie = True
            jump lapor_tenangkan_dulu

label lapor_tenangkan_dulu:
    scene bg taman
    with fade

    $ atur_posisi(rara="duo_kiri", kenzie="duo_kanan")
    show rara senang at sprite_duo_kiri
    show kenzie sedih at sprite_duo_kanan
    with dissolve

    "Kamu mengajak Kenzie duduk sebentar di bangku taman yang sejuk sebelum bel masuk kelas berikutnya berbunyi."
    rara "Tarik napas pelan-pelan dulu, Kenz. Gambarmu juga aman di map ini—mataharinya bagus banget kok, bukan telur dadar!"
    show kenzie senang at sprite_duo_kanan
    kenzie "Hehe... makasih, Ra. Sekarang aku sudah jauh lebih tenang untuk cerita ke Pak Joko."
    jump lapor_langsung_kantor

label lapor_langsung_kantor:
    scene bg kantor_guru
    with fade

    play music bgm_sedih fadeout 1.0 fadein 1.0 if_changed

    $ atur_posisi(joko="tiga_kiri", rara="tiga_tengah", kenzie="tiga_kanan")
    show joko kopi at sprite_tiga_kiri
    show rara normal at sprite_tiga_tengah
    show kenzie normal at sprite_tiga_kanan
    with dissolve

    rara "Assalamu'alaikum, Pak Joko. Boleh kami bicara sebentar?"
    show joko sapa at sprite_tiga_kiri
    pak_joko "Wa'alaikumussalam, Rara, Kenzie. Silakan masuk. Ada masalah apa, Nak?"

    if tahu_bukti_sebelumnya:
        $ d_document = True
        $ keberanian += 1
        show rara normal at sprite_tiga_tengah
        rara "Pak, kami ingin melaporkan perundungan yang dialami Kenzie. Sejak Senin minggu lalu di gerbang dan di kelas saat istirahat, Danisa terus mengejek seragam dan tas Kenzie."
        rara "Tadi pagi Danisa juga merebut kertas gambar Kenzie untuk pameran dan menertawakannya di depan kelas sampai Kenzie menangis."
        show joko jempol at sprite_tiga_kiri
        pak_joko "Penjelasan Rara sangat runtut dan jelas waktunya. Bapak sangat menghargai kalian mencatat dan mengingat kronologinya dengan tepat."
    else:
        show rara normal at sprite_tiga_tengah
        rara "Pak, tadi Danisa merebut dan mengejek gambar Kenzie di depan kelas. Kata Kenzie, ia juga sudah seminggu diejek soal seragam dan tasnya."
        show joko berpikir at sprite_tiga_kiri
        pak_joko "Terima kasih sudah berani bicara, Rara."

    show kenzie takut at sprite_tiga_kanan
    kenzie "Aku takut berangkat sekolah, Pak... Rasanya semua orang ikut menertawakanku."
    show joko kedip at sprite_tiga_kiri
    pak_joko "Perasaanmu sangat berharga, Kenzie. Melapor bukan hal yang salah. Bapak janji akan menangani ini dengan adil dan melindungi kalian."

    # ---------- Pak Joko Menindaklanjuti Danisa ----------
    scene bg kelas
    with fade

    play music bgm_tegang fadeout 1.0 fadein 1.0

    $ atur_posisi(danisa="empat_1", joko="empat_2", rara="empat_3", kenzie="empat_4")
    show danisa gugup at sprite_empat_1
    show joko pose_serius at sprite_empat_2
    show rara normal at sprite_empat_3
    show kenzie normal at sprite_empat_4
    with dissolve

    "Saat kelas sedang sepi di jam istirahat, Pak Joko mengajak Danisa berbicara empat mata bersama kalian agar tidak mempermalukannya di depan seluruh murid."
    pak_joko "Danisa, Bapak mendengar soal kejadian di gerbang dan di kelas pagi ini. Bapak ingin mendengar penjelasanmu."
    show danisa senyum_palsu at sprite_empat_1
    danisa "Aku cuma bercanda kok, Pak... Masa teman bercanda sedikit langsung dilaporin?"
    show joko curiga at sprite_empat_2
    pak_joko "Kalau satu orang tertawa dan yang lain menangis hingga takut berangkat sekolah, itu bukan bercanda. Itu menyakiti."
    show danisa buang_muka at sprite_empat_1
    danisa "..."
    show joko mengajar at sprite_empat_2
    pak_joko "Bayangkan kamu membuat karya semalaman lalu ditertawakan seisi kelas. Bagaimana rasanya?"

    play music bgm_sedih fadeout 1.0 fadein 1.0
    show danisa pusing at sprite_empat_1
    danisa "...Pasti sakit dan malu banget, Pak."
    danisa "Maaf, Kenzie... aku nggak sadar sudah bikin kamu takut datang ke sekolah."
    show joko tersenyum at sprite_empat_2
    pak_joko "Penyesalan harus disertai langkah nyata. Selama dua minggu ke depan, kamu akan menjadi tim bersama Kenzie dan Rara untuk menyiapkan Pameran Lukisan Madrasah."

    jump rute_pameran_bersama

# ==============================================================================
#  ADEGAN BERSAMA: PERSIAPAN PAMERAN LUKISAN DI LAPANGAN (GOOD vs NORMAL)
# ==============================================================================
label rute_pameran_bersama:
    scene bg lapangan
    with fade

    play music bgm_happy fadeout 1.2 fadein 1.2 if_changed

    "Beberapa hari kemudian, di lapangan madrasah yang teduh, persiapan Pameran Lukisan Kelas hampir selesai."
    "Kamu dan Kenzie sedang menata papan pajangan ketika Danisa datang sambil menenteng sebuah kotak cat air."

    $ atur_posisi(danisa="tiga_kiri", rara="tiga_tengah", kenzie="tiga_kanan")
    show danisa buang_muka at sprite_tiga_kiri
    show rara normal at sprite_tiga_tengah
    show kenzie kaget at sprite_tiga_kanan
    with dissolve

    danisa "Hmm... Kenzie, aku bawa cat airku yang warna langitnya masih banyak. Kalau kamu mau pakai untuk mempertegas warna sawah di gambarmu... pakai saja."
    show kenzie senang at sprite_tiga_kanan
    kenzie "Eh... beneran boleh, Danisa?"
    show danisa gugup at sprite_tiga_kiri
    danisa "Iya. Aku... agak canggung sebenarnya, takut kalian masih kesal."

    menu:
        "Bagaimana sikapmu menyambut Danisa saat ia berusaha berubah?"

        "Sambut dengan hangat dan ajak ia ikut menata papan pameran bersama.":
            $ empati += 1
            $ kesadaran_danisa += 1
            show rara senang at sprite_tiga_tengah
            rara "Nggak usah canggung, Danisa! Ayo bantu kami menempelkan label nama di papan sebelah kanan, tulisanmu kan paling rapi."
            show danisa terpesona at sprite_tiga_kiri
            danisa "Beneran? Makasih, Ra... Kenz... pelan-pelan aku belajar jadi teman yang lebih baik, ya."
            show kenzie tertawa at sprite_tiga_kanan
            kenzie "Sama-sama! Nanti kita foto bareng di depan papan pameran!"
            jump ending_good

        "Terima cat airnya seperlunya dengan sikap dingin agar cepat selesai tugas.":
            show rara bosan at sprite_tiga_tengah
            rara "Taruh saja di meja sebelah sana. Yang penting tugas dari Pak Joko cepat beres."
            show danisa buang_muka at sprite_tiga_kiri
            danisa "...Oh, oke."
            jump ending_normal_dingin

label ending_normal_dingin:
    scene bg kelas_kelabu
    with fade

    play music bgm_sedih fadeout 1.0 fadein 1.0

    "Tugas pameran selesai dikumpulkan tepat waktu, dan perundungan dari Danisa tidak pernah terulang kembali."
    "Namun, karena jarak dingin masih dipertahankan, Danisa memilih menjauh ke sudut lain dan hanya bekerja sebatas kewajiban. Luka lama berhenti bertambah, tetapi kehangatan pertemanan belum sepenuhnya tumbuh."

    $ persistent.ending_normal = True
    call screen ringkasan_ending(
        judul_ending="Normal Ending: Damai yang Masih Kaku",
        kategori="ENDING 2 / 4 - NORMAL ENDING",
        warna_judul="#fbbf24",
        pesan_moral="Memberi batasan tegas memang perlu, tetapi tetap memberi ruang bagi teman yang tulus ingin berubah akan membuat lingkungan kelas pulih jauh lebih baik.",
        tips_eksplorasi="Petunjuk: Sambut kerja sama Danisa dengan hangat saat persiapan pameran untuk membuka Good Ending!"
    )
    jump menu_akhir_ending

# ==============================================================================
#  ENDING 3: GOOD ENDING (PAMERAN LUKISAN KELAS -> CG ending_normal)
# ==============================================================================
label ending_good:
    scene cg ending_normal
    with Dissolve(1.5)

    play music bgm_ending_baik fadeout 1.5 fadein 1.5 if_changed

    "Hari Pameran Lukisan Madrasah pun tiba! Suasana kelas dipenuhi warna-warni gambar karya siswa yang digantung rapi."
    "Lukisan masjid di tengah sawah karya Kenzie terpajang dengan bangga di barisan utama—lengkap dengan matahari terbitnya yang cerah."
    "Pak Joko mengacungkan jempol dari belakang dengan senyum bangga, sementara kamu, Kenzie, dan Danisa bersorak bersama melihat hasil kerja keras tim kalian."
    "Dengan keberanian melapor atau menegur secara bijak serta bimbingan guru yang adil, korban terlindungi dan pelaku mendapat kesempatan nyata untuk belajar menghargai sesama."

    $ persistent.ending_good = True
    call screen ringkasan_ending(
        judul_ending="Good Ending: Pameran Lukisan Kelas",
        kategori="ENDING 3 / 4 - GOOD ENDING",
        warna_judul="#38bdf8",
        pesan_moral="Melapor kepada guru terpercaya (Delegate) bukan berarti mengadu, melainkan cara aman untuk melindungi teman dan memulihkan lingkungan belajar bersama.",
        tips_eksplorasi="Petunjuk: Masih ada sisi hati terdalam Danisa yang belum terungkap. Cobalah jalur Tegur Tenang di kelas dan temui Danisa di taman saat istirahat untuk membuka True Ending!"
    )
    jump menu_akhir_ending

# ==============================================================================
#  ENDING 4: TRUE ENDING (SAHABAT DI TAMAN -> CG ending_baik)
# ==============================================================================
label ending_true:
    scene bg taman
    with fade

    play music bgm_ending_baik fadeout 1.5 fadein 1.5 if_changed

    $ atur_posisi(danisa="tiga_kiri", rara="tiga_tengah", kenzie="tiga_kanan")
    show danisa senyum at sprite_tiga_kiri
    show rara senang at sprite_tiga_tengah
    show kenzie senang at sprite_tiga_kanan
    with dissolve

    "Sepulang sekolah, kalian bertiga duduk santai di bangku taman madrasah. Cahaya matahari sore menyinari daun-daun dengan lembut."
    show danisa terpesona at sprite_tiga_kiri
    danisa "Kenzie... kalau dilihat-lihat lagi, lukisan masjidmu ini warnanya beneran hangat. Aku salah bilang mataharinya kayak telur dadar."
    show kenzie tertawa at sprite_tiga_kanan
    kenzie "Hehe, tapi kalau dilihat dari jauh... bulat oranyenya memang sedikit mirip telur dadar sih."
    show rara tertawa at sprite_tiga_tengah
    rara "Hahaha! Nah, kalau yang ini aku nggak bisa membela lagi, Kenz!"
    show danisa senyum at sprite_tiga_kiri
    danisa "Hahaha! Kapan-kapan ajari aku mencampur warna langit kayak begitu ya, Kenz."

    scene cg ending_baik
    with Dissolve(1.5)

    "Di bangku taman itu, tiga sahabat tersenyum lebar memandangi kertas gambar masjid yang pernah hampir rusak."
    "Rara berani menegur dengan lembut, Kenzie berani menyuarakan batasnya, Pak Joko hadir memberi bimbingan yang adil, dan Danisa pun berani menurunkan egonya untuk berubah."
    "Keberanian yang dipadukan dengan empati mampu menyembuhkan luka korban sekaligus memutus beban pelaku—itulah makna sejati menjadi seorang Upstander."

    $ persistent.ending_true = True
    call screen ringkasan_ending(
        judul_ending="True Ending: Matahari di Balik Awan",
        kategori="ENDING 4 / 4 - TRUE ENDING",
        warna_judul="#4ade80",
        pesan_moral="Kita harus tegas menolak perbuatan perundungan, namun tetap peduli pada hati manusia di baliknya. Keberanian yang lembut mampu mengubah lawan menjadi sahabat.",
        tips_eksplorasi="Selamat! Kamu telah mencapai True Ending terbaik! Jangan lupa cek Pojok Edukasi atau ikuti Kuis Refleksi."
    )
    jump menu_akhir_ending

# ==============================================================================
#  MENU PENUTUP SETELAH RINGKASAN ENDING
# ==============================================================================
label menu_akhir_ending:
    menu:
        "Cerita selesai! Apa langkahmu selanjutnya?"

        "Ikuti Kuis Refleksi Singkat (4 Soal bersama Pak Joko).":
            jump kuis_refleksi

        "Ulang dari kejadian di kelas (Babak 3) untuk mencoba jalur lain.":
            jump muat_checkpoint_kelas

        "Mainkan ulang cerita dari paling awal (Babak 1).":
            jump start

        "Kembali ke Menu Utama.":
            stop music fadeout 2.0
            return
