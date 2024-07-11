from __future__ import annotations

from typing import TYPE_CHECKING

from advanced_alchemy.base import SlugKey, UUIDAuditBase
from sqlalchemy import ForeignKey, String, UUID
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy_utils.types import ChoiceType
from sqlalchemy_utils.types.encrypted.encrypted_type import SlugKey
from sqlalchemy_utils.types.encrypted.encrypted_type import EncryptedType



if TYPE_CHECKING:
    from .project import Project
    from ..task.task_status import TaskStatus
    from ..task.task_type import TaskType
    from .user import User
    from ..user_role import UserRole
    from ..workflow import Workflow




class Task(UUIDAuditBase):
    __tablename__ = "task"

    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(String(2048), nullable=True)
    project_id: Mapped[UUID] = mapped_column(ForeignKey("project.id", ondelete="CASCADE"), nullable=False)
    workflow_id: Mapped[UUID] = mapped_column(ForeignKey("workflow.id", ondelete="CASCADE"), nullable=False)
    status: Mapped[TaskStatus] = mapped_column(
        String(length=50),
        default=TaskStatus.QUEUED,
        #nullable=False,
        index=True,
    )
    task_type: Mapped[TaskType] = mapped_column(
        String(length=50),

    )