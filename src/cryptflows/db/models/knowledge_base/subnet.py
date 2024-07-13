# src/cryptflows/db/models/knowledge_base/subnet.py
from __future__ import annotations

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ...database import KnowledgeBaseBase

class Subnet(KnowledgeBaseBase):
    __tablename__ = "subnet"
    cidr: Mapped[str] = mapped_column(String(length=18), nullable=False)  # CIDR notation, e.g., 192.168.1.0/24
    network_id: Mapped[int] = mapped_column(ForeignKey("network.id"), nullable=False)
    
    network = relationship("Network", back_populates="subnets")
