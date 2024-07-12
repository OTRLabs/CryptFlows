# src/cryptflows/db/models/knowledge_base/note.py
from __future__ import annotations

from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql.schema import ForeignKey

from ...database import KnowledgeBaseBase

class Note(KnowledgeBaseBase):
    __tablename__ = "note"
    title: Mapped[str] = mapped_column(String(length=255), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    topic_id: Mapped[int] = mapped_column(ForeignKey("topic.id"), nullable=True)

    topic = relationship("Topic", back_populates="notes")
