import uuid

from sqlmodel import SQLModel, Field, Column, DateTime
from datetime import datetime, timezone


# Base Model
class BaseModel(SQLModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, index=True)
    create_date: datetime = Field(default_factory=timezone.utc)
    update_date: datetime = Field(
                                sa_column=Column(
                                DateTime, default=timezone.utc, onupdate=timezone.utc, nullable=False
                                )
                            )