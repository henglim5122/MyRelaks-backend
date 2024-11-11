"""
Database configuration and setup using SQLAlchemy and PostgreSQL.
"""

import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Load environment variables from .env file
load_dotenv()

# Retrieve database credentials from environment variables
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DATABASE_URL = os.getenv("DATABASE_URL")  # Prefer DATABASE_URL if provided

# Construct the DATABASE_URL if not provided directly
if not DATABASE_URL:
    if not all([DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME]):
        raise RuntimeError("Database credentials are not fully set in the environment variables.")
    DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

print(f"Connecting to database: {DATABASE_URL}")

# Initialize the SQLAlchemy engine
try:
    engine = create_engine(
        DATABASE_URL,
        pool_size=5,
        max_overflow=10,
        pool_timeout=30,
        pool_recycle=1800,
        echo=True,  # Set to True for SQL query logging (optional)
    )
except Exception as exc:
    raise RuntimeError(f"Failed to create engine: {exc}") from exc

# Create a sessionmaker for database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define the Base class for declarative models
Base = declarative_base()

def get_db():
    """
    Provides a database session dependency.
    Ensures the session is closed after use.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
