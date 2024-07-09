from __future__ import annotations
import os
import json
import logging
from typing import List
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Enum, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from ....configs.config import Config
import pika
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from rich.console import Console
from ....configs.config import Config
from .project_models import Project, Task
from advanced_alchemy.base import UUIDBase
from rich.prompt import Prompt
class ProjectUtils:

    def __init__(self):
        pass
        
    def init_project_db_session() -> sessionmaker:
        db_path = 'project_management.db'
        engine = create_engine(f'duckdb:///{db_path}')
        
        try:
            if not os.path.exists(db_path):
                logging.info(f'Creating database at {db_path}')
                UUIDBase.metadata.create_all(engine)
            else:
                logging.info(f'Reading from database at {db_path}')
                
            Session = sessionmaker(bind=engine)
            return Session
        except Exception as e:
            logging.error(f'Error initializing project database session: {e}')
            raise e

    # Project management functions
    def create_project(console: Console, name: str) -> Project:
        console.print(f'Creating project!')
        
        session = ProjectUtils.init_project_db_session()
        try:
            project = Project(name=name, created_at=datetime.now())
            session.add(project)
            session.commit()
            session.refresh(project)
            
            console.print(f'Project created: {project}')

            return project
        except Exception as e:
            logging.error(f'Error creating project: {e}')
            session.rollback()
            raise e
        finally:
            session.close()

    def get_projects(session: sessionmaker) -> List[Project]:
        try:
            projects = session.query(Project).all()
            return projects
        except Exception as e:
            logging.error(f'Error getting projects: {e}')
            raise e
        finally:
            session.close()

    def add_task_to_project(session: sessionmaker, project_id: int, task_name: str, description: str) -> None:
        try:
            task = Task(project_id=project_id, title=task_name, description=description, completed=False)
            session.add(task)
            session.commit()
            session.refresh(task)
        except Exception as e:
            logging.error(f'Error adding task to project: {e}')
            session.rollback()
            raise e
        finally:
            session.close()

    def get_tasks_for_project(session: sessionmaker, project_id: int) -> List[Task]:
        try:
            tasks = session.query(Task).filter_by(project_id=project_id).all()
            return tasks
        except Exception as e:
            logging.error(f'Error getting tasks for project: {e}')
            raise e
        finally:
            session.close()

    # Task queue management functions
    def send_task_to_queue(task_data: dict) -> None:
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
            channel = connection.channel()
            channel.queue_declare(queue=task_data['queue'])
            channel.basic_publish(exchange='', routing_key=task_data['queue'], body=json.dumps(task_data['body']))
            logging.info(f"Sent task {task_data['body']} to queue {task_data['queue']}")
        except Exception as e:
            logging.error(f'Error sending task to queue: {e}')
            raise e
        finally:
            connection.close()

    def consume_task_from_queue(task_data: dict) -> None:
        def callback(ch, method, properties, body):
            logging.info(f"Received task: {body}")
            # Here you can add the logic to process the task
            ch.basic_ack(delivery_tag=method.delivery_tag)

        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
            channel = connection.channel()
            channel.queue_declare(queue=task_data['queue'])
            channel.basic_consume(queue=task_data['queue'], on_message_callback=callback)
            logging.info(f"Consuming tasks from queue {task_data['queue']}")
            channel.start_consuming()
        except Exception as e:
            logging.error(f'Error consuming task from queue: {e}')
            raise e
        finally:
            connection.close()


    from datetime import datetime


    from typing import List

    def list_available_projects() -> List[Project]:
        """
        This function lists all available projects in the database.

        :return: List of Project objects
        """
        session = Session()

        projects = session.query(Project).all()

        return projects



    def remove_project(console: Console, session: Session, project_id: int) -> None:
        """
        This function removes a project from the database.

        :param session: SQLAlchemy session of type Session
        :param project_id: ID of the project to remove of type int
        :return: None
        """
        console.print(f"Removing project with ID {project_id}...")
        project: Project = session.query(Project).get(project_id)
        session.delete(project)
        session.commit()
        console.print(f"Project with ID {project_id} removed successfully.")
