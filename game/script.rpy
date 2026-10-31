# Setting karakter
define rara = Character("Rara", color="#8d16a1")
define kenzie = Character("Kenzie", color="#4b261b")
define darisa = Character("Darisa", color="#FFB7B7")
define pak_joko = Character("Pak joko", color="#10c747")

# Background sekolah MI
image bg lorong = "background/lorong_kelas.png"
image bg kelas = "background/ruang_kelas.png"
image bg halaman = "background/halaman_sekolah.png"
image bg lapangan = "background/lapangan_sekolah.png"
image bg jalan = "background/jalan_perkampungan.png"
image bg Rumah = "background/rumah_depan.png"
image bg taman = "background/taman.png" 
image bg kantor guru = "background/kantor_guru.png"

# Sprite karakter rara
image rara normal = "images/characters/rara/rara_netral.png"
image rara sedih = "images/characters/rara/rara_sedih.png"
image rara bosan = "images/characters/rara/rara_bosan.png"
image rara kaget = "images/characters/rara/rara_kaget.png"
image rara kecewa = "images/characters/rara/rara_kecewa.png"
image rara curiga = "images/characters/rara/rara_curiga.png"
image rara takut = "images/characters/rara/rara_takut.png"
image rara marah besar = "images/characters/rara/rara_sangat_marah.png"
image rara senang = "images/characters/rara/rara_senang.png"
image rara panik = "images/characters/rara/rara_panik.png"
image rara kesal = "images/characters/rara/rara_kesal.png"
image rara cape = "images/characters/rara/rara_capek.png"
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
image kenzie marah besar = "images/characters/Kenzie/k_sangat_marah.png"
image kenzie senang = "images/characters/Kenzie/k_senang.png"
image kenzie panik = "images/characters/Kenzie/k_panik.png"
image kenzie kesal = "images/characters/Kenzie/k_kesal.png"
image kenzie tidur = "images/characters/Kenzie/k_tidur.png"
image kenzie menangis = "images/characters/Kenzie/k_menangis.png"

# sprite karakter darisa

image danisa normal = "images/characters/Danisa/Danisa_netral.png"
image danisa senyum = "images/characters/Danisa/Danisa_senyum.png"
image danisa mengejek = "images/characters/Danisa/Danisa_mengejek.png"
image danisa marah = "images/characters/Danisa/Danisa_marah.png"
image danisa bosan = "images/characters/Danisa/Danisa_bosan.png"
image danisa angkuh = "images/characters/Danisa/Danisa_angkuh.png"
image danisa buang muka = "images/characters/Danisa/Danisa_buang_muka.png"
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
image danisa senyum palsu = "images/characters/Danisa/Danisa_senyum_palsu.png"
image danisa jahil = "images/characters/Danisa/Danisa_jahil.png"
image danisa curiga = "images/characters/Danisa/Danisa_curiga.png"

# sprite karakter pak joko

image pak joko normal = "images/characters/Pak_joko/j_netral.png"
image pak joko sapa = "images/characters/Pak_joko/j_sapa.png"
image pak joko marah = "images/characters/Pak_joko/j_marah.png"
image pak joko tersenyum = "images/characters/Pak_joko/j_tersenyum.png"
image pak joko berpikir  = "images/characters/Pak_joko/j_berpikir.png"
image pak joko curiga = "images/characters/Pak_joko/j_curiga.png"
image pak joko mengedip tersenyum = "images/characters/Pak_joko/j_kedip.png"
image pak joko jempol = "images/characters/Pak_joko/j_jempol.png"
image pak joko pose serius = "images/characters/Pak_joko/j_pose_dagu.png"
image pak joko kaget = "images/characters/Pak_joko/j_kaget.png"
image pak joko mengajar = "images/characters/Pak_joko/j_mengajar.png"

#transform

# Variabel
transform sprite_kiri:
    fit "contain"
    xysize (300, 380)
    xalign 0.2
    yalign 1.0
    yoffset -gui.textbox_height

transform sprite_tengah:
    fit "contain"
    xysize (300, 380)
    xalign 0.5
    yalign 1.0
    yoffset -gui.textbox_height

