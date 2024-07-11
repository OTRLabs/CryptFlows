from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from advanced_alchemy.base import UUIDAuditBase
if TYPE_CHECKING:
    from .project_role import ProjectRole
    from .team import Team
    from .user import User
    from .user_role import UserRole


class Workflow(UUIDAuditBase):
    name = Column(String)
    description = Column(String)
    project_id = Column(UUID, ForeignKey("project.id"))
    project = relationship("Project", back_populates="workflows")
    project_roles = relationship("ProjectRole", back_populates="workflow")
    team_id = Column(UUID, ForeignKey("team.id"))