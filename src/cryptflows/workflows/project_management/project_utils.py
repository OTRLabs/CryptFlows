from __future__ import annotations
import os
import json
import logging
from datetime import datetime
from typing import List

import pika
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from ...configs.config import Config
from .project_models import Base, Project, Task, ProjectRepository, TaskRepository


# Initialize logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def init_project_db_session() -> Session:
    """Initialize and return a session for the project database."""
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
def create_project(session: Session, name: str, description: str) -> Project:
    """Create a new project and add it to the database."""
    try:
        project = Project(name=name, description=description)
        session.add(project)
        session.commit()
        session.refresh(project)
        logging.info(f'Project created: {project}')
        return project
    except Exception as e:
        session.rollback()
        logging.error(f'Error creating project: {e}')
        raise e


def get_projects(session: Session) -> List[Project]:
    """Retrieve all projects from the database."""
    try:
        projects = session.query(Project).all()
        logging.info(f'Retrieved projects: {projects}')
        return projects
    except Exception as e:
        logging.error(f'Error retrieving projects: {e}')
        raise e
    finally:
        session.close()


def add_task_to_project(session: Session, project_id: int, task_name: str, description: str, queue: str) -> Task:
    """Add a new task to a project."""
    try:
        task = Task(project_id=project_id, title=task_name, description=description, completed=0)
        session.add(task)
        session.commit()
        session.refresh(task)
        logging.info(f'Task added to project {project_id}: {task}')
        return task
    except Exception as e:
        session.rollback()
        logging.error(f'Error adding task to project: {e}')
        raise e
    finally:
        session.close()


def get_tasks_for_project(session: Session, project_id: int) -> List[Task]:
    """Retrieve all tasks for a specific project."""
    try:
        tasks = session.query(Task).filter_by(project_id=project_id).all()
        logging.info(f'Retrieved tasks for project {project_id}: {tasks}')
        return tasks
    except Exception as e:
        logging.error(f'Error retrieving tasks for project: {e}')
        raise e
    finally:
        session.close()


# Task queue management functions
def send_task_to_queue(session: Session, project_id: int, task_id: int) -> None:
    """Send a task to the queue."""
    try:
        task = session.query(Task).filter_by(id=task_id).first()
        if task:
            task.completed = 1
            session.commit()
            logging.info(f'Task marked as completed: {task_id}')
        else:
            logging.error(f'Task not found: {task_id}')
            return

        # Send the task to the queue
        task_data = {"id": task_id, "project_id": project_id}
        send_task_to_queue_message(task_data)
        logging.info(f'Task sent to queue: {task_data}')
    except Exception as e:
        session.rollback()
        logging.error(f'Error sending task to queue: {e}')
        raise e
    finally:
        session.close()


def send_task_to_queue_message(task_data: dict) -> None:
    """Helper function to send a task message to the queue."""
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='task_queue')

        message = json.dumps(task_data)
        channel.basic_publish(exchange='', routing_key='task_queue', body=message)
        logging.info(f'Sent task to queue: {task_data}')

        connection.close()
    except Exception as e:
        logging.error(f'Error sending task to RabbitMQ queue: {e}')
        raise e


def consume_task_from_queue(task_data: dict) -> None:
    """Consume a task from the queue."""
    try:
        logging.info(f'Consuming task: {task_data}')
        task_id = task_data["id"]
        project_id = task_data["project_id"]

        session = init_project_db_session()
        send_task_to_queue(session, project_id, task_id)

        logging.info(f'Task consumed: {task_data}')
    except Exception as e:
        logging.error(f'Error consuming task: {e}')
        raise e
