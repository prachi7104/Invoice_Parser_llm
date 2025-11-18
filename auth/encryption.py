import os
import base64
from dotenv import load_dotenv
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

load_dotenv()  # Loads .env variables

# Salt must be secret, random, and consistent -> stored in .env
SALT = os.getenv("ENCRYPTION_SALT", None)

if SALT is None:
    raise ValueError("ENCRYPTION_SALT not set in environment variables.")

SALT = SALT.encode()

def get_user_fernet_key(username: str) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=b"",
        iterations=390000,
    )
    return base64.urlsafe_b64encode(kdf.derive(username.encode()))
