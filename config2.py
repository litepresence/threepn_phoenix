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

TOKEN = ""  # token from the @botfather
CHANNELS = {
    "threepn_bot": "-1001651701128",
    "threepn": "-1001498534218",
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

#"bigdocsfiesta",
#"deanofiles",

USERS = [
    "0101xtmd",
    "10spanky1",
    "1plus2equals3d",
    "3d_amendment",
    "3d_oa",
    "3dnrn",
    "3dprintgeneral",
    "albert9x19",
    "arthurclaudeen",
    "awcy_arms",
    "bigtangringo",
    "blackrosewolf2",
    "booligancustoms",
    "boomhands",
    "bowtiedankylo",
    "brokenbulletz",
    "bumpybigloo",
    "catsprayallday",
    "chairmanwon",
    "clonewar1",
    "comeoutandpla",
    "crabwickthechad",
    "ctrlpew",
    "daddywarbux3",
    "daikondefense",
    "darkscarecrow22",
    "de_faultt",
    "dianexis",
    "digitalnimbus_",
    "dispensedparts",
    "dmtx1010",
    "doctorwhip",
    "dogenado_exe",
    "dootdefense",
    "fedplots",
    "ferretpass",
    "ffftechnology",
    "firebirdprints",
    "foobadoo1",
    "freeman13372",
    "fuckleberry90",
    "geraldkatz9",
    "ghostgunnews",
    "goongundesigns",
    "guns_3d",
    "gunsnbitcoin",
    "guttercheese",
    "innernetpizza",
    "invaderzip_",
    "iprintgunz",
    "jerrycurld",
    "jnyboy",
    "kadecad1",
    "klaviermeister2",
    "km3d3",
    "krrawn",
    "krus_chiki",
    "kyelermorgan",
    "kyleprintspews",
    "legsenergy",
    "liberty_jedi",
    "lopointgoat",
    "makerrezzy",
    "menendez3d",
    "minty_pass",
    "moderatorgage",
    "mprtech2",
    "mrjmezz",
    "mrsnow_makes",
    "navigoboom",
    "nguyenkvvn",
    "nickdoff23",
    "osinttechnical",
    "other_sig",
    "p80ralph",
    "pincusrob",
    "plastikgatz",
    "polymaker_3d",
    "post_offensive",
    "print2a_repo",
    "printingguns",
    "printsandtherev",
    "printyour2a",
    "prometheuzzzzzz",
    "proteusfosscad",
    "protouniverse3d",
    "realquietbryan",
    "ricecutta0",
    "riptiderails",
    "rkneegrow",
    "rkspookware",
    "sdi_school",
    "spacebound3dp",
    "spooky3dpg",
    "stayfree3dp",
    "stevekreitler",
    "suckboytony1",
    "tedyheremc",
    "thathicks",
    "the_zer0fux",
    "therustymosin",
    "trophy_trout",
    "walrus_pajamas",
    "xaniken",
    "xyeezyszn",
    "youmaycall_me_v"
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
