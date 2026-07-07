textpos = 0
timedrawing = False
ldldrawing = False
veryuppercase = False
pressuretrend = False
musicdir = None
mesoid = "NWSPIL"
extra = ""
crawlint = 0
ldlbg = ""
old = set()
crawls = [
    (
        "9DCrew.org is your home for technology related shenanigans! Whether for FreeStar or something else we thank you for your patronage!",
        True,
    ),
    (
        "OTA SAVES LIVES! By buying an Over-The-Air Antenna from your local Walmart, Target, or Electronics Store, you can save over 20 Non-Smart TV’s from the landfill!",
        True,
    ),
    (
        "CABLE CONTRIBUTES TO LIFE… like you should pay them anything! Hop aboard fellow pirate and sail the seas with me! Argh!",
        True,
    ),
    (
        "Genericable Digital Cable offers more choices - VOD, HDTV packages, more  sports & more movies! Order Digital Basic Plus Today for only $1/month for two months, plus receive FREE digital installation, Limited time offer. Digital Cable not available in all areas. Visit your local Midwest Genericable office today to sign up!",
        True,
    ),
    ("Spob, can I get a glass of water? *click, thump thump thump* OH NO- *BANG*", True),
    (
        "With WebTV, you to can access this new fangled internet thing from the comfort of the couch! It might not work well like at all but at least it can maybe play doom! Go to webtv.zone on...wait if you don't have internet how are you gonna visit that site?? This ad is dumb.",
        True,
    ),
    (
        "All Eyes Turn to The Weather Channel. Using the Weather Crawl is an inexpensive way to get more exposure for your company, by increasing your companys visibility on cable TV. The Weather Crawl runs 24 Hours/day, 7 days/week. Limited Availability-Call 555-555-5555 for more info.",
        True,
    ),
    (
        " 9DCrew.org is America's #1 Technology and Weather website. Trusted. Reliable. Accurate. Visit 9DCrew.org today.",
        True,
    ),
    
    
    ("", True),
    ("", True),
    ("", True),
]
outputs = []
schedule = ""
ldlmode = False
forever = True
foreverldl = True
aspect = True
socket = False
smode = 0
radarint = 0.25
radarhold = 2.5
ldllf = False
mainlogo = "./logos/9dlogo.png"
radarlogo = "./logos/9dradar.png"
extensions = ()
audiodevice = "Default"
metric = False
borderless = False
vencoder = "libx264"
widescreen = False
mute = False
compress = False
radarsetting = 0
lsort = 0
smoothscale = True
musicsetting = 0
crawllen = 40
tidal = ("", "", "", "")
framerate = 60
efullscreen = False
ldlfeed = ""
flavor = ["intro", "cc", "xf", "lf", "lo", "al"]
flavor_times = [5.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0]

mainloc = "John F. Kennedy International Airport"
mainloc2 = "Kennedy Arpt"
efname = "New York Metro"
obsloc = [
    ["Bridgeport, CT", "Bridgeport"],
    ["Islip, NY", "Islip"],
    ["John F. Kennedy International Airport", "Kennedy Arpt"],
    ["La Guardia Airport", "La Guardia Apt"],
    ["Newark, NJ", "Newark"],
    ["Teterboro, NJ", "Teterboro"],
    ["Westchester County, NY", "Westchester Co"],
]
reglocs = [loc[0] for loc in obsloc]
regnames = [loc[1] for loc in obsloc]
