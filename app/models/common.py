import uuid

from sqlmodel import Field
from typing import Optional
from datetime import datetime, timezone

def utcnow():
    return datetime.now(timezone.utc)

# Base Model
class IdCreateMixin:
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, index=True)
    create_date: Optional[datetime] = Field(default_factory=utcnow)