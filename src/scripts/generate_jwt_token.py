import jwt
from datetime import datetime, timedelta

# Secret key
secret_key = "my-super-secret"

# Payload (claims)
payload = {
    "sub": "user123",  # Subject (typically a user identifier)
    "exp": datetime.utcnow() + timedelta(days=1),  # Expiration time (1 day from now)
    "iat": datetime.utcnow(),  # Issued at time
}

# Generate JWT token
token = jwt.encode(payload, secret_key, algorithm="HS256")

print("Generated JWT token:", token)
