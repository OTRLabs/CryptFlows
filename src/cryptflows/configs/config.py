import os
from dotenv import load_dotenv

load_dotenv()




class Config:
    SEAWEEDFS_HOST=os.getenv("SEAWEEDFS_HOST")
    SEAWEEDFS_PORT=os.getenv("SEAWEEDFS_PORT")
    SEAWEEDFS_USERNAME=os.getenv("SEAWEEDFS_USERNAME")
    SEAWEEDFS_PASSWORD=os.getenv("SEAWEEDFS_PASSWORD")
    
    DUCKDB_PATH=os.getenv("DUCKDB_HOST")
    DUCKDB_PORT=os.getenv("DUCKDB_PORT")
    DUCKDB_USERNAME=os.getenv("DUCKDB_USERNAME")
    DUCKDB_PASSWORD=os.getenv("DUCKDB_PASSWORD")
    
    RABBITMQ_HOST=os.getenv("RABBITMQ_HOST")
    RABBITMQ_PORT=os.getenv("RABBITMQ_PORT")
    RABBITMQ_USER=os.getenv("RABBITMQ_USER")
    RABBITMQ_PASSWORD=os.getenv("RABBITMQ_PASSWORD")

    SQLITE_DB_PATH=os.getenv("SQLITE_DB_PATH", "sqlite:///cryptflows.db")