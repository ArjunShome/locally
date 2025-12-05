"""
Mixins and common code base which can be reutilized
"""

import uuid
from typing import Optional
from datetime import datetime, timezone

from sqlmodel import Field

def utcnow():
    """
    UDF for getting utcnow time
    """
    return datetime.now(timezone.utc)

# Base Model
class IdCreateMixin:  # pylint: disable=too-few-public-methods
    """
    Docstring for IdCreateMixin mixin class
    """
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, index=True)
    create_date: Optional[datetime] = Field(default_factory=utcnow)
