import uuid

from sqlmodel import SQLModel, Field, Column, DateTime
from datetime import datetime
from typing import Optional
from app.models.common import IdCreateMixin, utcnow


class UserBookedServiceFeedback(SQLModel, IdCreateMixin, table=True):
    __tablename__ = "user_booked_service_feedback"
    user_booked_service_id: uuid.UUID = Field(default_factory=uuid.uuid4, foreign_key="user_booked_service.id")
    feedback: Optional[str] = None
    rating: int = Field(gt=0, lt=6)
    update_date: datetime = Field(
        sa_column=Column(
        DateTime(timezone=True), default=utcnow, onupdate=utcnow, nullable=False
        )
    )