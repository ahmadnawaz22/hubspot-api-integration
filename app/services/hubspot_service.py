from hubspot import HubSpot
from app.core.config import settings

class HubSpotService:
    def __init__(self):
        self.client = HubSpot(access_token=settings.hubspot_access_token)
    
    def test_connection(self):
        """Test if HubSpot connection works"""
        try:
            response = self.client.crm.contacts.basic_api.get_page(limit=1)
            return {
                "status": "connected", 
                "message": "Successfully connected to HubSpot",
                "test": "Retrieved contacts successfully"
            }
        except Exception as e:
            return {"status": "error", "message": str(e)}
    
    def get_contacts(self, limit=100):
        """Get contacts from HubSpot"""
        try:
            response = self.client.crm.contacts.basic_api.get_page(limit=limit)
            contacts = []
            for contact in response.results:
                contacts.append({
                    "id": contact.id,
                    "email": contact.properties.get("email"),
                    "firstname": contact.properties.get("firstname"),
                    "lastname": contact.properties.get("lastname"),
                    "company": contact.properties.get("company"),
                    "phone": contact.properties.get("phone"),
                    "city": contact.properties.get("city"),
                    "created_date": contact.created_at,
                    "last_modified": contact.updated_at
                })
            return {"status": "success", "count": len(contacts), "contacts": contacts}
        except Exception as e:
            return {"status": "error", "message": str(e)}
    
    def get_companies(self, limit=100):
        """Get companies from HubSpot"""
        try:
            response = self.client.crm.companies.basic_api.get_page(limit=limit)
            companies = []
            for company in response.results:
                companies.append({
                    "id": company.id,
                    "name": company.properties.get("name"),
                    "domain": company.properties.get("domain"),
                    "city": company.properties.get("city"),
                    "industry": company.properties.get("industry"),
                    "created_date": company.created_at
                })
            return {"status": "success", "count": len(companies), "companies": companies}
        except Exception as e:
            return {"status": "error", "message": str(e)}
    
    def get_deals(self, limit=100):
        """Get deals from HubSpot"""
        try:
            response = self.client.crm.deals.basic_api.get_page(limit=limit)
            deals = []
            for deal in response.results:
                deals.append({
                    "id": deal.id,
                    "dealname": deal.properties.get("dealname"),
                    "amount": deal.properties.get("amount"),
                    "dealstage": deal.properties.get("dealstage"),
                    "closedate": deal.properties.get("closedate"),
                    "pipeline": deal.properties.get("pipeline"),
                    "created_date": deal.created_at
                })
            return {"status": "success", "count": len(deals), "deals": deals}
        except Exception as e:
            return {"status": "error", "message": str(e)}
    
    def get_pipelines(self):
        """Get all pipelines"""
        try:
            response = self.client.crm.pipelines.pipelines_api.get_all(object_type="deals")
            pipelines = []
            for pipeline in response.results:
                stages = []
                for stage in pipeline.stages:
                    stages.append({
                        "id": stage.id,
                        "label": stage.label,
                        "display_order": stage.display_order
                    })
                pipelines.append({
                    "id": pipeline.id,
                    "label": pipeline.label,
                    "stages": stages
                })
            return {"status": "success", "pipelines": pipelines}
        except Exception as e:
            return {"status": "error", "message": str(e)}

# Create singleton instance
hubspot_service = HubSpotService()