import uuid

from sqlmodel import SQLModel, Field, Column, DateTime
from datetime import datetime

from app.lib.utils import ServiceStatusType
from app.models.common import IdCreateMixin, utcnow

class UserBookedService(SQLModel, IdCreateMixin, table=True):
    __tablename__ = "user_booked_service"
    user_id: uuid.UUID = Field(default_factory=uuid.uuid4, foreign_key="user.id")
    service_id: uuid.UUID = Field(default_factory=uuid.uuid4, foreign_key="service.id")
    serice_status: ServiceStatusType = Field(default_factory=ServiceStatusType.Booked)
    update_date: datetime = Field(
        sa_column=Column(
        DateTime(timezone=True), default=utcnow, onupdate=utcnow, nullable=False
        )
    )