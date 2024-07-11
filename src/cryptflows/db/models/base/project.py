from __future__ import annotations

from typing import TYPE_CHECKING

from advanced_alchemy.base import UUIDAuditBase
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
#from sqlalchemy_utils.types import ChoiceType
#from sqlalchemy_utils.types.encrypted.encrypted_type import SlugKey



if TYPE_CHECKING:
    from ..project.project_status import ProjectStatus
    from .team import Team
    from .user import User
    from ..user.user_role import UserRole

class Project(UUIDAuditBase):
    __tablename__ = "project"
    name: Mapped[str] = mapped_column(String(length=255), nullable=False)
    #slug: Mapped[str] = mapped_column(SlugKey(length=50), nullable=False, index=True)
    description: Mapped[str] = mapped_column(String(length=255), nullable=True)