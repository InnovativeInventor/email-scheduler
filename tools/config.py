import os
from dotenv import load_dotenv

load_dotenv(override=True)

EMAIL_USERNAME = os.getenv("EMAIL_USERNAME")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
DB = os.getenv("DATABASE")
