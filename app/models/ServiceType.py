from sqlmodel import SQLModel, Field, Column, DateTime
from typing import Optional
from datetime import datetime

from app.models.common import IdCreateMixin, utcnow

class ServiceType(SQLModel, IdCreateMixin, table=True):
    __tablename__ = "service_type"
    service_type_name: str = Field(unique=True, index=True)
    service_type_description: Optional[str] = None
    is_active: bool = Field(default=True)
    update_date: datetime = Field(
        sa_column=Column(
        DateTime(timezone=True), default=utcnow, onupdate=utcnow, nullable=False
        )
    )