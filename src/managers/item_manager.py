from sqlalchemy.orm import Session
from src.dao.item import ItemDAO
import uuid


class ItemManager:
    def create_item(db_session: Session,  name: str):
        return ItemDAO.create_item(db_session, name, uuid.uuid4())

    def get_item_by_id(db_session: Session, item_id: uuid.UUID):
        return ItemDAO.get_item_by_id(db_session, item_id)
