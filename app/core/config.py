from pydantic_settings import BaseSettings
from typing import List, Optional
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    # Application
    app_name: str = "HubSpot API Integration"
    app_env: str = "development"
    app_host: str = "0.0.0.0"
    app_port: int = 8000
    
    # HubSpot
    hubspot_access_token: str
    
    # Database
    database_url: Optional[str] = None
    database_pool_size: Optional[int] = 10
    database_max_overflow: Optional[int] = 20
    
    # Redis
    redis_url: Optional[str] = None
    redis_password: Optional[str] = ""
    
    # Security
    secret_key: str
    access_token_expire_minutes: int = 30
    refresh_token_expire_days: Optional[int] = 7
    
    # Logging
    log_level: str = "INFO"
    log_file: str = "logs/app.log"
    
    # CORS
    cors_origins: List[str] = ["http://localhost:3000", "http://localhost:8000"]
    
    # Webhook
    webhook_secret: Optional[str] = None
    
    class Config:
        env_file = ".env"
        extra = "allow"

settings = Settings()