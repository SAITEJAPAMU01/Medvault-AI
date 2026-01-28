import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv

# Load the .env file from Backend directory
load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

# Get the key from the environment
key = os.getenv("MASTER_KEY")

# SAFETY CHECK: If the key is missing, stop and warn the user
if not key:
    raise ValueError("CRITICAL ERROR: MASTER_KEY not found in .env file! Please check Step 1 of the instructions.")

try:
    fernet = Fernet(key)
except Exception:
    raise ValueError("CRITICAL ERROR: MASTER_KEY is invalid. It must be a 32-byte URL-safe base64 string.")

def encrypt_medical_data(text: str):
    """Locks the data"""
    return fernet.encrypt(text.encode()).decode()

def decrypt_medical_data(encrypted_text: str):
    """Unlocks the data"""
    return fernet.decrypt(encrypted_text.encode()).decode()