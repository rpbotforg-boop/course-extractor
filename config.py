import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", '')
    API_ID = int(os.environ.get("API_ID", '27433400'))
    API_HASH = os.environ.get("API_HASH", '1a286620de5ffe0a7d9b57e604293555')
    AUTH_USER = os.environ.get('AUTH_USERS', '6201066540').split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
    HOST = "https://drm-api-six.vercel.app"
    CREDIT = "Obito™"#Here You Can Change with Your Name  or any custom name or title you prefer


