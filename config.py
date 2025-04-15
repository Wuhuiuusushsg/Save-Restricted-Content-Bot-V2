# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "20054245"))
API_HASH = getenv("API_HASH", "431f22f320ed5d69225d3b3fc253fc0d")
BOT_TOKEN = getenv("BOT_TOKEN", "8117739787:AAEFB7RuDBny6sR7lCtRbZom3LbI2VVqtZQ")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5034929962").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://motivationhubiit2025:75RgOXQzxYICxc30@cluster0.l6wktoc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "")
CHANNEL_ID = int(getenv("CHANNEL_ID", ""))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "10000"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", "")
AD_API = getenv("AD_API", "")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", None)
INSTA_COOKIES = getenv("INSTA_COOKIES", None)
