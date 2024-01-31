from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from src.models.Payloads import ItemModel
from src.managers.item_manager import ItemManager
from src.managers.database_manager import get_db_session
from src.authenticate.jwt_authenticate import authenticate_jwt
from src.error_handlers.error_handler import error_handler

router = APIRouter()


@router.get("/health")
def read_health():
    return JSONResponse({}, status_code=200)


@error_handler
@router.post("/item")
def post_item(
    item: ItemModel,
    db_session: Session = Depends(get_db_session),
    jwt_token: str = Depends(authenticate_jwt)
):

    return ItemManager.create_item(db_session, item.name)
