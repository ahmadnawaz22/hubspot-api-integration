from hubspot import HubSpot
from app.core.config import settings

class HubSpotService:
    def __init__(self):
        self.client = HubSpot(access_token=settings.hubspot_access_token)
    
    def test_connection(self):
        """Test if HubSpot connection works"""
        try:
            # Try to get contacts to test connection
            response = self.client.crm.contacts.basic_api.get_page(limit=1)
            return {
                "status": "connected", 
                "message": "Successfully connected to HubSpot",
                "test": "Retrieved contacts successfully"
            }
        except Exception as e:
            return {"status": "error", "message": str(e)}

# Create singleton instance
hubspot_service = HubSpotService()