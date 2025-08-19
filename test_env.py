from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv("HUBSPOT_ACCESS_TOKEN")
secret = os.getenv("SECRET_KEY")

print(f"Token starts with: {token[:15]}..." if token else "No token found")
print(f"Secret key loaded: {'Yes' if secret else 'No'}")