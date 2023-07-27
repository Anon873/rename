import re
import os

class Config(object):
    START_PIC   = os.environ.get("START_PIC", "")
    TOKEN = os.environ.get("TOKEN", "")
    API_ID = int(os.environ.get("API_ID", ""))
    API_HASH = os.environ.get("API_HASH", "")
    STRING = os.environ.get("STRING", "")

    
    
    
