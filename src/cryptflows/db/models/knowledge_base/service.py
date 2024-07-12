# src/cryptflows/db/models/knowledge_base/service.py
from __future__ import annotations

from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ...database import KnowledgeBaseBase

class Service(KnowledgeBaseBase):
    __tablename__ = "service"
    name: Mapped[str] = mapped_column(String(length=255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    port: Mapped[int] = mapped_column(nullable=False)
    protocol: Mapped[str] = mapped_column(String(length=10), nullable=False)
    host_id: Mapped[int] = mapped_column(ForeignKey("host.id"), nullable=False)
    
    host = relationship("Host", back_populates="services")