transform sprite_kanan:
    fit "contain"
    xysize (300, 380)
    xalign 0.8
    yalign 1.0
    yoffset -gui.textbox_height

# Variabel
default pilihan = 0

label start:
    scene bg kelas
    with fade

    show rara normal at sprite_kiri
    show danisa normal at sprite_tengah
    show kenzie normal at sprite_kanan

    kenzie "Rara, ayo masuk kelas. Hari ini kita belajar bareng lagi."
    rara "Ayo, Kenzie. Aku semangat banget hari ini."

    show danisa mengejek at sprite_tengah
    darisa "Eh, lihat tuh! Kamu datang lagi dengan baju yang sama. Emang nggak malu?"
    show rara kaget at sprite_kiri
    rara "Ah, itu... aku nggak bermaksud apa-apa."
    show kenzie sedih at sprite_kanan
    kenzie "Rara... dia bilang seperti itu terus."
    show danisa sinis at sprite_tengah
    darisa "Hahaha, kalian semua terlalu peka. Jangan dibuat drama. Aku cuma bercanda, kok."
    show rara takut at sprite_kiri
    rara "Aku nggak nyaman dengarnya..."
    show kenzie menangis at sprite_kanan
    kenzie "Aku nggak kuat kalau terus dibully seperti ini..."

    menu:
        "Diam saja dan tidak ikut campur.":
            $ pilihan = 1
            jump ending_diam

        "Menegur Darisa dengan tegas.":
            $ pilihan = 2
            jump rute_tegur

        "Melapor ke Pak Joko.":
            $ pilihan = 3
            jump rute_lapor

label ending_diam:
    scene bg kelas
    with fade

    show rara cape at sprite_kiri
    show danisa mengejek at sprite_tengah
    show kenzie menangis at sprite_kanan

    rara "Aku takut... aku nggak berani berkata apa-apa."
    darisa "Tuh, kan. Nggak ada yang berani melawanku."
    kenzie "Aku ingin diberi perlindungan, bukan tinggal diam..."
    show rara kecewa at sprite_kiri
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

    show rara normal at sprite_kiri
    show danisa angkuh at sprite_tengah
    show kenzie sedih at sprite_kanan

    menu:
        "Bicara keras dan tegas.":
            jump tegur_keras

        "Bicara baik-baik dan sopan.":
            jump tegur_baik

label tegur_keras:
    show rara marah at sprite_kiri
    rara "Darisa! Cukup! Jangan terus menghina Kenzie seperti itu. Kita semua sama di sekolah ini!"
    show danisa meremehkan at sprite_tengah
    darisa "Ah, orang sepertimu memang gampang tersinggung. Ini cuma bercanda, kenapa dibuat heboh?"
    show kenzie takut at sprite_kanan
    kenzie "Aku takut... aku nggak tahu harus bilang apa."
    show rara kesal at sprite_kiri
    rara "Bercanda yang menyakitkan tetap salah. Kamu nggak boleh mengganggu teman seperti ini."
    jump masuk_pak_joko

label tegur_baik:
    show rara normal at sprite_kiri
    rara "Darisa, aku tahu kamu mungkin nggak sadar, tapi kata-katamu menyakitkan. Tolong berhenti mengganggu Kenzie."
    show danisa angkuh at sprite_tengah
    darisa "Aku nggak menyalahkan siapa pun. Kalau kalian merasa sakit, berarti kalian terlalu sensitif."
    show kenzie sedih at sprite_kanan
    kenzie "Aku ingin dihormati, bukan ditertawakan."
    show rara sedih at sprite_kiri
    rara "Aku hanya ingin semua teman merasa aman dan dihargai."
    jump masuk_pak_joko

