## =============================================================================
##  FITUR EKSTRA PKM: POJOK EDUKASI, GALERI ENDING, RINGKASAN, & KUIS REFLEKSI
## =============================================================================

default persistent.ending_bad = False
default persistent.ending_normal = False
default persistent.ending_good = False
default persistent.ending_true = False
default persistent.quiz_tertinggi = 0
default persistent.quiz_sudah = False

## -----------------------------------------------------------------------------
##  1. LAYAR POJOK EDUKASI ANTI-PERUNDUNGAN
## -----------------------------------------------------------------------------
screen pojok_edukasi():

    tag menu
    default tab_edukasi = "konsep"

    use game_menu(_("Pojok Edukasi"), scroll="viewport", spacing=20):

        vbox:
            spacing 24
            xfill True

            hbox:
                spacing 16
                box_wrap True

                textbutton _("1. Mengenal Perundungan"):
                    action SetScreenVariable("tab_edukasi", "konsep")
                    selected (tab_edukasi == "konsep")
                    padding (22, 12)
                    idle_background Solid("#1e293bcc")
                    hover_background Solid("#0369a1e6")
                    selected_idle_background Solid("#0284c7e6")
                    selected_hover_background Solid("#0284c7ff")

                textbutton _("2. Strategi 5D (Upstander)"):
                    action SetScreenVariable("tab_edukasi", "5d")
                    selected (tab_edukasi == "5d")
                    padding (22, 12)
                    idle_background Solid("#1e293bcc")
                    hover_background Solid("#0369a1e6")
                    selected_idle_background Solid("#0284c7e6")
                    selected_hover_background Solid("#0284c7ff")

                textbutton _("3. Kanal Bantuan"):
                    action SetScreenVariable("tab_edukasi", "bantuan")
                    selected (tab_edukasi == "bantuan")
                    padding (22, 12)
                    idle_background Solid("#1e293bcc")
                    hover_background Solid("#0369a1e6")
                    selected_idle_background Solid("#0284c7e6")
                    selected_hover_background Solid("#0284c7ff")

            if tab_edukasi == "konsep":

                frame:
                    background Solid("#0f172ad9")
                    padding (30, 24)
                    xfill True

                    vbox:
                        spacing 12

                        text _("Apa Itu Perundungan (Bullying)?"):
                            color "#7dd3fc"
                            size 34
                            bold True

                        text _("Perundungan bukan sekadar 'bercanda'. Sebuah tindakan disebut perundungan apabila memiliki tiga ciri utama: (1) dilakukan secara {b}sengaja{/b} untuk menyakiti atau merendahkan, (2) terjadi secara {b}berulang{/b}, dan (3) terdapat {b}ketimpangan kuasa{/b} (fisik, status sosial, atau jumlah pendukung) sehingga korban merasa tidak berdaya."):
                            color "#e2e8f0"
                            size 26

                frame:
                    background Solid("#0f172ad9")
                    padding (30, 24)
                    xfill True

                    vbox:
                        spacing 12

                        text _("Bentuk-Bentuk Perundungan di Sekolah"):
                            color "#7dd3fc"
                            size 34
                            bold True

                        text _("{b}- Verbal:{/b} mengejek nama orang tua, menghina kondisi barang/seragam, menertawakan karya atau penampilan teman.\n{b}- Sosial / Relasional:{/b} mengucilkan, menyebar gosip, mengajak seisi kelas menertawakan satu anak.\n{b}- Fisik:{/b} mendorong, memukul, merampas, atau merusak barang milik teman.\n{b}- Siber (Online):{/b} mengirim pesan ejekan atau menyebar foto memalukan lewat grup chat/media sosial."):
                            color "#e2e8f0"
                            size 26

                frame:
                    background Solid("#0f172ad9")
                    padding (30, 24)
                    xfill True

                    vbox:
                        spacing 12

                        text _("Bystander vs Upstander"):
                            color "#7dd3fc"
                            size 34
                            bold True

                        text _("{b}Bystander{/b} adalah saksi mata yang hanya menonton atau diam saat perundungan terjadi. Sikap diam sering membuat pelaku merasa aman dan korban merasa sendirian.\n\n{b}Upstander{/b} adalah saksi mata yang berani mengambil langkah aman untuk menghentikan perundungan atau mendukung korban—baik secara langsung maupun dengan meminta bantuan orang dewasa terpercaya."):
                            color "#e2e8f0"
                            size 26

            elif tab_edukasi == "5d":

                frame:
                    background Solid("#0f172ad9")
                    padding (30, 24)
                    xfill True

                    vbox:
                        spacing 14

                        text _("Metode Intervensi 5D untuk Menjadi Upstander"):
                            color "#7dd3fc"
                            size 34
                            bold True

                        text _("Kamu tidak harus membalas dengan bentakan atau perkelahian untuk menolong teman. Pilih cara yang aman sesuai situasi:"):
                            color "#cbd5e1"
                            size 25

                        text _("{b}1. Direct (Tegur Langsung dengan Tenang):{/b} Menyampaikan dengan tegas namun tidak menghina bahwa perilaku mengejek itu menyakiti dan harus dihentikan.\n\n{b}2. Distract (Alihkan Perhatian):{/b} Memutus momen perundungan dengan mengalihkan topik atau mengajak korban menjauh dari kerumunan.\n\n{b}3. Delegate (Laporkan / Libatkan Orang Dewasa):{/b} Meminta bantuan wali kelas, guru BK, atau orang tua. Melapor demi keamanan bukanlah 'mengadu'!\n\n{b}4. Delay (Dampingi Setelah Kejadian):{/b} Menemani dan menenangkan korban setelah insiden agar ia tahu bahwa ia tidak sendirian.\n\n{b}5. Document (Catat Kronologi):{/b} Mengingat atau mencatat waktu, tempat, dan kejadian berulang sebagai bukti jelas saat melapor ke guru."):
                            color "#e2e8f0"
                            size 26

            elif tab_edukasi == "bantuan":

                frame:
                    background Solid("#0f172ad9")
                    padding (30, 24)
                    xfill True

                    vbox:
                        spacing 12

                        text _("Ke Mana Harus Melapor Jika Terjadi Perundungan?"):
                            color "#7dd3fc"
                            size 34
                            bold True

                        text _("{b}1. Lingkungan Sekolah:{/b} Wali kelas, Guru Bimbingan Konseling (BK), atau Kepala Sekolah/Madrasah.\n{b}2. Lingkungan Rumah:{/b} Orang tua, wali, atau kakak yang dipercaya.\n{b}3. Layanan Resmi Negara:{/b}\n- {b}SAPA 129 (KemenPPPA):{/b} Telepon {b}129{/b} atau WhatsApp {b}08111-129-129{/b}\n- {b}KPAI (Komisi Perlindungan Anak Indonesia):{/b} Portal pengaduan resmi kpai.go.id"):
                            color "#e2e8f0"
                            size 26

                frame:
                    background Solid("#0f172ad9")
                    padding (30, 24)
                    xfill True

                    vbox:
                        spacing 10

                        text _("Catatan Penting"):
                            color "#7dd3fc"
                            size 30
                            bold True

                        text _("Pelaku perundungan pun sering kali menyimpan tekanan atau luka di rumah. Menegaskan batas perilaku salah dan membina empati jauh lebih menyembuhkan daripada membalas ejekan dengan ejekan baru."):
                            color "#e2e8f0"
                            size 25

            frame:
                background Solid("#1e293bd9")
                padding (28, 20)
                xfill True

                hbox:
                    spacing 24
                    xfill True
                    yalign 0.5

                    vbox:
                        spacing 4
                        xmaximum 780

                        text _("Uji Pemahaman Anti-Perundungan"):
                            color "#ffffff"
                            size 28
                            bold True

                        if persistent.quiz_sudah:
                            text _("Skor Kuis Tertinggi: [persistent.quiz_tertinggi]/4"):
                                color "#86efac"
                                size 24
                        else:
                            text _("Coba 4 soal singkat bersama Pak Joko setelah membaca materi."):
                                color "#cbd5e1"
                                size 24

                    if main_menu:
                        textbutton _("Mulai Kuis Refleksi"):
                            action Start("kuis_refleksi")
                            align (1.0, 0.5)
                    else:
                        text _("(Kuis tersedia dari Menu Utama atau setelah Ending)"):
                            color "#94a3b8"
                            size 22
                            align (1.0, 0.5)
                            xmaximum 430
                            text_align 1.0


