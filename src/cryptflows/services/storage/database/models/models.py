from __future__ import annotations
from advanced_alchemy.base import UUIDBase
from advanced_alchemy.filters import LimitOffset
from advanced_alchemy.repository import SQLAlchemySyncRepository
from typing import TYPE_CHECKING
from sqlalchemy import Column, Integer, String, ForeignKey, Sequence, create_engine
from sqlalchemy.orm import relationship, declarative_base, sessionmaker
from .....configs.config import Config

# Define your base model
Base = declarative_base()

# Define your models
class Project(Base):
    __tablename__ = 'projects'
    
    id = Column(Integer, Sequence('project_id_seq'), primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    start_date = Column(String, nullable=False)
    end_date = Column(String)
    status = Column(String, nullable=False)
    scope = Column(String)
    
    tasks = relationship('Task', back_populates='project', cascade='all, delete-orphan')

class Task(Base):
    __tablename__ = 'tasks'
    
    id = Column(Integer, Sequence('task_id_seq'), primary_key=True)
    project_id = Column(Integer, ForeignKey('projects.id'), nullable=False)
    title = Column(String, nullable=False)
    description = Column(String)
    completed = Column(Integer, nullable=False, default=0)
    
    project = relationship('Project', back_populates='tasks')
