from sqlalchemy.orm import Session
from src.models.Tables import Items
import uuid


class ItemDAO:
    def create_item(db_session: Session,  name: str,  id: uuid.UUID):
        with db_session as db:
            new_item = Items(name=name, id=id)
            db.add(new_item)
            db.commit()
            db.refresh(new_item)
            return new_item

    def get_item_by_id(db_session: Session, item_id: uuid.UUID):
        with db_session as db:
            item = db.query(Items).filter(Items.id == item_id).first()
            return item
