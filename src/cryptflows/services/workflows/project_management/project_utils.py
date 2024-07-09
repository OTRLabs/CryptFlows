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
        
    def init_project_db_session(self, console: Console) -> sessionmaker:
            """Initialize the project database session.

            Args:
                console (Console): The console object for printing messages.

            Returns:
                sessionmaker: A sessionmaker bound to the database engine.
            """
            # Set the path for the project database
            db_path: str = 'project_management.db'
            
            # Create an engine to connect to the database using sqlite
            engine = create_engine(Config.SQLITE_DB_PATH)
            
            # Check if the database file exists
            if not os.path.exists(db_path):
                console.print(f'Creating database at {db_path}')
                # Create the necessary tables in the database
                UUIDBase.metadata.create_all(engine)
            else:
                console.print(f'Reading from database at {db_path}')
                
            # Create a sessionmaker bound to the engine
            session: sessionmaker = sessionmaker(bind=engine)
            return session

    # Project management functions
    def create_project(self, console: Console, name: str) -> Project:
            """Create a project with strongly typed arguments and return type.

            Args:
                console (Console): The console object for printing messages.
                name (str): The name of the project to create.

            Returns:
                Project: The created Project object.
            """
            console.print(f'Creating project!')
            
            session = self.init_project_db_session()
            try:
                project = Project(name=name)
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

    def get_projects(self, session: sessionmaker) -> List[Project]:
        try:
            projects = session.query(Project).all()
            return projects
        except Exception as e:
            logging.error(f'Error getting projects: {e}')
            raise e
        finally:
            session.close()

    def add_task_to_project(self,session: sessionmaker, project_id: int, task_name: str, description: str) -> None:
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

    def get_tasks_for_project(self, session: sessionmaker, project_id: int) -> List[Task]:
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

    def consume_task_from_queue(self, task_data: dict) -> None:
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

    def list_available_projects(self, console: Console, session: Session) -> List[Project]:
        """
        This function lists all available projects in the database.

        :return: List of Project objects
        """
        session = Session()

        projects = session.query(Project).all()
        console.print(f"Available projects: {projects}")
        return projects



    def remove_project(self, console: Console, session: Session, project_id: int) -> None:
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
