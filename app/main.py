"""
Main startup of the Application
"""

import uvicorn

from fastapi import FastAPI

from app.api import login_routes
from app.api import report_routes
from app.api import user_routes

# Creation of the application
app = FastAPI(title="Backend APIs for Locally.")

# Add all the application Routes
app.include_router(login_routes, prefix="/login", tags=["Login"])
app.include_router(report_routes, prefix="/report", tags=["Report"])
app.include_router(user_routes, prefix="/user", tags=["User"])

# Add all application middlewares
# app.add_middleware()



def main():
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    main()
