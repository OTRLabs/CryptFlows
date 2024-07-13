# src/cryptflows/db/models/knowledge_base/software.py
from __future__ import annotations

from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ...database import KnowledgeBaseBase

class Software(KnowledgeBaseBase):
    __tablename__ = "software"
    name: Mapped[str] = mapped_column(String(length=255), nullable=False)
    version: Mapped[str] = mapped_column(String(length=50), nullable=True)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    host_id: Mapped[int] = mapped_column(ForeignKey("host.id"), nullable=False)
    
    host = relationship("Host", back_populates="software")
