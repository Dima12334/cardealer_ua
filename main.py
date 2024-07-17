from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config.settings.settings import ALLOWED_HOSTS, ALLOWED_METHODS, ALLOWED_HEADERS, ALLOW_CREDENTIALS

app = FastAPI(title="CarDealer.ua")


app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_HOSTS,
    allow_credentials=ALLOW_CREDENTIALS,
    allow_methods=ALLOWED_METHODS,
    allow_headers=ALLOWED_HEADERS,
)
