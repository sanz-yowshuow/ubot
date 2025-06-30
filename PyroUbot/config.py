import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "200"))

DEVS = list(map(int, os.getenv("DEVS", "1261135074").split()))

API_ID = int(os.getenv("API_ID", "28469785"))

API_HASH = os.getenv("API_HASH", "d8d9227c40f6b393c221d412d178b783")

BOT_TOKEN = os.getenv("BOT_TOKEN", "7311970846:AAGAUvrykErJlspIlP31QyQm2Jw-ZlTGeHk")

OWNER_ID = int(os.getenv("OWNER_ID", "1261135074"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002312835928").split()))

RMBG_API = os.getenv("RMBG_API", "tqX9ye8ySBucCZDvpHL4fk8c")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://SanzXd:sanzxd@cluster0.zkxf6n2.mongodb.net/SanzXd?retryWrites=true&w=majority&appName=Cluster0")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1002312835928"))
