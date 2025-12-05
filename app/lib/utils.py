"""
All Utilities for the project
"""

from enum import Enum

class ServiceStatusType(Enum):
    Booked = "Booked"
    Accepted = "Accepted"
    Rejected = "Rejected"
    Inprogress = "Inprogress"
    Completed = "Completed"
    