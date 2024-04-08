from dotenv import load_dotenv
import os
load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
TIMEOUT = 5
HEADER = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0"}
MAX_RETURN_VALUE_LENGTH = 2000
