import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", '8225118430:AAEOFTRcVH3Au1LR0iFyasUb4U5CGATuoT4')
    API_ID = int(os.environ.get("API_ID", '22447622'))
    API_HASH = os.environ.get("API_HASH", '543b62d58d3e723e766ba57a984ab65d')
    AUTH_USER = os.environ.get('AUTH_USERS', '777756062').split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
    HOST = "https://drm-api-six.vercel.app"
    CREDIT = "Obito™"#Here You Can Change with Your Name  or any custom name or title you prefer



