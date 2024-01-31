from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.managers.config_manager import CONFIG

metadata = MetaData()
Base = declarative_base(metadata=metadata)


class DatabaseManager:
    _instance = None  # Class variable to store the instance

    def __init__(self, database_url: str):
        self.engine = create_engine(database_url)
        self.metadata = MetaData()
        self.SessionLocal = sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=self.engine)
        Base.metadata.create_all(bind=self.engine)

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls(CONFIG.DATABASE_URL)
        return cls._instance


def get_db_session():
    db = DatabaseManager.get_instance().SessionLocal()
    try:
        yield db
    finally:
        db.close()
