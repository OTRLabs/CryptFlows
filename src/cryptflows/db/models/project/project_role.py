from __future__ import annotations

from typing import TYPE_CHECKING

from advanced_alchemy.base import UUIDAuditBase
from sqlalchemy import ForeignKey, UUID, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.schema import UniqueConstraint
from datetime import datetime, UTC



if TYPE_CHECKING:
    from ..base.project import Project
    from ..base.user import User
    from ..user.user_role import UserRole
    from ..base.role import Role

class ProjectRole(UUIDAuditBase):
    __tablename__ = "project_role"
    __table_args__ = (
        UniqueConstraint("project_id", "role_id"),
        {"comment": "Links a project to a specific role."},
    )

    project_id: Mapped[UUID] = mapped_column(ForeignKey("project.id", ondelete="cascade"), nullable=False)
    role_id: Mapped[UUID] = mapped_column(ForeignKey("role.id", ondelete="cascade"), nullable=False)
    assigned_at: Mapped[datetime] = mapped_column(default=datetime.now(UTC))
    project: Mapped[Project] = relationship(back_populates="roles", innerjoin=True, uselist=False, lazy="joined")
    role: Mapped[Role] = relationship(back_populates="projects", innerjoin=True, uselist=False, lazy="joined")
    