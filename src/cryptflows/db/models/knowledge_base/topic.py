# src/cryptflows/db/models/knowledge_base/topic.py
from __future__ import annotations

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ...database import KnowledgeBaseBase

class Topic(KnowledgeBaseBase):
    __tablename__ = "topic"
    name: Mapped[str] = mapped_column(String(length=100), nullable=False)
    description: Mapped[str] = mapped_column(String(length=255), nullable=True)
    category_id: Mapped[int] = mapped_column(ForeignKey("category.id"), nullable=False)
    
    category = relationship("Category", back_populates="topics")