## -----------------------------------------------------------------------------
##  2. LAYAR GALERI ENDING & PREVIEW CG
## -----------------------------------------------------------------------------
screen galeri_ending():

    tag menu

    $ _total_terbuka = sum(1 for _x in [persistent.ending_bad, persistent.ending_normal, persistent.ending_good, persistent.ending_true] if _x)

    use game_menu(_("Galeri Ending"), scroll="viewport", spacing=20):

        vbox:
            spacing 20
            xfill True

            frame:
                background Solid("#1e293bd9")
                padding (26, 18)
                xfill True

                hbox:
                    spacing 20

                    text _("Progres Koleksi Ending: [_total_terbuka] / 4 Terbuka"):
                        color "#7dd3fc"
                        size 30
                        bold True

                    if _total_terbuka == 4:
                        text _("(Semua jalur cerita telah ditemukan!)"):
                            color "#86efac"
                            size 26
                            yalign 0.5

            ## Kartu 1: Bad Ending
            frame:
                background Solid("#0f172ad9")
                padding (22, 20)
                xfill True

                hbox:
                    spacing 26

                    if persistent.ending_bad:
                        imagebutton:
                            idle Transform("images/cg/ending_buruk.png", xysize=(320, 180), fit="cover")
                            hover Transform("images/cg/ending_buruk.png", xysize=(320, 180), fit="cover", matrixcolor=BrightnessMatrix(0.08))
                            action Show("preview_cg", cg_path="images/cg/ending_buruk.png", judul="Bad Ending: Sunyi di Bangku Sebelah", keterangan="Akibat terus memilih diam saat menyaksikan perundungan, Kenzie kehilangan rasa amannya di sekolah.")
                    else:
                        frame:
                            background Solid("#1e293bff")
                            xysize (320, 180)
                            text _("TERKUNCI") align (0.5, 0.5) color "#64748b" size 26

                    vbox:
                        spacing 8
                        yalign 0.5
                        xmaximum 860

                        text _("Ending 1 - Bad Ending: Sunyi di Bangku Sebelah"):
                            color ("#f87171" if persistent.ending_bad else "#94a3b8")
                            size 30
                            bold True

                        if persistent.ending_bad:
                            text _("Status: Terbuka  |  Klik gambar di kiri untuk melihat CG penuh."):
                                color "#cbd5e1"
                                size 24
                            text _("Diam di tengah ketidakadilan bukan sikap netral, melainkan membiarkan korban merasa sendirian."):
                                color "#e2e8f0"
                                size 24
                        else:
                            text _("Status: Terkunci"):
                                color "#64748b"
                                size 24
                            text _("Petunjuk: Terjadi jika Rara memilih terus diam di kelas hingga menolak bertindak di hari berikutnya."):
                                color "#94a3b8"
                                size 24

            ## Kartu 2: Normal Ending
            frame:
                background Solid("#0f172ad9")
                padding (22, 20)
                xfill True

                hbox:
                    spacing 26

                    if persistent.ending_normal:
                        imagebutton:
                            idle Transform("images/background/ruang_kelas.png", xysize=(320, 180), fit="cover", matrixcolor=TintMatrix("#9eb2cc") * SaturationMatrix(0.55) * BrightnessMatrix(-0.12))
                            hover Transform("images/background/ruang_kelas.png", xysize=(320, 180), fit="cover", matrixcolor=TintMatrix("#b0c4de") * SaturationMatrix(0.65))
                            action Show("preview_cg", cg_path="images/background/ruang_kelas.png", judul="Normal Ending: Luka yang Belum Sepenuhnya Pulih", keterangan="Perundungan berhasil dihentikan, namun cara yang terlalu keras atau tindakan yang terlambat menyisakan jarak di antara teman.")
                    else:
                        frame:
                            background Solid("#1e293bff")
                            xysize (320, 180)
                            text _("TERKUNCI") align (0.5, 0.5) color "#64748b" size 26

                    vbox:
                        spacing 8
                        yalign 0.5
                        xmaximum 860

                        text _("Ending 2 - Normal Ending: Luka yang Belum Pulih"):
                            color ("#fbbf24" if persistent.ending_normal else "#94a3b8")
                            size 30
                            bold True

                        if persistent.ending_normal:
                            text _("Status: Terbuka  |  Klik gambar di kiri untuk melihat adegan penutup."):
                                color "#cbd5e1"
                                size 24
                            text _("Niat membela perlu diimbangi cara yang tepat waktu dan tidak membalas emosi dengan amarah."):
                                color "#e2e8f0"
                                size 24
                        else:
                            text _("Status: Terkunci"):
                                color "#64748b"
                                size 24
                            text _("Petunjuk: Terjadi jika menegur dengan bentakan tanpa introspeksi, atau sempat diam lalu terlambat melapor."):
                                color "#94a3b8"
                                size 24

            ## Kartu 3: Good Ending
            frame:
                background Solid("#0f172ad9")
                padding (22, 20)
                xfill True

                hbox:
                    spacing 26

                    if persistent.ending_good:
                        imagebutton:
                            idle Transform("images/cg/ending_normal.png", xysize=(320, 180), fit="cover")
                            hover Transform("images/cg/ending_normal.png", xysize=(320, 180), fit="cover", matrixcolor=BrightnessMatrix(0.08))
                            action Show("preview_cg", cg_path="images/cg/ending_normal.png", judul="Good Ending: Pameran Lukisan Kelas", keterangan="Dengan bantuan Pak Joko dan kerja sama yang adil, Kenzie kembali aman berkarya dan Danisa belajar menghargai usaha temannya.")
                    else:
                        frame:
                            background Solid("#1e293bff")
                            xysize (320, 180)
                            text _("TERKUNCI") align (0.5, 0.5) color "#64748b" size 26

                    vbox:
                        spacing 8
                        yalign 0.5
                        xmaximum 860

                        text _("Ending 3 - Good Ending: Pameran Lukisan Kelas"):
                            color ("#38bdf8" if persistent.ending_good else "#94a3b8")
                            size 30
                            bold True

                        if persistent.ending_good:
                            text _("Status: Terbuka  |  Klik gambar di kiri untuk melihat CG penuh."):
                                color "#cbd5e1"
                                size 24
                            text _("Melapor kepada guru terpercaya adalah langkah tepat untuk melindungi korban dan membina pelaku secara adil."):
                                color "#e2e8f0"
                                size 24
                        else:
                            text _("Status: Terkunci"):
                                color "#64748b"
                                size 24
                            text _("Petunjuk: Libatkan Pak Joko melalui jalur Melapor (Delegate) dan bangun kerja sama saat persiapan pameran."):
                                color "#94a3b8"
                                size 24

            ## Kartu 4: True Ending
            frame:
                background Solid("#0f172ad9")
                padding (22, 20)
                xfill True

                hbox:
                    spacing 26

                    if persistent.ending_true:
                        imagebutton:
                            idle Transform("images/cg/ending_baik.png", xysize=(320, 180), fit="cover")
                            hover Transform("images/cg/ending_baik.png", xysize=(320, 180), fit="cover", matrixcolor=BrightnessMatrix(0.08))
                            action Show("preview_cg", cg_path="images/cg/ending_baik.png", judul="True Ending: Matahari di Balik Awan", keterangan="Keberanian yang lembut, pendampingan untuk Kenzie, dan kesediaan mendengar isi hati Danisa menyembuhkan akar masalah hingga lahir persahabatan baru.")
                    else:
                        frame:
                            background Solid("#1e293bff")
                            xysize (320, 180)
                            text _("TERKUNCI") align (0.5, 0.5) color "#64748b" size 26

                    vbox:
                        spacing 8
                        yalign 0.5
                        xmaximum 860

                        text _("Ending 4 - True Ending: Matahari di Balik Awan"):
                            color ("#4ade80" if persistent.ending_true else "#94a3b8")
                            size 30
                            bold True

                        if persistent.ending_true:
                            text _("Status: Terbuka  |  Klik gambar di kiri untuk melihat CG penuh."):
                                color "#cbd5e1"
                                size 24
                            text _("Tegas pada perbuatan salah, tetapi tetap peduli pada hati manusianya—itulah keberanian sejati."):
                                color "#e2e8f0"
                                size 24
                        else:
                            text _("Status: Terkunci"):
                                color "#64748b"
                                size 24
                            text _("Petunjuk: Tegur dengan tenang tanpa mempermalukan, dampingi Kenzie, dan dengarkan alasan di balik sikap Danisa."):
                                color "#94a3b8"
                                size 24


