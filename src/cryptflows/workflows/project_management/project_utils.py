from __future__ import annotations
import os
from typing import Dict, List, Any

import json
import logging
import pika
from datetime import datetime
from ...configs.config import Config
from .project_models import Base, Project, Task, ProjectRepository, TaskRepository
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def init_project_db_session():
    db_path = 'project_management.db'
    engine = create_engine(f'duckdb:///{db_path}')
    session = None
    try:
        if not os.path.exists(db_path):
            logging.info(f'Creating database at {db_path}')
            Base.metadata.create_all(engine)
        else:
            logging.info(f'Reading from database at {db_path}')
        Session = sessionmaker(bind=engine)
        session = Session()
    except Exception as e:
        logging.error(f'Error initializing project database session: {e}')
        raise e
    return session


# Project management functions
def create_project(session: sessionmaker, name: str, description: str):
    project = Project(name=name, description=description)
    session.add(project)
    session.commit()
    session.refresh(project)
    return project

def get_projects(session: sessionmaker) -> List[Project]:
    projects = session.query(Project).all()
    session.close()
    return projects

def add_task_to_project(session: sessionmaker, project_id: int, task_name: str, description: str, queue: str) -> None:
    task = Task(project_id=project_id, title=task_name, description=description, completed=0)
    session.add(task)
    session.commit()
    session.refresh(task)
    session.close()


def get_tasks_for_project(session: sessionmaker, project_id: int):
    tasks = session.query(Task).filter_by(project_id=project_id).all()
    session.close()
    return tasks


# Task queue management functions
def send_task_to_queue(session: sessionmaker, project_id: int, task_id: int) -> None:
    
    print(f"Sending task: {task_id}")
    task = session.query(Task).filter_by(id=task_id).first()
    task.completed = 1
    session.commit()
    
    print(f"Task sent: {task_id}")
    session.close()
    
    # Send the task to the queue
    task_data = {"id": task_id, "project_id": project_id}
    send_task_to_queue(task_data)
    
    
    
    
def consume_task_from_queue(task_data: dict) -> None:
    print(f"Consuming task: {task_data}")
    task_id = task_data["id"]
    project_id = task_data["project_id"]
    send_task_to_queue(project_id, task_id)
    # TODO: make sure the task is removed from the queue when completed
    print(f"Task consumed: {task_data}")
    
    