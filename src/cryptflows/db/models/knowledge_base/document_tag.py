from sqlalchemy import Table, Column, ForeignKey
from ...database import KnowledgeBaseBase
_document_tag = Table(
    'document_tag',
    KnowledgeBaseBase.metadata,
    Column('document_id', ForeignKey('document.id'), primary_key=True),
    Column('tag_id', ForeignKey('tag.id'), primary_key=True)
)



class DocumentTag(KnowledgeBaseBase):
    __tablename__ = "document_tag"
    document_id = Column(ForeignKey("document.id"), primary_key=True)
    tag_id = Column(ForeignKey("tag.id"), primary_key=True)