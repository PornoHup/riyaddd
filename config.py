from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://images.app.goo.gl/gUqiKSRGJkcB16LDA")
START_IMG = getenv("START_IMG", "https://images.app.goo.gl/2EnpdVRQ2fx531AD9")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/TuralBlogg")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/NezrinBot")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5809546648").split()))


FAILED = "https://www.instagram.com/p/CIvUqiXDGs5/?igsh=c25hZ2p3NnhrMDNr"
