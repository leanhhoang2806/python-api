from pydantic import BaseModel


class Configuration(BaseModel):
    DATABASE_URL: str
    JWT_SECRET: str
