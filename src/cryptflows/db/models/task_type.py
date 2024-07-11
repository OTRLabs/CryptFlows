from __future__ import annotations

from typing import TYPE_CHECKING

from advanced_alchemy.base import UUIDAuditBase
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy_utils.types import ChoiceType
from sqlalchemy_utils.types.encrypted.encrypted_type import EncryptedType
from sqlalchemy.ext.associationproxy import AssociationProxy, association_proxy


if TYPE_CHECKING:
    from .project_role import ProjectRole
    from .team import Team
    from .user import User
    from .user_role import UserRole


class TaskType(UUIDAuditBase):
    """Task Type."""

    name: str
    slug: str
    description: str
    project_role: Mapped[ProjectRole] = relationship(
        back_populates="task_types", innerjoin=True, uselist=False, lazy="joined"
    )
    project_role_name: AssociationProxy[str] = association_proxy("project_role", "name")