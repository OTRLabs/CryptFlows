# src/cryptflows/db/models/knowledge_base/entity.py
from __future__ import annotations

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from ...database import KnowledgeBaseBase

class Entity(KnowledgeBaseBase):
    __tablename__ = "entity"
    entity_type: Mapped[str] = mapped_column(String(length=50), nullable=False)
    name: Mapped[str] = mapped_column(String(length=255), nullable=False)
