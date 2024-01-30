from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.managers.config_manager import CONFIG

metadata = MetaData()
Base = declarative_base(metadata=metadata)


class DatabaseManager:
    def __init__(self, database_url: str):
        self.engine = create_engine(database_url)
        self.metadata = MetaData()
        self.SessionLocal = sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=self.engine)
        Base.metadata.create_all(bind=self.engine)


database_manager = DatabaseManager(CONFIG.DATABASE_URL)


def get_db_session():
    db = database_manager.SessionLocal()
    try:
        yield db
    finally:
        db.close()
