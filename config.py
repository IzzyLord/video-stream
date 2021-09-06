from os import path, getenv
from dotenv import load_dotenv

if path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
BOT_TOKEN = getenv("BOT_TOKEN", "1980188996:AAGzKJf4QYhYeMAGljZxXer8CAO3twrCRDU)
API_ID = int(getenv("API_ID", "7134686"))
API_HASH = getenv("API_HASH", "5f8f1d7649857c1ed2d63026d24f2277)
SESSION_NAME = getenv("SESSION_NAME", "BQC2DzJhu2h04fkhSRe0bX4gTSxuMGrTVDt_2R8R2H3aJz-TOj3fPNtmqIGN-nduTcsYzKBqf0YpukVimZ__CBU6TBxT80w92XaPIRfIyoB3gOkJ7E-uXcUCk8ngqcrykMWWzrNm-k0-zANSPWJw9PalDTbL-ppI-0O56Q3I-X00o6ZuPjRKoaCNnMU3mfaL8idt4EdexmZYoW80YAsEstFGBwsjGnBLDke2ENoWObahrjouXWyz1bSDF0WMHIzjosRCcd7VnhQeOnm_KNVC3rXcAJaxByhTkIgUO7gqKrR4QvnNs2e3TvA1A6nYl2pjirpIMQu572KlIIq4YgGwkmwvcuiJBAA)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "15"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "TGVideoStream")
BOT_USERNAME = getenv("BOT_USERNAME", "JawaraStreamBot")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . ?").split())
