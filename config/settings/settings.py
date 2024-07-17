import os

from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")
DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

DB_HOST_TEST = os.environ.get("DB_HOST_TEST")
DB_PORT_TEST = os.environ.get("DB_PORT_TEST")
DB_NAME_TEST = os.environ.get("DB_NAME_TEST")
DB_USER_TEST = os.environ.get("DB_USER_TEST")
DB_PASS_TEST = os.environ.get("DB_PASS_TEST")

REDIS_CACHE_URL = os.environ.get("REDIS_CACHE_URL")
CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL")

SECRET_AUTH = os.environ.get("SECRET_AUTH")

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS")
ALLOWED_METHODS = os.environ.get("ALLOWED_METHODS")
ALLOWED_HEADERS = os.environ.get("ALLOWED_HEADERS")
ALLOW_CREDENTIALS = os.environ.get("ALLOW_CREDENTIALS")

SMTP_USER = os.environ.get("SMTP_USER")
SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD")