label masuk_pak_joko:
    scene bg kelas
    with dissolve

    show pak joko curiga at sprite_tengah
    show rara normal at sprite_kiri
    show kenzie normal at sprite_kanan

    pak_joko "Ada apa ini? Kenapa suasana kelas jadi ribut begitu?"
    show danisa cemas at sprite_tengah
    darisa "Eh, Pak... aku nggak bermaksud mengganggu. Aku cuma bercanda, itu tidak penting."
    show rara normal at sprite_kiri
    rara "Pak Joko, Darisa terus merundung Kenzie. Saya merasa tidak adil kalau dibiarkan begitu."
    show kenzie sedih at sprite_kanan
    kenzie "Aku merasa takut dan sedih, Pak."
    show pak joko marah at sprite_tengah
    pak_joko "Tidak ada yang boleh merendahkan teman di kelas ini. Saya akan menindaklanjuti. Ikut saya ke kantor guru."

    scene bg kantor guru
    with fade

    show pak joko normal at sprite_tengah
    show rara normal at sprite_kiri
    show kenzie normal at sprite_kanan
    show danisa normal at offscreenleft

    pak_joko "Baik. Saya akan mendengarkan semua pihak. Yang penting, kita harus menyelesaikan masalah ini dengan jujur dan adil."
    rara "Terima kasih, Pak. Saya khawatir kalau tidak segera ditangani, situasinya akan makin buruk."
    kenzie "Aku senang ada yang peduli dan mau mendengar aku."
    show danisa cemas at offscreenleft
    darisa "Aku... aku nggak menyadari hal itu sangat menyakitkan. Aku minta maaf, Kenzie."
    show pak joko tersenyum at sprite_tengah
    pak_joko "Kalian semua harus belajar menghormati satu sama lain. Kalau ada masalah, jangan dibiarkan sendiri. Laporkan dan selesaikan dengan baik."

    scene bg kantor guru
    with dissolve

    "True Ending: Kebenaran terungkap dan tindakan bullying dihentikan."
    "Rara berani menegur, Pak Joko hadir untuk menyelesaikan masalah, dan Kenzie akhirnya merasa aman kembali."
    "Kamu memilih tindakan yang benar: peduli, berani, dan menghormati sesama."
    return

label rute_lapor:
    scene bg kelas
    with fade

    show rara normal at sprite_kiri
    show danisa normal at sprite_tengah
    show kenzie menangis at sprite_kanan

    rara "Pak Joko! Saya ingin melapor. Darisa terus merundung Kenzie di kelas."
    show pak joko curiga at sprite_tengah
    pak_joko "Saya dengar, Rara. Ayo, saya ikut melihat dan mendengarkan semuanya."
    show danisa cemas at sprite_tengah
    darisa "Pak, aku nggak bermaksud buruk. Hanya bercanda, ya."
    show pak joko marah at sprite_tengah
    pak_joko "Bercanda yang menyakiti teman tetap salah. Saya tidak akan membiarkan hal seperti ini terus berlanjut."
    show kenzie sedih at sprite_kanan
    kenzie "Aku merasa lega ada yang mau mendengar keluhanku."

    scene bg kantor_guru
    with fade

    show pak joko normal at sprite_tengah
    show rara normal at sprite_kiri
    show kenzie normal at sprite_kanan
    show danisa normal at offscreenleft

    pak_joko "Dari yang saya dengar, perilaku kalian berdua sudah melanggar nilai sopan santun di sekolah."
    rara "Saya hanya ingin semua teman merasa aman dan nyaman belajar, Pak."
    darisa "Aku benar-benar minta maaf. Aku tidak tahu tindakanku menimbulkan luka seperti ini."
    kenzie "Terima kasih, Rara. Kamu berani membantu aku dan menyampaikan kebenaran."
    show pak joko tersenyum at sprite_tengah
    pak_joko "Kalian semua harus menebus kesalahan dengan memperbaiki sikap dan tidak mengulanginya lagi. Kita semua harus saling menjaga kedamaian."

    scene bg kantor guru
    with dissolve

    "True Ending: Laporan diterima dan masalah diselesaikan dengan bijaksana."
    "Rara tidak tinggal diam, Pak Joko menegur tindakan bullying secara adil, dan Kenzie merasa aman kembali."
    "Kamu memilih menolong dengan cara yang benar dan bertanggung jawab."
    return
