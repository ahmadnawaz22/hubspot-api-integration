from fastapi import FastAPI
from app.core.config import settings
from app.services.hubspot_service import hubspot_service

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

@app.get("/api/contacts")
async def get_contacts(limit: int = 10):
    return hubspot_service.get_contacts(limit=limit)

@app.get("/api/companies")
async def get_companies(limit: int = 10):
    return hubspot_service.get_companies(limit=limit)

@app.get("/api/deals")
async def get_deals(limit: int = 10):
    return hubspot_service.get_deals(limit=limit)

@app.get("/api/pipelines")
async def get_pipelines():
    return hubspot_service.get_pipelines()