screen preview_cg(cg_path, judul, keterangan):

    modal True
    zorder 250

    add Solid("#020617eb")

    vbox:
        align (0.5, 0.5)
        spacing 18

        frame:
            background Solid("#0f172aff")
            padding (12, 12)
            xalign 0.5

            add Transform(cg_path, xysize=(1360, 765), fit="contain")

        frame:
            background Solid("#0f172ae6")
            padding (28, 18)
            xsize 1360
            xalign 0.5

            hbox:
                xfill True
                spacing 24

                vbox:
                    spacing 4
                    xmaximum 1060

                    text judul:
                        color "#7dd3fc"
                        size 28
                        bold True

                    text keterangan:
                        color "#e2e8f0"
                        size 23

                textbutton _("Tutup"):
                    action Hide("preview_cg")
                    align (1.0, 0.5)

    key "game_menu" action Hide("preview_cg")


## -----------------------------------------------------------------------------
##  3. LAYAR RINGKASAN JEJAK PILIHAN DI AKHIR CERITA
## -----------------------------------------------------------------------------
screen ringkasan_ending(judul_ending, kategori, warna_judul, pesan_moral, tips_eksplorasi):

    modal True
    zorder 150

    add Solid("#020617cc")

    frame:
        background Solid("#0f172af2")
        padding (44, 34)
        align (0.5, 0.5)
        xsize 1240

        vbox:
            spacing 20

            vbox:
                spacing 6

                text kategori:
                    color warna_judul
                    size 24
                    bold True

                text judul_ending:
                    color "#ffffff"
                    size 42
                    bold True

            frame:
                background Solid("#1e293bcc")
                padding (24, 18)
                xfill True

                vbox:
                    spacing 10

                    text _("Indikator Sikap Upstander Selama Permainan"):
                        color "#7dd3fc"
                        size 26
                        bold True

                    grid 2 2:
                        spacing 16
                        xfill True

                        text _("Keberanian Membela: [keberanian]"):
                            color "#e2e8f0"
                            size 25
                        text _("Empati & Kepekaan: [empati]"):
                            color "#e2e8f0"
                            size 25
                        text _("Kepercayaan Kenzie: [kepercayaan_kenzie]"):
                            color "#e2e8f0"
                            size 25
                        text _("Kesadaran Danisa: [kesadaran_danisa]"):
                            color "#e2e8f0"
                            size 25

            frame:
                background Solid("#1e293bcc")
                padding (24, 18)
                xfill True

                vbox:
                    spacing 10

                    text _("Jejak Strategi 5D yang Kamu Terapkan"):
                        color "#7dd3fc"
                        size 26
                        bold True

                    $ _st_direct = "Diterapkan" if d_direct else "Belum"
                    $ _st_distract = "Diterapkan" if d_distract else "Belum"
                    $ _st_delegate = "Diterapkan" if d_delegate else "Belum"
                    $ _st_delay = "Diterapkan" if d_delay else "Belum"
                    $ _st_document = "Diterapkan" if d_document else "Belum"

                    hbox:
                        spacing 28
                        box_wrap True

                        text ("Direct: " + _st_direct):
                            color ("#86efac" if d_direct else "#94a3b8")
                            size 24
                        text ("Distract: " + _st_distract):
                            color ("#86efac" if d_distract else "#94a3b8")
                            size 24
                        text ("Delegate: " + _st_delegate):
                            color ("#86efac" if d_delegate else "#94a3b8")
                            size 24
                        text ("Delay: " + _st_delay):
                            color ("#86efac" if d_delay else "#94a3b8")
                            size 24
                        text ("Document: " + _st_document):
                            color ("#86efac" if d_document else "#94a3b8")
                            size 24

            text pesan_moral:
                color "#f8fafc"
                size 26

            if tips_eksplorasi:
                text tips_eksplorasi:
                    color "#fde68a"
                    size 23

            hbox:
                xalign 1.0
                textbutton _("Lanjutkan"):
                    action Return()


