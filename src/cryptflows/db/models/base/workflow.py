from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from advanced_alchemy.base import UUIDAuditBase
if TYPE_CHECKING:
    from ..base.team import Team
    from .user import User
    from ..user.user_role import UserRole
    from ..base.project import Project
    
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import MetaData
from sqlalchemy.types import CHAR, Integer, TypeDecorator, VARCHAR
from advanced_alchemy.base import UUIDAuditBase
from typing import Any, Optional
from uuid import UUID
from sqlalchemy import Column, ForeignKey, String



class Workflow(UUIDAuditBase):
    name: Mapped[str] = Column(String)
    description: Mapped[str | None] = mapped_column(String(length=500), nullable=True, default=None)
    workflow_type: Mapped[str] = Column(String)
    project_id: Mapped[UUID] = Column(UUID, ForeignKey("project.id"))
    project: Mapped[Project | None] = relationship("Project", back_populates="workflows")
    project_roles: Mapped[list[ProjectRole]] = relationship("ProjectRole", back_populates="workflow")
    team_id: Mapped[UUID | None] = Column(UUID, ForeignKey("team.id"))

