from src.models.Configuration import Configuration
import os


def parse_config():
    return Configuration(
        DATABASE_URL=os.environ.get("DATABASE_URL"),
        JWT_SECRET=os.environ.get("JWT_SECRET"))


CONFIG = parse_config()
