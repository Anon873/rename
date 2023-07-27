import re
import os

class Config(object):
    START_PIC   = os.environ.get("START_PIC", "")
    TOKEN = os.environ.get("TOKEN", "")
    API_ID = int(os.environ.get("API_ID", ""))
    API_HASH = os.environ.get("API_HASH", "")
    STRING = os.environ.get("STRING", "")
    DB_NAME = os.environ.get("DB_NAME", "")
    DB_URL = os.environ.get("DB_URL", "")
    ADMIN = os.environ.get("ADMIN", "")
    CHANNEL = os.environ.get("CHANNEL", "")
    LAZY_PIC = os.environ.get("LAZY_PIC", "")
    LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "")

    
    
    
