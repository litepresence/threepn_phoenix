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
REPOST = 7200  # seconds between posts to main channel

MSG = (  # message header for telegram post
    "JOIN @threepn_phoenix\n"
    + "*** BACKUP @the_gatalog NOW ***\n"
    + "https://t.me/s/threepn_phoenix/30000001765"
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
USERS = [
    "0101xtmd",
    "10spanky1",
    "1plus2equals3d",
    "2acountrycouple",
    "3d_amendment",
    "3d_oa",
    "3dnrn",
    "3dprintgeneral",
    "3dyour2a",
    "albert9x19",
    "archie_2aprint",
    "armedj0y",
    "arthurclaudeen",
    "autunite1878",
    "avesrails",
    "awcy_arms",
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
    "bumpybigloo",
    "cathode_g",
    "catsprayallday",
    "chairmanwon",
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
    "darkscarecrow22",
    "de_faultt",
    "defcad",
    "dianexis",
    "digitalnimbus_",
    "dirtyjobsinre",
    "dispensedparts",
    "dissidentrexy",
    "dmtx1010",
    "doctorwhip",
    "dogenado_exe",
    "dootdefense",
    "drdeath1776",
    "eaglerun23",
    "edc208",
    "elatedpariah",
    "fedplots",
    "ferretpass",
    "ffftechnology",
    "firebirdprints",
    "fmda1776",
    "foobadoo1",
    "freeman13372",
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
    "hoffmantactical",
    "huntereatschalk",
    "incel_gamer",
    "innernetpizza",
    "invaderzip_",
    "iprintgunz",
    "itsreallyjason",
    "jaegercompny",
    "jc_arms",
    "jerrycurld",
    "jnyboy",
    "kadecad1",
    "klaviermeister2",
    "km3d3",
    "krrawn",
    "krus_chiki",
    "kyelermorgan",
    "kyleprintspews",
    "laffs_dynamics",
    "lcultivated",
    "legsenergy",
    "liberty_jedi",
    "lopointgoat",
    "louisvillegun",
    "mainemike79",
    "makerrezzy",
    "mattyboyyyyy",
    "menendez3d",
    "minty_pass",
    "mirrorlessj",
    "mnyenemymuchhnr",
    "moderatorgage",
    "mprtech2",
    "mrjmezz",
    "mrninjaburg",
    "mrsnow_makes",
    "napalmrising",
    "navigoboom",
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
    "riptiderails",
    "rkneegrow",
    "rkspookware",
    "robert7075307",
    "sabrprints",
    "samizdat_steve",
    "sdi_school",
    "shackleford_777",
    "simplyhuffy",
    "smokiemcagee",
    "spacebound3dp",
    "spooky3dpg",
    "spottydraft",
    "ssgtkotyk",
    "stayfree3dp",
    "stevekreitler",
    "stfudvs",
    "suckboytony1",
    "tedyheremc",
    "thathicks",
    "the_frost_boss",
    "the_zer0fux",
    "thebattlecock",
    "thegencatton",
    "therustymosin",
    "timeoutwithtl",
    "trophy_trout",
    "tryvngle",
    "uberpoor",
    "upndownthewatr",
    "vega_holdings",
    "vegancokehead69",
    "walrus_pajamas",
    "xaniken",
    "xyeezyszn",
    "yeezy_prints",
    "youmaycall_me_v",
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
