from fastapi import APIRouter

user_routes = APIRouter()


# APIs
@user_routes.get("/ping")
async def ping():
    return {"message": "pong"} 
