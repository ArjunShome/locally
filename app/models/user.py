"""
DB table for User
"""
from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel, Field, DateTime, Column

from app.models.common import IdCreateMixin, utcnow

# User table

class User(SQLModel, IdCreateMixin, table=True):
    """
    User DB table definition
    """
    __tablename__ = "user"
    first_name: str
    last_name: str
    email: str = Field(unique=True, index=True)
    username: str = Field(unique=True, index=True)
    password: str
    contact_number: Optional[int] = None
    age: Optional[int] = None
    is_active: bool = Field(default=True)
    update_date: datetime = Field(
        sa_column=Column(
        DateTime(timezone=True), default=utcnow, onupdate=utcnow, nullable=False
        )
    )
