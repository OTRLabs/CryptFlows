# src/cryptflows/db/models/knowledge_base/network.py
from __future__ import annotations

from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from ...database import KnowledgeBaseBase

class Network(KnowledgeBaseBase):
    __tablename__ = "network"
    name: Mapped[str] = mapped_column(String(length=255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    cidr: Mapped[str] = mapped_column(String(length=18), nullable=False)  # CIDR notation, e.g., 192.168.0.0/24
