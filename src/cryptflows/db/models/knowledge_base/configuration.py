# src/cryptflows/db/models/knowledge_base/configuration.py
from __future__ import annotations

from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from ...database import KnowledgeBaseBase

class Configuration(KnowledgeBaseBase):
    __tablename__ = "configuration"
    key: Mapped[str] = mapped_column(String(length=255), nullable=False)
    value: Mapped[str] = mapped_column(Text, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
