# src/cryptflows/db/models/knowledge_base/hardware.py
from __future__ import annotations

from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ...database import KnowledgeBaseBase

class Hardware(KnowledgeBaseBase):
    __tablename__ = "hardware"
    type: Mapped[str] = mapped_column(String(length=255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    host_id: Mapped[int] = mapped_column(ForeignKey("host.id"), nullable=False)
    
    host = relationship("Host", back_populates="hardware")
