from __future__ import annotations

from enum import Enum
from typing import TYPE_CHECKING


class ProjectStatus(str, Enum):
    """Project Status."""

    active = "active"
    deleted = "deleted"
    paused = "paused"
    planned = "planned"
    suspended = "suspended"
    inactive = "inactive"

    def __str__(self) -> str:
        return self.value
