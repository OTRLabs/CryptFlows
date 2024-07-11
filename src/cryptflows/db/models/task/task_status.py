from __future__ import annotations
from typing import TYPE_CHECKING
from enum import Enum

class TaskStatus(str, Enum):
    """
    Task Status
    """
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    CANCELLED = "CANCELLED"

    if TYPE_CHECKING:
        def __str__(self) -> str:
            return super().__str__()
        