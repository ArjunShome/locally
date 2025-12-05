"""
Model for the Service DB table 
"""

import uuid
from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel, Field, Column, DateTime

from app.models.common import IdCreateMixin, utcnow

class Service(SQLModel, IdCreateMixin, table=True):
    """
    Service Table in Database
    """
    __tablename__ = "service"
    owner_id: uuid.UUID = Field(default_factory=uuid.uuid4, foreign_key="user.id")
    service_type_id: uuid.UUID = Field(default_factory=uuid.uuid4, foreign_key="service_type.id")
    service_name: str = Field(unique=True, index=True)
    service_description: Optional[str] = None
    service_contact_number: Optional[int] = None
    service_latitude: float = Field(nullable=False)
    service_longitude: float = Field(nullable=False)
    service_city: Optional[str] = None
    servcice_state: Optional[str] = None
    service_age: Optional[int] = None
    is_active: bool = Field(default=True)
    update_date: datetime = Field(
        sa_column=Column(
        DateTime(timezone=True), default=utcnow, onupdate=utcnow, nullable=False
        )
    )
