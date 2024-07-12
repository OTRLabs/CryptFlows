# src/cryptflows/db/models/knowledge_base/organization.py
from __future__ import annotations

from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from ...database import KnowledgeBaseBase

class Organization(KnowledgeBaseBase):
    __tablename__ = "organization"
    name: Mapped[str] = mapped_column(String(length=255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
