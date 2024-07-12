from __future__ import annotations

from enum import Enum


class WorkflowStatus(Enum):
    active = "active"
    inactive = "inactive"
    deleted = "deleted"

    def __str__(self) -> str:
        return self.value