# src/cryptflows/db/models/knowledge_base/ip_address.py
from __future__ import annotations

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ...database import KnowledgeBaseBase

class IPAddress(KnowledgeBaseBase):
    __tablename__ = "ip_address"
    address: Mapped[str] = mapped_column(String(length=45), nullable=False, unique=True)  # IPv4 and IPv6 compatible
    host_id: Mapped[int] = mapped_column(ForeignKey("host.id"), nullable=True)
    
    host = relationship("Host", back_populates="ip_addresses")
