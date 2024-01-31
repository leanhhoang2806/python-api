import jwt
from datetime import datetime, timedelta

secret_key = "my-super-secret"

payload = {
    "sub": "user123",
    "exp": datetime.utcnow() + timedelta(days=1),
    "iat": datetime.utcnow(),
}

token = jwt.encode(payload, secret_key, algorithm="HS256")

print("Generated JWT token:", token)
