 # HubSpot API Integration

A production-ready Python API for integrating with HubSpot CRM using FastAPI.

## Features

- 🔐 OAuth 2.0 authentication flow
- 📊 Full CRUD operations for Contacts, Companies, and Deals
- 🔄 Automatic token refresh
- 🪝 Webhook support for real-time updates
- 📝 Comprehensive logging
- 🐳 Docker support
- 🧪 Unit and integration tests
- 📚 OpenAPI documentation

## Tech Stack

- **FastAPI** - Modern Python web framework
- **HubSpot API Client** - Official Python SDK
- **PostgreSQL** - Primary database
- **Redis** - Token storage and caching
- **SQLAlchemy** - ORM
- **Alembic** - Database migrations

## Quick Start

### Prerequisites

- Python 3.9+
- PostgreSQL 13+
- Redis 6+
- HubSpot Developer Account

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/hubspot-api-integration.git
cd hubspot-api-integration
