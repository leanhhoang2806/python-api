from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2AuthorizationCodeBearer
from src.managers.config_manager import CONFIG
import jwt

oauth2_scheme = OAuth2AuthorizationCodeBearer(
    tokenUrl="token",
    authorizationUrl="authorize"
)


def authenticate_jwt(token: str = Depends(oauth2_scheme)) -> str:
    try:
        decoded_token = jwt.decode(
            token,
            CONFIG.JWT_SECRET,
            algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return decoded_token
