import os
import json
from dotenv import load_dotenv
load_dotenv()

CONFIG_FILE = 'config.json'
_config = {}
if CONFIG_FILE:
    with open(CONFIG_FILE, 'r') as configfile:
        _config = json.loads(configfile)

ENVIRONMENT = os.getenv('ENVIRONMENT', _config.get('ENVIRONMENT', None))
BASE_URL = os.getenv('BASE_URL', _config.get('BASE_URL', None))
CALLBACK_HOST = os.getenv('CALLBACK_HOST', _config.get('CALLBACK_HOST', None))
COLLECTION_PRIMARY_KEY = os.getenv('COLLECTION_PRIMARY_KEY', _config.get('COLLECTION_PRIMARY_KEY', None))
COLLECTION_USER_ID = os.getenv('COLLECTION_USER_ID', _config.get('COLLECTION_USER_ID', None))
COLLECTION_API_SECRET = os.getenv('COLLECTION_API_SECRET', _config.get('COLLECTION_API_SECRET', None))
