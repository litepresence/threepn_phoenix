"""
 ╔════════════════════════════╗
 ║ ╔═╗╔╦╗╔═╗╔═╗╔═╗  ╔╗ ╔═╗╔╦╗ ║
 ║  ╠╣ ║║╠═╝╠╣ ╠═╣  ╠╩╗║ ║ ║  ║
 ║ ╚═╝╚╩╝╩  ╚  ╩ ╩  ╚═╝╚═╝ ╩  ║
 ╚════════════════════════════╝<logo>


we each run a bot
we're all nodes in a rebroadcasting network;
we each have our own telegram room we own,
but we each have message posting rights to one another's rooms
on an apostolic/egalitarian/voluntarist level (via chat) we share posting rights.
as well; rooms are something like `af1651es3PNe78f05`.
we keep track of whoever is in any of the rooms and send out invites to past members of
any group after getting shut down. we keep track of where other admins rooms are via chat.
maybe these bots each grab stuff
from twitter, youtube, odysee, other telegram channels...
via ai it makes suggestions to the bot channel.
the bot makes sure that anything posted in any of the nodes you're parroting
gets reposted on your main channel.
and anything posted in any of the nodes your following
gets reposted on your bot channel.

Configuration File

WTFPL litepresence 2021
"""

# token from the @botfather
TOKEN = ""

# to get forward_from_channel id forward a msg from the channel to @JsonDumpBot
# the id should begin with -100
CHANNELS = {
    "threepn_bot": "-1001651701128",
    "threepn_phoenix": "-1001597790834",
}
BOT_CHANNEL = "threepn_bot"
MAIN_CHANNEL = "threepn_phoenix"

FOLLOW = [  # post to the bot channel
    "mrgunsngear",
    #"printersdeals",
    #"gunsstl",
]
PARROT = [  # post to the main channel
    "defensedistributed",
    #"deterrence_dispensed_fans",
]
DEV = True  # additional printing
DEPLOY = True  # True to post to telegram
DISPLAY = False  # Display haar results
RESTART = False  # Delete database and start fresh
CROP = 0  # take only the first CROP from list of USERS; 0 for all
DAYS = 7  # days to look back in time on what has been posted upon initialization
DELAY = 5 # between external calls
DEPTH = 50 # tweets to look back for each twitter user
REPOST = 3600  # seconds between posts to main channel
BAN_INTERVAL = 20

MSG = (  # message header for telegram post
    "3D PRINTING NATION'S PHOENIX\n"
    + "Where Free Men Arise to Arm Themselves\n\n"
    + "JOIN https://t.me/the_gatalog"
)


# https://tweeterid.com/
# tweet_extractor.py unit_test()


# Twitter Banned
# bigdocsfiesta
# deanofiles

