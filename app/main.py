from app.services.hubspot_service import hubspot_service
from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(title=settings.app_name)

@app.get("/")
async def root():
    return {
        "message": "HubSpot API Integration",
        "status": "running"
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/api/test-hubspot")
async def test_hubspot_connection():
    return hubspot_service.test_connection()