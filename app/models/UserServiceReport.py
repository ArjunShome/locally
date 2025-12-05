"""
DB Table for user service report
"""

import uuid
from datetime import datetime
from sqlmodel import SQLModel, Field, Column, DateTime
from app.models.common import IdCreateMixin, utcnow


class UserServiceReport(SQLModel, IdCreateMixin, table=True):
    __tablename__ = "user_service_report"
    user_id: uuid.UUID = Field(default_factory=uuid.uuid4, foreign_key="user.id")
    service_id: uuid.UUID = Field(default_factory=uuid.uuid4, foreign_key="service.id")
    report_file_url: str = Field(nullable=False)
    update_date: datetime = Field(
        sa_column=Column(
        DateTime(timezone=True), default=utcnow, onupdate=utcnow, nullable=False
        )
    )