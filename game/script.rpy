# Setting karakter
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
                if slot is not None:
                    attrs = renpy.get_attributes(tag)
                    nama_dengan_atribut = tag if not attrs else tag + " " + " ".join(attrs)
                    renpy.show(nama_dengan_atribut, at_list=[slot, talk_bounce])
            return None
        return callback

define rara = Character("Rara", color="#8d16a1", callback=loncat_bicara("rara"))
define kenzie = Character("Kenzie", color="#b9d5ff", callback=loncat_bicara("kenzie"))
define danisa = Character("Danisa", color="#FFB7B7", callback=loncat_bicara("danisa"))
define pak_joko = Character("Pak Joko", color="#7fd99a", callback=loncat_bicara("joko"))

# Background sekolah MI
image bg lorong = "images/background/lorong_kelas.png"
image bg kelas = "images/background/ruang_kelas.png"
image bg halaman = "images/background/halaman_sekolah.png"
image bg lapangan = "images/background/lapangan_sekolah.png"
image bg jalan = "images/background/jalan_perkampungan.png"
image bg rumah = "images/background/halaman_rumah.png"
image bg taman = "images/background/taman.png"
image bg kantor_guru = "images/background/kantor_guru.png"

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

label start:
    scene bg kelas
    with fade

    show danisa normal at sprite_kiri
    show rara normal at sprite_kanan_dalam
    show kenzie normal at sprite_kanan

    # [DIPERPANJANG]
    danisa "Rara, ayo masuk kelas. Hari ini kita belajar bareng lagi."
    rara "Ayo, Kenzie. Aku semangat banget hari ini, dan aku ingin belajar dengan tenang."
    show danisa mengejek at sprite_kiri
    danisa "Lihat, kamu datang lagi dengan baju yang sama. Emang nggak malu?"
    show rara kaget at sprite_kanan_dalam
    rara "Ah, itu... aku nggak bermaksud apa-apa. Aku cuma ingin ikut belajar seperti teman-teman lain."
    show kenzie sedih at sprite_kanan
    kenzie "Rara... dia bilang seperti itu terus. Aku merasa takut, tapi aku juga nggak mau bikin ribut."
    show danisa sinis at sprite_kiri
    danisa "Hahaha, kalian semua terlalu peka. Itu cuma candaan. Jangan dibuat drama, ya."
    show rara takut at sprite_kanan_dalam
    rara "Aku nggak nyaman dengarnya... kata-katanya selalu menyakitkan."
    show kenzie menangis at sprite_kanan
    kenzie "Aku nggak kuat kalau terus dibully seperti ini. Aku ingin ada yang membela aku."

    menu:
        "Diam saja dan tidak ikut campur.":
            $ pilihan = 1
            jump ending_diam

        "Menegur Danisa dengan tegas.":
            $ pilihan = 2
            jump rute_tegur

        "Melapor ke Pak Joko.":
            $ pilihan = 3
            jump rute_lapor

label ending_diam:
    scene bg kelas
    with fade

    show rara capek at sprite_kanan_dalam
    show danisa mengejek at sprite_kiri
    show kenzie menangis at sprite_kanan

    # [DIPERPANJANG]
    rara "Aku takut... aku nggak berani berkata apa-apa. Aku takut kalau aku ikut bicara, semuanya jadi lebih buruk."
    danisa "Tuh, kan. Nggak ada yang berani melawanku. Aku masih bisa lakukan ini terus."
    kenzie "Aku ingin diberi perlindungan, bukan tinggal diam... Aku sedih, dan aku merasa sendirian."
    show rara kecewa at sprite_kanan_dalam
    rara "Aku menyesal. Aku memilih diam, padahal seharusnya aku membantu."

    scene bg halaman
    with dissolve

    "Bad Ending: Penyesalan karena menjadi bystander."
    "Karena kamu memilih diam, tindakan merundung itu terus berlanjut dan Kenzie tetap terluka."
    "Kamu sadar bahwa tidak ikut campur juga berarti membiarkan ketidakadilan terjadi."
    return

label rute_tegur:
    scene bg kelas
    with fade

    show danisa angkuh at sprite_kiri
    show rara normal at sprite_kanan_dalam
    show kenzie sedih at sprite_kanan

    # [DIPERPANJANG]
    menu:
        "Bicara keras dan tegas.":
            jump tegur_keras

        "Bicara baik-baik dan sopan.":
            jump tegur_baik

label tegur_keras:
    show rara marah at sprite_kanan_dalam
    rara "Danisa! Cukup! Jangan terus menghina Kenzie seperti itu. Kita semua sama di sekolah ini!"
    show danisa meremehkan at sprite_kiri
    danisa "Ah, orang sepertimu memang gampang tersinggung. Ini cuma bercanda, kenapa dibuat heboh?"
    show kenzie takut at sprite_kanan
    kenzie "Aku takut... aku nggak tahu harus bilang apa."
    show rara kesal at sprite_kanan_dalam
    rara "Bercanda yang menyakitkan tetap salah. Kamu nggak boleh mengganggu teman seperti ini."
    jump masuk_pak_joko

