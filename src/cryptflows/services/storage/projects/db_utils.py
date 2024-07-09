from .project_db import Session, Project
from datetime import datetime


def list_available_projects() -> list:

    session = Session()

    projects = session.query(Project).all()

    return projects

def create_new_project(project_name: str):
    # Create a new session
    session = Session()

    # Create a new project
    new_project = Project(
        name="HTB Lab - Lame",
        project_type="Hack the Box",
        description="Beginner-friendly HTB machine for practice",
        status="In Progress"
    )

    # Add the new project to the session and commit
    session.add(new_project)
    session.commit()

    # Query all projects
    projects = session.query(Project).all()
    for project in projects:
        print(f"Project: {project.name}, Type: {project.project_type}, Status: {project.status}")

    # Close the session
    session.close()