# Found by Bot
# Mon Aug 29 00:13:36 2022 upndownthewatr
# Mon Aug 29 08:19:08 2022 ktacticalweebs
# Mon Aug 29 10:14:16 2022 prospacedog
# Mon Aug 29 11:30:04 2022 pimtooll
# Mon Aug 29 15:33:14 2022 edc208
# Tue Aug 30 03:42:00 2022 cathode_g
# Thu Sep  1 00:23:40 2022 avesrails
# Thu Sep  1 04:26:25 2022 3dyour2a
# Fri Sep  2 00:42:27 2022 itsreallyjason
# Fri Sep  2 04:45:17 2022 robert7075307
# Fri Sep  2 20:56:46 2022 vegancokehead69
# Tue Sep  6 15:59:10 2022 mrninjaburg
# Wed Sep  7 08:10:24 2022 mattyboyyyyy
# Wed Sep  7 14:14:45 2022 smokiemcagee
# Thu Sep  8 16:33:02 2022 huntereatschalk
# Thu Sep  8 22:37:16 2022 dissidentrexy
# Fri Sep  9 12:47:01 2022 projectslair
# Fri Sep  9 20:52:22 2022 samizdat_steve
# Mon Sep 12 15:38:56 2022 thebattlecock
# Tue Sep 13 17:59:27 2022 boracho20
# Thu Sep 15 18:31:09 2022 chuck_your_guru
# Fri Sep 16 02:51:32 2022 the_frost_boss
# Sat Sep 17 05:10:19 2022 mirrorlessj
# Sat Sep 17 11:14:31 2022 ricky2a3d
# Sat Sep 17 21:21:24 2022 vega_holdings
# Sun Sep 18 03:25:32 2022 hoffmantactical
# Mon Sep 19 15:50:27 2022 ssgtkotyk
# Tue Sep 20 01:57:22 2022 yeezy_prints
# Wed Sep 21 02:14:39 2022 2acountrycouple
# Wed Sep 21 12:22:06 2022 stfudvs
# Fri Sep 23 09:10:36 2022 happylandwrkshp
# Sat Sep 24 01:21:41 2022 tryvngle
# Sat Sep 24 09:27:06 2022 autunite1878
# Sat Sep 24 17:32:30 2022 rane909
# Sat Sep 24 21:35:17 2022 phil_phisher
# Tue Sep 27 06:11:51 2022 commanderapaul
# Tue Sep 27 22:22:42 2022 elatedpariah
# Wed Sep 28 08:29:29 2022 incel_gamer
# Thu Sep 29 04:52:22 2022 timeoutwithtl
# Sat Oct  1 05:25:11 2022 jc_arms
# Wed Oct  5 07:57:23 2022 psychicrhino
# Thu Oct  6 06:11:53 2022 napalmrising
# Sun Oct  9 04:56:17 2022 cnc_kitchen
# Mon Oct 10 13:18:40 2022 nickmunny
# Mon Oct 10 17:21:06 2022 oa_3d
# Sun Oct 16 04:32:48 2022 lcultivated
# Wed Oct 19 01:15:29 2022 shackleford_777
# Thu Oct 20 05:33:09 2022 defcad
# Fri Oct 21 22:58:08 2022 agcast4
# Sat Oct 22 17:05:09 2022 mhmiranusa
# Wed Oct 26 00:33:54 2022 kylejengel4
# Fri Oct 28 12:23:54 2022 u8onetu
# Sat Oct 29 10:30:43 2022 slamdan88
# Sat Oct 29 20:39:10 2022 4doorsmorehore
# Sun Oct 30 16:45:21 2022 stephenberkner
# Sun Nov  6 20:39:29 2022 _evan__jones_
# Mon Nov  7 20:46:58 2022 n1ghttr4c3
# Mon Nov 14 07:14:14 2022 maybeblanks
# Wed Nov 16 21:36:54 2022 skate_n_thrash
# Thu Nov 24 21:03:37 2022 bulletholz
# Sat Nov 26 09:14:43 2022 liberty17766
# Tue Dec  6 00:27:07 2022 jake_hanrahan
# Fri Dec 16 01:45:40 2022 heavenlyf33t
# Sun Jan 22 12:44:01 2023 2a3dprint
# Sun Jan 22 16:45:17 2023 photonray1
# Mon Jan 23 16:53:53 2023 jamesstout
# Wed Jan 25 13:07:39 2023 zoopyloops
# Fri Mar  3 15:33:41 2023 mafcorporation
# Sat Mar  4 01:09:17 2023 dinimbuslabs
# Sat Mar  4 05:10:46 2023 family_joules3d
# Sat Mar  4 07:11:30 2023 the_aveees
# Sat Mar  4 23:17:24 2023 doubleclutch229
# Tue Mar  7 13:40:47 2023 neutron__nick
# Wed Mar  8 19:51:14 2023 wishappfuelfltr
# Thu Mar  9 03:54:11 2023 yzy_prints
# Thu Mar  9 11:57:08 2023 rightsofrefusal
# Thu Mar  9 20:00:08 2023 danny_meatball
# Sat Mar 11 00:11:44 2023 josephtheparrot
# Sun Mar 12 09:22:47 2023 tacticalhandle
# Sun Mar 12 15:24:46 2023 marconiarmory
# Tue Mar 14 01:35:44 2023 shadzey1
# Tue Mar 14 16:00:04 2023 chrono52
# Tue Mar 14 18:00:50 2023 leoprecision
# Wed Mar 15 13:04:43 2023 digitalspaz
# Wed Mar 15 15:05:29 2023 austinreas
# Fri Mar 17 05:19:53 2023 balaclavaboi69
# Fri Mar 17 09:21:26 2023 tacticalxr
# Sat Mar 18 11:35:21 2023 r/fosscad/comments/11u5ika/sudy_2352_is_live/
# Sat Mar 18 17:37:38 2023 r/fosscad/comments/11tcagj/testing_1_of_2_rainbow_pla_filaments/
# Sun Mar 19 05:42:13 2023 r/fosscad/comments/11u64hs/2_thickness_5_density_fuzzy_skin_printed_in_1/
# Sun Mar 19 09:43:45 2023 r/fosscad/comments/11ttq4w/commence_project_amigo/
# Sun Mar 19 13:45:17 2023 r/fosscad/comments/11v9tfg/faux_wood_using_copic_ink_refills_damn_near/
# Sun Mar 19 17:46:49 2023 r/fosscad/comments/11v71lw/built_my_first_ar_today/
# Sun Mar 19 19:47:36 2023 scsupermoto
# Sun Mar 19 21:48:21 2023 r/fosscad/comments/11v36u4/baby_banger_shorty_pipe_hitter_37mm_and/
# Mon Mar 20 01:49:53 2023 r/fosscad/comments/11uw2g6/jus_need_a_gen_5_slide_lock_spring/
# Mon Mar 20 13:54:29 2023 jefedej63847622
# Mon Mar 20 23:08:36 2023 freerosswoodwrk
USERS = [
    "0101xtmd",
    "10spanky1",
    "1plus2equals3d",
    "2a3dprint",
    "2acountrycouple",
    "3d_amendment",
    "3d_oa",
    "3dnrn",
    "3dprintgeneral",
    "3dyour2a",
    "4doorsmorehore",
    "_evan__jones_",
    "agcast4",
    "albert9x19",
    "archie_2aprint",
    "armedj0y",
    "arthurclaudeen",
    "austinreas",
    "autunite1878",
    "avesrails",
    "awcy_arms",
    "balaclavaboi69",
    "beaneronline",
    "bigtangringo",
    "blackrosewolf2",
    "bludz41",
    "booligancustoms",
    "boomhands",
    "boostwillis",
    "boracho20",
    "bowtiedankylo",
    "brokenbulletz",
    "bulletholz",
    "bumpybigloo",
    "cathode_g",
    "catsprayallday",
    "chairmanwon",
    "chrono52",
    "chuck_your_guru",
    "clonewar1",
    "cnc_kitchen",
    "comeoutandpla",
    "commanderapaul",
    "crabwickthechad",
    "ctrlpew",
    "ctrlpew2",
    "daddywarbux3",
    "daikondefense",
    "danny_meatball",
    "darkscarecrow22",
    "de_faultt",
    "defcad",
    "dianexis",
    "digitalnimbus_",
    "digitalspaz",
    "dinimbuslabs",
    "dirtyjobsinre",
    "dispensedparts",
    "dissidentrexy",
    "dmtx1010",
    "doctorwhip",
    "dogenado_exe",
    "dootdefense",
    "doubleclutch229",
    "drdeath1776",
    "eaglerun23",
    "edc208",
    "elatedpariah",
    "family_joules3d",
    "fedplots",
    "ferretpass",
    "ffftechnology",
    "firebirdprints",
    "fmda1776",
    "foobadoo1",
    "freeman13372",
    "freerosswoodwrk",
    "fuckleberry90",
    "geraldkatz9",
    "ghostgunnews",
    "goongundesigns",
    "graveyardguns1",
    "guns_3d",
    "gunsnbitcoin",
    "guttercheese",
    "hamhawkfirearms",
    "happylandwrkshp",
    "heavenlyf33t",
    "hoffmantactical",
    "huntereatschalk",
    "incel_gamer",
    "innernetpizza",
    "invaderzip_",
    "iprintgunz",
    "itsreallyjason",
    "jaegercompny",
    "jake_hanrahan",
    "jamesstout",
    "jc_arms",
    "jefedej63847622",
    "jerrycurld",
    "jnyboy",
    "josephtheparrot",
    "kadecad1",
    "klaviermeister2",
    "km3d3",
    "krrawn",
    "krus_chiki",
    "kyelermorgan",
    "kylejengel4",
    "kyleprintspews",
    "laffs_dynamics",
    "lcultivated",
    "legsenergy",
    "leoprecision",
    "liberty17766",
    "liberty_jedi",
    "litepresence/threepn_phoenix",
    "lopointgoat",
    "louisvillegun",
    "mafcorporation",
    "mainemike79",
    "makerrezzy",
    "marconiarmory",
    "mattyboyyyyy",
    "maybeblanks",
    "menendez3d",
    "mhmiranusa",
    "minty_pass",
    "mirrorlessj",
    "mnyenemymuchhnr",
    "moderatorgage",
    "mprtech2",
    "mrjmezz",
    "mrninjaburg",
    "mrsnow_makes",
    "n1ghttr4c3",
    "napalmrising",
    "navigoboom",
    "neutron__nick",
    "nguyenkvvn",
    "nickdoff23",
    "nickmunny",
    "oa_3d",
    "oobliveshow",
    "osinttechnical",
    "other_sig",
    "p80ralph",
    "pancreasthief",
    "pewtang",
    "phil_phisher",
    "photonray1",
    "pimtooll",
    "pincusrob",
    "plastikgatz",
    "polymaker_3d",
    "post_offensive",
    "print2a_repo",
    "printingguns",
    "printsandtherev",
    "printyour2a",
    "profess51940942",
    "projectslair",
    "prometheuzzzzzz",
    "prospacedog",
    "proteusfosscad",
    "protouniverse3d",
    "psychicrhino",
    "rane909",
    "realquietbryan",
    "ricecutta0",
    "ricky2a3d",
    "rightsofrefusal",
    "riptiderails",
    "rkneegrow",
    "rkspookware",
    "robert7075307",
    "sabrprints",
    "samizdat_steve",
    "scsupermoto",
    "sdi_school",
    "shackleford_777",
    "shadzey1",
    "simplyhuffy",
    "skate_n_thrash",
    "slamdan88",
    "smokiemcagee",
    "spacebound3dp",
    "spooky3dpg",
    "spottydraft",
    "ssgtkotyk",
    "stayfree3dp",
    "stephenberkner",
    "stevekreitler",
    "stfudvs",
    "suckboytony1",
    "tacticalhandle",
    "tacticalxr",
    "tedyheremc",
    "thathicks",
    "the_aveees",
    "the_frost_boss",
    "the_zer0fux",
    "thebattlecock",
    "thegencatton",
    "therustymosin",
    "timeoutwithtl",
    "trophy_trout",
    "tryvngle",
    "u8onetu",
    "uberpoor",
    "upndownthewatr",
    "vega_holdings",
    "vegancokehead69",
    "walrus_pajamas",
    "wishappfuelfltr",
    "xaniken",
    "xyeezyszn",
    "yeezy_prints",
    "youmaycall_me_v",
    "yzy_prints",
    "zoopyloops",
    "zuccthis"
]


TRUE_CASCADES = [
    "cascade_guns.xml",
    "cascade_guns2.xml",
]

FALSE_CASCADES = [
    "cascade_anime.xml",
    "cascade_upperbody.xml",
    # "cascade_smile.xml",
    "cascade_russian_plate_number.xml",
    "cascade_righteye_2splits.xml",
    "cascade_profileface.xml",
    "cascade_lowerbody.xml",
    "cascade_licence_plate_rus_16stages.xml",
    "cascade_lefteye_2splits.xml",
    # "cascade_fullbody.xml",
    "cascade_frontalface_default.xml",
    "cascade_frontalface_alt_tree.xml",
    "cascade_frontalface_alt2.xml",
    "cascade_frontalface_alt.xml",
    "cascade_frontalcatface_extended.xml",
    "cascade_frontalcatface.xml",
    "cascade_eye_tree_eyeglasses.xml",
    "cascade_eye.xml",
    "cascade_dogs.xml",
    # "cascade_cats.xml",
    "cascade_cars.xml",
]
if CROP:
    USERS = USERS[:CROP:]
LOGO = __doc__.split("<logo>")[0]
