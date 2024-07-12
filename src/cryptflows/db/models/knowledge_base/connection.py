# src/cryptflows/db/models/knowledge_base/connection.py
from __future__ import annotations

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ...database import KnowledgeBaseBase

class Connection(KnowledgeBaseBase):
    __tablename__ = "connection"
    from_entity_id: Mapped[int] = mapped_column(ForeignKey("entity.id"), nullable=False)
    to_entity_id: Mapped[int] = mapped_column(ForeignKey("entity.id"), nullable=False)
    
    from_entity = relationship("Entity", foreign_keys=[from_entity_id])
    to_entity = relationship("Entity", foreign_keys=[to_entity_id])
