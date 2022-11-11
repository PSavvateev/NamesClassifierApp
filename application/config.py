import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    CSRF_ENABLED = True

    # Set up the App SECRET_KEY
    SECRET_KEY = os.environ["SECRET_KEY"]
    WTF_CSRF_SECRET_KEY = os.environ["WTF_CSRF_SECRET_KEY"]