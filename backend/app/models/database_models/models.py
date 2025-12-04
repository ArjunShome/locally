import uuid

from sqlmodel import Field
from typing import Optional

from app.lib.utils import ServiceStatusType
from app.models.database_models.base_model import BaseModel

# User table

class User(BaseModel, table=True):
    first_name: str
    last_name: str
    email: str = Field(unique=True, index=True)
    username: str = Field(unique=True, index=True)
    password: str
    contact_number: Optional[int] = None
    age: Optional[int] = None
    is_active: bool = Field(default=True)
    
    
    
# Service Tables

class ServiceType(BaseModel, table=True):
    service_type_name: str = Field(unique=True, index=True)
    service_type_description: Optional[str] = None
    is_active: bool = Field(default=True)

class Service(BaseModel, table=True):
    owner_id: uuid.UUID = Field(default_factory=uuid.uuid4, foreign_key="user.id")
    service_type_id: uuid.UUID = Field(default_factory=uuid.uuid4, foreign_key="servicetype.id")    
    service_name: str = Field(unique=True, index=True)
    service_description: Optional[str] = None
    service_contact_number: Optional[int] = None
    service_latitude: float = Field(nullable=False)
    service_longitude: float = Field(nullable=False)
    service_city: Optional[str] = None
    servcice_state: Optional[str] = None
    is_active: bool = Field(default=True)
    
    
    
# User Service association tables

class UserBookedService(BaseModel, table=True):
    user_id: uuid.UUID = Field(default_factory=uuid.uuid4, foreign_key="user.id")
    service_id: uuid.UUID = Field(default_factory=uuid.uuid4, foreign_key="service.id")
    serice_status: ServiceStatusType = Field(default_factory=ServiceStatusType.Booked)
    
class UserBookedServiceFeedback(BaseModel, table=True):
    user_booked_service_id: uuid.UUID = Field(default_factory=uuid.uuid4, foreign_key="userbookedservice.id")
    feedback: Optional[str] = None
    rating: int = Field(gt=0, lt=6)
    
class UserServiceReport(BaseModel, table=True):
    user_id: uuid.UUID = Field(default_factory=uuid.uuid4, foreign_key="user.id")
    service_id: uuid.UUID = Field(default_factory=uuid.uuid4, foreign_key="service.id")
    report_file_url: str = Field(nullable=False)