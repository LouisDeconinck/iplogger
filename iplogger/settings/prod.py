from .base import *
import dj_database_url
import os
from dotenv import load_dotenv
load_dotenv()

DEBUG = False
ALLOWED_HOSTS = ['127.0.0.1']

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

DATABASES = {
	"default": dj_database_url.parse(os.environ.get("DB_EXT_URL"))
}
