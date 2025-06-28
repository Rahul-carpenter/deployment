import os
from dotenv import load_dotenv

# Load environment variables early
load_dotenv()

class Config:
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST")
    DB_NAME = os.getenv("DB_NAME")

    if not all([DB_USER, DB_PASSWORD, DB_HOST, DB_NAME]):
        raise RuntimeError("Missing one or more environment variables.")

    SQLALCHEMY_DATABASE_URI = (
        f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
