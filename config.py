import os
from dotenv import load_dotenv

load_dotenv()

# All sensitive values MUST come from environment variables
JWT_KEY = os.getenv("JWT_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
TESSERACT_CMD = os.getenv("TESSERACT_CMD")

# Optional local storage dir (safe default)
LOCAL_STORAGE_DIR = os.getenv("LOCAL_STORAGE_DIR", "invoices_data")

# Fail fast if critical variables are missing
if not JWT_KEY:
    raise ValueError("JWT_KEY is not set. Please add it to your .env file.")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set. Please add it to your .env file.")
