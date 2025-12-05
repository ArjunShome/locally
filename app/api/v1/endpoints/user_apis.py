"""
Endpoints for User APIS
"""

from fastapi import APIRouter

user_routes = APIRouter()


# APIs
@user_routes.get("/ping")
async def ping():
    """
    Check application health
    """
    return {"message": "pong"}
