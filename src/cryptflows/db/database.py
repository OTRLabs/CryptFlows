# db/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from config.base import DATABASES

# Create engines
default_engine = create_engine(DATABASES["default"])
knowledge_base_engine = create_engine(DATABASES["knowledge_base"])

# Create session makers
DefaultSession = sessionmaker(bind=default_engine)
KnowledgeBaseSession = sessionmaker(bind=knowledge_base_engine)

# Base classes
DefaultBase = declarative_base()
KnowledgeBaseBase = declarative_base()