label tegur_baik:
    show rara normal at sprite_kanan_dalam
    rara "Danisa, aku tahu kamu mungkin nggak sadar, tapi kata-katamu menyakitkan. Tolong berhenti mengganggu Kenzie."
    show danisa angkuh at sprite_kiri
    danisa "Aku nggak menyalahkan siapa pun. Kalau kalian merasa sakit, berarti kalian terlalu sensitif."
    show kenzie sedih at sprite_kanan
    kenzie "Aku ingin dihormati, bukan ditertawakan."
    show rara sedih at sprite_kanan_dalam
    rara "Aku hanya ingin semua teman merasa aman dan dihargai."
    jump masuk_pak_joko

label masuk_pak_joko:
    scene bg kelas
    with fade

    show joko curiga at sprite_tengah
    show rara normal at sprite_kanan_dalam
    show kenzie normal at sprite_kanan
    show danisa cemas at sprite_kiri

    # [DIPERPANJANG]
    pak_joko "Ada apa ini? Kenapa suasana kelas jadi ribut begitu?"
    danisa "Eh, Pak... aku nggak bermaksud mengganggu. Aku cuma bercanda, itu tidak penting."
    rara "Pak Joko, Danisa terus merundung Kenzie. Saya merasa tidak adil kalau dibiarkan begitu."
    kenzie "Aku merasa takut dan sedih, Pak. Aku ingin dibela dan didengar."
    show joko marah at sprite_tengah
    pak_joko "Tidak ada yang boleh merendahkan teman di kelas ini. Saya akan menindaklanjuti. Ikut saya ke kantor guru."

    scene bg kantor_guru
    with fade

    show joko normal at sprite_tengah
    show rara normal at sprite_kanan_dalam
    show kenzie normal at sprite_kanan
    show danisa normal at sprite_kiri

    # [DIPERPANJANG]
    pak_joko "Baik. Saya akan mendengarkan semua pihak. Yang penting, kita harus menyelesaikan masalah ini dengan jujur dan adil."
    rara "Terima kasih, Pak. Saya khawatir kalau tidak segera ditangani, situasinya akan makin buruk."
    kenzie "Aku senang ada yang peduli dan mau mendengar aku."
    show danisa cemas at sprite_kiri
    danisa "Aku... aku nggak menyadari hal itu sangat menyakitkan. Aku minta maaf, Kenzie."
    show joko tersenyum at sprite_tengah
    pak_joko "Kalian semua harus belajar menghormati satu sama lain. Kalau ada masalah, jangan dibiarkan sendiri. Laporkan dan selesaikan dengan baik."

    scene bg kantor_guru
    with dissolve

    "True Ending: Kebenaran terungkap dan tindakan bullying dihentikan."
    "Rara berani menegur, Pak Joko hadir untuk menyelesaikan masalah, dan Kenzie akhirnya merasa aman kembali."
    "Kamu memilih tindakan yang benar: peduli, berani, dan menghormati sesama."
    return

label rute_lapor:
    scene bg kelas
    with fade

    show danisa normal at sprite_kiri
    show rara normal at sprite_kanan_dalam
    show kenzie menangis at sprite_kanan

    # [DIPERPANJANG]
    rara "Pak Joko! Saya ingin melapor. Danisa terus merundung Kenzie di kelas, dan aku nggak mau hal itu terus terjadi."
    show joko curiga at sprite_tengah
    pak_joko "Saya dengar, Rara. Ayo, saya ikut melihat dan mendengarkan semuanya."
    show danisa cemas at sprite_kiri
    danisa "Pak, aku nggak bermaksud buruk. Hanya bercanda, ya."
    show joko marah at sprite_tengah
    pak_joko "Bercanda yang menyakiti teman tetap salah. Saya tidak akan membiarkan hal seperti ini terus berlanjut."
    show kenzie sedih at sprite_kanan
    kenzie "Aku merasa lega ada yang mau mendengar keluhanku."

    scene bg kantor_guru
    with fade

    show joko normal at sprite_tengah
    show rara normal at sprite_kanan_dalam
    show kenzie normal at sprite_kanan
    show danisa normal at sprite_kiri

    # [DIPERPANJANG]
    pak_joko "Dari yang saya dengar, perilaku kalian berdua sudah melanggar nilai sopan santun di sekolah."
    rara "Saya hanya ingin semua teman merasa aman dan nyaman belajar, Pak."
    danisa "Aku benar-benar minta maaf. Aku tidak tahu tindakanku menimbulkan luka seperti ini."
    kenzie "Terima kasih, Rara. Kamu berani membantu aku dan menyampaikan kebenaran."
    show joko tersenyum at sprite_tengah
    pak_joko "Kalian semua harus menebus kesalahan dengan memperbaiki sikap dan tidak mengulanginya lagi. Kita semua harus saling menjaga kedamaian."

    scene bg kantor_guru
    with dissolve

    "True Ending: Laporan diterima dan masalah diselesaikan dengan bijaksana."
    "Rara tidak tinggal diam, Pak Joko menegur tindakan bullying secara adil, dan Kenzie merasa aman kembali."
    "Kamu memilih menolong dengan cara yang benar dan bertanggung jawab."
    return
