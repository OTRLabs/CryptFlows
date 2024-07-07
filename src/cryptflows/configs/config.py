from dotenv import load_dotenv

load_dotenv()

import os


class Config:
    SEAWEEDFS_HOST=os.getenv("SEAWEEDFS_HOST")
    SEAWEEDFS_PORT=os.getenv("SEAWEEDFS_PORT")
    SEAWEEDFS_USERNAME=os.getenv("SEAWEEDFS_USERNAME")
    SEAWEEDFS_PASSWORD=os.getenv("SEAWEEDFS_PASSWORD")
    
    DUCKDB_HOST=os.getenv("DUCKDB_HOST")
    DUCKDB_PORT=os.getenv("DUCKDB_PORT")
    DUCKDB_USERNAME=os.getenv("DUCKDB_USERNAME")
    DUCKDB_PASSWORD=os.getenv("DUCKDB_PASSWORD")