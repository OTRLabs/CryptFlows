# src/cryptflows/db/models/knowledge_base/person.py
from __future__ import annotations

from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from ...database import KnowledgeBaseBase

class Person(KnowledgeBaseBase):
    __tablename__ = "person"
    name: Mapped[str] = mapped_column(String(length=255), nullable=False)
    bio: Mapped[str] = mapped_column(Text, nullable=True)
