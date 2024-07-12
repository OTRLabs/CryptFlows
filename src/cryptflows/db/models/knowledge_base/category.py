# src/cryptflows/db/models/knowledge_base/category.py
from __future__ import annotations

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from ...database import KnowledgeBaseBase

class Category(KnowledgeBaseBase):
    __tablename__ = "category"
    name: Mapped[str] = mapped_column(String(length=100), unique=True, nullable=False)
    description: Mapped[str] = mapped_column(String(length=255), nullable=True)