## -----------------------------------------------------------------------------
##  4. KUIS REFLEKSI INTERAKTIF (UNTUK EVALUASI PEMAHAMAN PKM)
## -----------------------------------------------------------------------------
label kuis_refleksi:
    scene bg kelas
    with fade

    play music bgm_happy fadeout 1.0 fadein 1.0 if_changed

    $ skor_kuis = 0
    $ atur_posisi(joko="tengah")
    show joko sapa at sprite_tengah
    with dissolve

    pak_joko "Halo! Sebelum selesai, Bapak punya 4 pertanyaan singkat untuk refleksi bersama tentang kisah Rara, Kenzie, dan Danisa."
    show joko mengajar at sprite_tengah
    pak_joko "Santai saja, ini bukan ujian nilai, melainkan latihan memahami cara menjadi sahabat yang peduli."

    ## Soal 1
    show joko berpikir at sprite_tengah
    menu:
        "Soal 1/4: Kapan sebuah ejekan seperti 'mataharimu kayak telur dadar' berubah dari candaan menjadi perundungan?"

        "Ketika dilakukan berulang dengan tujuan merendahkan hingga korban merasa takut dan tidak aman.":
            $ skor_kuis += 1
            show joko jempol at sprite_tengah
            pak_joko "Tepat sekali! Candaan membuat semua orang tertawa bersama. Jika satu pihak menangis atau merasa terancam secara berulang, itu sudah termasuk perundungan."

        "Hanya kalau sampai terjadi perkelahian fisik.":
            show joko mengajar at sprite_tengah
            pak_joko "Kurang tepat, ya. Perundungan tidak selalu fisik—ejekan verbal, pengucilan sosial, dan merendahkan karya teman di depan kelas juga melukai hati secara serius."

        "Kalau pelakunya sengaja merusak barang saja.":
            show joko mengajar at sprite_tengah
            pak_joko "Belum lengkap, Nak. Merusak barang memang termasuk perundungan, tetapi ejekan kata-kata yang dilakukan berulang hingga membuat teman takut sekolah juga merupakan perundungan."

    ## Soal 2
    show joko berpikir at sprite_tengah
    menu:
        "Soal 2/4: Jika Rara memilih diam dan pura-pura membaca buku saat Kenzie diejek karena takut menjadi sasaran berikutnya, peran apa yang sedang terjadi?"

        "Upstander, karena menjaga diri agar tidak ikut bertengkar.":
            show joko pose_serius at sprite_tengah
            pak_joko "Hati-hati, diam dan membiarkan ketidakadilan terjadi disebut bystander pasif. Meskipun alasannya takut, hal itu sering membuat pelaku merasa bebas melanjutkan perundungan."

        "Bystander pasif, yang diamnya dapat membuat korban merasa sendirian.":
            $ skor_kuis += 1
            show joko kedip at sprite_tengah
            pak_joko "Benar! Rasa takut itu manusiawi, tetapi diam bukanlah sikap netral. Ada banyak cara aman untuk menolong tanpa harus berkelahi."

        "Pelaku utama perundungan.":
            show joko mengajar at sprite_tengah
            pak_joko "Bukan pelaku utama, melainkan bystander pasif. Namun jika saksi mata tidak bertindak atau malah ikut tertawa, perundungan akan semakin sulit berhenti."

    ## Soal 3
    show joko berpikir at sprite_tengah
    menu:
        "Soal 3/4: Mengajak korban menepi ke lorong untuk memutus kerumunan, lalu menenangkannya setelah kejadian, termasuk penerapan strategi 5D bagian apa?"

        "Distract (mengalihkan situasi) dan Delay (mendampingi korban).":
            $ skor_kuis += 1
            show joko jempol at sprite_tengah
            pak_joko "Hebat! Kamu tidak harus selalu beradu mulut di tempat. Mengalihkan situasi dan mendampingi perasaan teman setelahnya adalah tindakan upstander yang sangat efektif."

        "Direct dan balas dendam.":
            show joko mengajar at sprite_tengah
            pak_joko "Tidak ada balas dendam dalam prinsip 5D. Mengalihkan situasi disebut Distract, sedangkan mendampingi korban sesudahnya disebut Delay."

        "Mengabaikan masalah agar cepat selesai.":
            show joko mengajar at sprite_tengah
            pak_joko "Bukan mengabaikan, justru itu cara cerdas melindungi teman: Distract (mengalihkan situasi dari kerumunan) dan Delay (mendampingi dan menenangkan korban)."

    ## Soal 4
    show joko berpikir at sprite_tengah
    menu:
        "Soal 4/4: Mengapa melapor kepada guru atau orang tua (Delegate) tidak sama dengan 'tukang mengadu'?"

        "Karena tujuannya melindungi keselamatan dan memulihkan keadaan, bukan mencari sensasi atau balas dendam.":
            $ skor_kuis += 1
            show joko jempol at sprite_tengah
            pak_joko "Seratus persen benar! Mengadu bertujuan menjatuhkan orang lain demi keisengan, sedangkan melapor bertujuan menjaga keamanan semua pihak agar masalah ditangani dengan adil."

        "Karena murid boleh melaporkan siapa saja agar mendapat hadiah dari guru.":
            show joko mengajar at sprite_tengah
            pak_joko "Tentu bukan untuk mencari hadiah. Melapor dilakukan karena ada teman yang terluka atau terancam dan kita butuh bantuan orang dewasa yang berwenang."

        "Sebenarnya sama saja, jadi lebih baik tidak usah melapor selamanya.":
            show joko pose_serius at sprite_tengah
            pak_joko "Jangan sampai keliru, ya. Masalah yang berulang dan membuat anak takut bersekolah justru membutuhkan bantuan guru atau orang tua agar berhenti dengan aman."

    ## Hasil akhir kuis
    $ persistent.quiz_sudah = True
    if skor_kuis > persistent.quiz_tertinggi:
        $ persistent.quiz_tertinggi = skor_kuis

    if skor_kuis == 4:
        show joko jempol at sprite_tengah
        pak_joko "Luar biasa! Skor kamu 4/4! Kamu sudah memahami cara menjadi Upstander yang berani, empatik, dan bijaksana."
    elif skor_kuis >= 2:
        show joko kedip at sprite_tengah
        pak_joko "Bagus! Skor kamu [skor_kuis]/4. Kamu sudah memahami dasar-dasarnya, dan kamu bisa menengok Pojok Edukasi kapan saja untuk mengulang materi 5D."
    else:
        show joko sapa at sprite_tengah
        pak_joko "Skor kamu [skor_kuis]/4. Tidak apa-apa, belajar menjadi berani dan peduli memang butuh proses. Coba baca Pojok Edukasi atau eksplorasi rute cerita yang lain, ya!"

    menu:
        "Apa yang ingin kamu lakukan selanjutnya?"

        "Mainkan cerita dari awal lagi.":
            jump start

        "Kembali ke Menu Utama.":
            stop music fadeout 1.5
            return
