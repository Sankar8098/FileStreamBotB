from os import environ as env

class Telegram:
    API_ID = env.get("TELEGRAM_API_ID", 23990433)
    API_HASH = env.get("TELEGRAM_API_HASH", "e6c4b6ee1933711bc4da9d7d17e1eb20")
    OWNER_ID = int(env.get("OWNER_ID", 5821871362))
    ALLOWED_USER_IDS = env.get("ALLOWED_USER_IDS", "").split()
    BOT_USERNAME = env.get("TELEGRAM_BOT_USERNAME", "File_ToLinks_Bot")
    BOT_TOKEN = env.get("TELEGRAM_BOT_TOKEN", "5977289238:AAFUOFc0r9FHw0hPbNMmYvVjm_j2EyiH25k")
    CHANNEL_ID = int(env.get("TELEGRAM_CHANNEL_ID", -1001682397310))
    BOT_WORKERS = int(env.get("BOT_WORKERS", 10))
    SECRET_CODE_LENGTH = int(env.get("SECRET_CODE_LENGTH", 12))

class Server:
    BASE_URL = env.get("BASE_URL", "https://fwcge-219461eb25a1.herokuapp.com/")
    BIND_ADDRESS = env.get("BIND_ADDRESS", "0.0.0.0")
    PORT = int(env.get("PORT", 8080))

# LOGGING CONFIGURATION
LOGGER_CONFIG_JSON = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s][%(name)s][%(levelname)s] -> %(message)s',
            'datefmt': '%d/%m/%Y %H:%M:%S'
        },
    },
    'handlers': {
        'file_handler': {
            'class': 'logging.FileHandler',
            'filename': 'event-log.txt',
            'formatter': 'default'
        },
        'stream_handler': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        }
    },
    'loggers': {
        'uvicorn': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        },
        'uvicorn.error': {
            'level': 'WARNING',
            'handlers': ['file_handler', 'stream_handler']
        },
        'bot': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        }
    }
}
