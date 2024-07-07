from __future__ import annotations
from typing import TYPE_CHECKING
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy import Column, Integer, String, create_engine, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from advanced_alchemy import Base, Repository

# Define your base model

# Define your models
class Project(Base):
    __tablename__ = 'projects'
    
    id = Column(Integer, Sequence('project_id_seq'), primary_key=True)
    name = Column(String)
    description = Column(String)

class Task(Base):
    __tablename__ = 'tasks'
    
    id = Column(Integer, Sequence('task_id_seq'), primary_key=True)
    project_id = Column(Integer)
    title = Column(String)
    description = Column(String)
    completed = Column(Integer)

# Repositories for the models
class ProjectRepository(Repository[Project]):
    model_type = Project

class TaskRepository(Repository[Task]):
    model_type = Task
