# src/cryptflows/db/models/knowledge_base/media.py
from __future__ import annotations

from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from ...database import KnowledgeBaseBase

class Media(KnowledgeBaseBase):
    __tablename__ = "media"
    title: Mapped[str] = mapped_column(String(length=255), nullable=False)
    type: Mapped[str] = mapped_column(String(length=50), nullable=False)
    url: Mapped[str] = mapped_column(String(length=2083), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
