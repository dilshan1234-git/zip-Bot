import os

class Config(object):
     
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6880188560:AAHpk9t0uWT1CURv7NqJIJCZ3XsPyywGc8E")
    API_ID = int(os.environ.get("API_ID", "14631157"))
    API_HASH = os.environ.get("API_HASH", "aa7c2b3be68a7488abdb9de6ce78d311")
    
    
