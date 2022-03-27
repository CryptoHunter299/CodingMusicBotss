from os import getenv
from os.path import exists
from dotenv import load_dotenv

load_dotenv("local.env" if exists("local.env") else None)


class Config:
    api_id = int(getenv("API_ID", "0"))
    api_hash = getenv("API_HASH")
    bot_token = getenv("BOT_TOKEN")
    session = getenv("SESSION")
    owner_id = int(getenv("OWNER_ID", "0"))


config = Config()
