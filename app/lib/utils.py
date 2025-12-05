"""
All Utilities for the project
"""

from enum import Enum

class ServiceStatusType(Enum):
    """
    Docstring for ServiceStatusType
    """
    BOOKED = "Booked"
    ACCEPTED = "Accepted"
    INPROGRESS = "Inprogress"
    COMPLETED = "Completed"

